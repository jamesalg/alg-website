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
