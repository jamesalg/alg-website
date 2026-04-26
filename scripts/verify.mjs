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
//
// Exit code 0 = pass. Non-zero = fail.

import { readdir, readFile, stat } from 'node:fs/promises';
import { join, relative } from 'node:path';

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
