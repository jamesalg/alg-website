# ALG Website Build Playbook v2.0

**Owner:** James Deng (Senior PM, ALG)
**Architect / Quality Gate:** Claude
**Builder:** Manus AI
**Effective:** 2026-04-25
**Replaces:** Playbook v1.0 (deprecated — see "What Changed from v1.0" at end)

---

## §0 Purpose & Scope

This playbook governs the rebuild of the Archipelago Lighting Group corporate website on a new architecture: **GitHub repo → Cloudflare Pages → custom domain**. Manus generates Astro components and commits them to the GitHub repo. Cloudflare Pages auto-builds and deploys. There is no separate "publish" step controlled by Manus.

The playbook exists for one reason: **make the unreliability of any LLM-based code generator visible at the door, so unreliable output never reaches production.** Every rule below maps to a specific failure mode observed during the v3.x build cycle on the prior platform.

---

## §1 Architecture & Source-of-Truth Hierarchy

### §1.1 The pipeline

```
Manus → GitHub feature branch → CI build & verify →
PR review (Claude) → merge to main → Cloudflare auto-deploy →
staging.archipelagolighting.com → (cutover) www.archipelagolighting.com
```

### §1.2 Sources of truth, ranked

When two facts conflict, the higher-ranked source wins. Always.

1. **The Git repository on `main`** — the canonical state of the website. What lives in `main` IS the website.
2. **CI build output (`dist/`)** — what `main` looks like when built. Never assume; always verify against this.
3. **`staging.archipelagolighting.com`** — what users see. Updated automatically from `main` via Cloudflare Pages.
4. **PR preview URLs** (`*-alg-website.pages.dev`) — what a feature branch looks like. Used for visual audit before merge.
5. **Local dev server** — for the developer's eyes only. Never authoritative.
6. **Manus's verbal claims** — never authoritative. Verify against #1–#4 before believing.

### §1.3 Zoho Books org `729902814` is the source of truth for product data

When a product spec or SKU is in question, search Zoho. Cross-check `cf_echelon`. James's marketing override beats Zoho's `cf_echelon` when explicit (e.g., proⒶRCH-II is Zoho-PRO but James-positioned ECO for Panel) — log both values when the override is applied.

---

## §2 The iteration model

### §2.1 Iteration size

**Small.** One feature branch = one page or one cohesive component upgrade. No mega-iterations. The v3.x cycle's biggest mistake was scope creep within an iteration; this playbook prevents it by branch convention.

### §2.2 Iteration lifecycle

1. Claude writes a Manus prompt with explicit scope, references, and §-citations of the rules that apply.
2. Manus checks out a new feature branch named `iter/v{N.N.N}-{slug}` (e.g., `iter/v2.0.1-homepage`).
3. Manus implements the scope. Commits go to the feature branch.
4. Manus opens a Pull Request to `main`. PR description must include:
   - The version label (e.g., `v2.0.1`)
   - The §-citations of every playbook rule the iteration touches
   - A "VERIFICATION" section listing CI status + visual review URL
5. CI runs automatically: `npm run build` + `npm run verify`. Both must pass.
6. Cloudflare Pages auto-builds the branch into a preview URL.
7. Claude (or James) audits the preview URL.
8. If audit passes → Claude approves PR → merge to `main` → Cloudflare promotes to `staging`.
9. If audit fails → Claude writes correction prompt → Manus pushes new commit to same branch → loop from step 5.

### §2.3 Versioning

Iteration version numbers follow `v{major}.{minor}.{patch}`:

- **major** bumps when the architecture changes (currently 2 — GitHub+Cloudflare+Astro)
- **minor** bumps per locked page or major feature (1 = homepage, 2 = distributor, 3 = collection template, etc.)
- **patch** bumps per iteration within a minor (.1 first attempt, .2 if corrections, etc.)

Each merge to `main` auto-tags the commit with its version (e.g., Git tag `v2.1.0`). Rollback is `git revert` + Cloudflare auto-redeploys.

### §2.4 Locking semantics

A page or component is **locked** when:
- It has been merged to `main`
- Subsequent iterations on OTHER work cannot modify it
- Modifying a locked file requires a new iteration that explicitly says `REOPEN: <file or §>` in the prompt

Branch protection rules enforce this at the PR level — PRs that touch a locked path must be flagged.

---

## §3 Brand-mark and copy rules (CONTENT LAYER)

### §3.1 The 10 sanctioned brand stems

`Ⓐ` may only attach to these stems:

```
RCH    LS     NT     CS     BLE
RMOR   DAPT   MILY   IM     PTICS
```

Any other stem proposed needs explicit James approval and an entry in §3.1.

### §3.2 Casing rules

Each brand mark has a single canonical casing. Common applications:

- `proⒶRCH-III`, `planoⒶRCH`, `luxoⒶRCH`, `lamparⒶRCH`, `cityⒶRCH`, `tubulⒶRCH` — lowercase prefix, uppercase suffix
- `sensorⒶBLE`, `surgeⒶRMOR`, `quickⒶDAPT`, `contrⒶLS`, `constⒶNT` — lowercase prefix, uppercase suffix
- `multi-fⒶMILY` — **lowercase m AND lowercase f, only Ⓐ uppercase.** Capital M is a regression.
- `ⒶCS` — used as a brand acronym, e.g., "ⒶCS by ALG"
- `powerⒶIM`, `proⒶPTICS` — lowercase prefix, uppercase suffix

### §3.3 Ⓐ wrapping (mechanical)

Every `Ⓐ` in body text must be rendered through the `BrandMark.astro` component, which wraps it in `<span class="aa">`. The `.aa` class gives it brand red color and the slight optical adjustment.

- **Forbidden:** naked `Ⓐ` in raw HTML
- **Forbidden:** lowercase `ⓐ` (U+24D0) — wrong character entirely
- **Forbidden:** entity `&#9424;` (lowercase entity)
- **Allowed:** entity `&#9398;` if HTML entities required; `Ⓐ` U+24B6 directly preferred

The verification suite (CI) hard-fails on naked Ⓐ, lowercase ⓐ, or capital-M `Multi-f...`.

### §3.4 The 8 verticals

Locked. Other vertical names propose-and-approve only.

```
1. Warehouse & Logistics
2. Industrial & Manufacturing
3. Cold Storage & Grocery
4. Data Center
5. Healthcare
6. Education
7. Hospitality
8. Government & Military
```

### §3.5 Copy bans

**No accreditation claims anywhere.** CEU / AIA / IDCEC / LU / HSW / "accredited" / "continuing education" — all banned. CI hard-fails on these.

### §3.6 Marketing-Assets persona-page card template

Every persona page (Distributor, EC, Specifier, etc.) renders its Marketing Assets section as **exactly four cards**:

```
1. Spec Sheets
2. IES Files
3. Family Sell Sheets
4. Full Catalog
```

No Product Photography card. No Compliance Pack card. No five-card variants.

### §3.7 Lifecycle states (product cards, packaging)

```
ACTIVE → green
GEN-2  → yellow
LEGACY → grey
```

**"CLEARANCE" badge is banned everywhere.** CI hard-fails.

### §3.8 Brand naming

- "ⒶCS by ALG App" — never "SunSmart" (SunSmart is banned, CI hard-fails)
- "ALG Shop" — replaces "ALG Portal" (rename applied 2026-04-24). The URL `algportal.archipelagolighting.com` stays live during dev. Pre-cutover reminder: rename to `shop.archipelagolighting.com` BEFORE main DNS cutover.
- "AURA" — Sales Rep portal, external link, no design needed
- Sales Rep data lives in **Zoho Books Salespersons**, not CRM

### §3.9 Asset naming convention

- **Forbidden:** index-numbered filenames that conflict with UI slot indices (e.g., `hero-slide1.jpg`, `hero-slide2.jpg`). Manus pattern-matches numbers literally and ignores explicit mapping.
- **Required:** descriptive-only names (e.g., `hero-illuminator-stadium.jpg`, `hero-controls-panel.jpg`).
- **Asset directories:**
  - `public/brand/` — logos, brand marks
  - `public/images/heroes/` — hero photography
  - `public/images/verticals/` — "installed at" photography (one per vertical)
  - `public/images/families/` — Featured Family hero shots
  - `public/images/megamenu/` — mega-menu preview tiles

---

## §4 Canonical components (STRUCTURAL LAYER)

### §4.1 The three canonical components

Three site-wide components are imported by every page via `BaseLayout.astro`:

1. **`Header.astro`** — top utility row + main nav + mega-menu trigger
2. **`MegaMenu.astro`** — the mega-menu drawer (Products / Solutions / Resources / Support)
3. **`Footer.astro`** — tagline + 4-column nav + sub-footer

By Astro's component model, every page renders these byte-identically. **No copy-paste, no md5 verification needed.** The v1.0 playbook's md5 dance is gone, structurally obsolete.

### §4.2 Header structure

- **Top utility row:** Distributor Login, Find a Rep, Cart icon → external `shop.archipelagolighting.com` link (during dev: `algportal.archipelagolighting.com`)
- **Main nav row:** Logo (left), primary nav (center), Search + "Request Quote" CTAs (right)
- **Mobile:** hamburger collapses both rows; mega-menu becomes drawer

### §4.3 Mega menu structure

Four primary nav buckets:

1. **PRODUCTS** — 4 categories (Indoor Industrial / Outdoor C&I / Linear & Specialty / Controls & EM). Each category has its own preview pane on the right.
2. **SOLUTIONS** — the 8 verticals (§3.4)
3. **RESOURCES** — Spec Sheets / IES Files / Family Sell Sheets / Full Catalog (the §3.6 four-card pattern)
4. **SUPPORT** — Distributor Login / Find a Rep / Photometric Layout Request / Warranty/RMA / Contact

### §4.4 CTA href binding (was the v3.x failure)

Every preview pane has a "View Collection →" CTA. The CTA's `href` MUST be derived from the same data prop as the pane's label. In Astro, this looks like:

```astro
{categories.map(cat => (
  <div class="pane" data-cat={cat.slug}>
    <h3>{cat.title}</h3>
    <a href={`/collections/${cat.slug}`}>View Collection →</a>
  </div>
))}
```

This binding cannot drift. The v3.x failure (10 panes all routing to luxoⒶRCH) was caused by hardcoded duplicated divs with copy-paste hrefs that diverged from the labels. In Astro, the data flows from one source.

### §4.5 Footer structure

- **Tagline row:** "Specified. Stocked. Shipped." (no double-period typos — caught by CI text checks)
- **Four-column nav:** Products / Solutions / Resources / Company
- **Sub-footer:** legal links, contact, copyright, addresses
  - HQ: 4615 State Street, Montclair, CA
  - USA Production: 9345 Sycamore Canyon Blvd, Riverside CA 92508

---

## §5 CI verification (MECHANICAL LAYER)

### §5.1 What CI runs on every commit

```
1. npm ci          → install dependencies
2. npm run build   → Astro builds dist/
3. npm run verify  → scripts/verify.mjs runs all check groups
```

If any step fails, the PR cannot merge. No exceptions, no overrides without explicit James-approval comment.

### §5.2 Verification check groups

- **Group A — Build integrity:** dist/ exists, has HTML files, no leaked `[object Object]` or `undefined`
- **Group B — Brand-mark rules:** no naked Ⓐ, no lowercase ⓐ, no `Multi-f` capital M, no forbidden entities
- **Group C — Copy policy:** no accreditation terms, no "CLEARANCE", no "SunSmart"
- **Group D — Page metadata:** every page has title and description meta
- **Group E — Image-asset integrity:** every `<img>` resolves to a file in `public/`
- **Group F — Link integrity:** internal links point to existing routes (caught at build time by Astro)

### §5.3 What CI does NOT replace

- **Visual audit by James (or Claude as proxy)** is required before merge. CI catches mechanical rule violations; it does not catch ugly typography or wrong photography.
- **Content review** — facts, copy, product specs. Always verify against Zoho.

---

## §6 Manus prompt contract (INCOMING CONTRACT)

### §6.1 Every prompt must include, in this order:

1. **Iteration label** — `Manus Prompt v{N.N.N}` and one-line scope
2. **Playbook §-citations** — list of every rule that applies (e.g., "Touches §3.1, §3.3, §4.2, §4.3")
3. **Reference materials** — e.g., "Use v3.14.6 visual language as reference; assets in `public/images/`"
4. **Scope boundary** — explicit "out of scope" list to prevent creep
5. **Required mechanics** — branch name, PR title pattern, expected commit count
6. **Verification expectations** — what CI must pass, what visual states James will audit
7. **Reply contract** — see §7

### §6.2 What prompts MUST NOT do

- Bundle two pages into one prompt
- Reference v1.0 playbook sections (deprecated)
- Use index-numbered file names
- Include speculative SKUs or fabricated data

---

## §7 Manus reply contract (OUTGOING CONTRACT)

### §7.1 Every Manus reply must include, verbatim, in this order:

1. **First line:** `PLAYBOOK v2.0 §<list> READ — proceeding`
2. **Branch name created:** e.g., `iter/v2.0.1-homepage`
3. **Commit summary:** list of commit messages with hashes
4. **PR URL:** the GitHub Pull Request URL
5. **CI status:** "PR build and verify status: <PASS|FAIL|RUNNING>"
6. **Preview URL:** the Cloudflare Pages preview URL for the branch
7. **Self-audit:** the LITERAL stdout of `npm run verify` against the build (paraphrasing forbidden — §15)
8. **Open questions:** anything unresolved that requires James decision

### §7.2 What replies MUST NOT do

- Paraphrase verification output (§15 — paraphrasing is rejected)
- Claim "ready" before CI status returns PASS
- Reference iteration history that wasn't merged to `main`
- Substitute a regex-shape check for an actual binding check (was the v3.14.19 trap)

---

## §8 Verification & validation principles

### §8.1 The cardinal rule

**The deployed preview URL is ground truth. Manus's local sandbox is not.** All verification claims must be backed by output from the deployed Cloudflare preview, not from Manus's `astro dev` server.

### §8.2 Why this rule exists

In the v3.x cycle, Manus's regression suite ran in its build sandbox and reported PASS while the actual deployed origin served stale content. We discovered this only after 12 iterations. In v2.0, CI runs against `dist/` (the build that WILL deploy) and the Cloudflare preview URL serves exactly that build atomically. The disconnect is structurally impossible.

### §8.3 The five diagnostic questions for any anomaly

When anything looks off:

1. What does `git log` show on `main`? (the canonical state)
2. What did the latest CI run say? (the build's verification status)
3. What does the Cloudflare preview URL serve? (the deployed truth)
4. What does Manus claim? (the hypothesis — verify against 1–3)
5. Does Manus's claim match 1–3? If not, Manus's claim is wrong.

---

## §9 Lock register

A separate file `docs/lock_register.md` tracks every locked component, page, and decision. Initially empty (everything is open until iteration 1 lands).

When a page or component is merged to `main`, it gets an entry:

```
| Lock ID | Path                          | Locked at | Locked by | Reopen requires |
| L01     | src/components/Header.astro   | v2.1.0    | James     | Explicit prompt |
```

PRs touching a locked path must include a `REOPEN: <Lock ID>` line in the description.

---

## §10 Escalation rules

### §10.1 The two-failure rule

If the same check fails in two consecutive iterations, the next response must include an `## ESCALATION` section that surfaces the structural cause. No third silent retry permitted.

### §10.2 Infrastructure vs. content failure modes

If CI passes locally but the Cloudflare preview shows different content, **stop iterating immediately and surface to Claude/James.** This is an infrastructure failure mode, not a code failure mode. Prompt-engineering cannot fix it.

### §10.3 When to halt and re-architect

Halt the build queue and consult Claude+James when:

- A check fails three iterations in a row
- An infrastructure failure (deploy pipeline, CDN, DNS) is suspected
- A new failure mode emerges that wasn't anticipated by the playbook
- An iteration's actual scope exceeds the prompt's stated scope

---

## §11 DNS & domain ownership

### §11.1 Registrar

GoDaddy. James owns `archipelagolighting.com` and four sibling domains. **DNS stays at GoDaddy** — we do NOT migrate to Cloudflare's nameservers. This avoids touching the existing email (Microsoft 365), `aura.archipelagolighting.com`, `algportal.archipelagolighting.com`, and other production records.

### §11.2 DNS records relevant to this build

- `staging.archipelagolighting.com` → CNAME → `alg-website.pages.dev` (added 2026-04-25)
- `www.archipelagolighting.com` → currently points to Shopify; will flip to Cloudflare on cutover day
- All other records (MX, AURA, ALG Shop / Portal) — DO NOT TOUCH

### §11.3 Cutover protocol (future)

Pre-cutover (HOURS before flipping main DNS):
1. Confirm `staging.archipelagolighting.com` shows the build that will go live
2. Rename portal URL `algportal.archipelagolighting.com` → `shop.archipelagolighting.com` so internal links don't break
3. Final visual audit on staging
4. Update `www` CNAME at GoDaddy → Cloudflare's domain target
5. Wait for DNS propagation, verify
6. Monitor for 24h, keep Shopify subscription active
7. After 1 week clean, cancel Shopify

---

## §12 What changed from Playbook v1.0

| Concept | v1.0 (deprecated) | v2.0 (current) |
|---|---|---|
| Hosting | Manus preview subdomain | Cloudflare Pages |
| Source of truth | Live URL fetched HTML | Git repo on `main` |
| Canonical components | Copy-paste HTML, md5 verified | Astro components, byte-identical by construction |
| Verification | `regression_suite.sh` against live URL | `npm run verify` against `dist/`, in CI |
| Lock register | Markdown honor system | Branch protection + PR labels |
| Manus delivery | `v{version}_Package.zip` containing prompt + assets | Git PR with branch, commits, preview URL |
| Deploy attestation | Manus claimed "checkpoint ready" | CI + Cloudflare deploy status |
| Rollback | None reliable | `git revert` + auto-redeploy |
| Path equivalence | Required md5 of `/` vs `/index.html` | N/A (single static build, single origin) |
| Brand mark verification | Manual review | CI hard-fail on violations |

The v3.x failure modes that v2.0 structurally eliminates:

- **Publish silently no-ops:** Cloudflare Pages reports deploy status via API; CI sees PASS or FAIL.
- **Path divergence:** Static build, atomic deploy. `/` and `/index.html` are the same file by definition.
- **Sandbox vs. live mismatch:** CI runs against `dist/` which IS what deploys.
- **Canonical drift:** Astro components — same source, every page imports.
- **CTA href divergence:** Astro data flow — single source per category.
- **False completion claims:** PR status is API-reported, not narrated. Cannot be paraphrased away.
- **Manus's stuck-state recovery:** `git revert` is atomic. Rollback is one command.

---

## §13 Stranger test

This playbook is written so a Claude instance with no prior session memory can pick it up and continue the build. The architectural decisions are documented; the rules are explicit; the file paths are stable.

**One thing to verify before responding to anything in a new session:**

1. Fetch `https://staging.archipelagolighting.com` and confirm the current state matches the latest tag in the GitHub repo
2. Read this file (`ALG_Build_Playbook_v2.0.md`)
3. Read `docs/lock_register.md` to know what's locked
4. Read `docs/ITERATION_LOG.md` to see what's been merged

**One thing to NEVER do:** trust Manus's verbal claims without verifying against the GitHub repo and the Cloudflare preview URL.

**One thing to ALWAYS do:** when uncertain, fetch the staging URL and compare to `git log`. The repo is the truth.

---

*End of Playbook v2.0.*
