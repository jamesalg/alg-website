#!/usr/bin/env python3
"""patch_g2_remaining.py — patch remaining 7 decor pages for G2 fidelity"""
import re, os

BASE = '/home/ubuntu/alg-website/src/pages/collections'

FULL_DIMMERS_JS = """const dimmers = [
  { model: 'TGCL-153P', brand: 'Lutron', type: 'CL (TRIAC)', series: 'Toggler' },
  { model: 'SCL-153P', brand: 'Lutron', type: 'CL (TRIAC)', series: 'Skylark' },
  { model: 'DVCL-153P', brand: 'Lutron', type: 'CL', series: 'Diva CL' },
  { model: 'LGCL-153P', brand: 'Lutron', type: 'CL', series: 'Lyneo' },
  { model: 'MACL-153M', brand: 'Lutron', type: 'CL', series: 'Maestro CL' },
  { model: 'PD-6WCL', brand: 'Lutron', type: 'Caseta wireless', series: 'Smart-home' },
  { model: 'AY-600P', brand: 'Lutron', type: 'Incandescent / TRIAC', series: 'Ariadni' },
  { model: 'D-600P', brand: 'Lutron', type: 'Incandescent / TRIAC', series: 'Diva' },
  { model: 'GL-600P', brand: 'Lutron', type: 'Incandescent / TRIAC', series: 'Glyder' },
  { model: 'S-600P', brand: 'Lutron', type: 'Incandescent / TRIAC', series: 'Skylark' },
  { model: 'DV-600P', brand: 'Lutron', type: 'Incandescent / TRIAC', series: 'Diva legacy' },
  { model: 'SELV-300P', brand: 'Lutron', type: 'ELV', series: 'Skylark ELV' },
  { model: 'DVELV-300P', brand: 'Lutron', type: 'ELV', series: 'Diva ELV' },
  { model: 'NTELV-500', brand: 'Lutron', type: 'ELV', series: 'Nova T ELV' },
  { model: 'RRD-6NA', brand: 'Lutron', type: 'RadioRA 2', series: 'Whole-home wireless' },
  { model: 'MRF-2-6ELV-120', brand: 'Lutron', type: 'RadioRA 2 ELV', series: 'Whole-home wireless ELV' },
  { model: 'HQRD-6NA', brand: 'Lutron', type: 'HomeWorks QS', series: 'Estate-grade' },
  { model: 'DSL06-1LZ', brand: 'Leviton', type: 'CL', series: 'Decora Sureslide CL' },
  { model: 'HCL45-3PW', brand: 'Legrand', type: 'CL', series: 'radiant CL' },
  { model: 'FLR603P', brand: 'Forbes & Lomax', type: 'TRIAC', series: 'Designer rotary' },
  { model: 'FLRLV603P', brand: 'Forbes & Lomax', type: 'ELV', series: 'Designer rotary ELV' },
  { model: 'DAL06P', brand: 'Cooper', type: 'CL', series: 'Aspire' },
];"""

THREE_SWATCHES_DD = ('<dd>\n'
    '            <span class="swatch" style="background:rgba(239,230,210,0.5);border:1px solid rgba(26,19,10,0.3);" title="Clear"></span><span style="font-size:0.85rem;">Clear</span>\n'
    '            &nbsp;\n'
    '            <span class="swatch" style="background:#C7822E;" title="Amber"></span><span style="font-size:0.85rem;">Amber</span>\n'
    '            &nbsp;\n'
    '            <span class="swatch" style="background:#6E5236;" title="Smoked"></span><span style="font-size:0.85rem;">Smoked</span>\n'
    '          </dd>')

PAGES = [
    ('vintage-decor/candelabra.astro', 'candelabra-spec-grid', 'ed'),
    ('vintage-decor/globe.astro', 'globe-spec-grid', 'ed'),
    ('nostalgic-decor/a19.astro', 'ns-spec-grid', 'ns'),
    ('nostalgic-decor/b10.astro', 'ns-spec-grid', 'ns'),
    ('nostalgic-decor/ca10.astro', 'ns-spec-grid', 'ns'),
    ('nostalgic-decor/g25.astro', 'ns-spec-grid', 'ns'),
    ('nostalgic-decor/s14.astro', 'ns-spec-grid', 'ns'),
]

def make_toc_sidebar(grid_class, prefix):
    sections = [
        ('spec-color', 'Color &amp; Filament'),
        ('spec-electrical', 'Electrical'),
        ('spec-dimming', 'Dimming &amp; Controls'),
        ('spec-materials', 'Materials &amp; Finish'),
        ('spec-compliance', 'Compliance &amp; Warranty'),
    ]
    nav_lines = []
    for i, (anchor, label) in enumerate(sections):
        active_class = ' active' if i == 0 else ''
        nav_lines.append(
            '          <a href="#' + anchor + '" class="toc-link' + active_class + '">'
            '<span style="font-family:var(--' + prefix + '-mono);font-size:0.65rem;opacity:0.55;">'
            + str(i+1).zfill(2) + '</span> ' + label + '</a>'
        )
    nav_html = '\n'.join(nav_lines)
    return (
        '      <aside aria-label="Spec sections" style="position:sticky;top:1.5rem;">\n'
        '        <p style="font-family:var(--' + prefix + '-mono);font-size:0.65rem;letter-spacing:0.18em;opacity:0.55;margin-bottom:0.75rem;padding:0 0.75rem;">SPEC SECTIONS</p>\n'
        '        <nav style="display:flex;flex-direction:column;gap:0.25rem;">\n'
        + nav_html + '\n'
        '        </nav>\n'
        '      </aside>\n'
        '      <div style="display:flex;flex-direction:column;gap:3rem;">'
    )

print("=== G2 REMAINING PATCH ===")
for rel, grid_class, prefix in PAGES:
    path = os.path.join(BASE, rel)
    if not os.path.exists(path):
        print(f'  {rel}: MISSING')
        continue
    with open(path) as f:
        src = f.read()
    orig = src
    changes = []

    # 1. Expand dimmers to 22
    m = re.search(r'const dimmers = \[.*?\];', src, re.DOTALL)
    if m:
        old_count = m.group(0).count('model:')
        if old_count < 22:
            src = src.replace(m.group(0), FULL_DIMMERS_JS)
            changes.append('dimmers->22')

    # 2. Spec grid -> TOC sidebar
    old_grid = '<div style="display:grid;grid-template-columns:1fr 1fr;gap:3rem;" class="' + grid_class + '">'
    if old_grid in src:
        sidebar = make_toc_sidebar(grid_class, prefix)
        new_grid = '<div style="display:grid;grid-template-columns:220px 1fr;gap:3rem;align-items:start;" class="' + grid_class + '">\n' + sidebar
        src = src.replace(old_grid, new_grid)
        # Remove grid-column:1/-1 from compliance
        src = src.replace('<article id="spec-compliance" style="grid-column:1/-1;">', '<article id="spec-compliance">')
        src = src.replace('<dl style="display:grid;grid-template-columns:1fr 1fr;gap:0 2rem;">', '<dl>')
        # Add closing </div> for content wrapper before the media query style block
        marker = '<style>\n      @media (max-width: 900px) { .' + grid_class
        if marker in src:
            src = src.replace(marker, '\n      </div>\n    ' + marker)
        else:
            # Try alternate format
            marker2 = '@media (max-width: 900px) { .' + grid_class
            if marker2 in src:
                idx = src.index(marker2)
                # Find the start of the <style> tag before this
                style_start = src.rindex('<style>', 0, idx)
                src = src[:style_start] + '\n      </div>\n    ' + src[style_start:]
        changes.append('toc-sidebar')

    # 3. Ensure 3 swatches in glass finish row
    swatch_count = src.count('class="swatch"')
    if swatch_count < 3:
        m2 = re.search(r'<dt>Glass (?:options|finish|type|color)</dt>\s*<dd>(.*?)</dd>', src, re.DOTALL | re.IGNORECASE)
        if m2:
            src = src[:m2.start()] + '<dt>Glass finish</dt>\n          ' + THREE_SWATCHES_DD + src[m2.end():]
            changes.append('swatches->3')

    if src != orig:
        with open(path, 'w') as f:
            f.write(src)
        print(f'  {rel}: PATCHED ({", ".join(changes)})')
    else:
        print(f'  {rel}: NO CHANGE (tried: {", ".join(changes) if changes else "nothing matched"})')

print("\n=== VERIFICATION ===")
all_pages = [
    'vintage-decor/victorian.astro',
    'vintage-decor/tubular.astro',
    'vintage-decor/radio.astro',
    'vintage-decor/candelabra.astro',
    'vintage-decor/globe.astro',
    'nostalgic-decor/a19.astro',
    'nostalgic-decor/b10.astro',
    'nostalgic-decor/ca10.astro',
    'nostalgic-decor/g25.astro',
    'nostalgic-decor/s14.astro',
]
for rel in all_pages:
    path = os.path.join(BASE, rel)
    if not os.path.exists(path):
        print(f'  {rel}: MISSING')
        continue
    with open(path) as f:
        src = f.read()
    sw = src.count('class="swatch"')
    tl = src.count('class="toc-link')
    dm = src.count("model: '")
    lp = 'lifestyle-photo' in src
    status = 'OK' if (sw >= 3 and tl >= 5 and dm >= 22 and lp) else 'NEEDS REVIEW'
    print(f'  {rel}: swatch={sw}, toc-link={tl}, dimmers={dm}, lifestyle={lp} -> {status}')
