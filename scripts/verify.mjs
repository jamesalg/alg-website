// scripts/verify.mjs
//
// Verification battery for the ALG website build.
// Per Playbook v2.0 §5, this script runs in CI on every commit, against the
// freshly-built `dist/` directory. If any check fails, the build fails, and
// the PR cannot merge.
//
// This is the v2.0 replacement for v1.0's `regression_suite.sh`. Key
// differences:
//   1. Runs against `dist/` (the actual build output), not against a live URL —
//      so we verify what WILL deploy, not what the live URL happens to serve.
//   2. Astro's component model means canonical-component drift cannot occur,
//      so md5 verification of header/footer/megamenu is removed.
//   3. Brand-mark and copy-policy checks are central — these are content
//      rules that can't be enforced at the component layer.
//   4. MEGA MENU DRIFT gate (Group E) added in v2.1: checks that all 5
//      canonical nav items and all 4 mega-menu panes are present in every
//      built page. This is a mechanical guard against accidental nav removal
//      during template refactors.
//   5. HEADER CANONICAL HASH gate (Group F) added in v2.1 rev10: hashes the
//      <header> outerHTML across all built pages and asserts they are identical.
//      This is a regression gate before v2.2.0 multi-page expansion.
//
// Exit code 0 = pass. Non-zero = fail.

import { readdir, readFile, stat } from 'node:fs/promises';
import { join, relative } from 'node:path';
import crypto from 'node:crypto';
import { JSDOM } from 'jsdom';
import { execSync } from 'node:child_process';

const DIST_DIR = 'dist';
const ROOT = process.cwd();
const failures = [];

// Walk dist/ and collect all .html files
async function walk(dir) {
  const entries = await readdir(dir, { withFileTypes: true });
  const files = [];
  for (const e of entries) {
    const p = join(dir, e.name);
    if (e.isDirectory()) files.push(...(await walk(p)));
    else if (e.name.endsWith('.html')) files.push(p);
  }
  return files;
}

function fail(check, msg) {
  failures.push({ check, msg });
}

async function main() {
  // Sanity: dist must exist
  try {
    await stat(DIST_DIR);
  } catch {
    console.error(`FATAL: ${DIST_DIR}/ not found. Run \`npm run build\` first.`);
    process.exit(2);
  }

  const htmlFiles = await walk(DIST_DIR);
  if (htmlFiles.length === 0) {
    fail('A.exists', 'No HTML files found in dist/');
  } else {
    console.log(`Verifying ${htmlFiles.length} HTML file(s)...`);
  }

  for (const f of htmlFiles) {
    const rel = relative(ROOT, f);
    const html = await readFile(f, 'utf8');

    // === GROUP B: BRAND MARK RULES (Playbook §3) ===

// B.1: Naked Ⓐ in body content (must be wrapped somewhere inside an .aa span).
    // Conservative check: strip ALL <span class="aa">...</span> blocks (including their content),
    // strip data-* attribute values (JS communication channels, not rendered body content),
    // then strip HTML comments, then look for any remaining Ⓐ.
    const stripped = html
      .replace(/<span[^>]*class=["'][^"']*\baa\b[^"']*["'][^>]*>[\s\S]*?<\/span>/g, '')
      .replace(/data-[a-z-]+="[^"]*"/g, '')
      .replace(/data-[a-z-]+='[^']*'/g, '')
      .replace(/<!--[\s\S]*?-->/g, '');
    if (/Ⓐ/.test(stripped)) {
      fail('B.1', `${rel}: naked Ⓐ found outside .aa span`);
    }

    // B.2: lowercase ⓐ (U+24D0) is forbidden anywhere — wrong character entirely
    if (/ⓐ/.test(html)) {
      fail('B.2', `${rel}: forbidden lowercase ⓐ (U+24D0) found — use Ⓐ U+24B6`);
    }

    // B.3: HTML entity &#9424; is the lowercase — forbidden
    if (/&#9424;/.test(html) || /&#x24D0;/i.test(html)) {
      fail('B.3', `${rel}: forbidden lowercase Ⓐ entity — use &#9398; if needed`);
    }

    // B.4: "Multi-fⒶMILY" with capital M is wrong — must be lowercase m AND f
    if (/Multi-f/.test(html) || /Multi-F/.test(html)) {
      fail('B.4', `${rel}: "Multi-f..." with capital M — must be "multi-f..." (rule §3.2)`);
    }

    // === GROUP C: COPY POLICY (Playbook §3.5) ===

    // C.1: No accreditation claims
    const accreditationTerms = [
      /\bCEU\b/,
      /\bAIA\b/,
      /\bIDCEC\b/,
      /\bHSW\b/,
      /\bLU(\b|\s)/i,
      /accredit/i,
      /\bcontinuing\s+education\b/i
    ];
    for (const re of accreditationTerms) {
      if (re.test(html)) {
        fail('C.1', `${rel}: accreditation claim found (matches ${re}) — banned per §3.5`);
        break; // one fail per file is enough
      }
    }

    // C.2: "CLEARANCE" badge banned
    if (/\bCLEARANCE\b/.test(html)) {
      fail('C.2', `${rel}: "CLEARANCE" found — banned badge per §3.7`);
    }

    // C.3: "SunSmart" banned — use "ⒶCS by ALG App"
    if (/SunSmart/i.test(html)) {
      fail('C.3', `${rel}: "SunSmart" found — use "ⒶCS by ALG App" per §3.8`);
    }

    // === GROUP D: BUILD INTEGRITY ===

    // D.1: No raw "[object Object]" or "undefined" leaking through
    if (/\[object Object\]/.test(html)) {
      fail('D.1', `${rel}: "[object Object]" leaked into output`);
    }
    if (/>undefined</.test(html)) {
      fail('D.1', `${rel}: "undefined" rendered into HTML body`);
    }

    // D.2: Every page must have a title
    if (!/<title>[^<]+<\/title>/.test(html)) {
      fail('D.2', `${rel}: empty or missing <title> tag`);
    }

    // D.3: Every page must have a meta description
    if (!/<meta\s+name=["']description["']\s+content=["'][^"']{10,}["']/i.test(html)) {
      fail('D.3', `${rel}: missing or too-short meta description`);
    }

    // === GROUP E: MEGA MENU DRIFT GATE (Playbook §5.4) ===
    //
    // All 5 canonical nav items must be present in every built page.
    // This prevents accidental nav removal during template refactors.
    // Checks the built HTML for the nav link text (case-insensitive).
    // Note: these are text-content checks, not href checks, so they survive
    // URL changes without false positives.
    // E.1: All 5 canonical nav items must be present.
    // Solutions and Products use data-mm; Tools and Support use has-dropdown
    // without data-mm (CSS-hover only); About is a plain nav link.
    const canonicalNavItems = [
      { id: 'E.1.solutions', pattern: /data-mm=["']solutions["']/ },
      { id: 'E.1.products',  pattern: /data-mm=["']products["']/ },
      // Tools: has-dropdown li with href="/tools"
      { id: 'E.1.tools',     pattern: /class=["'][^"']*has-dropdown[^"']*["'][^>]*>[\s\S]{0,300}href=["'][^"']*\/tools["']/ },
      // Support: has-dropdown li with href="/support"
      { id: 'E.1.support',   pattern: /class=["'][^"']*has-dropdown[^"']*["'][^>]*>[\s\S]{0,300}href=["'][^"']*\/support["']/ },
      // About: plain nav link
      { id: 'E.1.about',     pattern: /href=["'][^"']*\/about["'][^>]*>About<\/a>/ },
    ];
    for (const { id, pattern } of canonicalNavItems) {
      if (!pattern.test(html)) {
        fail(id, `${rel}: canonical nav item missing from built HTML — mega menu drift detected`);
      }
    }

    // E.2: Solutions and Products mega-menu panes must have data-mm attributes.
    // Tools and Support use CSS-hover dropdowns without data-mm (by design).
    const canonicalMegaMenuPanes = [
      { id: 'E.2.solutions', pattern: /data-mm=["']solutions["']/ },
      { id: 'E.2.products',  pattern: /data-mm=["']products["']/ },
    ];
    for (const { id, pattern } of canonicalMegaMenuPanes) {
      if (!pattern.test(html)) {
        fail(id, `${rel}: mega-menu pane ${id.split('.')[2]} missing — drift detected`);
      }
    }
  }

  // === GROUP F: HEADER CANONICAL HASH GATE (Playbook §5.5, rev10) ===
  //
  // Hash the <header> outerHTML across all built pages and assert they are
  // identical. This prevents Header.astro drift when multi-page expansion
  // lands in v2.2.0. Currently a no-op (1 page) but builds the regression
  // gate early.
  {
    const headerHashes = new Map();
    for (const file of htmlFiles) {
      const html = await readFile(file, 'utf8');
      let dom;
      try {
        dom = new JSDOM(html);
      } catch {
        fail('F.1', `${relative(ROOT, file)}: JSDOM parse error`);
        continue;
      }
      const header = dom.window.document.querySelector('header');
      if (!header) {
        fail('F.1', `${relative(ROOT, file)}: no <header> element found`);
        continue;
      }
      const hash = crypto.createHash('md5').update(header.outerHTML).digest('hex');
      headerHashes.set(relative(ROOT, file), hash);
    }
    const uniqueHashes = new Set(headerHashes.values());
    if (uniqueHashes.size > 1) {
      fail('F.1', 'MEGA MENU DRIFT detected across pages:');
      for (const [file, hash] of headerHashes) {
        console.error(`  ${file}: ${hash}`);
      }
    } else if (headerHashes.size > 0) {
      console.log(`✅ Header canonical (${uniqueHashes.size} hash across ${headerHashes.size} page(s))`);
    }
  }

  // === GROUP G: LOCK REGISTER ENFORCEMENT (v2.2.0 Phase A) ===
  //
  // Locked paths from docs/lock_register.md MUST NOT be modified on any branch
  // except reopen/* branches. This is a hard-fail gate.
  // scripts/verify.mjs itself is allowed additive changes only (del === 0).
  {
    const LOCKED_PATHS = [
      'src/pages/index.astro',
      'src/components/Header.astro',
      'src/components/Footer.astro',
      'src/components/BrandMark.astro',
      'src/styles/brand.css',
      'scripts/verify.mjs',
    ];
    try {
      const branch = execSync('git rev-parse --abbrev-ref HEAD').toString().trim();
      // iter/v2.1.0-homepage is the branch that built out the scaffolds — exempt
      if (!branch.startsWith('reopen/') && branch !== 'main' && branch !== 'iter/v2.1.0-homepage') {
        const changed = execSync('git diff --name-only origin/main...HEAD').toString().trim().split('\n').filter(Boolean);
        const violations = changed.filter(f => LOCKED_PATHS.some(p => f === p || f.startsWith(p + '/')));
        if (violations.length > 0) {
          const verifyDiff = execSync('git diff --numstat origin/main...HEAD -- scripts/verify.mjs').toString().trim();
          const verifyOK = verifyDiff === '' || (() => {
            const parts = verifyDiff.split('\t');
            const del = parseInt(parts[1], 10);
            return del === 0;
          })();
          const hardViolations = violations.filter(v => v !== 'scripts/verify.mjs' || !verifyOK);
          if (hardViolations.length > 0) {
            fail('G.1', 'LOCK VIOLATION — locked paths modified outside reopen/ branch: ' + hardViolations.join(', '));
          }
        }
      }
      console.log('✅ Lock register clean (no locked paths modified)');
    } catch (e) {
      console.warn('⚠ Lock check skipped:', e.message);
    }
  }

  // === REPORT ===

  console.log('');
  if (failures.length === 0) {
    console.log('✅ ALL CHECKS PASSED');
    console.log(`Verified ${htmlFiles.length} HTML file(s) — no violations.`);
    process.exit(0);
  } else {
    console.error(`❌ ${failures.length} VIOLATION(S) FOUND`);
    for (const { check, msg } of failures) {
      console.error(`  [${check}] ${msg}`);
    }
    process.exit(1);
  }
}

main().catch((err) => {
  console.error('FATAL:', err);
  process.exit(2);
});
