# How to audit a Manus reply contract

1. Open the per-deploy Cloudflare alias URL from the reply (NOT staging.archipelagolighting.com)
2. Scroll to the footer. Find the build-hash badge: `build a1b2c3d · 2026-04-28T03:14Z`
3. Confirm the build hash (a1b2c3d) matches the first 7 chars of the PR's commit hash
4. If they match: you are looking at the exact build that was claimed. Proceed with audit.
5. If they don't match: cache lag on Cloudflare. Wait 5 minutes, hard-reload (Cmd+Shift+R), retry.
6. If still mismatched after 10 minutes: real bug. Report in chat with: PR commit hash, observed build hash, screenshot.

## Why staging.archipelagolighting.com is not the canonical audit target

- DNS-aliased to the latest deploy, but the alias itself can lag
- CDN edge cache holds previous responses for minutes
- Browser cache holds CSS/JS/images for hours
- All three layers can serve "stale" content while Manus has already shipped

The per-deploy URL bypasses all three.

## Build hash badge location

Every page on the site renders a build-hash badge at the very bottom of the footer, below the copyright line:

```
build a1b2c3d · 2026-04-28T03:14Z
```

- `a1b2c3d` = first 7 chars of the git commit SHA this build was produced from
- `2026-04-28T03:14Z` = build timestamp in ISO 8601 UTC, minute precision

If the badge reads `build dev · local`, the page was built locally without GitHub Actions env vars — not a CI/CD build.

## Quick reference

| Scenario | Action |
|---|---|
| Badge hash matches PR commit | Audit with confidence — you are on the right build |
| Badge hash doesn't match | Wait 5 min, hard-reload (Cmd+Shift+R), retry |
| Still mismatched after 10 min | Report: PR commit hash + observed badge hash + screenshot |
| Badge reads `build dev · local` | Wrong URL — open the per-deploy URL from the reply contract |
| No badge visible | Track A from v2.7.7 failed — report as PR defect |
