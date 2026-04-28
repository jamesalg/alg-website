# Cloudflare Pages Build Configuration

## Required settings in the CF Pages dashboard

Navigate to: **Workers & Pages → alg-website → Settings → Build & deployments**

### Build command

```
npm run cf-build
```

**NOT** `npm run build`. The `cf-build` script passes Cloudflare's built-in `CF_PAGES_COMMIT_SHA` and `CF_PAGES_BUILD_DATE` env vars into the Astro static build, which stamps every page footer with the real 7-char commit hash.

Using `npm run build` (without the env vars) produces `build dev · local` on every page.

### Build output directory

```
dist
```

### Root directory

```
/
```

### Node.js version

```
20
```

### Environment variables

No additional environment variables are required. The `cf-build` script reads from CF Pages' own built-in variables:

| CF Built-in Variable | Used as |
|---|---|
| `CF_PAGES_COMMIT_SHA` | `PUBLIC_BUILD_HASH` (7-char slice in Footer.astro) |
| `CF_PAGES_BUILD_DATE` | `PUBLIC_BUILD_TIME` (ISO timestamp in Footer.astro) |

These are injected automatically by CF Pages — no manual configuration needed.

## Verification

After changing the build command, trigger a new deploy. Visit any page on the resulting `alg-website-XXX.pages.dev` URL and confirm the footer badge reads:

```
build {7-char commit hash} · {ISO timestamp}
```

Not `build dev · local`.

## GitHub Actions (CI only)

The `.github/workflows/build-and-verify.yml` workflow runs build + verify on every push/PR to `main`. It injects `PUBLIC_BUILD_HASH` and `PUBLIC_BUILD_TIME` for the CI build. This workflow does **not** deploy to CF Pages — it is CI only.

The canonical deploy path is: **GitHub push → CF Pages auto-build → CF Pages deploy**.

The CI workflow and CF Pages build are independent. Both must use the correct build command.
