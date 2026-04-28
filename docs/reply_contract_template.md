# Reply Contract Template

Use this template for every PR reply contract. All sections are required unless marked optional.

---

## 1. Build output

Paste the literal `npm run build` stdout here.

```
[build] XX page(s) built in X.XXs
[build] Complete!
```

## 2. Verifier output

Paste the literal `node scripts/verify.mjs` stdout here. Must end with `ALL CHECKS PASSED`.

```
Verifying XX HTML file(s)...
✅ ...
✅ ALL CHECKS PASSED
Verified XX HTML file(s) — no violations.
```

## 3. Commit hash on main

Short (7-char) commit hash after squash-merge. This hash will appear in the build-hash badge in the footer.

```
{7-char hash} — squash-merged from {branch} via PR #{number}
```

## 4. Auto-merge status

```
Auto-merge enabled: YES, mergeMethod: SQUASH
```

## 5. Per-deploy Cloudflare alias URL — canonical audit target — REQUIRED, NOT staging.archipelagolighting.com

This per-deploy URL is the canonical audit target for this PR. James will audit THIS URL, not the
staging alias. The per-deploy URL is immutable and bypasses CDN/DNS/browser cache —
it points at the exact build artifact for this PR.

Format: `https://alg-website-6ar-{commit-hash}.pages.dev` (or whatever Cloudflare Pages
issues for this deploy)

After verifying the build-hash badge in the footer of this URL matches the commit
hash on this PR (Track A from v2.7.7), audits are unambiguous: what's rendered there
IS what shipped.

**If the per-deploy URL is missing from this reply, the PR is auto-failed regardless of
other evidence.**

## 6. Per-track table

| Track | Status | Evidence |
|-------|--------|----------|
| {Track label} | ✅/❌ | {Description of evidence} |

## 7. Mandatory greps

Paste each grep command and its output.

## 8. Screenshots

Attach screenshots as specified in the PR prompt.

## 9. Open questions (optional)

List any deviations, surprises, or items requiring James's decision.
