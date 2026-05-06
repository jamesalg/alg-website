#!/usr/bin/env python3
"""
port_pdps.py — Convert luxoARCH mockup HTML files to Astro PDP pages.

For each slug:
1. Read the mockup HTML
2. Extract <style> blocks, body content (excluding mockup header/nav)
3. Wrap in BaseLayout with correct title/description/bodyClass
4. Replace asset paths: assets/{slug}/ → /products/{slug}/assets/
5. Replace CDN cert URLs → /products/illuminator/assets/certs/
6. Replace cross-family asset paths: assets/{other}/ → /products/{other}/assets/
7. Remove mockup-banner, placeholder site-header, placeholder footer
8. Wire WorkDrive URLs from wd_urls.json
9. Write to src/pages/products/{slug}/index.astro
"""

import re
import json
import os
from pathlib import Path

MOCKUP_DIR = Path("/home/ubuntu/upload/manus_luxoARCH_handoff/manus_luxoARCH_handoff_2026-05-05/v2_mockups/luxoARCH")
PAGES_DIR = Path("/home/ubuntu/alg-website/src/pages/products")
WD_URLS_FILE = Path("/home/ubuntu/alg-website/scripts/wd_urls.json")

with open(WD_URLS_FILE) as f:
    WD_URLS = json.load(f)

# PDP metadata: slug → (title, description, bodyClass, series_name)
PDP_META = {
    "anaheim": {
        "title": "Anaheim Series — LWPA Adjustable Wall Pack | Archipelago Lighting Group",
        "description": "The LWPA Anaheim Series delivers 5,000–10,000 lm from 50–100W. ECO-tier adjustable wall pack for commercial perimeter and security lighting.",
        "bodyClass": "page-anaheim-pdp",
        "series": "Anaheim Series",
        "tier": "ECO",
    },
    "atlanta": {
        "title": "Atlanta Series — LWPA Adjustable Wall Pack PRO | Archipelago Lighting Group",
        "description": "The LWPA Atlanta Series delivers 8,000–16,000 lm from 80–150W. PRO-tier adjustable wall pack with WattSELECT and advanced controls.",
        "bodyClass": "page-atlanta-pdp",
        "series": "Atlanta Series",
        "tier": "PRO",
    },
    "aura": {
        "title": "Aura Series — LCWS LED Cylinder Wall Sconce | Archipelago Lighting Group",
        "description": "The LCWS Aura Series offers 4 housings, 4-WattSELECT, and beamADJUST 50°/60°/70°. Specification-grade LED cylinder wall sconce for architectural accent lighting.",
        "bodyClass": "page-aura-pdp",
        "series": "Aura Series",
        "tier": "PRO",
    },
    "everest": {
        "title": "Everest Series — LFLD Flood Light | Archipelago Lighting Group",
        "description": "The LFLD Everest Series delivers 8,000–20,000 lm from 80–200W. ECO-tier LED flood light for commercial and industrial area lighting.",
        "bodyClass": "page-everest-pdp",
        "series": "Everest Series",
        "tier": "ECO",
    },
    "guardian": {
        "title": "Guardian Series — LWPC Classic Wall Pack | Archipelago Lighting Group",
        "description": "The LWPC Guardian Series delivers 5,000–10,000 lm from 50–100W. ECO-tier classic wall pack for commercial building perimeter and security lighting.",
        "bodyClass": "page-guardian-pdp",
        "series": "Guardian Series",
        "tier": "ECO",
    },
    "heritage": {
        "title": "Heritage Series — LSAL Area Light | Archipelago Lighting Group",
        "description": "The LSAL Heritage Series delivers 10,000–40,000 lm from 80–320W. ECO-tier LED area light for parking lots, roadways, and commercial sites.",
        "bodyClass": "page-heritage-pdp",
        "series": "Heritage Series",
        "tier": "ECO",
    },
    "navigator": {
        "title": "Navigator Series — LCNP LED Canopy Light | Archipelago Lighting Group",
        "description": "The LCNP Navigator Series delivers 4,000–12,000 lm from 40–120W. ECO-tier LED canopy light for gas stations, parking structures, and covered walkways.",
        "bodyClass": "page-navigator-pdp",
        "series": "Navigator Series",
        "tier": "ECO",
    },
    "nightwatch": {
        "title": "Nightwatch Series — LWPFC Full Cutoff Wall Pack PRO | Archipelago Lighting Group",
        "description": "The LWPFC Nightwatch Series delivers 8,000–20,000 lm from 80–200W. PRO-tier full cutoff wall pack with WattSELECT and 0–10V dimming.",
        "bodyClass": "page-nightwatch-pdp",
        "series": "Nightwatch Series",
        "tier": "PRO",
    },
    "pathfinder": {
        "title": "Pathfinder Series — LCNP LED Canopy Light PRO | Archipelago Lighting Group",
        "description": "The LCNP Pathfinder Series delivers 6,000–18,000 lm from 60–180W. PRO-tier LED canopy light with WattSELECT and sensor-ready design.",
        "bodyClass": "page-pathfinder-pdp",
        "series": "Pathfinder Series",
        "tier": "PRO",
    },
    "radiator": {
        "title": "Radiator Series — LSPL Sports Lighter | Archipelago Lighting Group",
        "description": "The LSPL Radiator Series delivers broadcast-quality sports lighting for mid-tier venues. PRO-tier LED sports lighter for high school fields, recreational facilities, and municipal parks.",
        "bodyClass": "page-radiator-pdp",
        "series": "Radiator Series",
        "tier": "PRO",
    },
    "ramparts": {
        "title": "Ramparts Series — LWPE Entryway Wall Pack | Archipelago Lighting Group",
        "description": "The LWPE Ramparts Series delivers 3,000–6,000 lm from 30–60W. ECO-tier entryway wall pack for building entrances, corridors, and perimeter lighting.",
        "bodyClass": "page-ramparts-pdp",
        "series": "Ramparts Series",
        "tier": "ECO",
    },
    "sentinel": {
        "title": "Sentinel Series — LWPC Classic Wall Pack PRO | Archipelago Lighting Group",
        "description": "The LWPC Sentinel Series delivers 8,000–20,000 lm from 80–200W. PRO-tier classic wall pack with WattSELECT, 0–10V dimming, and 7-year warranty.",
        "bodyClass": "page-sentinel-pdp",
        "series": "Sentinel Series",
        "tier": "PRO",
    },
    "watchtower": {
        "title": "Watchtower Series — LWPFC Full Cutoff Wall Pack | Archipelago Lighting Group",
        "description": "The LWPFC Watchtower Series delivers 5,000–12,000 lm from 50–120W. ECO-tier full cutoff wall pack for commercial security and perimeter lighting.",
        "bodyClass": "page-watchtower-pdp",
        "series": "Watchtower Series",
        "tier": "ECO",
    },
    "wedge": {
        "title": "Wedge Series — LWPE Entryway Wall Pack | Archipelago Lighting Group",
        "description": "The LWPE Wedge-I Series delivers 2,000–5,000 lm from 20–50W. ECO-tier slim entryway wall pack for building entrances and pathway lighting.",
        "bodyClass": "page-wedge-pdp",
        "series": "Wedge Series",
        "tier": "ECO",
    },
}

ALL_SLUGS = list(PDP_META.keys())

def extract_body_content(html: str) -> str:
    """Extract content between <body> and </body>, stripping mockup-specific elements."""
    # Get body content
    m = re.search(r'<body[^>]*>(.*)</body>', html, re.DOTALL)
    if not m:
        return html
    body = m.group(1)
    
    # Remove mockup banner
    body = re.sub(r'<div class="mockup-banner"[^>]*>.*?</div>', '', body, flags=re.DOTALL)
    
    # Remove placeholder site-header (everything from <header class="site-header to matching </header>)
    body = re.sub(r'<header class="site-header"[^>]*>.*?</header>', '', body, flags=re.DOTALL)
    
    # Remove placeholder footer (everything from <footer to </footer>)
    body = re.sub(r'<footer[^>]*>.*?</footer>', '', body, flags=re.DOTALL)
    
    # Remove placeholder nav (sticky nav at top of body if present)
    body = re.sub(r'<nav class="site-nav"[^>]*>.*?</nav>', '', body, flags=re.DOTALL)
    
    return body.strip()

def extract_style_blocks(html: str) -> str:
    """Extract all <style> blocks from <head>."""
    styles = re.findall(r'<style[^>]*>(.*?)</style>', html, re.DOTALL)
    return '\n'.join(styles)

def fix_asset_paths(content: str, slug: str) -> str:
    """Replace relative asset paths with absolute /products/ paths."""
    # Replace assets/{slug}/ → /products/{slug}/assets/
    for s in ALL_SLUGS:
        content = content.replace(f'assets/{s}/', f'/products/{s}/assets/')
    
    # Replace CDN cert URLs → local cert paths
    cdn_base = 'https://www.archipelagolighting.com/cdn/shop/t/24/assets/'
    content = content.replace(f'{cdn_base}dlc.svg', '/products/illuminator/assets/certs/dlc.svg')
    content = content.replace(f'{cdn_base}etl.svg', '/products/illuminator/assets/certs/etl.svg')
    content = content.replace(f'{cdn_base}rohs.svg', '/products/illuminator/assets/certs/rohs.svg')
    content = content.replace(f'{cdn_base}wet-location.svg', '/products/illuminator/assets/certs/wet-location.svg')
    
    # Replace any remaining bare assets/ paths (for cert SVGs at root)
    content = re.sub(r'src="assets/(dlc|etl|rohs|wet-location)\.svg"', 
                     lambda m: f'src="/products/illuminator/assets/certs/{m.group(1)}.svg"', content)
    
    return content

def wire_wd_urls(content: str, slug: str) -> str:
    """Replace placeholder WorkDrive URL comments with actual URLs."""
    urls = WD_URLS.get(slug, {})
    
    # Replace placeholder patterns like href="#" on WorkDrive download buttons
    # The mockups use href="WORKDRIVE_DATASHEET_URL" or href="#" with data attributes
    for slot, url in urls.items():
        if url:
            # Replace placeholder patterns
            content = content.replace(f'WORKDRIVE_{slot.upper()}_URL', url)
            content = content.replace(f'href="#{slot}"', f'href="{url}" target="_blank" rel="noopener"')
    
    return content

def remove_google_fonts(content: str) -> str:
    """Remove Google Fonts link tags (self-hosted via global.css)."""
    content = re.sub(r'<link[^>]*fonts\.googleapis\.com[^>]*>', '', content)
    content = re.sub(r'<link[^>]*fonts\.gstatic\.com[^>]*>', '', content)
    return content

def build_schema_json(slug: str, meta: dict) -> str:
    """Build a minimal Product schema.org JSON-LD for the PDP."""
    return f'''    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Product",
      "name": "{meta['series']}",
      "brand": {{
        "@type": "Brand",
        "name": "Archipelago Lighting Group"
      }},
      "description": "{meta['description']}",
      "category": "Commercial LED Luminaire",
      "url": "https://www.archipelagolighting.com/products/{slug}/",
      "offers": {{
        "@type": "Offer",
        "availability": "https://schema.org/InStock",
        "priceCurrency": "USD",
        "seller": {{
          "@type": "Organization",
          "name": "Archipelago Lighting Group"
        }}
      }}
    }}
    </script>'''

def port_pdp(slug: str) -> bool:
    """Port a single PDP mockup to an Astro page. Returns True on success."""
    mockup_path = MOCKUP_DIR / f"mockup_{slug}_pdp_v1.html"
    if not mockup_path.exists():
        print(f"  ERROR: mockup not found: {mockup_path}")
        return False
    
    with open(mockup_path, encoding='utf-8') as f:
        html = f.read()
    
    meta = PDP_META[slug]
    
    # Extract style blocks from head
    style_content = extract_style_blocks(html)
    
    # Extract body content
    body_content = extract_body_content(html)
    
    # Fix asset paths
    body_content = fix_asset_paths(body_content, slug)
    style_content = fix_asset_paths(style_content, slug)
    
    # Wire WorkDrive URLs
    body_content = wire_wd_urls(body_content, slug)
    
    # Build the Astro page
    schema_json = build_schema_json(slug, meta)
    
    astro_page = f'''---
/**
 * {meta['series']} PDP — v1 Production Build
 * Route: /products/{slug}/
 * Ported from mockup_{slug}_pdp_v1.html per PDP_BUILD_PLAYBOOK.md
 *
 * Swap-outs from mockup:
 *   - Placeholder site-header → ALG global Header via BaseLayout
 *   - assets/{slug}/ → /products/{slug}/assets/
 *   - CDN cert URLs → /products/illuminator/assets/certs/
 *   - Google Fonts → self-hosted via global.css
 *   - Schema.org Product JSON-LD injected in <head>
 */
import BaseLayout from '../../../layouts/BaseLayout.astro';
---
<BaseLayout
  title="{meta['title']}"
  description="{meta['description']}"
  bodyClass="{meta['bodyClass']}"
>
  <Fragment slot="head">
{schema_json}
  </Fragment>
<style is:global>
{style_content}
</style>
{body_content}
</BaseLayout>
'''
    
    # Create output directory
    out_dir = PAGES_DIR / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "index.astro"
    
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(astro_page)
    
    lines = astro_page.count('\n')
    print(f"  ✓ {slug}: {lines} lines → {out_path}")
    return True

def main():
    print("=== Porting 14 luxoARCH PDPs to Astro ===\n")
    
    # Phase 3: PDPs 1-7
    phase3 = ["anaheim", "atlanta", "aura", "everest", "guardian", "heritage", "navigator"]
    print("--- Phase 3: PDPs 1-7 ---")
    for slug in phase3:
        port_pdp(slug)
    
    # Phase 4: PDPs 8-14
    phase4 = ["nightwatch", "pathfinder", "radiator", "ramparts", "sentinel", "watchtower", "wedge"]
    print("\n--- Phase 4: PDPs 8-14 ---")
    for slug in phase4:
        port_pdp(slug)
    
    print("\n=== Done. Checking output ===")
    for slug in phase3 + phase4:
        out_path = PAGES_DIR / slug / "index.astro"
        if out_path.exists():
            size = out_path.stat().st_size
            print(f"  {slug}: {size:,} bytes")
        else:
            print(f"  MISSING: {slug}")

if __name__ == "__main__":
    main()
