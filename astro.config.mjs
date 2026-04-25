import { defineConfig } from 'astro/config';

// Astro config for ALG Website
// Output: static site
// Hosted by: Cloudflare Pages
// Source of truth: this repo on GitHub
//
// Per Playbook v2.0 §1: Manus generates Astro components, commits to GitHub,
// Cloudflare Pages auto-builds and deploys. There is no separate "publish" step.

export default defineConfig({
  site: 'https://archipelagolighting.com',
  output: 'static',
  build: {
    format: 'directory'
  },
  trailingSlash: 'never',
  // Compression handled by Cloudflare CDN — no in-build minification quirks
});
