# Iteration Log — ALG Website v2.0

Per Playbook v2.0 §13. Every iteration that merges to `main` gets an entry here.

---

## v2.0.0 — Foundation

**Merged:** (pending — initial commit)
**Author:** Claude (architect)
**Scope:** Repository scaffolding only.

**Includes:**
- Astro project skeleton (`package.json`, `astro.config.mjs`, `.gitignore`)
- Component scaffolds: `Header.astro`, `MegaMenu.astro`, `Footer.astro`, `BrandMark.astro`
- Base layout: `BaseLayout.astro`
- Global styles: `brand.css`, `global.css`
- Placeholder homepage (replaced in v2.1.x)
- Verification suite: `scripts/verify.mjs`
- CI workflow: `.github/workflows/build-and-verify.yml`
- 23 production assets carried forward from v3.14.6
- Documentation: Playbook v2.0, Lock Register v2.0, this log, asset inventory

**Excluded by design (v2.0.0 scope boundary):**
- No actual page implementation — that's v2.1.x
- No real Header/MegaMenu/Footer markup — scaffolds only
- No content beyond brand-mark utility test on placeholder homepage

**Verification:** `npm run build` succeeds, `npm run verify` passes against placeholder.

---

## Upcoming

- **v2.1.x — Homepage rebuild** (Manus iteration 1)
- **v2.2.x — Distributor persona page** (sibling to homepage, reuses canonical components)
- **v2.3.x — Collection template** (luxoⒶRCH or planoⒶRCH first; the other hydrates fast)
- **v2.4.x — Illuminator PDP from Storyboard B**
- **v2.5.x+ — Sibling collections** (lamparⒶRCH, cityⒶRCH, tubulⒶRCH)
