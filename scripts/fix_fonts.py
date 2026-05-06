#!/usr/bin/env python3
"""
fix_fonts.py — Canonicalize all font-family declarations site-wide.

Canonical rules:
  - Body/UI text:       'Lato', system-ui, -apple-system, sans-serif
  - Eyebrow/label caps: 'Lato', system-ui, sans-serif  (ui-monospace → Lato)
  - Serif headings:     'Cormorant Garamond', 'Playfair Display', Georgia, serif  (keep as-is)
  - Monospace (code):   JetBrains Mono  (keep as-is)

Non-canonical values to replace:
  1. ui-monospace, monospace  → 'Lato', system-ui, sans-serif
  2. ui-monospace,monospace   → 'Lato', system-ui, sans-serif
  3. Inter, -apple-system, … → 'Lato', system-ui, -apple-system, sans-serif
  4. -apple-system, BlinkMacSystemFont, … (no Lato prefix) → 'Lato', system-ui, -apple-system, sans-serif
  5. Georgia, serif (standalone, not part of Cormorant stack) → keep (it's a fallback in the serif stack)
"""

import re
import os
import glob

LATO_SANS = "'Lato', system-ui, -apple-system, sans-serif"
LATO_SANS_SHORT = "'Lato', system-ui, sans-serif"

# Files to process
src_root = "/home/ubuntu/alg-website/src"
patterns = ["**/*.astro", "**/*.css"]

def fix_content(content, filepath):
    original = content
    changes = []

    # 1. Fix brand.css --font-sans and --font-display variables
    if "brand.css" in filepath:
        new = re.sub(
            r"--font-sans:\s*'Inter',\s*-apple-system[^;]+;",
            f"--font-sans: {LATO_SANS};",
            content
        )
        if new != content:
            changes.append("brand.css --font-sans → Lato")
            content = new
        new = re.sub(
            r"--font-display:\s*'Inter'[^;]+;",
            f"--font-display: {LATO_SANS};",
            content
        )
        if new != content:
            changes.append("brand.css --font-display → Lato")
            content = new
        return content, changes

    # 2. Replace ui-monospace, monospace (with or without spaces)
    new = re.sub(
        r"font-family:\s*ui-monospace,\s*monospace",
        f"font-family: {LATO_SANS_SHORT}",
        content
    )
    if new != content:
        count = content.count("ui-monospace")
        changes.append(f"ui-monospace → Lato ({count} occurrences)")
        content = new

    # 3. Replace font-family:ui-monospace,monospace (no spaces, inline style)
    new = re.sub(
        r"font-family:ui-monospace,monospace",
        f"font-family:{LATO_SANS_SHORT}",
        content
    )
    if new != content:
        changes.append("inline ui-monospace → Lato")
        content = new

    # 4. Replace font-family="ui-monospace,monospace" (SVG attribute)
    new = re.sub(
        r'font-family="ui-monospace,monospace"',
        f'font-family="Lato, sans-serif"',
        content
    )
    if new != content:
        changes.append("SVG font-family ui-monospace → Lato")
        content = new

    # 5. Replace -apple-system, BlinkMacSystemFont without Lato prefix
    # Only match if NOT already preceded by Lato or Cormorant
    new = re.sub(
        r"font-family:\s*-apple-system,\s*BlinkMacSystemFont[^;\"']+",
        f"font-family: {LATO_SANS}",
        content
    )
    if new != content:
        changes.append("-apple-system (no Lato) → Lato")
        content = new

    # 6. Replace Inter, -apple-system without Lato prefix
    new = re.sub(
        r"font-family:\s*Inter,\s*-apple-system[^;\"']+",
        f"font-family: {LATO_SANS}",
        content
    )
    if new != content:
        changes.append("Inter → Lato")
        content = new

    # 7. Replace 'Inter', -apple-system (quoted)
    new = re.sub(
        r"font-family:\s*'Inter',\s*-apple-system[^;\"']+",
        f"font-family: {LATO_SANS}",
        content
    )
    if new != content:
        changes.append("'Inter' → Lato")
        content = new

    # 8. Replace 'Sora', sans-serif → Lato (Sora is not loaded)
    new = re.sub(
        r"font-family:\s*'Sora',\s*sans-serif",
        f"font-family: {LATO_SANS_SHORT}",
        content
    )
    if new != content:
        count = len(re.findall(r"font-family:\s*'Sora'", content))
        changes.append(f"'Sora' → Lato ({count} occurrences)")
        content = new

    # 9. Replace font-family:'Sora',sans-serif (no spaces, inline)
    new = re.sub(
        r"font-family:'Sora',sans-serif",
        f"font-family:{LATO_SANS_SHORT}",
        content
    )
    if new != content:
        changes.append("inline 'Sora' → Lato")
        content = new

    return content, changes


total_files = 0
total_changes = 0

for pattern in patterns:
    for filepath in glob.glob(os.path.join(src_root, pattern), recursive=True):
        with open(filepath, encoding="utf-8") as f:
            content = f.read()
        
        fixed, changes = fix_content(content, filepath)
        
        if changes:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(fixed)
            rel = filepath.replace(src_root + "/", "")
            print(f"  FIXED  {rel}")
            for c in changes:
                print(f"         → {c}")
            total_files += 1
            total_changes += len(changes)

print(f"\nDone: {total_files} files fixed, {total_changes} change groups applied.")
