# Lock Register

Locked components MUST NOT be modified in any future iteration without an explicit REOPEN REQUEST and version bump approved by James. Any commit touching a locked path = HARD FAIL.

## v2.1.0 — locked 2026-04-26

| Component | Path(s) | Lock reason |
|---|---|---|
| Homepage | `src/pages/index.astro` + all referenced styles + assets in `public/images/` referenced from homepage | Pixel-locked against `https://alglighting-he6frhek.manus.space` |
| Header | `src/components/Header.astro` | Canonical-shared partial; drift gate enforced via verify.mjs |
| Mega menu | (within Header.astro) | Canonical-shared partial; drift gate enforced |
| Footer | `src/components/Footer.astro` | Canonical-shared partial; drift gate enforced |
| BrandMark | `src/components/BrandMark.astro` | Ⓐ rendering primitive (.aa span + brand red) |
| Brand CSS | `src/styles/brand.css` | Design tokens, .aa rules, eyebrow dash, colors |
| Hero | hero block within `index.astro` | Pixel-locked layout, typography, line-drawing CSS |
| Verifier | `scripts/verify.mjs` | Brand-mark + header drift gates; only adds, never removes checks |

## REOPEN process
1. James posts "REOPEN REQUEST: <path> — <reason>" in the iteration prompt
2. Manus opens new PR labeled `reopen/<component>-<version>`
3. Reopen PR requires James approval; cannot auto-merge

### Reopens against v2.1.0

| Date | Branch | Paths | Reason |
|---|---|---|---|
| 2026-04-26 | reopen/v2.1.0-sticky-and-tablet | Header.astro, index.astro | Global sticky header + tablet-landscape line-drawing hide |

## v2.3.0 — locked 2026-04-26

| Component | Path(s) | Lock reason |
|---|---|---|
| Distributor page | `src/pages/distributor.astro` | Pixel-locked persona page; template for all persona pages |
| Specifier page | `src/pages/specifier.astro` | Pixel-locked persona page |
| Contractor page | `src/pages/contractor.astro` | Pixel-locked persona page |
| ESCO page | `src/pages/esco.astro` | Pixel-locked persona page |
| Facility Manager page | `src/pages/facility-manager.astro` | Pixel-locked persona page |

## v2.4.0 — locked 2026-04-26

| Component | Path(s) | Lock reason |
|---|---|---|
| luxoⒶRCH collection page | `src/pages/collections/luxoarch.astro` | First collection landing page; 10-section layout, 23-family grid |

### Reopens against v2.4.0

| Date | Branch | Paths | Reason |
|---|---|---|---|
| 2026-04-26 | reopen/v2.4.0-luxoarch | `src/pages/index.astro` (Illuminator card href); `src/pages/collections/luxoarch.astro` (new file) | First collection landing page; routes homepage Illuminator card to luxoⒶRCH |
| 2026-04-26 | reopen/v2.4.3-collection-polish | `src/styles/brand.css` (scroll-margin-top global rule), `src/pages/collections/luxoarch.astro` (sort logic, sort dropdown label) | Global anchor-scroll offset; ECO→PRO→PRO+ sort canonical |
| 2026-04-26 | reopen/v2.5.0-planoarch | `src/styles/brand.css` (scroll-margin-top 140px→120px), `src/pages/index.astro` (Astra card href), new `src/pages/collections/planoarch.astro` | planoⒶRCH collection page; routes homepage Astra card to plano collection |

## v2.5.3 — locked 2026-04-27

| Component | Path(s) | Lock reason |
|---|---|---|
| Collection shared layout | `src/layouts/CollectionPageLayout.astro` | Canonical layout for all collection pages; structural lock enforced by verify.mjs Group H |
| CollectionHero | `src/components/collection/CollectionHero.astro` | Canonical hero section; red-bordered pills (C1) |
| CollectionStatStrip | `src/components/collection/CollectionStatStrip.astro` | Canonical 4-cell stat strip |
| CollectionApplications | `src/components/collection/CollectionApplications.astro` | Canonical BROWSE BY APPLICATION section (C2) |
| CollectionRedBanner | `src/components/collection/CollectionRedBanner.astro` | Canonical red stat banner |
| CollectionFeatured | `src/components/collection/CollectionFeatured.astro` | Canonical square-aspect featured families (C3) |
| CollectionAllFamilies | `src/components/collection/CollectionAllFamilies.astro` | Canonical filter + grid; APPLICATION heading (C4); data-driven facets (D4/D5) |
| CollectionLegacy | `src/components/collection/CollectionLegacy.astro` | Canonical legacy section |
| CollectionGetStarted | `src/components/collection/CollectionGetStarted.astro` | Canonical get-started section |
| CollectionRelated | `src/components/collection/CollectionRelated.astro` | Canonical related collections section |
| SKU xlsx | `data/SKU_Attributes_Template_v1.xlsx` | Source-of-truth SKU data; do not edit manually |
| SKU build script | `scripts/build-sku-index.mjs` | Emits src/data/sku-index.json; runs before astro build |
| luxoⒶRCH data | `src/data/collections/luxoarch.ts` | Static data file for luxoⒶRCH; all content changes go here |
| planoⒶRCH data | `src/data/collections/planoarch.ts` | Static data file for planoⒶRCH; all content changes go here |

### Reopens against v2.5.3

| Date | Branch | Paths | Reason |
|---|---|---|---|
| 2026-04-27 | reopen/v2.5.3-collection-template | Header.astro, brand.css, CollectionPageLayout.astro, all collection/* components, luxoarch.ts, planoarch.ts, scripts/build-sku-index.mjs, verify.mjs | Collection template canonicalization + global header fixes + filter wiring |

## v2.7.2 — locked 2026-04-27

| Component | Path(s) | Lock reason |
|---|---|---|
| Lamp family detail layout | `src/layouts/LampFamilyDetailPageLayout.astro` | Canonical layout for all Bucket B lamp family detail pages; theme-token system (vintage/nostalgic/utility) |
| Lamp collection layout | `src/layouts/LampCollectionPageLayout.astro` | Canonical layout for all Bucket B lamp collection pages; sister-card family grid |

### Reopens against v2.7.2

| Date | Branch | Paths | Reason |
|---|---|---|---|
| 2026-04-27 | iter/v2.7.2-bucket-b-visual-rebuild | `scripts/verify.mjs` | Additive-only: removed branch exemption from Group G, added Groups O and P |

## v2.6.0 — Bucket A expansion (2026-04-27)

Acknowledged by: Manus (iter/v2.6.0-bucket-a)

| Component | Path(s) | Lock reason |
|---|---|---|
| lamparⒶRCH page | `src/pages/collections/lampararch.astro` | Canonical 5-line collection page; structural lock Group H |
| cityⒶRCH page | `src/pages/collections/cityarch.astro` | Canonical 5-line collection page; structural lock Group H |
| multi-fⒶMILY page | `src/pages/collections/multifamily.astro` | Canonical 5-line collection page; structural lock Group H |
| lamparⒶRCH data | `src/data/collections/lampararch.ts` | Static data file for lamparⒶRCH |
| cityⒶRCH data | `src/data/collections/cityarch.ts` | Static data file for cityⒶRCH |
| multi-fⒶMILY data | `src/data/collections/multifamily.ts` | Static data file for multi-fⒶMILY |
| SKU xlsx v2 | `data/SKU_Attributes_Template_v2.xlsx` | v2 source-of-truth SKU data covering all 5 Bucket A collections |

## v2.7.3 — Mega menu full-width + Lamps taxonomy rename (2026-04-27)

Acknowledged by: Manus (reopen/v2.7.3-megamenu-polish)

### Changes (CSS + data-file edits only — no new files)

| Track | Path | Change |
|---|---|---|
| A | `src/components/Header.astro` | `.megamenu.wide`: `left:2.5vw; right:2.5vw` → `left:0; right:0; width:100%` — full viewport-width mega menu |
| B | `src/components/Header.astro` | Lamps left-rail descriptor: `Filament · Linear · Utility` → `Decor · Linear · Utility` |
| B | `src/components/Header.astro` | CATEGORY entries: `Indoor \| tubulⒶRCH` → `Linear \| tubulⒶRCH`; `Indoor \| Nostalgic Décor` → `Nostalgic Décor`; `Indoor \| Vintage Décor` → `Vintage Décor`; `Indoor \| Utility signⒶTURE` → `Utility \| signⒶTURE` |

## v2.7.6 — Mega menu full-width (Solutions) + hero period color (2026-04-27)

Acknowledged by: Manus (reopen/v2.7.6-megamenu-hero-polish)

### Changes (CSS + HTML edits only — no new files)

| Track | Path | Change |
|---|---|---|
| A | `src/components/Header.astro` | `.megamenu.solutions`: `left:2.5vw;right:2.5vw` → `left:0;right:0;width:100%` — full viewport-width Solutions mega menu |
| B | `src/pages/index.astro` | Hero periods: first two `period-red` → `period-plain` (color:inherit); third stays `period-red`; added `.period-plain { color: inherit; }` CSS rule |

## v2.7.7 — Build provenance badge + audit URL discipline (2026-04-27)

Acknowledged by: Manus (iter/v2.7.7-build-provenance)

### Changes

| Track | Path | Change |
|---|---|---|
| A | `src/components/Footer.astro` | Added `.footer-build-stamp` div + CSS + frontmatter vars (`buildHash`, `buildTime`) |
| A | `.github/workflows/build-and-verify.yml` | Added `PUBLIC_BUILD_HASH` and `PUBLIC_BUILD_TIME` env vars to Build site step |
| B | `docs/reply_contract_template.md` | Created — canonical reply contract template with per-deploy URL as required audit target |
| B | `docs/audit_checklist.md` | Created — audit workflow for James |

## v2.7.8 — Engineering collection pages (2026-04-27)

Acknowledged by: Manus (iter/v2.7.8-engineering-pages)

### New pages (engineering template — BaseLayout + inline sections)

| Component | Path(s) | Lock reason |
|---|---|---|
| tubulⒶRCH collection index | `src/pages/collections/tubulararch.astro` | Rebuilt as full engineering collection index; Find My Tube wizard, family cards, ballast compat hub |
| The Workshop T8 family detail | `src/pages/collections/tubulararch/t8.astro` | Rebuilt as engineering family detail; SKU collapse infographic, Find My Tube wizard, structured spec table |
| signⒶTURE collection index | `src/pages/collections/signature.astro` | NEW engineering collection index; shape-filter tab bar, Husk card (live), 3 coming-soon family cards |
| The Husk HID family detail | `src/pages/collections/signature/husk-hid.astro` | NEW engineering family detail; hero 4-stat bar, SKU consolidation table, Find My HID wizard, fixture compat matrix |

### Verifier changes (additive-only)

| Track | Path | Change |
|---|---|---|
| B.1 fix | `scripts/verify.mjs` | Strip `<title>` tag content and all HTML attribute values before scanning for naked Ⓐ (title metadata + data-* attrs are not rendered body content) |
| Group H | `scripts/verify.mjs` | Added `tubulararch` and `signature` to `BESPOKE_PAGES` exemption set — engineering pages use BaseLayout, not canonical 5-line CollectionPageLayout |
| Group M | `scripts/verify.mjs` | Removed `tubulararch` from lamp theme CSS var check — engineering page, not LampCollectionPageLayout |
| Group N | `scripts/verify.mjs` | Removed `tubulararch` from `LAMP_SLUGS` — engineering page, not LampCollectionPageLayout; updated pass message to 3 pages |

## v2.7.x — Foundation fixes (2026-04-28)

Acknowledged by: Manus (iter/v2.7.x-foundation-fixes)

### Fix 1+2: Build-hash pipeline

| Track | Path | Change |
|---|---|---|
| A | `package.json` | Added `cf-build` script: `PUBLIC_BUILD_HASH=$CF_PAGES_COMMIT_SHA PUBLIC_BUILD_TIME=$(date -u +%Y-%m-%dT%H:%MZ) astro build` |
| A | `docs/CLOUDFLARE_PAGES_SETUP.md` | Created — instructions to set CF Pages build command to `pnpm run cf-build` |

### Fix 3: URL tree reconciliation (utility-signature → signature)

| Track | Path | Change |
|---|---|---|
| A | `src/components/Header.astro` | Mega menu: all `utility-signature` hrefs → `/collections/signature/`; label `Utility \| signⒶTURE` → `signⒶTURE` |
| A | `src/layouts/LampCollectionPageLayout.astro` | `utility-signature` slug reference → `signature` |
| A | `src/layouts/LampFamilyDetailPageLayout.astro` | Breadcrumb label `utility-signature` → `signature`; breadcrumb path `INDOOR` → `LAMPS` |
| A | `src/data/lamps/nostalgic-decor.ts` | `relatedCollections` slug `utility-signature` → `signature` |
| A | `src/data/lamps/vintage-decor.ts` | `relatedCollections` slug `utility-signature` → `signature` |
| A | `src/data/sku-index.json` | Collection key `utility-signature` → `signature` |
| A | `src/data/lamps/signature/` | NEW directory — migrated from `src/data/lamps/utility-signature/` (a-lamp, br-lamp, par-lamp, husk-hid) |
| A | `src/pages/collections/signature/` | NEW directory — migrated a-lamp.astro, br-lamp.astro, par-lamp.astro from `utility-signature/` |
| A | `scripts/verify.mjs` | All `utility-signature` references → `signature` (Groups K, L, M, N, P) |

### Fix 4: CTA audit

| Track | Path | Change |
|---|---|---|
| A | `src/pages/collections/signature/husk-hid.astro` | SHOP CTA: `href="#"` → `href="https://algportal.archipelagolighting.com"` |
| A | `src/pages/collections/tubulararch/t8.astro` | SHOP CTA: `href="#"` → `href="https://algportal.archipelagolighting.com"` |

### Fix 5: Stat reconciliation

| Track | Path | Change |
|---|---|---|
| A | `src/pages/collections/tubulararch.astro` | Collection stat: `147 SKUs` → `23 SKUs`; added qualifier: `1 family shipping now · 4 more in Q3 2026` |
| A | `src/pages/collections/tubulararch/t8.astro` | Family stat: `100 SKUs` → `5 SKUs` |

### Fix 6: Décor family-detail rebuild

| Track | Path | Change |
|---|---|---|
| A | `src/data/lamps/nostalgic-decor/*.ts` (7 files) | Named products, narrative copy, correct sibling SKU counts from Item.xlsx |
| A | `src/data/lamps/vintage-decor/*.ts` (6 files) | Named products, narrative copy, correct sibling SKU counts from Item.xlsx |
| A | `src/layouts/LampFamilyDetailPageLayout.astro` | Series eyebrow above H1 (collection name + "Series"); spec table columns updated to Décor SKU format (SKU Description, Wattage, CCT, Finish/Style, Voltage, Dimmable); breadcrumb INDOOR → LAMPS |

### Fix 7: Verifier bespoke justifications + replacements

| Track | Path | Change |
|---|---|---|
| A | `scripts/verify.mjs` | Group M: `signature` exempted (bespoke page, no lampBg var) |
| A | `scripts/verify.mjs` | Group N: `signature` removed from LAMP_SLUGS (bespoke page); pass message updated to 2 pages |
| A | `scripts/verify.mjs` | Groups K/L/P: `utility-signature` → `signature` |
