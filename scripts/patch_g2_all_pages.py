#!/usr/bin/env python3
"""
patch_g2_all_pages.py — v2.7.13 G2 fidelity patch for all 11 remaining decor pages

For each page:
1. Expand dimmers array to 22 entries (the full GEN-2 list)
2. Restructure spec grid to 220px TOC sidebar + content column
3. Ensure 3 swatch chips in the glass finish row
"""
import re, os

BASE = '/home/ubuntu/alg-website/src/pages/collections'

# The canonical 22-entry GEN-2 dimmer list
FULL_DIMMERS = [
    ('TGCL-153P', 'Lutron', 'CL (TRIAC)', 'Toggler · neutral required'),
    ('SCL-153P', 'Lutron', 'CL (TRIAC)', 'Skylark · neutral required'),
    ('DVCL-153P', 'Lutron', 'CL', 'Diva CL · neutral required'),
    ('LGCL-153P', 'Lutron', 'CL', 'Lyneo'),
    ('MACL-153M', 'Lutron', 'CL', 'Maestro CL multi-location'),
    ('PD-6WCL', 'Lutron', 'Caseta wireless', 'Smart-home compatible'),
    ('AY-600P', 'Lutron', 'Incandescent / TRIAC', 'Ariadni'),
    ('D-600P', 'Lutron', 'Incandescent / TRIAC', 'Diva'),
    ('GL-600P', 'Lutron', 'Incandescent / TRIAC', 'Glyder'),
    ('S-600P', 'Lutron', 'Incandescent / TRIAC', 'Skylark'),
    ('DV-600P', 'Lutron', 'Incandescent / TRIAC', 'Diva (legacy)'),
    ('SELV-300P', 'Lutron', 'ELV', 'Skylark ELV'),
    ('DVELV-300P', 'Lutron', 'ELV', 'Diva ELV'),
    ('NTELV-500', 'Lutron', 'ELV', 'Nova T ELV'),
    ('RRD-6NA', 'Lutron', 'RadioRA 2', 'Whole-home wireless'),
    ('MRF-2-6ELV-120', 'Lutron', 'RadioRA 2 ELV', 'Whole-home wireless ELV'),
    ('HQRD-6NA', 'Lutron', 'HomeWorks QS', 'Estate-grade'),
    ('DSL06-1LZ', 'Leviton', 'CL', 'Decora Sureslide CL'),
    ('HCL45-3PW', 'Legrand', 'CL', 'radiant CL'),
    ('FLR603P', 'Forbes & Lomax', 'TRIAC', 'Designer rotary'),
    ('FLRLV603P', 'Forbes & Lomax', 'ELV', 'Designer rotary ELV'),
    ('DAL06P', 'Cooper', 'CL', 'Aspire'),
]

def make_dimmers_js():
    lines = ['const dimmers = [']
    for model, brand, dtype, series in FULL_DIMMERS:
        lines.append(f"  {{ model: '{model}', brand: '{brand}', type: '{dtype}', series: '{series}' }},")
    lines.append('];')
    return '\n'.join(lines)

FULL_DIMMERS_JS = make_dimmers_js()

def patch_dimmers(src):
    """Replace any existing dimmers array with the full 22-entry list."""
    m = re.search(r'const dimmers = \[.*?\];', src, re.DOTALL)
    if not m:
        return src, False
    return src.replace(m.group(0), FULL_DIMMERS_JS), True

def make_toc_sidebar(prefix, sections):
    """Generate the TOC sidebar HTML for a given page prefix and section list."""
    nav_items = []
    for i, (anchor, label) in enumerate(sections, 1):
        active = ' active' if i == 1 else ''
        nav_items.append(
            f'          <a href="#{anchor}" class="toc-link{active}">'
            f'<span style="font-family:var(--{prefix}-mono);font-size:0.65rem;opacity:0.55;">'
            f'{i:02d}</span> {label}</a>'
        )
    nav_html = '\n'.join(nav_items)
    return f"""      <aside aria-label="Spec sections" style="position:sticky;top:1.5rem;">
        <p style="font-family:var(--{prefix}-mono);font-size:0.65rem;letter-spacing:0.18em;opacity:0.55;margin-bottom:0.75rem;padding:0 0.75rem;">SPEC SECTIONS</p>
        <nav style="display:flex;flex-direction:column;gap:0.25rem;">
{nav_html}
        </nav>
      </aside>
      <div style="display:flex;flex-direction:column;gap:3rem;">"""

STANDARD_SECTIONS = [
    ('spec-color', 'Color &amp; Filament'),
    ('spec-electrical', 'Electrical'),
    ('spec-dimming', 'Dimming &amp; Controls'),
    ('spec-materials', 'Materials &amp; Finish'),
    ('spec-compliance', 'Compliance &amp; Warranty'),
]

def patch_spec_grid(src, grid_class, prefix):
    """Replace 2-column spec grid with TOC sidebar + content column."""
    # Find the spec grid div
    pattern = rf'<div style="display:grid;grid-template-columns:1fr 1fr;gap:3rem;" class="{grid_class}">'
    if pattern not in src:
        # Try without the style attribute (some pages may differ)
        return src, False

    toc_html = make_toc_sidebar(prefix, STANDARD_SECTIONS)
    new_open = f'<div style="display:grid;grid-template-columns:220px 1fr;gap:3rem;align-items:start;" class="{grid_class}">\n{toc_html}'
    src = src.replace(pattern, new_open)

    # Remove grid-column:1/-1 from the compliance article (no longer needed in single-column layout)
    src = re.sub(
        r'<article id="spec-compliance" style="grid-column:1/-1;">',
        '<article id="spec-compliance">',
        src
    )
    # Remove the 2-column dl from compliance
    src = re.sub(
        r'<dl style="display:grid;grid-template-columns:1fr 1fr;gap:0 2rem;">',
        '<dl>',
        src
    )
    # Close the content div before closing the grid div
    # Find the closing </div> of the spec grid and add the content div closer
    # The grid div ends with </div> after the last article + style block
    # We need to add </div> before the grid's closing </div>
    # Strategy: find the media query style block and add </div> before it
    src = re.sub(
        rf'(\s*<style>\s*@media \(max-width: 900px\) \{{ \.{grid_class} \{{ grid-template-columns: 1fr !important; \}}\s*\}}.*?</style>)',
        r'\n      </div>\1',
        src,
        flags=re.DOTALL
    )
    return src, True

def ensure_three_swatches(src):
    """Make sure the glass finish row has 3 swatch chips (Clear, Amber, Smoked)."""
    # Check if already has 3 swatches
    swatch_count = src.count('class="swatch"')
    if swatch_count >= 3:
        return src, False

    # Find the glass finish row and inject the third swatch
    # Pattern: dd containing swatch chips but only 2
    three_swatches = (
        '<span class="swatch" style="background:rgba(239,230,210,0.5);border:1px solid rgba(26,19,10,0.3);" title="Clear"></span><span style="font-size:0.85rem;">Clear (C)</span>\n'
        '            &nbsp;\n'
        '            <span class="swatch" style="background:#C7822E;" title="Amber"></span><span style="font-size:0.85rem;">Amber (V · X)</span>\n'
        '            &nbsp;\n'
        '            <span class="swatch" style="background:#6E5236;" title="Smoked"></span><span style="font-size:0.85rem;">Smoked (M)</span>'
    )

    # Find the glass finish dd and replace its content
    def replace_glass_dd(m):
        existing = m.group(1)
        if 'swatch' in existing and existing.count('swatch') >= 3:
            return m.group(0)
        return f'<dd>\n            {three_swatches}\n          </dd>'

    new_src = re.sub(
        r'<dd>([^<]*(?:<span[^>]*swatch[^>]*>[^<]*</span>[^<]*){1,2}[^<]*(?:Clear|Amber|Smoked|glass|Glass)[^<]*)</dd>',
        replace_glass_dd,
        src
    )
    if new_src != src:
        return new_src, True

    # Fallback: look for glass options row and inject swatches
    # Pattern: <dt>Glass options</dt><dd>...</dd> or <dt>Glass finish</dt><dd>...</dd>
    def inject_into_glass_row(m):
        dd_content = m.group(1)
        if 'swatch' in dd_content:
            return m.group(0)
        return f'<dd>\n            {three_swatches}\n          </dd>'

    new_src = re.sub(
        r'<dt>Glass (?:options|finish|type|color)</dt>\s*<dd>(.*?)</dd>',
        lambda m: '<dt>Glass finish</dt>\n          ' + inject_into_glass_row(type('M', (), {'group': lambda self, n: m.group(n)})()),
        src,
        flags=re.DOTALL | re.IGNORECASE
    )
    if new_src != src:
        return new_src, True

    return src, False

# Page configurations: (rel_path, grid_class, css_prefix)
PAGES = [
    ('vintage-decor/victorian.astro', 'victorian-spec-grid', 'ed'),
    ('vintage-decor/tubular.astro', 'tubular-spec-grid', 'ed'),
    ('vintage-decor/radio.astro', 'radio-spec-grid', 'ed'),
    ('vintage-decor/candelabra.astro', 'candelabra-spec-grid', 'ed'),
    ('vintage-decor/globe.astro', 'globe-spec-grid', 'ed'),
    ('nostalgic-decor/a19.astro', 'ns-spec-grid', 'ns'),
    ('nostalgic-decor/b10.astro', 'ns-spec-grid', 'ns'),
    ('nostalgic-decor/ca10.astro', 'ns-spec-grid', 'ns'),
    ('nostalgic-decor/g25.astro', 'ns-spec-grid', 'ns'),
    ('nostalgic-decor/s14.astro', 'ns-spec-grid', 'ns'),
]

print("=== G2 FULL PATCH ===")
for rel, grid_class, prefix in PAGES:
    path = os.path.join(BASE, rel)
    if not os.path.exists(path):
        print(f"  {rel}: MISSING")
        continue

    with open(path, 'r') as f:
        src = f.read()

    original = src
    changes = []

    src, changed = patch_dimmers(src)
    if changed:
        changes.append('dimmers->22')

    src, changed = patch_spec_grid(src, grid_class, prefix)
    if changed:
        changes.append('toc-sidebar')

    src, changed = ensure_three_swatches(src)
    if changed:
        changes.append('swatches->3')

    if src != original:
        with open(path, 'w') as f:
            f.write(src)
        print(f"  {rel}: PATCHED ({', '.join(changes)})")
    else:
        print(f"  {rel}: NO CHANGE (tried: {', '.join(changes) if changes else 'nothing matched'})")

print("\nDone.")
