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
