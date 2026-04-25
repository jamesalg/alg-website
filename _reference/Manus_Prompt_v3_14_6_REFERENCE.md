# Manus — Homepage v3.14.6 Cleanup

**5 mechanical swaps + 1 brand-mark stem extension + 19-file asset ingestion. Publish with dev-strip bump.**

---

## 0. ASSET INGESTION (mandatory first step)

Drop the attached 19 files into `/manus-storage/` (or your equivalent asset directory). Preserve filenames exactly.

**From `ALG_NanoBanana_Assets/` (18 files):**

| Filename | Slotted for |
|---|---|
| `hero-slide1-illuminator-stadium.jpg` | Hero slide 1 (future swap, not this iteration) |
| `hero-slide2-warehouse-highbay.jpg` | Archive (future use) |
| `hero-slide3-outdoor-area.jpg` | Archive (future use) |
| `hero-slide4-controls-panel.jpg` | Archive (future use) |
| `hero-slide5-commercial-office.jpg` | **Hero slide 4 — THIS ITERATION, §3.1** |
| `alg-hero-sports.jpg` | Archive |
| `alg-hero-warehouse.jpg` | Archive |
| `alg-hero-outdoor.jpg` | Archive |
| `alg-layout-design.jpg` | Future: layout-request CTA section |
| `alg-product-illuminator.jpg` | Future: Illuminator product page |
| `installed-hospital.jpg` | Future: Installed-at vertical grid (Healthcare) |
| `installed-manufacturing.jpg` | Future: Installed-at (Industrial & Manufacturing) |
| `installed-municipality.jpg` | Future: Installed-at (Government & Military) |
| `installed-parking.jpg` | Future: Installed-at vertical |
| `installed-retail.jpg` | Future: Installed-at (Hospitality) |
| `installed-school.jpg` | Future: Installed-at (Education) |
| `installed-stadium.jpg` | Future: Illuminator product page |
| `installed-warehouse.jpg` | Future: Installed-at (Warehouse & Logistics) |

**From `wwm-safety-controls/` (1 file):**

| Filename | Slotted for |
|---|---|
| `wwm-safety-controls.jpg` | **WHAT WE MAKE / Safety & Controls card — THIS ITERATION, §3.3** |

Only `hero-slide5-commercial-office.jpg` and `wwm-safety-controls.jpg` are used THIS iteration. The remaining 17 files are ingested into storage for future surfaces (Illuminator PDP, Installed-at vertical strip, other surfaces in the wireframe march). No current assignment — just park them.

---

## 1. GLOBAL RULES — in effect, unchanged

- Author-time `@` → Ⓐ substitution — **stem list extends from 8 to 10 this iteration (see §3.5)**
- "ALG Portal" → "ALG Shop" global rename
- No accreditation claims anywhere
- Mega menu container size stays constant regardless of tier count
- Sign In links open in new tab
- Dev-strip MUST update with every version bump
- Self-report precision: before/after quotes for every claimed change
- Lock state from v3.14.5: tier-grid positioning (ECO slot 1 / PRO slot 2 / PRO+ slot 3 — locked, don't change)

---

## 2. NAME THIS VERSION

Dev-strip target:

```
MOCKUP v3.14.6 · April 24, 2026 · Manus-authored · Hero 4 clean office asset · WWM Indoor = Nano Banana club-store · WWM Safety = final composite · WWM card gap 24px + responsive left-justify · Stocked. single period · Brand stems +IM +PTICS
```

---

## 3. HOMEPAGE v3.14.6 — FIVE FIXES

### 3.1 Hero slide 4 — swap background image

**Current state:** Hero 4 renders the previous asset (`a1_01_hero_slide3.png`) which contained v3.6 page chrome baked in — dev-strip, nav bar, right-column hero panel all visible inside the hero area.

**Fix:** replace with `hero-slide5-commercial-office.jpg` from the asset pack. Clean photograph of a commercial office interior showing 2×2 back-lit panels in ceiling, people at desks, glass-walled conference room. No chrome, no baked-in text, full native dimensions (~3400×1900).

**Implementation guidance:**

```css
.hero-slide-4 .hero-bg {
  background-image: url('/manus-storage/hero-slide5-commercial-office.jpg');
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
}
```

All hero text overlays (H1 `Specified. Stocked. Shipped.`, eyebrow `COMMERCIAL & INDUSTRIAL · DLC PREMIUM`, product-panel right column with `proⒶRCH-III` + specs + CTAs) continue to render as HTML on top of the background — same pattern as heroes 1-3.

**Acceptance:** Hero 4 renders a clean office ceiling view. No dev-strip or nav bar visible inside the hero area. No duplicated `proⒶRCH-III` text inside the image.

### 3.2 WHAT WE MAKE / Indoor Luminaires — Nano Banana generation

**Current state:** Indoor Luminaires card shows a small-stockroom image (neither the v3.14.4 warehouse asset nor anything updated since).

**Fix:** generate a new image via Nano Banana (or your equivalent image generator) for this card specifically. Do **not** use `hero-slide2-warehouse-highbay.jpg` from the asset pack (that's for a different future surface). Generate fresh.

**Nano Banana prompt (use verbatim):**

> A wide interior photograph of a big-box club warehouse retail store (Costco-style), focused on the industrial high-bay LED luminaires mounted to the exposed-truss ceiling. Wide aisles between tall pallet racks stocked with bulk product. Polished concrete floor reflecting the lighting. Subtle warm-white LED glow from circular high-bay fixtures, evenly spaced across the ceiling grid. Focal emphasis on the lighting fixtures and their clean geometric arrangement. Photorealistic, commercial photography style, slight wide-angle lens, daytime ambient mixed with LED illumination. No people, no branded signage, no shopping carts.

Target filename: `wwm-indoor-warehouse-v2.jpg`. 4:3 or 3:2 aspect ratio works best for the card.

**Acceptance:** Indoor Luminaires card shows a big-box warehouse interior with industrial high-bay LED fixtures prominently visible in the ceiling. No fake branding, no people, no cart-level retail detail that distracts from the ceiling/lighting focus.

### 3.3 WHAT WE MAKE / Safety & Controls — swap image

**Current state:** Safety & Controls card shows a corridor with exit signs (from a previous Manus generation, not James's composite).

**Fix:** replace with `wwm-safety-controls.jpg` from the asset pack. This is James's final 6-product composite: emergency driver + battery pack + EXIT sign + occupancy sensor + wall controller + ceiling sensor, laid flat on cream background, matching existing Nano Banana mega-preview aesthetic.

**Acceptance:** Safety & Controls card displays the 6-product composite. All 6 products visible on cream background.

### 3.4 WHAT WE MAKE / Card spacing + responsive layout

**Current state:** 3 cards (Indoor / Outdoor / Safety & Controls) sit at ~56px gap between each card. Visually un-grouped — reads as 3 isolated tiles.

**Fix:** tighten gap to 24px. At narrow viewport, all cards left-justify (don't center, don't stretch) and flow as a wrapped row.

**Implementation:**

```css
.wwm-card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 380px));
  gap: 24px;
  justify-content: start;  /* left-justify, not center */
}
```

Breakpoint behavior:
- Desktop (3 cards fit): all 3 in a row, 24px gaps, left-justified
- Tablet / narrow (only 2 fit): 2 cards top row + 1 card second row, all left-justified
- Mobile (1 fits): single column, all left-justified

**Do NOT use** `justify-content: center` (spreads cards apart when container is wider) or `justify-content: space-between` (restores the big gaps James is fixing).

**Acceptance:** resize browser window from 1920px down to 400px. Cards stay tightly grouped (24px gap), wrap naturally, always left-justified — never centered, never spread to the edges.

### 3.5 Brand-mark stem extension — 8 stems → 10 stems

**Current state:** the author-time `@` → `Ⓐ` substitution rule covers 8 stems:  
`RCH, LS, NT, CS, BLE, RMOR, DAPT, MILY`

**Fix:** extend to 10 stems. Add:
- `IM` — for `powerⒶIM™` (sports-lighting pivot-hinge feature)
- `PTICS` — for `proⒶPTICS™` (NEMA 3-distribution optics feature)

**Updated regex / substitution list:**

```
/@(?=RCH|LS|NT|CS|BLE|RMOR|DAPT|MILY|IM|PTICS)\b/g → Ⓐ
```

These two stems don't appear on the current homepage (they're sports-lighting specific, surfacing on the Illuminator PDP in a future iteration). But the substitution rule goes live now so that any content brought in from Zoho or datasheets renders the brand marks correctly.

**Acceptance:** a grep for `@(?=RCH|LS|NT|CS|BLE|RMOR|DAPT|MILY|IM|PTICS)` across the published page returns **zero matches** (all should be `Ⓐ`). Where `@IM` and `@PTICS` aren't present in current copy, the rule is latent — which is correct.

### 3.6 Hero H1 typo — `Stocked..` → `Stocked.`

**Current state:** hero H1 across all 4 slides reads `Specified. Stocked.. Shipped.` — double period after "Stocked".

**Fix:** remove one period. Target:

```
Specified. Stocked. Shipped.
```

Single period after each word.

**Acceptance:** rendered HTML source shows exactly one `.` after `Stocked` in the H1.

---

## 4. REPLY FORMAT

1. Permanent URL (unchanged — same `.manus.space` domain, newer published content)
2. Verification commands:
   ```
   curl -s https://alglighting-he6frhek.manus.space/index.html | grep -oP 'MOCKUP v[\d.]+' | head -1
   # Expected: MOCKUP v3.14.6
   
   curl -s https://alglighting-he6frhek.manus.space/index.html | grep -c 'Stocked\.\.'
   # Expected: 0
   
   curl -s https://alglighting-he6frhek.manus.space/index.html | grep -cP '@(?=RCH|LS|NT|CS|BLE|RMOR|DAPT|MILY|IM|PTICS)'
   # Expected: 0
   ```
3. Before/after quotes for each of the 5 fixes. Per playbook §2, "Done" alone is not acceptable.
4. Screencaps at 1440×900 desktop:
   - v3.14.6-01: Hero 4 showing clean office ceiling (no chrome)
   - v3.14.6-02: WWM Indoor Luminaires showing new Nano Banana club-store image
   - v3.14.6-03: WWM Safety & Controls showing 6-product composite
   - v3.14.6-04: WWM section at 1920px viewport — 3 cards with 24px gaps, left-justified
   - v3.14.6-05: WWM section at 900px viewport — 2 cards top + 1 card below, all left-justified
   - v3.14.6-06: WWM section at 400px viewport — single column, left-justified
   - v3.14.6-07: Hero H1 close-up showing `Stocked.` single period

---

## 5. OUT OF SCOPE FOR v3.14.6

- Illuminator product page (separate storyboard in flight — Manus spec to follow)
- luxoⒶRCH collection page (separate storyboard in flight — Manus spec to follow)
- Distributor page (no changes this iteration; v1.0.4 stays)
- Application page layer (Architectural Linear storyboard paused pending collection + series work)
- Installed-at vertical strip real photos (assets are ingested but not yet slotted — future iteration)
- Other persona pages (EC, Specifier, ESCO, Contractor, End User)

---

## 6. CONTEXT — LOCKED ITEMS (DO NOT CHANGE)

- Tier-grid positioning (ECO=1, PRO=2, PRO+=3) — locked from v3.14.5
- Mega menu tier card sizing — currently ~260×260, locked
- Hero slide 1, 2, 3 images — unchanged this iteration
- Persona chip links (Distributor → /distributor.html) — locked
- ALG logo → homepage link — locked
- Footer content — unchanged
