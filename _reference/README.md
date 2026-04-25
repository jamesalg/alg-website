# Reference Materials — v3.14.6

These files are the visual target for v2.1.x homepage rebuild. They are NOT to be deployed; they live here only for Manus to study while implementing.

**These files are excluded from the build.** The folder is not part of `dist/`.

## Files

- `v3_14_x_live_homepage.html` — the homepage as it was deployed on the prior platform (v3.14.x state). This is the structural reference. Do not copy-paste; reproduce in Astro components.
- `v3_10_homepage_reference.html` — earlier state (v3.10) for additional reference if helpful
- `Manus_Prompt_v3_14_6_REFERENCE.md` — the v3.14.6 prompt that produced the visual we trust
- `screenshots/` — visual references (full page, individual sections, mega-menu states)

## How to use these

1. Open `v3_14_x_live_homepage.html` and scan the section structure — hero slider, Featured Families, "Installed at", footer
2. Look at the screenshots for visual / typographic reference
3. Reproduce the look using Astro components (Header, MegaMenu, Footer, BrandMark) and inline page CSS where appropriate

**Do NOT** ship the v3.14.x HTML or its `manus-storage/` image references. The new repo uses its own `public/` paths.

## After v2.1.x merges

Once iteration 1 lands clean, Claude will assess whether to keep this folder or remove it. Keeping it doesn't hurt (excluded from build), but it adds repo weight. Likely outcome: archive the folder after v2.3.x or so.
