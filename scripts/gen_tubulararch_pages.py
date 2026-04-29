#!/usr/bin/env python3
"""
v2.7.12 — Generate tubulⒶRCH family pages using the T8 pattern.
Pages: t5, pl, pll, u6
"""
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

T8_CSS = """
  :root {
    --t8-accent: #F32740;
    --t8-warm: #F5C24A;
    --t8-char: #0F0F0F;
    --t8-paper: #F8F6F2;
    --t8-paper2: #F0EDE7;
    --t8-ink: #111111;
    --t8-mono: 'JetBrains Mono', ui-monospace, monospace;
    --t8-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  }
  .t8-paper  { background: var(--t8-paper); color: var(--t8-ink); }
  .t8-paper2 { background: var(--t8-paper2); color: var(--t8-ink); }
  .t8-dark   { background: var(--t8-char); color: white; }
  .t8-eyebrow { font-family: var(--t8-mono); font-size: 0.68rem; letter-spacing: 0.18em; text-transform: uppercase; }
  .t8-eyebrow-rule::before { content: ""; display: inline-block; width: 28px; height: 1px; background: var(--t8-accent); vertical-align: middle; margin-right: 12px; }
  .t8-accent-text { color: var(--t8-accent); }
  .t8-warm-text   { color: var(--t8-warm); }
  .t8-h1 { font-family: var(--t8-sans); font-weight: 800; letter-spacing: -0.025em; line-height: 1.0; }
  .t8-h2 { font-family: var(--t8-sans); font-weight: 800; letter-spacing: -0.02em; line-height: 1.05; }
  .t8-stat-num { font-family: var(--t8-sans); font-weight: 900; font-size: 1.75rem; letter-spacing: -0.02em; line-height: 1; color: var(--t8-accent); }
  .t8-stat-label { font-family: var(--t8-mono); font-size: 0.6rem; letter-spacing: 0.14em; text-transform: uppercase; opacity: 0.65; margin-top: 4px; }
  .t8-btn { display: inline-flex; align-items: center; gap: 6px; padding: 12px 24px; font-size: 0.78rem; font-weight: 700; letter-spacing: 0.06em; text-decoration: none; cursor: pointer; border: none; transition: background 0.15s; font-family: var(--t8-mono); }
  .t8-btn-primary { background: var(--t8-accent); color: white; }
  .t8-btn-primary:hover { background: #d01f33; }
  .t8-btn-outline { background: transparent; color: var(--t8-ink); border: 1.5px solid rgba(17,17,17,0.3); }
  .t8-btn-outline:hover { border-color: var(--t8-ink); }
  .t8-btn-ghost { background: transparent; color: var(--t8-ink); }
  .t8-btn-ghost:hover { text-decoration: underline; }
  .t8-trust-badge { font-family: var(--t8-mono); font-size: 0.6rem; letter-spacing: 0.12em; text-transform: uppercase; padding: 4px 10px; border: 1px solid rgba(17,17,17,0.2); display: inline-block; }
  .t8-photo-ph { background: #1a1a1a; aspect-ratio: 4/3; display: flex; align-items: center; justify-content: center; }
  .t8-photo-ph-text { font-family: var(--t8-mono); font-size: 10px; letter-spacing: 0.14em; text-transform: uppercase; text-align: center; padding: 2rem; border: 1px dashed rgba(255,255,255,0.12); margin: 2rem; color: rgba(255,255,255,0.4); }
  .t8-spec-row { display: grid; grid-template-columns: 1fr 2fr; gap: 1rem; padding: 0.75rem 0; border-bottom: 1px solid rgba(17,17,17,0.08); font-size: 0.875rem; }
  .t8-spec-row dt { font-family: var(--t8-mono); font-size: 0.7rem; letter-spacing: 0.08em; opacity: 0.7; }
  .t8-spec-row dd { margin: 0; }
  .t8-spec-block-num { font-family: var(--t8-mono); font-size: 0.6rem; letter-spacing: 0.18em; color: var(--t8-accent); }
  .t8-candor { background: rgba(245,194,74,0.12); border-left: 3px solid var(--t8-warm); padding: 1.5rem 2rem; }
  .t8-candor-ey { font-family: var(--t8-mono); color: #8a6510; font-size: 0.68rem; letter-spacing: 0.18em; text-transform: uppercase; }
  .t8-sku-table { width: 100%; background: white; border: 1px solid rgba(17,17,17,0.1); font-family: var(--t8-mono); font-size: 0.7rem; }
  .t8-sku-table th { padding: 0.75rem 1rem; text-align: left; border-bottom: 1px solid rgba(17,17,17,0.1); font-weight: 700; letter-spacing: 0.1em; opacity: 0.7; }
  .t8-sku-table td { padding: 0.6rem 1rem; border-bottom: 1px solid rgba(17,17,17,0.06); }
  .t8-sister-card { display: block; padding: 1.25rem; border: 1px solid rgba(17,17,17,0.1); background: white; text-decoration: none; color: inherit; transition: border-color 0.15s; }
  .t8-sister-card:hover { border-color: var(--t8-accent); }
  .t8-breadcrumb { border-bottom: 1px solid rgba(17,17,17,0.1); background: white; }
  .t8-breadcrumb__inner { max-width: 1536px; margin: 0 auto; padding: 12px 24px; font-family: var(--t8-mono); font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase; opacity: 0.7; }
  .t8-breadcrumb a { color: inherit; text-decoration: none; }
  .t8-breadcrumb a:hover { color: var(--t8-accent); opacity: 1; }
"""

# Sister families for tubulararch
TUBULARARCH_SISTERS = [
    ('t5', 'T5', 'Slim T5', 'T5HE / T5HO \u00b7 electronic ballast or bypass'),
    ('t8', 'T8', 'Workhorse T8', '4ft G13 bipin \u00b7 Type A+B hybrid'),
    ('pl', 'PL', 'Compact PL', '2G11 / G24q-3 / G23 biax retrofit'),
    ('pll', 'PLL', 'Long-Pin PLL', 'Wraparound &amp; corridor retrofit'),
    ('u6', 'U6', 'U-Bend U6', '2\u00d72 troffer drop-in retrofit'),
]


def sku_row(s):
    return (
        f"  {{ sku: '{s['sku']}', finish: '{s['finish']}', base: '{s['base']}', "
        f"watts: '{s['watts']}', eq: '{s['eq']}', lumens: '{s['lumens']}', "
        f"cct: '{s['cct']}', cri: '{s['cri']}', cert: '{s['cert']}' }},"
    )


def sister_cards(current_slug, sisters):
    cards = []
    for slug, shape, name, tagline in sisters:
        if slug == current_slug:
            continue
        cards.append(f"""      <a href="/collections/tubulararch/{slug}/" class="t8-sister-card">
        <p style="font-family:var(--t8-mono);font-size:0.65rem;letter-spacing:0.12em;opacity:0.6;margin-bottom:0.5rem;">{shape} \u00b7 Q3 <span class="cy">2026</span></p>
        <h3 style="font-weight:600;margin-bottom:0.25rem;">{name}</h3>
        <p style="font-size:0.8rem;opacity:0.7;">{tagline}</p>
      </a>""")
    return '\n'.join(cards)


def spec_rows(items):
    return '\n'.join(f'          <div class="t8-spec-row"><dt>{k}</dt><dd>{v}</dd></div>' for k, v in items)


def build_tubulararch_page(cfg):
    slug = cfg['slug']
    title_full = cfg['title_full']
    sub_register = cfg['sub_register']
    tagline = cfg['tagline']
    description = cfg['description']
    meta_desc = cfg['meta_desc']
    watts = cfg['watts']
    lumens = cfg['lumens']
    cri = cfg['cri']
    skus = cfg['skus']
    trust_badges = cfg.get('trust_badges', ['cULus LISTED', 'DLC LISTED', '5-YEAR WARRANTY'])
    specs = cfg['specs']
    photo_label = cfg.get('photo_label', f'{title_full.upper()} PRODUCT PHOTOGRAPHY')
    sku_note = cfg.get('sku_note', 'ALTERNATIVE WATTAGES AVAILABLE AS SPECIAL ORDER \u00b7 CONTACT SALES@ARCHIPELAGOLIGHTING.COM')
    datasheet_url = cfg.get('datasheet_url', 'null')
    candor = cfg.get('candor', '')
    sku_subtitle = cfg.get('sku_subtitle', f'Active {slug.upper()} variants.')

    skus_js = '[\n' + '\n'.join(sku_row(s) for s in skus) + '\n]'
    trust_html = '\n'.join(f'        <span class="t8-trust-badge">{b}</span>' for b in trust_badges)
    sisters_html = sister_cards(slug, TUBULARARCH_SISTERS)

    candor_section = ''
    if candor:
        candor_section = f"""<!-- ENGINEERING CANDOR -->
<section class="t8-paper2">
  <div style="max-width:1536px;margin:0 auto;padding:3rem 1.5rem;">
    <div class="t8-candor" style="max-width:56rem;">
      <p class="t8-candor-ey" style="margin-bottom:0.75rem;">\u2014 ENGINEERING CANDOR \u00b7 LAB VS. FIELD</p>
      <h3 style="font-size:1.25rem;font-weight:700;margin-bottom:0.75rem;">Where the spec-sheet number and the field number diverge.</h3>
      <p style="font-size:0.9rem;line-height:1.7;opacity:0.9;">{candor}</p>
    </div>
  </div>
</section>"""

    spec_color = specs.get('color', {})
    spec_elec = specs.get('electrical', {})
    spec_dim = specs.get('dimming', {})
    spec_mat = specs.get('materials', {})
    spec_comp = specs.get('compliance', {})

    page = f"""---
/**
 * {title_full} \u2014 tubul<span class="aa">\u24b6</span>RCH Family Detail Page
 * v2.7.12 \u2014 migrated to T8 pattern
 * Route: /collections/tubulararch/{slug}
 */
import BaseLayout from '../../../layouts/BaseLayout.astro';
import ResourceCard from '../../../components/ResourceCard.astro';

const resources = [
  {{
    icon: 'PDF',
    title: 'Datasheet',
    desc: '{title_full} product datasheet',
    url: {datasheet_url},
    family: '{title_full}',
    resource: 'Datasheet',
  }},
  {{
    icon: 'IES',
    title: 'IES Files',
    desc: 'Photometric data per CCT and series',
    url: null,
    family: '{title_full}',
    resource: 'IES Files',
  }},
  {{
    icon: 'PDF',
    title: 'Ballast Compatibility List',
    desc: 'Per-ballast pass / caveat at rated load',
    url: null,
    family: '{title_full}',
    resource: 'Ballast Compatibility List',
  }},
  {{
    icon: 'PDF',
    title: 'Install Guide',
    desc: 'Installation instructions for {title_full}',
    url: null,
    family: '{title_full}',
    resource: 'Install Guide',
  }},
];

const skus = {skus_js};
---
<BaseLayout
  title="{title_full} \u2014 Linear LED Retrofit | tubul<span class='aa'>\u24b6</span>RCH | Archipelago Lighting Group"
  description="{meta_desc}"
  bodyClass="page-{slug}-family"
>
<style>{T8_CSS}</style>

<div class="t8-breadcrumb">
  <div class="t8-breadcrumb__inner">
    <a href="/">HOME</a> \u203a
    <a href="/products/">PRODUCTS</a> \u203a
    <a href="/products/lamps/">LAMPS</a> \u203a
    <a href="/collections/tubulararch/">TUBUL<span class="aa">\u24b6</span>RCH</a> \u203a
    {title_full.upper()}
  </div>
</div>

<main id="main">

<!-- HERO -->
<section class="t8-paper" aria-labelledby="{slug}-hero-h1">
  <div style="max-width:1536px;margin:0 auto;padding:4rem 1.5rem;display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:center;" class="{slug}-hero-grid">
    <div class="t8-photo-ph">
      <div class="t8-photo-ph-text">{photo_label}<br><span style="opacity:0.5;">\u2014 ROOSTER CREATIVE DELIVERABLE \u2014</span></div>
    </div>
    <div>
      <p class="t8-eyebrow t8-eyebrow-rule" style="opacity:0.6;margin-bottom:1.5rem;"><span class="t8-accent-text">TUBUL<span class="aa">\u24b6</span>RCH \u00b7</span> {sub_register}</p>
      <h1 id="{slug}-hero-h1" class="t8-h1" style="font-size:clamp(2.5rem,5vw,3.75rem);margin-bottom:1rem;">{title_full}</h1>
      <p style="font-size:1rem;line-height:1.75;margin-bottom:2rem;opacity:0.85;max-width:36rem;">{description}</p>
      <dl style="display:grid;grid-template-columns:1fr 1fr;gap:1.25rem 2rem;margin-bottom:2rem;">
        <div><dd class="t8-stat-num">{watts}</dd><dt class="t8-stat-label">Wattage range</dt></div>
        <div><dd class="t8-stat-num">{lumens}</dd><dt class="t8-stat-label">Lumen output</dt></div>
        <div><dd class="t8-stat-num">{cri}</dd><dt class="t8-stat-label">CRI</dt></div>
        <div><dd class="t8-stat-num">5-yr</dd><dt class="t8-stat-label">Warranty</dt></div>
      </dl>
      <div style="display:flex;flex-wrap:wrap;gap:8px;margin-bottom:1.5rem;">
{trust_html}
      </div>
      <div style="display:flex;flex-wrap:wrap;gap:12px;">
        <a href="/support/sample-request?subject={title_full.replace(' ', '+')}+Quote" class="t8-btn t8-btn-primary">REQUEST QUOTE</a>
        <a href="https://algportal.archipelagolighting.com" class="t8-btn t8-btn-outline" target="_blank" rel="noopener">SHOP STOCK &amp; BUY</a>
        <a href="#resources" class="t8-btn t8-btn-ghost">DOCUMENTATION \u2193</a>
      </div>
    </div>
  </div>
</section>
<style>
  @media (max-width: 768px) {{ .{slug}-hero-grid {{ grid-template-columns: 1fr !important; }} }}
</style>

<!-- TAGLINE DARK SECTION -->
<section class="t8-dark" aria-labelledby="{slug}-tag-h2">
  <div style="max-width:1536px;margin:0 auto;padding:5rem 1.5rem;">
    <p class="t8-eyebrow" style="color:var(--t8-warm);margin-bottom:1.5rem;">\u2014 {sub_register}</p>
    <h2 id="{slug}-tag-h2" class="t8-h2" style="font-size:clamp(1.75rem,3.5vw,3rem);margin-bottom:1rem;">{tagline}</h2>
    <p style="opacity:0.7;max-width:48rem;line-height:1.7;">{description}</p>
  </div>
</section>

<!-- STRUCTURED SPEC TABLE -->
<section class="t8-paper" aria-labelledby="{slug}-spec-h2">
  <div style="max-width:1536px;margin:0 auto;padding:5rem 1.5rem;">
    <p class="t8-eyebrow t8-eyebrow-rule t8-accent-text" style="margin-bottom:1.5rem;">FULL SPECIFICATION</p>
    <h2 id="{slug}-spec-h2" class="t8-h2" style="font-size:clamp(1.5rem,3vw,2.5rem);margin-bottom:3rem;">The numbers that matter to a spec writer.</h2>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:3rem;" class="{slug}-spec-grid">
      <article>
        <p class="t8-spec-block-num" style="margin-bottom:0.5rem;">01</p>
        <h3 style="font-size:1.25rem;font-weight:700;margin-bottom:1rem;">Physical</h3>
        <dl>
{spec_rows(spec_color.items())}
        </dl>
      </article>
      <article>
        <p class="t8-spec-block-num" style="margin-bottom:0.5rem;">02</p>
        <h3 style="font-size:1.25rem;font-weight:700;margin-bottom:1rem;">Photometrics</h3>
        <dl>
{spec_rows(spec_elec.items())}
        </dl>
      </article>
      <article>
        <p class="t8-spec-block-num" style="margin-bottom:0.5rem;">03</p>
        <h3 style="font-size:1.25rem;font-weight:700;margin-bottom:1rem;">Electrical</h3>
        <dl>
{spec_rows(spec_dim.items())}
        </dl>
      </article>
      <article>
        <p class="t8-spec-block-num" style="margin-bottom:0.5rem;">04</p>
        <h3 style="font-size:1.25rem;font-weight:700;margin-bottom:1rem;">Retrofit Type &amp; Compatibility</h3>
        <dl>
{spec_rows(spec_mat.items())}
        </dl>
      </article>
      <article style="grid-column:1/-1;">
        <p class="t8-spec-block-num" style="margin-bottom:0.5rem;">05</p>
        <h3 style="font-size:1.25rem;font-weight:700;margin-bottom:1rem;">Compliance &amp; Listings</h3>
        <dl style="display:grid;grid-template-columns:1fr 1fr;gap:0 2rem;">
{spec_rows(spec_comp.items())}
        </dl>
      </article>
    </div>
    <style>
      @media (max-width: 900px) {{ .{slug}-spec-grid {{ grid-template-columns: 1fr !important; }} }}
      @media (max-width: 900px) {{ .{slug}-spec-grid article[style*="grid-column"] {{ grid-column: 1 !important; }} }}
    </style>
  </div>
</section>

{candor_section}

<!-- RESOURCES BLOCK -->
<section class="t8-paper2" id="resources" aria-labelledby="{slug}-resources-h2">
  <div style="max-width:1536px;margin:0 auto;padding:4rem 1.5rem;">
    <p class="t8-eyebrow t8-eyebrow-rule t8-accent-text" style="margin-bottom:1.5rem;">RESOURCES</p>
    <h2 id="{slug}-resources-h2" class="t8-h2" style="font-size:clamp(1.25rem,2.5vw,2rem);margin-bottom:2rem;">Everything a spec writer needs in one click.</h2>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;" class="{slug}-resources-grid">
      {{resources.map(r => <ResourceCard {{...r}} />)}}
    </div>
    <style>
      @media (max-width: 768px) {{ .{slug}-resources-grid {{ grid-template-columns: 1fr 1fr !important; }} }}
      @media (max-width: 480px) {{ .{slug}-resources-grid {{ grid-template-columns: 1fr !important; }} }}
    </style>
  </div>
</section>

<!-- SKU TABLE -->
<section class="t8-paper" aria-labelledby="{slug}-sku-h2">
  <div style="max-width:1536px;margin:0 auto;padding:5rem 1.5rem;">
    <p class="t8-eyebrow t8-eyebrow-rule t8-accent-text" style="margin-bottom:1.5rem;">ORDERABLE VARIANTS</p>
    <h2 id="{slug}-sku-h2" class="t8-h2" style="font-size:clamp(1.5rem,3vw,2.5rem);margin-bottom:0.75rem;">{sku_subtitle}</h2>
    <div style="overflow-x:auto;">
      <table class="t8-sku-table spec-table" style="min-width:700px;">
        <thead>
          <tr>
            <th>SKU</th><th>DESCRIPTION</th><th style="text-align:center;">BASE</th><th style="text-align:center;">WATTS</th><th style="text-align:center;">EQ.</th><th style="text-align:center;">LUMENS</th><th style="text-align:center;">CCT</th><th style="text-align:center;">CRI</th><th>CERT</th>
          </tr>
        </thead>
        <tbody>
          {{skus.map(s => (
            <tr>
              <td style="font-weight:600;">{{s.sku}}</td>
              <td>{{s.finish}}</td>
              <td style="text-align:center;">{{s.base}}</td>
              <td style="text-align:center;">{{s.watts}}</td>
              <td style="text-align:center;">{{s.eq}}</td>
              <td style="text-align:center;">{{s.lumens}}</td>
              <td style="text-align:center;">{{s.cct}}</td>
              <td style="text-align:center;">{{s.cri}}</td>
              <td>{{s.cert}}</td>
            </tr>
          ))}}
        </tbody>
      </table>
    </div>
    <p style="font-family:var(--t8-mono);font-size:0.6rem;letter-spacing:0.12em;opacity:0.5;margin-top:1rem;">\u25b8 {sku_note}</p>
  </div>
</section>

<!-- SISTER FAMILIES -->
<section class="t8-paper2" aria-labelledby="{slug}-sister-h2">
  <div style="max-width:1536px;margin:0 auto;padding:4rem 1.5rem;">
    <p class="t8-eyebrow t8-eyebrow-rule t8-accent-text" style="margin-bottom:1.5rem;">SISTER FAMILIES IN THIS COLLECTION</p>
    <h2 id="{slug}-sister-h2" class="t8-h2" style="font-size:clamp(1.25rem,2.5vw,2rem);margin-bottom:2rem;">Four more form factors. Same tubul<span class="aa">\u24b6</span>RCH standard.</h2>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;" class="{slug}-sister-grid">
{sisters_html}
    </div>
    <style>
      @media (max-width: 768px) {{ .{slug}-sister-grid {{ grid-template-columns: 1fr 1fr !important; }} }}
    </style>
  </div>
</section>

<!-- DARK CTA -->
<section class="t8-dark">
  <div style="max-width:1280px;margin:0 auto;padding:5rem 1.5rem;text-align:center;">
    <h2 class="t8-h2" style="font-size:clamp(1.75rem,3.5vw,2.75rem);margin-bottom:1.5rem;">Ready to retrofit?</h2>
    <p style="opacity:0.7;max-width:40rem;margin:0 auto 2rem;line-height:1.7;">Stock available. Samples shipped same day. Spec response under 24 hours.</p>
    <div style="display:flex;justify-content:center;gap:12px;flex-wrap:wrap;">
      <a href="/support/sample-request?subject={title_full.replace(' ', '+')}" class="t8-btn t8-btn-primary">REQUEST SAMPLE</a>
      <a href="https://algportal.archipelagolighting.com" class="t8-btn" style="background:transparent;color:white;border:1.5px solid rgba(255,255,255,0.3);" target="_blank" rel="noopener">SHOP STOCK &amp; BUY</a>
    </div>
  </div>
</section>

</main>

<script>
  document.querySelectorAll('.cy').forEach(function(e) {{
    (e as HTMLElement).textContent = String(new Date().getFullYear());
  }});
</script>
</BaseLayout>
"""
    return page


# ─── PRODUCT DATA ─────────────────────────────────────────────────────────────

PAGES = [
    {
        'slug': 't5',
        'title_full': 'Slim T5',
        'sub_register': 'LINEAR LED RETROFIT \u00b7 T5 \u00b7 G5 BIPIN',
        'tagline': 'The T5 retrofit for every fluorescent fixture still running T5HE and T5HO.',
        'description': 'T5HE and T5HO fluorescent replacements in a single dip-switchable lamp. G5 bipin base, 2ft and 4ft lengths, Type A (ballast-compatible) and Type B (bypass) in one SKU. The tubul<span class="aa">Ⓐ</span>RCH T5 retrofit.ofit.',
        'meta_desc': 'Slim T5: T5HE/T5HO LED retrofit, G5 bipin, Type A+B hybrid, DLC listed, 5-year warranty. The tubul\u24b6RCH T5 retrofit.',
        'watts': '10\u201315W',
        'lumens': '1,400\u20132,200 lm',
        'cri': '80+',
        'trust_badges': ['cULus LISTED', 'DLC LISTED', 'UL TYPE A+B HYBRID', '5-YEAR WARRANTY'],
        'photo_label': 'SLIM T5 PRODUCT PHOTOGRAPHY\nDIP-SWITCH DETAIL \u00b7 LAMP BODY \u00b7 4FT',
        'specs': {
            'color': {'Form factor': '4ft linear T5 \u00b7 G5 bipin (RoHS-compliant)', 'Length': '46.0 in (1168 mm)', 'Diameter': '0.625 in (15.9 mm)', 'Weight': '0.18 lb (82 g)', 'Operating temp': '-20\u00b0C to +45\u00b0C'},
            'electrical': {'Lumen output': '1,400\u20132,200 lm (wattage-dependent)', 'Efficacy': 'Up to 147 lm/W', 'CCT options': '3000K \u00b7 3500K \u00b7 4000K \u00b7 5000K', 'CRI': '\u226580', 'L70 life': '>50,000 hours (TM-21, 35\u00b0C ambient)'},
            'dimming': {'Input voltage': '120\u2013277V AC \u00b7 50/60 Hz', 'Wattage (dip-switch)': '10W \u00b7 12W \u00b7 15W', 'Power factor': '>0.90', 'THD': '<20%', 'Start time': '<0.5 s to full output'},
            'materials': {'Type A (ballast-compatible)': 'Works with electronic T5 ballasts \u00b7 no rewiring', 'Type B (bypass)': 'Direct line-voltage wiring \u00b7 ballast removed', 'Hybrid': 'Same SKU supports both Type A and Type B', 'Ballast compatibility': 'See Ballast Compatibility List'},
            'compliance': {'Safety': 'UL 1598C \u00b7 CSA \u00b7 cULus Listed', 'EMC': 'FCC Part 15 Class B', 'DLC': 'DLC Listed \u00b7 SSL Replacement Lamp QPL', 'Warranty': '5 years \u00b7 pro-rated \u00b7 field-failure replacement'},
        },
        'skus': [
            {'sku': 'LTT5-10W-30K-G5', 'finish': '4ft T5 \u00b7 G5', 'base': 'G5', 'watts': '10W', 'eq': '28W', 'lumens': '1,400', 'cct': '3000K', 'cri': '80+', 'cert': 'DLC'},
            {'sku': 'LTT5-10W-40K-G5', 'finish': '4ft T5 \u00b7 G5', 'base': 'G5', 'watts': '10W', 'eq': '28W', 'lumens': '1,400', 'cct': '4000K', 'cri': '80+', 'cert': 'DLC'},
            {'sku': 'LTT5-12W-35K-G5', 'finish': '4ft T5 \u00b7 G5', 'base': 'G5', 'watts': '12W', 'eq': '28W', 'lumens': '1,750', 'cct': '3500K', 'cri': '80+', 'cert': 'DLC'},
            {'sku': 'LTT5-15W-40K-G5', 'finish': '4ft T5 \u00b7 G5', 'base': 'G5', 'watts': '15W', 'eq': '54W', 'lumens': '2,200', 'cct': '4000K', 'cri': '80+', 'cert': 'DLC'},
            {'sku': 'LTT5-15W-50K-G5', 'finish': '4ft T5 \u00b7 G5', 'base': 'G5', 'watts': '15W', 'eq': '54W', 'lumens': '2,200', 'cct': '5000K', 'cri': '80+', 'cert': 'DLC'},
        ],
        'candor': 'T5 T5 ballast compatibility is more restrictive than T8. The Slim T5 has been tested against electronic T5 ballasts from Advance, Osram, GE, and Fulham. Magnetic T5 ballasts are not supported — Type B bypass is required for magnetic-ballast fixtures. The ballast compatibility list documents this explicitly; the spec sheet alone will not catch it.t.',
        'sku_subtitle': 'Active Slim T5 variants. G5 bipin. Dip-switchable wattage.',
    },
    {
        'slug': 'pl',
        'title_full': 'Compact PL',
        'sub_register': 'LINEAR LED RETROFIT \u00b7 PL \u00b7 G24 / G23 BASE',
        'tagline': 'The PL retrofit for 2G11, G24q-3, and G23 biax fixtures.',
        'description': 'PL-PL-C, PL-L, and biax fluorescent replacements for 2G11, G24q-3, and G23 base fixtures. Type A (ballast-compatible) and Type B (bypass) in one SKU. The tubul<span class="aa">Ⓐ</span>RCH compact PL retrofit.t.',
        'meta_desc': 'Compact PL: PL-C/PL-L/biax LED retrofit, G24/G23 base, Type A+B hybrid, DLC listed, 5-year warranty. The tubul\u24b6RCH compact PL retrofit.',
        'watts': '9\u201313W',
        'lumens': '900\u20131,300 lm',
        'cri': '80+',
        'trust_badges': ['cULus LISTED', 'DLC LISTED', 'UL TYPE A+B HYBRID', '5-YEAR WARRANTY'],
        'photo_label': 'COMPACT PL PRODUCT PHOTOGRAPHY\nLAMP BODY \u00b7 G24 BASE DETAIL',
        'specs': {
            'color': {'Form factor': 'PL-C / PL-L \u00b7 G24q-3 / G24d-3 / G23 base', 'Length': 'Varies by base (see datasheet)', 'Diameter': '1.2 in (30 mm) typ.', 'Weight': '0.20 lb (91 g) typ.', 'Operating temp': '-20\u00b0C to +45\u00b0C'},
            'electrical': {'Lumen output': '900\u20131,300 lm (wattage-dependent)', 'Efficacy': 'Up to 100 lm/W', 'CCT options': '3000K \u00b7 3500K \u00b7 4000K \u00b7 5000K', 'CRI': '\u226580', 'L70 life': '>50,000 hours (TM-21, 35\u00b0C ambient)'},
            'dimming': {'Input voltage': '120\u2013277V AC \u00b7 50/60 Hz', 'Wattage range': '9W \u2013 13W (per SKU)', 'Power factor': '>0.90', 'THD': '<20%', 'Start time': '<0.5 s to full output'},
            'materials': {'Type A (ballast-compatible)': 'Works with electronic PL ballasts \u00b7 no rewiring', 'Type B (bypass)': 'Direct line-voltage wiring \u00b7 ballast removed', 'Hybrid': 'Same SKU supports both Type A and Type B', 'Ballast compatibility': 'See Ballast Compatibility List'},
            'compliance': {'Safety': 'UL 1598C \u00b7 CSA \u00b7 cULus Listed', 'EMC': 'FCC Part 15 Class B', 'DLC': 'DLC Listed \u00b7 SSL Replacement Lamp QPL', 'Warranty': '5 years \u00b7 pro-rated \u00b7 field-failure replacement'},
        },
        'skus': [
            {'sku': 'LTPL-9W-30K-G24', 'finish': 'PL-C \u00b7 G24q-3', 'base': 'G24q-3', 'watts': '9W', 'eq': '26W', 'lumens': '900', 'cct': '3000K', 'cri': '80+', 'cert': 'DLC'},
            {'sku': 'LTPL-9W-40K-G24', 'finish': 'PL-C \u00b7 G24q-3', 'base': 'G24q-3', 'watts': '9W', 'eq': '26W', 'lumens': '900', 'cct': '4000K', 'cri': '80+', 'cert': 'DLC'},
            {'sku': 'LTPL-13W-35K-G24', 'finish': 'PL-C \u00b7 G24q-3', 'base': 'G24q-3', 'watts': '13W', 'eq': '32W', 'lumens': '1,300', 'cct': '3500K', 'cri': '80+', 'cert': 'DLC'},
            {'sku': 'LTPL-13W-40K-G24', 'finish': 'PL-C \u00b7 G24q-3', 'base': 'G24q-3', 'watts': '13W', 'eq': '32W', 'lumens': '1,300', 'cct': '4000K', 'cri': '80+', 'cert': 'DLC'},
            {'sku': 'LTPL-9W-40K-G23', 'finish': 'PL-S \u00b7 G23', 'base': 'G23', 'watts': '9W', 'eq': '13W', 'lumens': '900', 'cct': '4000K', 'cri': '80+', 'cert': 'DLC'},
        ],
        'candor': 'PL baPL ballast compatibility is the most restrictive in the tubul<span class="aa">Ⓐ</span>RCH line. 4-pin electronic ballasts (G24q-3) are generally compatible; 2-pin magnetic ballasts (G24d-3) require Type B bypass. Always verify the ballast type before specifying Type A mode. The ballast compatibility list documents this by model; the spec sheet alone will not catch magnetic-ballast fixtures.',
        'sku_subtitle': 'Active Compact PL variants. G24 and G23 base options.',
    },
    {
        'slug': 'pll',
        'title_full': 'Long-Pin PLL',
        'sub_register': 'LINEAR LED RETROFIT \u00b7 PLL \u00b7 2G11 BASE',
        'tagline': 'The PLL retrofit for wraparound and corridor fixtures with 2G11 base.',
        'description': 'PLL (lPLL (long-pin) fluorescent replacements for 2G11 base fixtures — wraparound fixtures, corridor lighting, and recessed downlights. Type A (ballast-compatible) and Type B (bypass) in one SKU. The tubul<span class="aa">Ⓐ</span>RCH long-pin PLL retrofit.fit.',
        'meta_desc': 'Long-Pin PLL: PLL LED retrofit, 2G11 base, Type A+B hybrid, DLC listed, 5-year warranty. The tubul\u24b6RCH PLL retrofit for wraparound and corridor fixtures.',
        'watts': '12\u201318W',
        'lumens': '1,200\u20131,800 lm',
        'cri': '80+',
        'trust_badges': ['cULus LISTED', 'DLC LISTED', 'UL TYPE A+B HYBRID', '5-YEAR WARRANTY'],
        'photo_label': 'LONG-PIN PLL PRODUCT PHOTOGRAPHY\nLAMP BODY \u00b7 2G11 BASE DETAIL',
        'specs': {
            'color': {'Form factor': 'PLL long-pin \u00b7 2G11 base', 'Length': '~16.5 in (419 mm) typ.', 'Diameter': '1.2 in (30 mm) typ.', 'Weight': '0.22 lb (100 g) typ.', 'Operating temp': '-20\u00b0C to +45\u00b0C'},
            'electrical': {'Lumen output': '1,200\u20131,800 lm (wattage-dependent)', 'Efficacy': 'Up to 100 lm/W', 'CCT options': '3000K \u00b7 3500K \u00b7 4000K \u00b7 5000K', 'CRI': '\u226580', 'L70 life': '>50,000 hours (TM-21, 35\u00b0C ambient)'},
            'dimming': {'Input voltage': '120\u2013277V AC \u00b7 50/60 Hz', 'Wattage range': '12W \u2013 18W (per SKU)', 'Power factor': '>0.90', 'THD': '<20%', 'Start time': '<0.5 s to full output'},
            'materials': {'Type A (ballast-compatible)': 'Works with electronic PLL ballasts \u00b7 no rewiring', 'Type B (bypass)': 'Direct line-voltage wiring \u00b7 ballast removed', 'Hybrid': 'Same SKU supports both Type A and Type B', 'Ballast compatibility': 'See Ballast Compatibility List'},
            'compliance': {'Safety': 'UL 1598C \u00b7 CSA \u00b7 cULus Listed', 'EMC': 'FCC Part 15 Class B', 'DLC': 'DLC Listed \u00b7 SSL Replacement Lamp QPL', 'Warranty': '5 years \u00b7 pro-rated \u00b7 field-failure replacement'},
        },
        'skus': [
            {'sku': 'LTPLL-12W-30K-2G11', 'finish': 'PLL \u00b7 2G11', 'base': '2G11', 'watts': '12W', 'eq': '36W', 'lumens': '1,200', 'cct': '3000K', 'cri': '80+', 'cert': 'DLC'},
            {'sku': 'LTPLL-12W-40K-2G11', 'finish': 'PLL \u00b7 2G11', 'base': '2G11', 'watts': '12W', 'eq': '36W', 'lumens': '1,200', 'cct': '4000K', 'cri': '80+', 'cert': 'DLC'},
            {'sku': 'LTPLL-18W-35K-2G11', 'finish': 'PLL \u00b7 2G11', 'base': '2G11', 'watts': '18W', 'eq': '55W', 'lumens': '1,800', 'cct': '3500K', 'cri': '80+', 'cert': 'DLC'},
            {'sku': 'LTPLL-18W-40K-2G11', 'finish': 'PLL \u00b7 2G11', 'base': '2G11', 'watts': '18W', 'eq': '55W', 'lumens': '1,800', 'cct': '4000K', 'cri': '80+', 'cert': 'DLC'},
            {'sku': 'LTPLL-18W-50K-2G11', 'finish': 'PLL \u00b7 2G11', 'base': '2G11', 'watts': '18W', 'eq': '55W', 'lumens': '1,800', 'cct': '5000K', 'cri': '80+', 'cert': 'DLC'},
        ],
        'candor': 'PLL 2G11 ballasts are among the least standardized in commercial fluorescent. The Long-Pin PLL has been tested against electronic ballasts from Advance, Osram, and Fulham. Magnetic 2G11 ballasts require Type B bypass. The ballast compatibility list documents this by model; the spec sheet alone will not catch magnetic-ballast fixtures.',
        'sku_subtitle': 'Active Long-Pin PLL variants. 2G11 base.',
    },
    {
        'slug': 'u6',
        'title_full': 'U-Bend U6',
        'sub_register': 'LINEAR LED RETROFIT \u00b7 U6 \u00b7 G13 BIPIN',
        'tagline': 'The U-bend T8 retrofit for 2\u00d72 troffer fixtures.',
        'description': 'U-bU-bend T8 fluorescent replacements for 2×2 troffer fixtures. G13 bipin base, Type A (ballast-compatible) and Type B (bypass) in one SKU. Drop-in retrofit for the most common 2×2 commercial troffer. The tubul<span class="aa">Ⓐ</span>RCH U-bend retrofit.nd retrofit.',
        'meta_desc': 'U-Bend U6: U-bend T8 LED retrofit, G13 bipin, Type A+B hybrid, DLC listed, 5-year warranty. The tubul\u24b6RCH U6 retrofit for 2x2 troffer fixtures.',
        'watts': '10.5\u201315W',
        'lumens': '1,400\u20132,000 lm',
        'cri': '80+',
        'trust_badges': ['cULus LISTED', 'DLC LISTED', 'UL TYPE A+B HYBRID', '5-YEAR WARRANTY'],
        'photo_label': 'U-BEND U6 PRODUCT PHOTOGRAPHY\nLAMP BODY \u00b7 U-BEND DETAIL \u00b7 2X2 TROFFER',
        'specs': {
            'color': {'Form factor': 'U-bend T8 \u00b7 G13 bipin (RoHS-compliant)', 'Leg spacing': '1.5 in (38 mm) \u00b7 matches standard U-bend fixture', 'Diameter': '1.0 in (25.4 mm)', 'Weight': '0.24 lb (109 g)', 'Operating temp': '-20\u00b0C to +45\u00b0C'},
            'electrical': {'Lumen output': '1,400\u20132,000 lm (wattage-dependent)', 'Efficacy': 'Up to 133 lm/W', 'CCT options': '3000K \u00b7 3500K \u00b7 4000K \u00b7 5000K', 'CRI': '\u226580', 'L70 life': '>50,000 hours (TM-21, 35\u00b0C ambient)'},
            'dimming': {'Input voltage': '120\u2013277V AC \u00b7 50/60 Hz', 'Wattage (dip-switch)': '10.5W \u00b7 12W \u00b7 15W', 'Power factor': '>0.90', 'THD': '<20%', 'Start time': '<0.5 s to full output'},
            'materials': {'Type A (ballast-compatible)': 'Works with electronic T8 U-bend ballasts \u00b7 no rewiring', 'Type B (bypass)': 'Direct line-voltage wiring \u00b7 ballast removed', 'Hybrid': 'Same SKU supports both Type A and Type B', 'Ballast compatibility': 'See Ballast Compatibility List'},
            'compliance': {'Safety': 'UL 1598C \u00b7 CSA \u00b7 cULus Listed', 'EMC': 'FCC Part 15 Class B', 'DLC': 'DLC Listed \u00b7 SSL Replacement Lamp QPL', 'Warranty': '5 years \u00b7 pro-rated \u00b7 field-failure replacement'},
        },
        'skus': [
            {'sku': 'LTU6-105W-30K-G13', 'finish': 'U6 U-bend \u00b7 G13', 'base': 'G13', 'watts': '10.5W', 'eq': '32W', 'lumens': '1,400', 'cct': '3000K', 'cri': '80+', 'cert': 'DLC'},
            {'sku': 'LTU6-105W-40K-G13', 'finish': 'U6 U-bend \u00b7 G13', 'base': 'G13', 'watts': '10.5W', 'eq': '32W', 'lumens': '1,400', 'cct': '4000K', 'cri': '80+', 'cert': 'DLC'},
            {'sku': 'LTU6-12W-35K-G13', 'finish': 'U6 U-bend \u00b7 G13', 'base': 'G13', 'watts': '12W', 'eq': '32W', 'lumens': '1,600', 'cct': '3500K', 'cri': '80+', 'cert': 'DLC'},
            {'sku': 'LTU6-15W-40K-G13', 'finish': 'U6 U-bend \u00b7 G13', 'base': 'G13', 'watts': '15W', 'eq': '40W', 'lumens': '2,000', 'cct': '4000K', 'cri': '80+', 'cert': 'DLC'},
            {'sku': 'LTU6-15W-50K-G13', 'finish': 'U6 U-bend \u00b7 G13', 'base': 'G13', 'watts': '15W', 'eq': '40W', 'lumens': '2,000', 'cct': '5000K', 'cri': '80+', 'cert': 'DLC'},
            {'sku': 'LTU6-15W-40K-G13/SR', 'finish': 'U6 U-bend \u00b7 G13 \u00b7 /SR', 'base': 'G13', 'watts': '15W', 'eq': '40W', 'lumens': '2,000', 'cct': '4000K', 'cri': '80+', 'cert': 'DLC'},
        ],
        'candor': 'U-bend T8 ballaU-bend T8 ballast compatibility follows the same rules as the Workhorse T8 — but the U-bend fixture geometry means the ballast is often in a more confined space with higher ambient temperatures. Real-world U-bend installs in recessed 2×2 troffers can run 5–10°C hotter than open-troffer T8 installs, reducing practical L70 life by 10–15%. The published L70 number is the conservative TM-21 calculation at 35°C.n at 35\u00b0C.',
        'sku_subtitle': 'Active U-Bend U6 variants. G13 bipin. Dip-switchable wattage.',
    },
]


if __name__ == '__main__':
    out_dir = os.path.join(BASE, 'src', 'pages', 'collections', 'tubulararch')
    for cfg in PAGES:
        slug = cfg['slug']
        path = os.path.join(out_dir, f'{slug}.astro')
        content = build_tubulararch_page(cfg)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        size = len(content.encode('utf-8'))
        print(f'  wrote {slug}.astro ({size:,} bytes)')
    print('Done.')
