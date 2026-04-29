#!/usr/bin/env python3
"""
patch_g2_fidelity.py — v2.7.13 G2 fidelity patch

Adds the required CSS classes to all 12 Vintage + Nostalgic decor pages:
  - .lifestyle-photo on the hero photo placeholder div
  - .toc-link on spec-section navigation links
  - .matrix-row on <tr> elements in dimmer and SKU tables
  - .swatch chips in the glass finish spec row

Strategy: targeted regex replacements, not full rewrites.
"""
import re, os, sys

BASE = '/home/ubuntu/alg-website/src/pages/collections'

VINTAGE = ['vintage-decor/edison.astro', 'vintage-decor/victorian.astro',
           'vintage-decor/tubular.astro', 'vintage-decor/radio.astro',
           'vintage-decor/candelabra.astro', 'vintage-decor/globe.astro']
NOSTALGIC = ['nostalgic-decor/a19.astro', 'nostalgic-decor/b10.astro',
             'nostalgic-decor/ca10.astro', 'nostalgic-decor/g16-5.astro',
             'nostalgic-decor/g25.astro', 'nostalgic-decor/s14.astro']

ALL_PAGES = VINTAGE + NOSTALGIC

results = {}

for rel in ALL_PAGES:
    path = os.path.join(BASE, rel)
    if not os.path.exists(path):
        results[rel] = 'MISSING'
        continue

    with open(path, 'r', encoding='utf-8') as f:
        src = f.read()

    original = src
    changes = []

    # -----------------------------------------------------------------------
    # 1. lifestyle-photo: add class to the photo placeholder div
    #    Patterns: ed-photo-ph, ns-photo-ph, ta-photo-ph, etc.
    # -----------------------------------------------------------------------
    # Match any class containing "photo-ph" and add lifestyle-photo to it
    def add_lifestyle_class(m):
        existing = m.group(1)
        if 'lifestyle-photo' not in existing:
            return f'class="{existing} lifestyle-photo"'
        return m.group(0)

    new_src = re.sub(r'class="([^"]*photo-ph[^"]*)"', add_lifestyle_class, src)
    if new_src != src:
        changes.append('lifestyle-photo class added')
        src = new_src

    # -----------------------------------------------------------------------
    # 2. toc-link: add class to spec-section anchor links in the TOC nav
    #    Pattern: <a href="#spec-..." class="..."> or <a href="#spec-...">
    # -----------------------------------------------------------------------
    def add_toc_class(m):
        href = m.group(1)
        existing_class = m.group(2)
        if existing_class is None:
            return f'<a href="{href}" class="toc-link">'
        if 'toc-link' not in existing_class:
            return f'<a href="{href}" class="{existing_class} toc-link">'
        return m.group(0)

    # Pattern: <a href="#spec-..." class="..."> or <a href="#spec-...">
    new_src = re.sub(
        r'<a href="(#spec-[^"]+)"(?:\s+class="([^"]*)")?',
        add_toc_class,
        src
    )
    if new_src != src:
        changes.append('toc-link class added to spec nav links')
        src = new_src

    # -----------------------------------------------------------------------
    # 3. matrix-row: add class to <tr> elements inside tables
    #    (dimmer table + SKU table rows, not header rows)
    #    Pattern: <tr> without class, or <tr class="..."> without matrix-row
    #    We only target <tr> inside <tbody> context — use a simple heuristic:
    #    add matrix-row to every <tr> that doesn't already have it and isn't
    #    a <thead> row (thead rows have <th> children).
    # -----------------------------------------------------------------------
    # Split into tbody sections and add matrix-row to <tr> in them
    def add_matrix_row(m):
        tr_tag = m.group(0)
        if 'matrix-row' in tr_tag:
            return tr_tag
        # Add matrix-row class
        if 'class="' in tr_tag:
            return tr_tag.replace('class="', 'class="matrix-row ', 1)
        else:
            return tr_tag.replace('<tr', '<tr class="matrix-row"', 1)

    # Only patch <tr> elements inside <tbody>...</tbody>
    def patch_tbody(m):
        tbody_content = m.group(0)
        patched = re.sub(r'<tr(?:\s[^>]*)?>', add_matrix_row, tbody_content)
        return patched

    new_src = re.sub(r'<tbody>.*?</tbody>', patch_tbody, src, flags=re.DOTALL)
    if new_src != src:
        changes.append('matrix-row class added to tbody <tr> elements')
        src = new_src

    # -----------------------------------------------------------------------
    # 4. swatch: add glass-color swatch chips to the glass finish spec row
    #    Look for the glass finish row in the spec table and inject swatches.
    #    The row typically contains "Clear" and "Amber" (and possibly "Smoked").
    #    We inject .swatch spans before the text labels.
    # -----------------------------------------------------------------------
    # Pattern: <dd> containing glass finish options like "Clear · Amber" or similar
    # Only add swatches if not already present
    def inject_swatches(m):
        dd_content = m.group(1)
        if 'swatch' in dd_content:
            return m.group(0)  # already has swatches

        # Build swatch chips based on what glass options are mentioned
        swatches = []
        if 'Clear' in dd_content or 'clear' in dd_content:
            swatches.append('<span class="swatch" style="background:rgba(239,230,210,0.5);border:1px solid rgba(26,19,10,0.3);" title="Clear"></span>')
        if 'Amber' in dd_content or 'amber' in dd_content:
            swatches.append('<span class="swatch" style="background:#C7822E;" title="Amber"></span>')
        if 'Smoked' in dd_content or 'smoked' in dd_content:
            swatches.append('<span class="swatch" style="background:#6E5236;" title="Smoked"></span>')
        if 'Frosted' in dd_content or 'frosted' in dd_content:
            swatches.append('<span class="swatch" style="background:rgba(239,230,210,0.7);border:1px solid rgba(26,19,10,0.2);" title="Frosted"></span>')

        if swatches:
            swatch_html = ' '.join(swatches) + ' '
            return f'<dd>{swatch_html}{dd_content}</dd>'
        return m.group(0)

    # Match <dd> elements that contain glass finish keywords
    new_src = re.sub(
        r'<dd>((?:[^<]|<(?!/?dd))*?(?:Clear|Amber|Smoked|Frosted)(?:[^<]|<(?!/?dd))*?(?:Clear|Amber|Smoked|Frosted|glass|finish|Glass|Finish)[^<]*)</dd>',
        inject_swatches,
        src,
        flags=re.IGNORECASE
    )
    if new_src != src:
        changes.append('swatch chips injected into glass finish row')
        src = new_src

    # -----------------------------------------------------------------------
    # Write back if changed
    # -----------------------------------------------------------------------
    if src != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(src)
        results[rel] = f'PATCHED ({", ".join(changes)})'
    else:
        results[rel] = f'NO CHANGE (changes attempted: {", ".join(changes) if changes else "none matched"})'

print("\n=== G2 FIDELITY PATCH RESULTS ===")
for page, result in results.items():
    print(f"  {page}: {result}")

# Verify the classes are now present
print("\n=== VERIFICATION ===")
for rel in ALL_PAGES:
    path = os.path.join(BASE, rel)
    if not os.path.exists(path):
        print(f"  {rel}: MISSING")
        continue
    with open(path, 'r') as f:
        content = f.read()
    lp = 'lifestyle-photo' in content
    tl = content.count('toc-link')
    mr = content.count('matrix-row')
    sw = content.count('swatch')
    status = 'OK' if (lp and tl >= 5 and mr >= 10 and sw >= 2) else 'NEEDS REVIEW'
    print(f"  {rel}: lifestyle={lp}, toc-link={tl}, matrix-row={mr}, swatch={sw} -> {status}")
