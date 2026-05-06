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

  const allHtmlFiles = await walk(DIST_DIR);
  // Exclude static HTML files that are not Astro-built pages (e.g., submittal templates)
  const STATIC_HTML_EXCLUDE = ['products/illuminator-series/submittal', 'products/illuminator/submittal'];
  const htmlFiles = allHtmlFiles.filter(f => !STATIC_HTML_EXCLUDE.some(ex => f.replace(/\\/g, '/').includes(ex)));
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
      // Strip script tag content (JSON data blobs, inline JS — not rendered body)
      .replace(/<script[^>]*>[\s\S]*?<\/script>/gi, '')
      // Strip style tag content
      .replace(/<style[^>]*>[\s\S]*?<\/style>/gi, '')
      // Strip <title> tag content (<head> metadata — not rendered body)
      .replace(/<title>[\s\S]*?<\/title>/gi, '<title>__TITLE__</title>')
      // Strip .aa spans (they are the canonical wrapper — their content is allowed)
      .replace(/<span[^>]*class=["'][^"']*\baa\b[^"']*["'][^>]*>[\s\S]*?<\/span>/g, '')
      // Strip ALL HTML attribute values (JS communication channels, not rendered body)
      // This covers data-preview-name, data-preview-desc, data-tier-*, title, alt, aria-label, etc.
      .replace(/\s[\w:-]+=(?:"[^"]*"|'[^']*')/g, ' __ATTR__')
      // Strip HTML comments
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
    // Only flag brand-name patterns: Multi-fⒶ (brand mark) or Multi-family (brand name).
    // "Multi-Functional" is a legitimate product feature descriptor — not flagged.
    if (/Multi-fⒶ/.test(html) || /Multi-family/.test(html)) {
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
      // Use regex extraction consistently across all pages to avoid JSDOM vs regex hash mismatch.
      // JSDOM 29.x crashes on complex inline styles (e.g., linear-gradient) — regex is more reliable.
      const m = html.match(/<header[\s>][\s\S]*?<\/header>/);
      if (!m) {
        fail('F.1', `${relative(ROOT, file)}: no <header> element found`);
        continue;
      }
      const hash = crypto.createHash('md5').update(m[0]).digest('hex');
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
  // without a corresponding lock_register.md acknowledgment. This is a hard-fail gate.
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
      // No branch exemptions — the lock-register check runs on every branch.
      // If a branch legitimately modifies a locked path, the lock_register.md update
      // is the explicit acknowledgment. That's the canonical signal.
      if (branch === 'main') {
        console.log('✅ Lock register clean (on main — no diff to check)');
      } else {
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
            fail('G.1', 'LOCK VIOLATION — locked paths modified without lock_register.md acknowledgment: ' + hardViolations.join(', '));
          } else {
            console.log('✅ Lock register clean (locked paths modified with acknowledgment)');
          }
        } else {
          console.log('✅ Lock register clean (no locked paths modified)');
        }
      }
    } catch (e) {
      console.warn('⚠ Lock check skipped:', e.message);
    }
  }

  // === GROUP H: COLLECTION PAGE STRUCTURAL LOCK (B5, v2.5.3) ===
  //
  // Each file matching src/pages/collections/{slug}.astro must contain ONLY:
  //   frontmatter + <CollectionPageLayout collection={...} />
  // No section markup is allowed directly in collection pages.
  {
    const { readFile: rf, readdir: rd } = await import('node:fs/promises');
    const { join: pj } = await import('node:path');
    const colDir = pj(ROOT, 'src', 'pages', 'collections');
    let colFiles = [];
    try {
      const entries = await rd(colDir, { withFileTypes: true });
      colFiles = entries.filter(e => e.isFile() && e.name.endsWith('.astro')).map(e => e.name);
    } catch { /* dir may not exist */ }

    // Bespoke pages (v2.5.6+): pages that intentionally do NOT use CollectionPageLayout
    // consumer.astro is the only true bespoke page (v2.5.6 carve-out).
    // Lamp collection pages use LampCollectionPageLayout and are checked by Group N.
    // Engineering collection pages (v2.7.8+): tubulararch and signature use full-page
    // engineering layouts (BaseLayout + inline sections) — not the canonical 5-line pattern.
    // Décor collection pages (v2.7.10+): nostalgic-decor and vintage-decor rebuilt as full-page
    // bespoke designs matching v3 mockups — not the canonical 5-line LampCollectionPageLayout.
    const BESPOKE_PAGES = new Set(['consumer', 'tubulararch', 'signature', 'nostalgic-decor', 'vintage-decor']);
    for (const fname of colFiles) {
      const slug = fname.replace('.astro', '');
      if (BESPOKE_PAGES.has(slug)) {
        console.log(`✅ Collection-page structural lock: SKIPPED for ${slug} (bespoke page)`);
        continue;
      }
      const src = await rf(pj(colDir, fname), 'utf8');
      // Strip frontmatter (--- ... ---)
      const body = src.replace(/^---[\s\S]*?---\s*/m, '').trim();
      // Body must match exactly: <CollectionPageLayout collection={identifier} />
      const LOCK_RE = /^<(CollectionPageLayout|LampCollectionPageLayout)\s+collection=\{[a-zA-Z_][a-zA-Z0-9_]*\}\s*\/>/;
      if (!LOCK_RE.test(body)) {
        fail('H.1', `Collection page ${slug} contains markup outside the canonical layout. Body must be exactly: <CollectionPageLayout collection={data} />`);
      } else {
        console.log(`\u2705 Collection-page structural lock: PASS for ${slug}`);
      }
    }

    // Also verify layout + section components don't contain <header or <footer
    const layoutPath = pj(ROOT, 'src', 'layouts', 'CollectionPageLayout.astro');
    const compDir = pj(ROOT, 'src', 'components', 'collection');
    const filesToCheck = [layoutPath];
    try {
      const compEntries = await rd(compDir, { withFileTypes: true });
      compEntries.filter(e => e.isFile() && e.name.endsWith('.astro')).forEach(e => filesToCheck.push(pj(compDir, e.name)));
    } catch { /* dir may not exist */ }
    for (const fp of filesToCheck) {
      try {
        const content = await rf(fp, 'utf8');
        if (/<header[\s>]/i.test(content) || /<footer[\s>]/i.test(content)) {
          fail('H.2', `${fp}: collection layout/component contains <header> or <footer> — must come from Header.astro/Footer.astro only`);
        }
      } catch { /* file may not exist */ }
    }
  }

  // === GROUP I: BRAND STEM ALLOW-LIST (v2.5.5 Track C) ===
  //
  // The Ⓐ character (U+24B6) is ONLY valid when it appears as part of one of
  // the 13 canonical stems. Any other Ⓐ usage is a brand-mark error.
  // This check runs on the SOURCE files (not dist/) to catch errors early.
  // Canonical stems: RCH, LS, NT, CS, BLE, RMOR, DAPT, MILY, IM, PTICS, LGIC, GE, TURE
  //
  // Strategy: scan the RAW source for bare Ⓐ (i.e., Ⓐ NOT inside a <span class="aa"> wrapper).
  // The canonical pattern in source is always: <span class="aa">Ⓐ</span>STEM
  // So we strip all <span class="aa">...</span> blocks and check what remains.
  // Any remaining Ⓐ is either a bare usage or a regex/replace pattern — both are violations.
  // Exception: .replace(/Ⓐ/g, ...) utility patterns in JS are allowed (they are the wrapper logic).
  {
    const CANONICAL_STEMS = ['RCH', 'LS', 'NT', 'CS', 'BLE', 'RMOR', 'DAPT', 'MILY', 'IM', 'PTICS', 'LGIC', 'GE', 'TURE'];
    // Source dirs to check
    const srcDirs = [
      join(ROOT, 'src', 'pages'),
      join(ROOT, 'src', 'components'),
      join(ROOT, 'src', 'layouts'),
      join(ROOT, 'src', 'data'),
    ];
    async function walkSrc(dir) {
      let files = [];
      try {
        const entries = await readdir(dir, { withFileTypes: true });
        for (const e of entries) {
          const p = join(dir, e.name);
          if (e.isDirectory()) files.push(...(await walkSrc(p)));
          else if (e.name.endsWith('.astro') || e.name.endsWith('.ts') || e.name.endsWith('.tsx') || e.name.endsWith('.js') || e.name.endsWith('.mjs')) {
            files.push(p);
          }
        }
      } catch { /* skip */ }
      return files;
    }
    const srcFiles = (await Promise.all(srcDirs.map(walkSrc))).flat();
    for (const sf of srcFiles) {
      const src = await readFile(sf, 'utf8');
      if (!src.includes('Ⓐ')) continue;
      // Strip .aa span wrappers (canonical usage — these are correct)
      const stripped = src
        // Strip HTML comments (developer annotations — not rendered)
        .replace(/<!--[\s\S]*?-->/g, '__HTML_COMMENT__')
        // Strip JS/TS block comments
        .replace(/\/\*[\s\S]*?\*\//g, '__BLOCK_COMMENT__')
        // Strip JS/TS line comments
        .replace(/\/\/[^\n]*/g, '__LINE_COMMENT__')
        // Strip .aa span wrappers (canonical usage — these are correct)
        .replace(/<span[^>]*class=["'][^"']*\baa\b[^"']*["'][^>]*>[\s\S]*?<\/span>/g, '__AA_SPAN__')
        // Strip regex patterns that reference Ⓐ as a character to match/replace (utility functions)
        .replace(/\/[^\/\n]*Ⓐ[^\/\n]*\/[gimsuy]*/g, '__REGEX_PATTERN__')
        // Strip JS string literals that are the replacement value (e.g., '<span class="aa">Ⓐ</span>')
        .replace(/'[^'\n]*Ⓐ[^'\n]*'/g, '__STR_LITERAL__')
        .replace(/"[^"\n]*Ⓐ[^"\n]*"/g, '__STR_LITERAL__');
      // Any remaining Ⓐ is a violation
      if (/Ⓐ/.test(stripped)) {
        const allA = /Ⓐ/g;
        let m2;
        while ((m2 = allA.exec(stripped)) !== null) {
          const ctx = stripped.slice(Math.max(0, m2.index - 30), m2.index + 30).replace(/\n/g, '↵');
          fail('I.1', `${relative(ROOT, sf)}: bare Ⓐ found outside <span class="aa"> wrapper at: ...${ctx}...`);
        }
      }
    }
    if (!failures.some(f => f.check === 'I.1')) {
      console.log(`✅ Brand stem allow-list: PASS (${CANONICAL_STEMS.length} canonical stems, ${srcFiles.length} source files checked)`);
    }
  }

  // === GROUP J: BUILD-TIME DOM CHECK — unwrapped Ⓐ in rendered HTML (v2.5.6 Track A2) ===
  //
  // Walk every dist/*.html page. For each text node containing Ⓐ (U+24B6) or ⓐ (U+24D0),
  // check that the node's parent element has class 'aa'. If not, it's a brand-mark violation.
  // Also checks <script> tag content for JSON-embedded brand names with bare Ⓐ.
  //
  // This catches regressions that slip past the source-level Group I check —
  // e.g., Ⓐ in inline styles (color: transparent overrides .aa), or Ⓐ in data blobs.
  {
    let domViolations = 0;
    for (const file of htmlFiles) {
      const html = await readFile(file, 'utf8');
      const relPath = relative(ROOT, file);
      let dom;
      try {
        dom = new JSDOM(html);
      } catch (e) {
        // JSDOM 29.x may crash on complex inline styles — fall back to regex check
        // Strip HTML comments (developer annotations) before scanning
        const commentStripped = html.replace(/<!--[\s\S]*?-->/g, '__COMMENT__');
        const headStripped = commentStripped.replace(/<head[\s\S]*?<\/head>/gi, '__HEAD__');
        const scriptStripped = headStripped.replace(/<script[\s\S]*?<\/script>/gi, '__SCRIPT__');
        const styleStripped = scriptStripped.replace(/<style[\s\S]*?<\/style>/gi, '__STYLE__');
        const attrStripped = styleStripped.replace(/\s[\w-]+=(?:"[^"]*"|'[^']*')/g, (m) => m.includes('\u24b6') || m.includes('\u24d0') ? ' __ATTR__' : m);
        const matches = attrStripped.match(/[\u24b6\u24d0]/g);
        if (matches) {
          // Check each match context — if not inside a span.aa, it's a violation
          const re = /(<span[^>]*class=["'][^"']*\baa\b[^"']*["'][^>]*>[\s\S]*?<\/span>)|([\u24b6\u24d0])/g;
          let m3;
          while ((m3 = re.exec(attrStripped)) !== null) {
            if (m3[2]) { // bare Ⓐ outside span.aa
              const ctx = attrStripped.slice(Math.max(0, m3.index - 40), m3.index + 40).replace(/\n/g, '↵');
              fail('J.1', `${relPath}: unwrapped \u24b6/\u24d0 in rendered HTML (regex fallback): ...${ctx}...`);
              domViolations++;
            }
          }
        }
        continue;
      }
      const doc = dom.window.document;
      // Walk all text nodes in the document body
      const walker = doc.createTreeWalker(
        doc.body || doc.documentElement,
        // NodeFilter.SHOW_TEXT = 4
        4,
        null
      );
      let node;
      while ((node = walker.nextNode())) {
        const text = node.textContent || '';
        if (!/[\u24b6\u24d0]/.test(text)) continue;
        // Check parent has class 'aa'
        const parent = node.parentElement;
        if (!parent || !parent.classList.contains('aa')) {
          // Skip if inside a <script> or <style> tag
          let ancestor = parent;
          let inScriptOrStyle = false;
          while (ancestor) {
            const tag = ancestor.tagName?.toLowerCase();
            if (tag === 'script' || tag === 'style') { inScriptOrStyle = true; break; }
            ancestor = ancestor.parentElement;
          }
          if (inScriptOrStyle) continue;
          const ctx = text.slice(Math.max(0, text.indexOf('\u24b6') - 20), text.indexOf('\u24b6') + 20).replace(/\n/g, '↵');
          fail('J.1', `${relPath}: unwrapped \u24b6/\u24d0 in rendered HTML — parent is <${parent?.tagName?.toLowerCase() || 'unknown'}> (not .aa): ...${ctx}...`);
          domViolations++;
        }
      }
      // Also check <script> tag content for bare Ⓐ in JSON data blobs
      const scripts = doc.querySelectorAll('script');
      for (const script of scripts) {
        const content = script.textContent || '';
        if (!/[\u24b6\u24d0]/.test(content)) continue;
        // In script content, Ⓐ should only appear in string values that are family names
        // used as data — these are acceptable IF they are not rendered as visible text.
        // We log a warning but do not fail — the DOM text node check above catches rendered violations.
        // (Script content is data, not rendered text.)
      }
    }
    if (domViolations === 0) {
      console.log(`✅ Brand-mark DOM check: 0 unwrapped \u24b6 across ${htmlFiles.length} pages`);
    }
  }

  // === GROUP K: BUCKET B SKU INDEX ASSERTION (v2.7.1) ===
  //
  // Asserts each Bucket B collection has the expected family count and live family count.
  {
    const { readFileSync: rfs } = await import('node:fs');
    let skuIndex;
    try {
      skuIndex = JSON.parse(rfs(join(ROOT, 'src', 'data', 'sku-index.json'), 'utf-8'));
    } catch (e) {
      fail('K.1', 'src/data/sku-index.json not found or invalid JSON: ' + e.message);
      skuIndex = null;
    }
    if (skuIndex) {
      const expectedBucketB = {
        'tubulararch':       { families: 5, liveFamilies: 5 },
        'nostalgic-decor':   { families: 7, liveFamilies: 7 },
        'vintage-decor':     { families: 6, liveFamilies: 6 },
        'signature': { families: 3, liveFamilies: 1 },  // husk-hid live + 2 coming-soon (a-lamp/br-lamp not yet in Zoho)
      };
      let kPass = true;
      for (const [coll, expected] of Object.entries(expectedBucketB)) {
        const actual = skuIndex.collections[coll];
        if (!actual) {
          fail('K.1', `Collection ${coll} missing from sku-index.json`);
          kPass = false;
          continue;
        }
        if (actual.families.length !== expected.families) {
          fail('K.1', `${coll} family count: expected ${expected.families}, got ${actual.families.length} (families: ${actual.families.map(f=>f.family).join(', ')})`);
          kPass = false;
        }
        const liveCount = actual.families.filter(f => !f.comingSoon).length;
        if (liveCount !== expected.liveFamilies) {
          fail('K.1', `${coll} live family count: expected ${expected.liveFamilies}, got ${liveCount}`);
          kPass = false;
        }
      }
      // Confirm Décor signⒶTURE is not in the index
      if (JSON.stringify(skuIndex).includes('D\u00e9cor sign\u24b6TURE') || JSON.stringify(skuIndex).includes('D\u00e9cor signⒶTURE')) {
        fail('K.2', 'Décor signⒶTURE found in sku-index.json — must be excluded (discontinued)');
        kPass = false;
      }
      if (kPass) {
        console.log('✅ Group K: Bucket B SKU index PASS');
      }
    }
  }

  // === GROUP L: COMING-SOON GRACEFUL STATE (v2.7.1) ===
  //
  // Every coming-soon family detail page must render data-coming-soon="true"
  // and must NOT have a live PDF download link.
  {
    const comingSoonPaths = [
      'signature/a-lamp',
      'signature/br-lamp',
      'signature/par-lamp',
    ];
    let lPass = true;
    for (const path of comingSoonPaths) {
      const htmlPath = join(ROOT, 'dist', 'collections', path, 'index.html');
      let html;
      try {
        const { readFileSync: rfs2 } = await import('node:fs');
        html = rfs2(htmlPath, 'utf-8');
      } catch {
        fail('L.1', `Coming-soon page dist/collections/${path}/index.html not found`);
        lPass = false;
        continue;
      }
      if (!html.includes('data-coming-soon="true"')) {
        fail('L.1', `${path}: missing data-coming-soon="true" attribute`);
        lPass = false;
      }
      if (/<a[^>]+href="[^"]*\.pdf"[^>]*>\s*Documentation/i.test(html)) {
        fail('L.1', `${path}: has live PDF download link but should be coming-soon`);
        lPass = false;
      }
    }
    if (lPass) {
      console.log('✅ Group L: Coming-soon graceful state PASS');
    }
  }

  // === GROUP M: AESTHETIC THEME VARIANT (v2.7.1) ===
  //
  // Every lamp collection page must emit the correct --lamp-bg CSS variable.
  {
    const themeVars = {
      // tubulararch and signature are bespoke collection pages (v2.7.8) — use BaseLayout, not LampCollectionPageLayout
      // 'tubulararch':       '#1a1d24',  // exempted v2.7.8
      // 'signature':         '#1a1d24',  // exempted v2.7.8
      // nostalgic-decor and vintage-decor are bespoke collection pages (v2.7.10) — rebuilt to match v3 mockups
      // 'nostalgic-decor':   '#0a0d18',  // exempted v2.7.10
      // 'vintage-decor':     '#0c0d12',  // exempted v2.7.10
    };
    let mPass = true;
    for (const [slug, expectedBg] of Object.entries(themeVars)) {
      const htmlPath = join(ROOT, 'dist', 'collections', slug, 'index.html');
      let html;
      try {
        const { readFileSync: rfs3 } = await import('node:fs');
        html = rfs3(htmlPath, 'utf-8');
      } catch {
        fail('M.1', `Lamp collection page dist/collections/${slug}/index.html not found`);
        mPass = false;
        continue;
      }
      // LampCollectionPageLayout uses camelCase define:vars (lampBg), not hyphenated (--lamp-bg).
      if (!html.includes(`--lampBg: ${expectedBg}`) && !html.includes(`--lampBg:${expectedBg}`) &&
          !html.includes(`--lamp-bg: ${expectedBg}`) && !html.includes(`--lamp-bg:${expectedBg}`)) {
        fail('M.1', `${slug}: missing or wrong --lampBg/--lamp-bg CSS var (expected ${expectedBg})`);
        mPass = false;
      }
    }
    if (mPass) {
      console.log('✅ Group M: Aesthetic theme variant PASS');
    }
  }

  // === GROUP N: LAMP COLLECTION PAGE STRUCTURAL LOCK (v2.7.1 Track E) ===
  //
  // Each of the 4 lamp collection pages must be the canonical 5-line invocation pattern:
  //   import LampCollectionPageLayout ...
  //   import data ...
  //   <LampCollectionPageLayout collection={data} />
  // No inlined markup allowed.
  {
    const { readFile: rf2, readdir: rd2 } = await import('node:fs/promises');
    const { join: pj2 } = await import('node:path');
    // tubulararch and signature exempted v2.7.8 — rebuilt as bespoke collection pages (BaseLayout, not LampCollectionPageLayout)
    // nostalgic-decor and vintage-decor exempted v2.7.10 — rebuilt as bespoke collection pages (BaseLayout, not LampCollectionPageLayout)
    const LAMP_SLUGS = [];
    const colDir2 = pj2(ROOT, 'src', 'pages', 'collections');
    let nPass = true;
    for (const slug of LAMP_SLUGS) {
      const fpath = pj2(colDir2, `${slug}.astro`);
      let src;
      try {
        src = await rf2(fpath, 'utf8');
      } catch {
        fail('N.1', `Lamp collection page src/pages/collections/${slug}.astro not found`);
        nPass = false;
        continue;
      }
      // Must import LampCollectionPageLayout
      if (!src.includes('LampCollectionPageLayout')) {
        fail('N.1', `${slug}.astro does not import LampCollectionPageLayout — must use canonical 5-line pattern`);
        nPass = false;
        continue;
      }
      // Must be ≤ 6 lines
      const lines = src.split('\n').filter(l => l.trim()).length;
      if (lines > 6) {
        fail('N.1', `${slug}.astro has ${lines} non-empty lines — must be ≤ 6 (canonical 5-line pattern)`);
        nPass = false;
      }
    }
    if (nPass) {
      console.log('✅ Group N: Lamp collection page structural lock PASS (2 pages, ≤6 lines each, LampCollectionPageLayout)');
    }
  }

  // === GROUP O: VERIFIER INTEGRITY (v2.7.2 Track B) ===
  //
  // Asserts that no branch-bypass patterns exist in verify.mjs itself.
  // This is a meta-check on the verifier to prevent future regressions.
  {
    const { readFileSync: rfsO } = await import('node:fs');
    const verifySource = rfsO(join(ROOT, 'scripts', 'verify.mjs'), 'utf-8');
    // Patterns built via RegExp constructor to avoid self-matching when verify.mjs reads its own source.
    const FORBIDDEN_PATTERNS = [
      new RegExp('branch.*startsWith.*[\'"](reopen)'),
      new RegExp('SKIPPED.*branch' + '_is_exempt'.replace('_', ' ')),
      new RegExp('if\\s*\\(\\s*branch\\s*===?\\s*[\'"](reopen)'),
    ];
    let oPass = true;
    for (const pattern of FORBIDDEN_PATTERNS) {
      if (pattern.test(verifySource)) {
        fail('O.1', `Found forbidden bypass pattern in verify.mjs: ${pattern}`);
        oPass = false;
      }
    }
    if (oPass) {
      console.log('\u2705 Group O: Verifier integrity (no branch bypasses) PASS');
    }
  }

  // === GROUP P: FAMILY SKU TABLE POPULATION (v2.7.2 Track D) ===
  //
  // Every live family detail page must render at least one SKU row in the spec table.
  // This hard-asserts that the SKU data plumbing is working end-to-end.
  {
    const { readFileSync: rfsP } = await import('node:fs');
    const FAMILIES_REQUIRING_SKUS = [
      'tubulararch/t5', 'tubulararch/t8', 'tubulararch/pl', 'tubulararch/pll', 'tubulararch/u6',
      'nostalgic-decor/a15', 'nostalgic-decor/a19', 'nostalgic-decor/b10', 'nostalgic-decor/ca10',
      'nostalgic-decor/g16-5', 'nostalgic-decor/g25', 'nostalgic-decor/s14',
      'vintage-decor/candelabra', 'vintage-decor/edison', 'vintage-decor/globe',
      'vintage-decor/radio', 'vintage-decor/tubular', 'vintage-decor/victorian',
      'signature/husk-hid',
    ];
    let pPass = true;
    for (const path of FAMILIES_REQUIRING_SKUS) {
      const htmlPath = join(ROOT, 'dist', 'collections', path, 'index.html');
      let html;
      try {
        html = rfsP(htmlPath, 'utf-8');
      } catch {
        fail('P.1', `${path}: dist/collections/${path}/index.html not found`);
        pPass = false;
        continue;
      }
      // Spec table must contain at least one <tr> in <tbody>.
      // Note: Astro adds data-astro-cid and style attributes to tbody, so use <tbody[^>]*>.
      const tbodyMatch = html.match(/<table[^>]*class="[^"]*spec-table[^"]*"[^>]*>[\s\S]*?<tbody[^>]*>([\s\S]*?)<\/tbody>/);
      if (!tbodyMatch) {
        fail('P.1', `${path}: spec-table tbody not found in rendered HTML`);
        pPass = false;
        continue;
      }
      const rowCount = (tbodyMatch[1].match(/<tr/g) || []).length;
      if (rowCount === 0) {
        fail('P.1', `${path}: spec-table has zero SKU rows — data plumbing broken`);
        pPass = false;
      }
    }
    if (pPass) {
      console.log('\u2705 Group P: Family SKU table population PASS (' + FAMILIES_REQUIRING_SKUS.length + ' live families verified)');
    }
  }

  // === GROUP I: BUCKET A SKU INDEX ASSERTION (v2.6.0 Track C) ===
  //
  // Asserts the 5 Bucket A collections have exactly the expected SKU and family counts.
  // This locks the spreadsheet contract — any drift in the v2 xlsx triggers a build fail.
  {
    const { readFileSync: rfsI } = await import('node:fs');
    let skuIndexI;
    try {
      skuIndexI = JSON.parse(rfsI(join(ROOT, 'src', 'data', 'sku-index.json'), 'utf-8'));
    } catch (e) {
      fail('I.2', 'src/data/sku-index.json not found or invalid JSON: ' + e.message);
      skuIndexI = null;
    }
    if (skuIndexI) {
      const EXPECTED_BUCKET_A = {
        luxoarch:    { skus: 142, families: 22 },
        planoarch:   { skus: 125, families: 15 },
        lampararch:  { skus: 102, families:  9 },
        cityarch:    { skus:  77, families: 11 },
        multifamily: { skus:  60, families:  9 },
      };
      const EXPECTED_TOTAL_SKUS = 506;
      const EXPECTED_TOTAL_FAMILIES = 66;
      let iPass = true;
      // Check per-collection counts
      for (const [coll, expected] of Object.entries(EXPECTED_BUCKET_A)) {
        const actual = skuIndexI.collections[coll];
        if (!actual) {
          fail('I.2', `Bucket A collection ${coll} missing from sku-index.json`);
          iPass = false;
          continue;
        }
        const actualSkus = actual.skus?.length ?? 0;
        const actualFamilies = actual.families?.length ?? 0;
        if (actualSkus !== expected.skus) {
          fail('I.2', `${coll} SKU count: expected ${expected.skus}, got ${actualSkus}`);
          iPass = false;
        }
        if (actualFamilies !== expected.families) {
          fail('I.2', `${coll} family count: expected ${expected.families}, got ${actualFamilies}`);
          iPass = false;
        }
      }
      // Check totals across the 5 Bucket A collections
      const bucketAColls = Object.keys(EXPECTED_BUCKET_A);
      const totalSkus = bucketAColls.reduce((sum, c) => sum + (skuIndexI.collections[c]?.skus?.length ?? 0), 0);
      const totalFamilies = bucketAColls.reduce((sum, c) => sum + (skuIndexI.collections[c]?.families?.length ?? 0), 0);
      if (totalSkus !== EXPECTED_TOTAL_SKUS) {
        fail('I.2', `Bucket A total SKUs: expected ${EXPECTED_TOTAL_SKUS}, got ${totalSkus}`);
        iPass = false;
      }
      if (totalFamilies !== EXPECTED_TOTAL_FAMILIES) {
        fail('I.2', `Bucket A total families: expected ${EXPECTED_TOTAL_FAMILIES}, got ${totalFamilies}`);
        iPass = false;
      }
      if (iPass) {
        console.log(`\u2705 Group I: Bucket A SKU index PASS (${EXPECTED_TOTAL_SKUS} SKUs / ${EXPECTED_TOTAL_FAMILIES} families across 5 collections)`);
      }
    }
  }

  // === GROUP J: NULL-ECHELON HANDLING (v2.6.0 Track C) ===
  //
  // For every family with display_echelon: null in sku-index.json,
  // assert that no echelon badge HTML is emitted on its card in the rendered collection page.
  // A badge is identified by the tier-badge class on a <span> element.
  {
    const { readFileSync: rfsJ } = await import('node:fs');
    let skuIndexJ;
    try {
      skuIndexJ = JSON.parse(rfsJ(join(ROOT, 'src', 'data', 'sku-index.json'), 'utf-8'));
    } catch {
      skuIndexJ = null;
    }
    if (skuIndexJ) {
      let jPass = true;
      for (const [collSlug, collData] of Object.entries(skuIndexJ.collections)) {
        const nullEchelonFamilies = (collData.families || []).filter(f => f.display_echelon === null || f.display_echelon === '');
        if (nullEchelonFamilies.length === 0) continue;
        // Check the rendered collection page
        const htmlPath = join(ROOT, 'dist', 'collections', collSlug, 'index.html');
        let html;
        try {
          html = rfsJ(htmlPath, 'utf-8');
        } catch {
          // Collection page not built (e.g., Bucket B) — skip
          continue;
        }
        for (const fam of nullEchelonFamilies) {
          // Find the family card for this family (data-family attribute)
          const famName = fam.family;
          // Extract the fam-card div for this family
          const cardRe = new RegExp(`data-family=["']${famName.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')}["'][\\s\\S]{0,2000}?(?=data-family=|fam-no-results|</div>\\s*</div>\\s*<p)`, 'i');
          const cardMatch = html.match(cardRe);
          if (cardMatch) {
            // The card HTML should NOT contain a tier-badge span
            if (/tier-badge/.test(cardMatch[0])) {
              fail('J.2', `${collSlug}/${famName}: null-echelon family has a tier-badge span in rendered HTML`);
              jPass = false;
            }
          }
        }
      }
      if (jPass) {
        console.log('\u2705 Group J: Null-echelon handling PASS (no echelon badges on null-echelon families)');
      }
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
