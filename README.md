# ALG Website — v2.0

The corporate website for Archipelago Lighting Group (ALG), a commercial and industrial LED lighting manufacturer.

**Live site:** `https://archipelagolighting.com` (after cutover; currently Shopify)
**Staging:** `https://staging.archipelagolighting.com` (Cloudflare Pages, auto-deploys from `main`)
**Domain registrar:** GoDaddy (DNS stays at GoDaddy, see Playbook §11)

## Architecture

```
Manus (builder) → GitHub (source of truth) → Cloudflare Pages (host) → Custom domain
```

- **Stack:** Astro (static site generator), CSS, no JS framework
- **Hosting:** Cloudflare Pages (Free tier — unlimited bandwidth, atomic deploys)
- **CI:** GitHub Actions runs `npm run build` + `npm run verify` on every PR
- **Cost:** ~$0/mo new spend (replaces ~$83/mo Shopify)

## Project structure

```
.
├── docs/                          # Playbook, lock register, iteration log, asset inventory
│   ├── ALG_Build_Playbook_v2.0.md ← the operating discipline (READ THIS FIRST)
│   ├── lock_register.md           ← what cannot change without explicit reopen
│   ├── ITERATION_LOG.md           ← what's merged so far
│   └── assets.md                  ← asset inventory + gaps
├── public/                        # Static assets served as-is
│   ├── brand/                     # Logos, brand marks
│   └── images/
│       ├── heroes/                # Hero slider photography
│       ├── verticals/             # "Installed at" vertical photography
│       ├── families/              # Featured Family hero shots
│       └── megamenu/              # Mega-menu preview tiles
├── src/
│   ├── components/                # Astro components
│   │   ├── BrandMark.astro        ← Ⓐ wrapping utility (mechanical brand-mark rule)
│   │   ├── Header.astro           ← Canonical site header (every page imports)
│   │   ├── MegaMenu.astro         ← Canonical mega-menu drawer
│   │   └── Footer.astro           ← Canonical site footer
│   ├── layouts/
│   │   └── BaseLayout.astro       ← Wraps every page with Header + Footer
│   ├── pages/                     # Each .astro file = one URL route
│   │   └── index.astro            ← Homepage (placeholder until Iteration 1)
│   └── styles/
│       ├── brand.css              ← Brand tokens, .aa class for Ⓐ
│       └── global.css             ← Containers, typography scale, buttons
├── scripts/
│   └── verify.mjs                 ← Verification suite (runs in CI)
├── .github/workflows/
│   └── build-and-verify.yml       ← CI pipeline
├── astro.config.mjs               ← Astro config (static output, Cloudflare-friendly)
├── package.json
└── README.md (this file)
```

## Local development

Requires Node.js 20+.

```bash
npm install              # one-time
npm run dev              # local dev server at http://localhost:4321
npm run build            # produces dist/ — what Cloudflare deploys
npm run verify           # runs the playbook check suite against dist/
```

## Discipline

**Read `docs/ALG_Build_Playbook_v2.0.md` before making any change.** It governs:

- How iterations are scoped, named, and merged
- Brand-mark rules (the Ⓐ character, the 10 stems, casing rules)
- Copy bans (no accreditation, no "CLEARANCE", no "SunSmart")
- Canonical components (3 of them, byte-identical via Astro)
- CTA href binding (the v3.x failure mode, structurally fixed in Astro)
- CI verification (mechanical, hard-fail on violations)
- Manus prompt + reply contracts
- DNS / cutover protocol

## Roles

- **James Deng (PM, ALG):** product owner, decision gate, visual auditor
- **Claude:** architect, prompt author, PR reviewer
- **Manus AI:** implementation (writes Astro components, opens PRs)
- **Cloudflare Pages + GitHub Actions:** automated deploy + verify

## How to pick this up cold (new session, no memory)

1. Read this README
2. Read `docs/ALG_Build_Playbook_v2.0.md` end-to-end
3. Read `docs/ITERATION_LOG.md` to see what's merged
4. Read `docs/lock_register.md` to see what's locked
5. Fetch `https://staging.archipelagolighting.com` to see the current deployed state
6. Compare to `git log --oneline` on `main` — they should agree

If they disagree, infrastructure is the suspect. Surface to James before iterating.
