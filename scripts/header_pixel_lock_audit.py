#!/usr/bin/env python3
"""
header_pixel_lock_audit.py — v27x_HeaderPixelLock
Captures computed styles and screenshots of the global header across 6 routes,
diffs against homepage canonical, and reports any deviations.

Usage:
  python3 scripts/header_pixel_lock_audit.py [--base-url URL] [--output-dir DIR]

Defaults:
  --base-url  https://staging.archipelagolighting.com
  --output-dir /tmp/header_audit
"""

import asyncio
import json
import sys
import os
import argparse
import hashlib
from pathlib import Path

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("ERROR: playwright not installed. Run: pip3 install playwright && python3 -m playwright install chromium")
    sys.exit(1)

try:
    from PIL import Image, ImageChops
    import numpy as np
    HAS_PIL = True
except ImportError:
    HAS_PIL = False
    print("WARNING: Pillow/numpy not available. Pixel diff will be skipped.")

ROUTES = [
    "/",
    "/products/illuminator/",
    "/collections/multi-family/",
    "/collections/consumer/",
    "/collections/planoarch/",
    "/contact/",
]

# For local preview server (trailingSlash: 'never'), strip trailing slashes
ROUTES_LOCAL = [
    "/",
    "/products/illuminator",
    "/collections/multi-family",
    "/collections/consumer",
    "/collections/planoarch",
    "/contact",
]

COMPUTED_PROPS = [
    "fontFamily", "fontSize", "fontWeight", "lineHeight", "letterSpacing",
    "textTransform", "color",
    "paddingTop", "paddingRight", "paddingBottom", "paddingLeft",
    "marginTop", "marginRight", "marginBottom", "marginLeft",
    "gap", "columnGap", "rowGap",
    "width", "height",
    "flexGrow", "flexShrink", "flexBasis",
    "justifyContent", "alignItems",
    "position", "top", "left", "right", "bottom",
    "boxSizing",
    "display",
    "overflow",
    "fontFeatureSettings",
    "textRendering",
    "webkitFontSmoothing",
]

JS_CAPTURE = """
(props) => {
    const header = document.querySelector('header#site-header') || document.querySelector('header');
    if (!header) return {error: 'no header element found'};

    function getSelector(el) {
        if (el.id) return '#' + el.id;
        const tag = el.tagName.toLowerCase();
        const cls = Array.from(el.classList).slice(0,2).join('.');
        const parent = el.parentElement;
        if (!parent) return tag;
        const siblings = Array.from(parent.children).filter(c => c.tagName === el.tagName);
        const idx = siblings.indexOf(el);
        const base = cls ? tag + '.' + cls : tag;
        return base + (siblings.length > 1 ? ':nth(' + idx + ')' : '');
    }

    function captureElement(el, depth) {
        const cs = window.getComputedStyle(el);
        const styles = {};
        for (const prop of props) {
            styles[prop] = cs[prop] || cs.getPropertyValue(
                prop.replace(/([A-Z])/g, '-$1').toLowerCase()
            );
        }
        const rect = el.getBoundingClientRect();
        return {
            selector: getSelector(el),
            tag: el.tagName.toLowerCase(),
            id: el.id || null,
            classes: Array.from(el.classList).join(' ') || null,
            rect: {x: Math.round(rect.x), y: Math.round(rect.y), w: Math.round(rect.width), h: Math.round(rect.height)},
            styles: styles,
            children: depth > 0 ? Array.from(el.children).map(c => captureElement(c, depth - 1)) : []
        };
    }

    return captureElement(header, 4);
}
"""

async def capture_route(page, base_url, route, output_dir, viewport_width=1440):
    url = base_url.rstrip('/') + route
    await page.set_viewport_size({"width": viewport_width, "height": 900})
    await page.goto(url, wait_until="domcontentloaded", timeout=30000)
    # Wait for fonts + 1000ms post-load delay per §4.1
    try:
        await page.evaluate("document.fonts.ready")
    except Exception:
        pass
    await page.wait_for_timeout(1500)

    # Capture computed styles
    styles = await page.evaluate(JS_CAPTURE, COMPUTED_PROPS)

    # Capture screenshot of header region (top 140px CSS = 280px at 2x DPR, but we use 1x here)
    header_el = await page.query_selector("header#site-header")
    if header_el:
        bbox = await header_el.bounding_box()
        if bbox:
            clip = {"x": 0, "y": 0, "width": viewport_width, "height": min(int(bbox["height"]) + 4, 150)}
            slug = route.strip('/').replace('/', '_') or 'homepage'
            screenshot_path = str(output_dir / f"header_{slug}.png")
            await page.screenshot(path=screenshot_path, clip=clip, full_page=False)
            styles["_screenshot"] = screenshot_path
            styles["_bbox"] = bbox

    return styles


def flatten_styles(node, prefix="", result=None):
    """Flatten nested style tree into {selector_path: {prop: value}} dict."""
    if result is None:
        result = {}
    if isinstance(node, dict) and "styles" in node:
        key = prefix + node.get("selector", "?")
        result[key] = node["styles"]
        for child in node.get("children", []):
            flatten_styles(child, key + " > ", result)
    return result


def diff_styles(canonical, test, route):
    """Return list of diffs between canonical and test style dicts."""
    diffs = []
    for selector, canon_styles in canonical.items():
        if selector not in test:
            diffs.append({"selector": selector, "issue": "element missing in test page"})
            continue
        test_styles = test[selector]
        for prop, canon_val in canon_styles.items():
            test_val = test_styles.get(prop, "MISSING")
            if canon_val != test_val:
                diffs.append({
                    "selector": selector,
                    "property": prop,
                    "homepage": canon_val,
                    "test_page": test_val,
                    "route": route,
                })
    return diffs


def pixel_diff(img1_path, img2_path, fuzz_pct=1.0):
    """
    Compute pixel diff equivalent to: compare -metric AE -fuzz 1%
    Returns (ae_count, diff_image_path)
    """
    if not HAS_PIL:
        return None, None

    img1 = Image.open(img1_path).convert("RGB")
    img2 = Image.open(img2_path).convert("RGB")

    # Ensure same size (crop to smaller)
    w = min(img1.width, img2.width)
    h = min(img1.height, img2.height)
    img1 = img1.crop((0, 0, w, h))
    img2 = img2.crop((0, 0, w, h))

    arr1 = np.array(img1, dtype=np.int32)
    arr2 = np.array(img2, dtype=np.int32)

    # Fuzz: pixels where ALL channels differ by <= fuzz_threshold are considered equal
    fuzz_threshold = int(255 * fuzz_pct / 100)
    diff = np.abs(arr1 - arr2)
    # A pixel "differs" if ANY channel exceeds fuzz_threshold
    differs = np.any(diff > fuzz_threshold, axis=2)
    ae_count = int(np.sum(differs))

    # Create diff image: differing pixels in magenta, matching in black
    diff_arr = np.zeros((h, w, 3), dtype=np.uint8)
    diff_arr[differs] = [255, 0, 255]  # magenta for differing pixels

    diff_path = img1_path.replace(".png", "_diff.png")
    Image.fromarray(diff_arr).save(diff_path)

    return ae_count, diff_path


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="https://staging.archipelagolighting.com")
    parser.add_argument("--output-dir", default="/tmp/header_audit")
    parser.add_argument("--local", action="store_true", help="Use local dev server at localhost:4321")
    args = parser.parse_args()

    if args.local:
        args.base_url = "http://localhost:4321"

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Use local routes (no trailing slash) for local preview server
    routes = ROUTES_LOCAL if args.local else ROUTES

    print(f"=== Header Pixel Lock Audit ===")
    print(f"Base URL: {args.base_url}")
    print(f"Output: {output_dir}")
    print(f"Routes: {routes}")
    print()

    all_styles = {}
    all_screenshots = {}

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1440, "height": 900},
            device_scale_factor=1,
        )
        page = await context.new_page()

        for route in routes:
            print(f"Capturing {route} ...")
            try:
                styles = await capture_route(page, args.base_url, route, output_dir)
                screenshot = styles.pop("_screenshot", None)
                bbox = styles.pop("_bbox", None)
                all_styles[route] = styles
                if screenshot:
                    all_screenshots[route] = screenshot
                print(f"  ✓ Captured. Screenshot: {screenshot}")
            except Exception as e:
                print(f"  ✗ ERROR: {e}")
                all_styles[route] = {"error": str(e)}

        await browser.close()

    # Save raw styles
    styles_path = output_dir / "all_styles.json"
    with open(styles_path, "w") as f:
        json.dump(all_styles, f, indent=2)
    print(f"\nStyles saved to {styles_path}")

    # Flatten and diff
    canonical_route = routes[0]
    canonical_flat = flatten_styles(all_styles[canonical_route])

    print(f"\n=== Computed Style Diffs (vs homepage) ===")
    all_diffs = {}
    total_diffs = 0

    for route in routes[1:]:
        if "error" in all_styles.get(route, {}):
            print(f"\n{route}: CAPTURE ERROR — {all_styles[route]['error']}")
            continue
        test_flat = flatten_styles(all_styles[route])
        diffs = diff_styles(canonical_flat, test_flat, route)
        all_diffs[route] = diffs
        total_diffs += len(diffs)
        if diffs:
            print(f"\n{route}: {len(diffs)} diff(s)")
            for d in diffs[:20]:  # Show first 20
                if "property" in d:
                    print(f"  [{d['selector']}] {d['property']}: homepage={d['homepage']!r} test={d['test_page']!r}")
                else:
                    print(f"  {d}")
            if len(diffs) > 20:
                print(f"  ... and {len(diffs)-20} more")
        else:
            print(f"\n{route}: ✅ 0 diffs")

    # Save diffs
    diffs_path = output_dir / "style_diffs.json"
    with open(diffs_path, "w") as f:
        json.dump(all_diffs, f, indent=2)
    print(f"\nDiffs saved to {diffs_path}")

    # Pixel diff
    print(f"\n=== Pixel Diffs (AE, fuzz=1%) ===")
    homepage_screenshot = all_screenshots.get("/")
    if not homepage_screenshot:
        print("ERROR: No homepage screenshot captured")
    else:
        pixel_results = {}
        for route in routes[1:]:
            test_screenshot = all_screenshots.get(route)
            if not test_screenshot:
                print(f"{route}: No screenshot")
                continue
            ae, diff_path = pixel_diff(homepage_screenshot, test_screenshot)
            pixel_results[route] = ae
            status = "✅ 0" if ae == 0 else f"❌ {ae}"
            print(f"  {route}: AE = {status} differing pixels")
            if ae > 0 and diff_path:
                print(f"    Diff image: {diff_path}")

        # Save pixel results
        pixel_path = output_dir / "pixel_results.json"
        with open(pixel_path, "w") as f:
            json.dump(pixel_results, f, indent=2)

    print(f"\n=== Summary ===")
    print(f"Total computed-style diffs: {total_diffs}")
    if 'pixel_results' in dir():
        total_ae = sum(pixel_results.values())
        print(f"Total pixel AE: {total_ae}")
        if total_diffs == 0 and total_ae == 0:
            print("✅ PIXEL LOCK PASS — All pages identical to homepage")
        else:
            print("❌ PIXEL LOCK FAIL — Diffs detected. Fix before deploying.")

    return all_diffs, all_screenshots


if __name__ == "__main__":
    asyncio.run(main())
