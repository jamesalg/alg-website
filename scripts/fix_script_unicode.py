#!/usr/bin/env python3
"""
fix_script_unicode.py
Escapes non-ASCII characters inside <script> blocks in Astro pages.
esbuild rejects raw Unicode in JS string literals unless they are escaped.
"""
import re
import os
import sys

SLUGS = [
    "anaheim", "atlanta", "aura", "everest", "guardian",
    "heritage", "navigator", "nightwatch", "pathfinder",
    "radiator", "ramparts", "sentinel", "watchtower", "wedge"
]

def escape_non_ascii_in_js(js_text):
    """Escape non-ASCII characters in JS string literals to \\uXXXX form."""
    result = []
    i = 0
    while i < len(js_text):
        c = js_text[i]
        if ord(c) > 127:
            result.append(f'\\u{ord(c):04X}')
        else:
            result.append(c)
        i += 1
    return ''.join(result)

def fix_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Find and fix all <script> blocks (not type="application/ld+json")
    def replace_script(m):
        tag = m.group(1)  # opening tag
        body = m.group(2)  # script body
        # Skip JSON-LD blocks
        if 'application/ld+json' in tag:
            return m.group(0)
        fixed_body = escape_non_ascii_in_js(body)
        return f'<script{tag}>{fixed_body}</script>'

    content = re.sub(
        r'<script([^>]*)>(.*?)</script>',
        replace_script,
        content,
        flags=re.DOTALL
    )

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Fixed: {path}")
        return True
    else:
        print(f"  No changes: {path}")
        return False

def main():
    base = '/home/ubuntu/alg-website/src/pages/products'
    fixed = 0
    for slug in SLUGS:
        path = os.path.join(base, slug, 'index.astro')
        if os.path.exists(path):
            if fix_file(path):
                fixed += 1
        else:
            print(f"  MISSING: {path}")
    # Also fix the radiator backup
    bak = os.path.join(base, 'radiator', 'index.astro.bak')
    if os.path.exists(bak):
        os.rename(bak, os.path.join(base, 'radiator', 'index.astro'))
        print("  Restored radiator/index.astro from .bak")
        if fix_file(os.path.join(base, 'radiator', 'index.astro')):
            fixed += 1
    print(f"\nDone. Fixed {fixed} files.")

if __name__ == '__main__':
    main()
