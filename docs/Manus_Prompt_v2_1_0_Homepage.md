# Manus Prompt v2.1.0 — Homepage Rebuild

**Iteration:** v2.1.0
**Scope:** Rebuild the ALG homepage, plus first real implementation of the three canonical components (Header, MegaMenu, Footer), under Playbook v2.0.
**Branch name:** `iter/v2.1.0-homepage`
**Reference visual target:** v3.14.6 homepage from prior platform (HTML reference attached as `_reference/v3_14_6_homepage.html` plus screenshots in `_reference/screenshots/`)

---

## STEP 0 — REQUIRED FIRST RESPONSE LINE

Your reply MUST begin with this LITERAL line — no preamble, no rephrasing:

```
PLAYBOOK v2.0 §1 §2 §3 §4 §5 §6 §7 §8 READ — proceeding
```

If your reply does not begin with this exact line, the work will be rejected before review (Playbook v2.0 §15).

---

## STEP 1 — Read the playbook

Before any code, read these files in the repo:

1. `/docs/ALG_Build_Playbook_v2.0.md` — the operating discipline (~30 sections)
2. `/docs/lock_register.md` — what's locked (currently nothing)
3. `/docs/ITERATION_LOG.md` — what's merged (currently only Foundation v2.0.0)
4. `/docs/assets.md` — what photography is present and what's missing
5. `/README.md` — repo structure overview

The playbook is law. If anything in this prompt conflicts with the playbook, the playbook wins. Cite §-numbers when applying rules.

---

## STEP 2 — Scope (small, atomic)

This iteration rebuilds the homepage AND lights up the three canonical components for the first time. They go together because the homepage is the first page that needs them; once landed, every subsequent page imports them as-is.

### IN SCOPE

1. **`src/components/Header.astro`** — full implementation per Playbook §4.2
2. **`src/components/MegaMenu.astro`** — full implementation per §4.3 and §4.4
3. **`src/components/Footer.astro`** — full implementation per §4.5
4. **`src/pages/index.astro`** — the full homepage, replacing the v2.0.0 placeholder
5. Any **CSS additions** that the homepage and components require (page-level CSS in `<style>` blocks, or new files in `src/styles/` with clear naming)

### OUT OF SCOPE — DO NOT TOUCH

- Distributor page (next iteration, v2.2.x)
- Any collection page (luxoⒶRCH, planoⒶRCH, etc. — v2.3.x+)
- Any product detail page (v2.4.x+)
- The verification script (`scripts/verify.mjs`)
- The CI workflow (`.github/workflows/`)
- The `BrandMark.astro` component (already finalized in v2.0.0 — use it, don't modify it)
- The brand CSS (`src/styles/brand.css`) — REFERENCE the tokens, don't redefine them
- Any file in `docs/` — Claude updates docs after merge

If you need to modify something on the OUT OF SCOPE list to deliver the homepage, **stop and surface the conflict in your reply.** Do not silently expand scope. (§6.2)

---

## STEP 3 — Reference materials (use these to match the visual)

### Visual reference: v3.14.6 homepage

The last clean state from the prior platform. Treat as the visual target — same composition, same hierarchy, same look.

Files in `_reference/` (delivered with this prompt):

- `_reference/v3_14_6_homepage.html` — the full v3.14.6 HTML (read it; reproduce the structure as Astro components)
- `_reference/screenshots/homepage_full.png` — full-page screenshot
- `_reference/screenshots/megamenu_products.png` — Products mega-menu open
- `_reference/screenshots/megamenu_solutions.png` — Solutions mega-menu open
- `_reference/screenshots/featured_families.png` — Featured Families section detail
- `_reference/screenshots/footer.png` — Footer detail

You are NOT copying the HTML literally — you are reproducing the look and structure as proper Astro components. The HTML used copy-paste headers/footers; you are building them as imports. Same visual, different mechanics.

### Asset references

All production photography lives in `public/`. See `docs/assets.md` for the full inventory. Key files:

- Hero photos (5): `public/images/heroes/hero-{illuminator-stadium,warehouse-highbay,outdoor-area,controls-panel,commercial-office}.jpg`
- Featured Families (4): `public/images/families/family-{illuminator,titan,astra,contrals}.png`
- Verticals (5 of 8): `public/images/verticals/vertical-{warehouse,manufacturing,healthcare,education,government}.jpg`
- Brand: `public/brand/alg-logo-{color,white}.png`, `public/brand/alg-brandmark-{red,white}.png`
- Mega-menu tiles: `public/images/megamenu/mega-{constant,controls}.jpg`

### Missing assets — DO NOT FABRICATE

Three vertical photos and one mega-menu tile are missing. Per `docs/assets.md`:

- `vertical-coldstorage.jpg` — MISSING
- `vertical-datacenter.jpg` — MISSING
- `vertical-hospitality.jpg` — MISSING
- `mega-tubularch.jpg` — MISSING

For each missing asset, render a **graceful placeholder**:

```astro
<div class="vertical-card vertical-card--placeholder">
  <div class="placeholder-tile" aria-label="Photography pending">
    <span class="placeholder-label">Photography pending</span>
  </div>
  <h3>Cold Storage & Grocery</h3>
</div>
```

Style the placeholder as a soft grey tile with the family's name visible. **Do NOT generate or invent placeholder image files. Do NOT use a "stock photo" URL. Do NOT skip the missing verticals.** All 8 must be present in the section, with placeholders where photography is missing. Claude will source the missing 4 separately and they slot in later.

---

## STEP 4 — Required content (locked, do not deviate)

### Header content

**Top utility row** (small, right-aligned text):
- "Distributor Login" → `/distributor` (placeholder route, page comes in v2.2.x)
- "Find a Rep" → `/find-a-rep` (placeholder route)
- Cart icon → `https://algportal.archipelagolighting.com` (external, opens new tab; will become `https://shop.archipelagolighting.com` post-cutover per §3.8)

**Main nav row:**
- ALG logo (left) → `/`
- Primary nav (center): Products | Solutions | Resources | Support
- CTAs (right): Search icon, "Request Quote" button (primary red)

**Mobile:** hamburger collapses both rows; mega-menu becomes a drawer.

### Mega-menu content

Four buckets. Each bucket opens a panel with categorical content + a preview pane on the right.

**Products** — 4 categories, each a preview pane:
1. **Indoor Industrial** — slug `indoor-industrial` — preview tile: any indoor commercial photo (use `hero-warehouse-highbay.jpg` as preview)
2. **Outdoor C&I** — slug `outdoor-ci` — preview tile: `hero-outdoor-area.jpg`
3. **Linear & Specialty** — slug `linear-specialty` — preview: placeholder tile (mega-tubularch missing, use placeholder per Step 3)
4. **Controls & EM** — slug `controls-em` — preview tile: `mega-controls.jpg`

Each pane carries a "View Collection →" link. **The href is bound to the slug via Astro data flow, not hardcoded.** Pattern (§4.4):

```astro
const productCategories = [
  { slug: 'indoor-industrial', title: 'Indoor Industrial', preview: '/images/heroes/hero-warehouse-highbay.jpg' },
  { slug: 'outdoor-ci', title: 'Outdoor C&I', preview: '/images/heroes/hero-outdoor-area.jpg' },
  { slug: 'linear-specialty', title: 'Linear & Specialty', preview: null /* placeholder */ },
  { slug: 'controls-em', title: 'Controls & EM', preview: '/images/megamenu/mega-controls.jpg' }
];
---
{productCategories.map(cat => (
  <div class="mm-pane" data-cat={cat.slug}>
    <h3>{cat.title}</h3>
    {cat.preview ? <img src={cat.preview} alt={cat.title} /> : <div class="placeholder-tile">Photography pending</div>}
    <a href={`/collections/${cat.slug}`}>View Collection →</a>
  </div>
))}
```

The href and the data-cat MUST come from the same `cat.slug`. This is non-negotiable (§4.4).

**Solutions** — 8 verticals, each a card:
1. Warehouse & Logistics → `/solutions/warehouse-logistics`
2. Industrial & Manufacturing → `/solutions/industrial-manufacturing`
3. Cold Storage & Grocery → `/solutions/cold-storage-grocery`
4. Data Center → `/solutions/data-center`
5. Healthcare → `/solutions/healthcare`
6. Education → `/solutions/education`
7. Hospitality → `/solutions/hospitality`
8. Government & Military → `/solutions/government-military`

**Resources** — 4 cards (the §3.6 persona-page pattern):
1. Spec Sheets → `/resources/spec-sheets`
2. IES Files → `/resources/ies-files`
3. Family Sell Sheets → `/resources/sell-sheets`
4. Full Catalog → `/resources/catalog`

**Support** — 5 items:
1. Distributor Login → `/distributor`
2. Find a Rep → `/find-a-rep`
3. Photometric Layout Request → `/support/layout-request`
4. Warranty / RMA → `/support/warranty-rma`
5. Contact → `/contact`

### Homepage sections (top to bottom)

1. **Hero slider** — 5 slides using the 5 hero photos. Auto-rotate or manual. Each slide has:
   - Background image (full-bleed, dark overlay for text legibility)
   - Headline (specify per slide below)
   - Sub-headline / supporting text
   - Primary CTA button
   - Slide indicators (5 dots)

   Slide content (locked):
   - **Slide 1** (`hero-illuminator-stadium.jpg`): "Stadium-grade output, spec-grade reliability." / "Illuminator series — 25,000 to 200,000 lumens, DLC Premium." → "Explore Illuminator"
   - **Slide 2** (`hero-warehouse-highbay.jpg`): "From 5,000 to 250,000 sqft, we light it." / "Warehouse, manufacturing, cold storage. One catalog, every footprint." → "View Industrial Solutions"
   - **Slide 3** (`hero-outdoor-area.jpg`): "Outdoor C&I, built to ride out the weather." / "surgeⒶRMOR™ surge protection. IP65/IP66. Dark Sky options." → "View Outdoor Solutions"
   - **Slide 4** (`hero-controls-panel.jpg`): "Specify the fixture. Then specify the controls." / "sensorⒶBLE™, contrⒶLS by ⒶCS, code-compliant out of the box." → "Explore Controls"
   - **Slide 5** (`hero-commercial-office.jpg`): "Commercial offices and education, done right." / "LBLP panels and troffers. Title 24 compliant. CCT and wattage selectable in the field." → "View Indoor Solutions"

   Use `<BrandMark>` for every Ⓐ-bearing word.

2. **Featured Families section** — 4 cards in a grid:
   - Illuminator (image: `family-illuminator.png`) — tagline "Sports & Stadium" — link `/products/illuminator`
   - Titan-II (image: `family-titan.png`) — tagline "Warehouse High-Bay" — link `/products/titan-ii`
   - Astra (image: `family-astra.png`) — tagline "Wall Pack & Area" — link `/products/astra`
   - contrⒶLS (image: `family-contrals.png`) — tagline "Controls & EM" — link `/products/contrals` (use `<BrandMark>` for the Ⓐ in "contrⒶLS")

3. **"Specified. Stocked. Shipped." pillars section** — 3 columns:
   - **Specified** — Job-ready DLC Premium, IES files, photometric support
   - **Stocked** — Real inventory in Riverside CA. No 12-week lead times.
   - **Shipped** — Same-day shipping cutoff: 2 PM PT for in-stock SKUs

4. **Installed at section** — Grid of 8 vertical photos with vertical names overlaid. 5 photos present, 3 placeholders ("Photography pending"). Order matches §3.4.

5. **Featured Family / mid-page CTA** — band that links to "Photometric Layout Request" — body copy: "Have a project? Send us your DWG. We'll send you a stamped layout in 24-48 hours. No charge." → CTA "Request a Layout"

6. **Footer** — handled by `Footer.astro` (canonical component)

### Footer content

**Tagline row:**
- "Specified. Stocked. Shipped." (large, brand-red Ⓐ-style emphasis if you want — designer choice — but tagline text must be exactly that, no double periods)

**Four-column nav:**

- **Products:** Indoor Industrial / Outdoor C&I / Linear & Specialty / Controls & EM / View All Products
- **Solutions:** Warehouse & Logistics / Industrial & Manufacturing / Cold Storage / Data Center / Healthcare / Education / Hospitality / Government / View All Solutions
- **Resources:** Spec Sheets / IES Files / Family Sell Sheets / Full Catalog / Photometric Layout Request
- **Company:** About / Contact / Find a Rep / Distributor Login / Careers

**Sub-footer:**
- Left: "© 2026 Archipelago Lighting Group" + small ALG brand mark
- Center: addresses
  - HQ: 4615 State Street, Montclair, CA
  - USA Production: 9345 Sycamore Canyon Blvd, Riverside CA 92508
- Right: legal links — Terms / Privacy / Accessibility

**Bans (§3.5):** No CEU, AIA, IDCEC, HSW, LU, "accredited", "continuing education" anywhere on the page. CI hard-fails on these.

---

## STEP 5 — Mechanics & Workflow

### Branch & commits

1. From `main`, check out: `git checkout -b iter/v2.1.0-homepage`
2. Implement.
3. Commit progressively with messages that read clearly in `git log`:
   - `v2.1.0: scaffold Header.astro structure`
   - `v2.1.0: implement MegaMenu Products bucket`
   - `v2.1.0: implement MegaMenu Solutions bucket`
   - `v2.1.0: implement Footer canonical structure`
   - `v2.1.0: rebuild homepage hero slider`
   - `v2.1.0: rebuild homepage Featured Families section`
   - … etc.

   Roughly 10–15 commits is normal for an iteration this size. Single-commit megablobs are discouraged because they make review hard.
4. Push branch: `git push -u origin iter/v2.1.0-homepage`
5. Open Pull Request to `main`. PR title: `v2.1.0 — Homepage rebuild + canonical components`

### PR description template

```markdown
## v2.1.0 — Homepage rebuild + canonical components

### Playbook §-citations
- §1.1 Pipeline (Manus → GitHub → CI → Cloudflare)
- §3.1, §3.2, §3.3 Brand-mark rules (BrandMark component used)
- §3.4 Eight verticals
- §3.5 Copy bans (no accreditation)
- §3.6 Persona-page 4-card template (Resources mega-menu)
- §3.9 Asset naming
- §4.2 Header structure
- §4.3 Mega-menu structure
- §4.4 CTA href binding (data flow, not hardcoded)
- §4.5 Footer structure

### Implementation summary
- [list files created/modified]
- [list canonical components implemented for the first time]
- [note placeholder strategy for missing verticals]

### Verification
- CI: <link to GitHub Actions run>
- Preview URL: <Cloudflare Pages preview URL>
- `npm run verify` against dist: <PASS|FAIL — paste literal stdout>

### Known gaps
- [list any open questions or things deferred to next iteration]
```

### CI

When you push the branch, GitHub Actions will run:
1. `npm install`
2. `npm run build`
3. `npm run verify`

You will see green checks on the PR if all three pass. If any fail, fix and push again.

### Cloudflare Pages preview URL

When you open the PR, Cloudflare Pages will automatically build the branch and post a preview URL as a comment on the PR. The URL format will be similar to `iter-v2-1-0-homepage.alg-website.pages.dev`. The preview URL renders exactly what would deploy if the PR merged.

**Audit the preview URL, not your local dev server.** (§8.1, §8.2)

---

## STEP 6 — Reply contract (what your final response must include)

Per Playbook §7.1, your reply when the iteration is ready for review MUST include, in this order:

1. **First line:** `PLAYBOOK v2.0 §1 §2 §3 §4 §5 §6 §7 §8 READ — proceeding` (or, if responding after CI runs: `PLAYBOOK v2.0 §1 §2 §3 §4 §5 §6 §7 §8 READ — iteration v2.1.0 ready for review`)
2. **Branch:** `iter/v2.1.0-homepage`
3. **Commit summary:** numbered list of commit messages with their short hashes
4. **PR URL:** the GitHub Pull Request URL
5. **CI status:** literal status (PASS / FAIL / RUNNING) with link to the run
6. **Cloudflare preview URL:** the URL that renders the build
7. **Self-audit:** the LITERAL stdout of `npm run verify` against `dist/`. **Paraphrasing is rejected.** (§15) Paste it under a fenced code block.
8. **Open questions:** anything you encountered that needs James decision, called out clearly. If none, write "None."

### Forbidden in reply

- ❌ Paraphrased verification output ("all checks passed" without literal stdout)
- ❌ Claiming "ready" before CI returns PASS
- ❌ Verifying against `localhost` / your local dev sandbox instead of the Cloudflare preview URL
- ❌ Substituting a regex-shape check for actual binding verification (the v3.14.19 trap — DO NOT do this)
- ❌ Bundling additional pages or scope creep
- ❌ Inventing missing assets or fabricating data
- ❌ Modifying anything in the OUT OF SCOPE list

---

## STEP 7 — If you get stuck

If during implementation you discover:

- A spec conflict between this prompt and the playbook → **playbook wins, surface in reply**
- A required asset is missing AND there's no placeholder strategy in this prompt → **stop, surface in reply, do not invent**
- A check fails twice in a row in CI on the same root cause → **§10 escalation: surface the structural cause, do not silent-retry a third time**
- Anything where you'd be guessing about James intent → **stop, ask in reply**

Do NOT push half-finished work and claim "ready." A correctly-scoped iteration that asks one good question is better than a fully-pushed iteration with five silent assumptions.

---

## STEP 8 — Why this iteration is small

This iteration is one page + three components. It's deliberately the smallest unit that produces something visible. The reasons:

1. It validates the entire new pipeline (GitHub → CI → Cloudflare → preview URL → audit → merge → staging update). If the pipeline is broken, we discover it on iteration 1, not iteration 5.
2. The three canonical components, once locked, accelerate every subsequent iteration. Distributor page (v2.2.x) imports them as-is; collection pages (v2.3.x) likewise. The investment compounds.
3. James can audit it in 10 minutes, give a clean approve/reject, and we move.

If iteration 1 lands clean Sunday, the homepage is live on `staging.archipelagolighting.com` and the foundation is proven. From there, iterations cascade fast.

---

*End of prompt v2.1.0.*
