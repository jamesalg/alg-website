#!/usr/bin/env python3
"""
v2.7.12 — Generate Vintage Décor family pages using the Edison pattern.
Pages: victorian, tubular, globe, radio, candelabra
"""
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VINTAGE_CSS = """
  :root {
    --ed-brick: #8B3A2A;
    --ed-cream: #EFE6D2;
    --ed-cream2: #E5D9C0;
    --ed-ink: #1A130A;
    --ed-umber: #1C0F06;
    --ed-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    --ed-serif: 'Georgia', 'Times New Roman', serif;
    --ed-mono: 'JetBrains Mono', ui-monospace, monospace;
  }
  .ed-cream  { background: var(--ed-cream); color: var(--ed-ink); }
  .ed-cream2 { background: var(--ed-cream2); color: var(--ed-ink); }
  .ed-umber  { background: var(--ed-umber); color: #EFE6D2; }
  .ed-eyebrow { font-family: var(--ed-mono); font-size: 0.68rem; letter-spacing: 0.18em; text-transform: uppercase; }
  .ed-eyebrow-rule::before { content: ""; display: inline-block; width: 28px; height: 1px; background: var(--ed-brick); vertical-align: middle; margin-right: 12px; }
  .ed-eyebrow-rule-light::before { background: rgba(245,194,74,0.7); }
  .ed-brick-text { color: var(--ed-brick); }
  .ed-h1 { font-family: var(--ed-serif); font-weight: 700; letter-spacing: -0.01em; line-height: 1.05; }
  .ed-h2 { font-family: var(--ed-serif); font-weight: 700; letter-spacing: -0.01em; line-height: 1.1; }
  .ed-serif-text { font-family: var(--ed-serif); }
  .ed-stat-num { font-family: var(--ed-sans); font-weight: 900; font-size: 1.5rem; letter-spacing: -0.02em; line-height: 1; color: var(--ed-brick); }
  .ed-stat-label { font-family: var(--ed-mono); font-size: 0.6rem; letter-spacing: 0.14em; text-transform: uppercase; opacity: 0.65; margin-top: 4px; }
  .ed-btn { display: inline-flex; align-items: center; gap: 6px; padding: 12px 24px; font-size: 0.78rem; font-weight: 700; letter-spacing: 0.06em; text-decoration: none; cursor: pointer; border: none; transition: background 0.15s; font-family: var(--ed-mono); }
  .ed-btn-primary { background: var(--ed-brick); color: white; }
  .ed-btn-primary:hover { background: #6e2d1f; }
  .ed-btn-outline { background: transparent; color: var(--ed-ink); border: 1.5px solid rgba(26,19,10,0.3); }
  .ed-btn-outline:hover { border-color: var(--ed-ink); }
  .ed-btn-ghost { background: transparent; color: var(--ed-ink); }
  .ed-btn-ghost:hover { text-decoration: underline; }
  .ed-trust-badge { font-family: var(--ed-mono); font-size: 0.6rem; letter-spacing: 0.12em; text-transform: uppercase; padding: 4px 10px; border: 1px solid rgba(26,19,10,0.2); display: inline-block; }
  .ed-photo-ph { background: #1C0F06; aspect-ratio: 4/3; display: flex; align-items: center; justify-content: center; }
  .ed-photo-ph-text { font-family: var(--ed-mono); font-size: 10px; letter-spacing: 0.14em; text-transform: uppercase; text-align: center; padding: 2rem; border: 1px dashed rgba(239,230,210,0.15); margin: 2rem; color: rgba(239,230,210,0.4); }
  .ed-spec-row { display: grid; grid-template-columns: 1fr 2fr; gap: 1rem; padding: 0.75rem 0; border-bottom: 1px solid rgba(26,19,10,0.08); font-size: 0.875rem; }
  .ed-spec-row dt { font-family: var(--ed-mono); font-size: 0.7rem; letter-spacing: 0.08em; opacity: 0.7; }
  .ed-spec-row dd { margin: 0; font-family: var(--ed-serif); }
  .ed-spec-block-num { font-family: var(--ed-mono); font-size: 0.6rem; letter-spacing: 0.18em; color: var(--ed-brick); }
  .ed-sku-table { width: 100%; background: white; border: 1px solid rgba(26,19,10,0.1); font-family: var(--ed-mono); font-size: 0.68rem; }
  .ed-sku-table th { padding: 0.75rem 1rem; text-align: left; border-bottom: 1px solid rgba(26,19,10,0.1); font-weight: 700; letter-spacing: 0.1em; opacity: 0.7; }
  .ed-sku-table td { padding: 0.6rem 1rem; border-bottom: 1px solid rgba(26,19,10,0.06); }
  .ed-sku-table tr:hover td { background: rgba(139,58,42,0.04); }
  .ed-sister-card { display: block; padding: 1.25rem; border: 1px solid rgba(26,19,10,0.1); background: var(--ed-cream); text-decoration: none; color: inherit; transition: border-color 0.15s; }
  .ed-sister-card:hover { border-color: var(--ed-brick); }
  .ed-breadcrumb { border-bottom: 1px solid rgba(26,19,10,0.1); background: white; }
  .ed-breadcrumb__inner { max-width: 1536px; margin: 0 auto; padding: 12px 24px; font-family: var(--ed-mono); font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase; opacity: 0.7; }
  .ed-breadcrumb a { color: inherit; text-decoration: none; }
  .ed-breadcrumb a:hover { color: var(--ed-brick); opacity: 1; }
  .ed-callout-ey { font-family: var(--ed-mono); font-size: 0.65rem; letter-spacing: 0.18em; text-transform: uppercase; color: #6e3a10; }
"""

DIMMERS_JS = """[
  { model: 'D-600P', brand: 'Lutron', type: 'Incandescent / TRIAC', series: 'Diva' },
  { model: 'GL-600P', brand: 'Lutron', type: 'Incandescent / TRIAC', series: 'Glyder' },
  { model: 'S-600P', brand: 'Lutron', type: 'Incandescent / TRIAC', series: 'Skylark' },
  { model: 'DV-600P', brand: 'Lutron', type: 'Incandescent / TRIAC', series: 'Diva (legacy)' },
  { model: 'SELV-300P', brand: 'Lutron', type: 'ELV', series: 'Skylark ELV' },
  { model: 'DVELV-300P', brand: 'Lutron', type: 'ELV', series: 'Diva ELV' },
  { model: 'NTELV-500', brand: 'Lutron', type: 'ELV', series: 'Nova T\u2605 ELV' },
  { model: 'RRD-6NA', brand: 'Lutron', type: 'RadioRA 2', series: 'Whole-home wireless' },
  { model: 'MRF-2-6ELV-120', brand: 'Lutron', type: 'RadioRA 2 ELV', series: 'Whole-home wireless ELV' },
  { model: 'HQRD-6NA', brand: 'Lutron', type: 'HomeWorks QS', series: 'HomeWorks QS \u00b7 estate-grade' },
  { model: 'DSL06-1LZ', brand: 'Leviton', type: 'CL', series: 'Decora Sureslide CL' },
  { model: 'HCL45-3PW', brand: 'Legrand', type: 'CL', series: 'radiant\u00ae CL' },
  { model: 'FLR603P', brand: 'Forbes & Lomax', type: 'TRIAC', series: 'Designer rotary' },
  { model: 'FLRLV603P', brand: 'Forbes & Lomax', type: 'ELV', series: 'Designer rotary ELV' },
  { model: 'DAL06P', brand: 'Cooper', type: 'CL', series: '\u2014' },
]"""

# Sister lamps section (same for all vintage pages)
VINTAGE_SISTERS = [
    ('victorian', 'VICTORIAN A19', 'The Belgravia', 'Victorian A19 in smoked, amber, squirrel-cage.'),
    ('edison', 'FOUNDRY ST19/ST21', 'The Foundry Edison', 'Squirrel-cage filament \u00b7 industrial revival.'),
    ('globe', 'GLOBE G25/G40', 'The Provence Globe', 'G25 and G40 globe in amber and smoked.'),
    ('radio', 'RADIO T10/T14', 'The Marconi Radio', 'T10 and T14 radio-style tubular.'),
    ('tubular', 'TUBULAR T9', 'The Brighton Tubular', 'T9 tubular in clear and amber.'),
    ('candelabra', 'CANDELABRA CA10', 'The Glasgow Candelabra', 'CA10 vintage candelabra in amber finish.'),
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
        cards.append(f"""      <a href="/collections/vintage-decor/{slug}/" class="ed-sister-card">
        <p style="font-family:var(--ed-mono);font-size:0.65rem;letter-spacing:0.12em;opacity:0.6;margin-bottom:0.5rem;">{shape}</p>
        <h3 class="ed-serif-text" style="font-size:1rem;margin-bottom:0.25rem;">{name}</h3>
        <p style="font-size:0.8rem;opacity:0.7;font-family:var(--ed-serif);">{tagline}</p>
      </a>""")
    return '\n'.join(cards)


def spec_rows(items):
    return '\n'.join(f'          <div class="ed-spec-row"><dt>{k}</dt><dd>{v}</dd></div>' for k, v in items)


def build_vintage_page(cfg):
    slug = cfg['slug']
    title_full = cfg['title_full']
    sub_register = cfg['sub_register']
    tagline = cfg['tagline']
    description = cfg['description']
    meta_desc = cfg['meta_desc']
    watts = cfg['watts']
    lumens = cfg['lumens']
    cri = cfg['cri']
    cct = cfg['cct']
    skus = cfg['skus']
    trust_badges = cfg.get('trust_badges', ['CRI 90+', 'UL LISTED', 'CEC TITLE 24 JA8', 'DIMMABLE TO 5%'])
    installs = cfg['installs']
    specs = cfg['specs']
    photo_label = cfg.get('photo_label', f'{title_full.upper()} IN SETTING')
    sku_note = cfg.get('sku_note', 'ALTERNATIVE CCTS AVAILABLE AS SPECIAL ORDER \u00b7 CONTACT SALES@ARCHIPELAGOLIGHTING.COM')
    datasheet_url = cfg.get('datasheet_url', 'null')
    filament_section = cfg.get('filament_section', '')
    binning_callout = cfg.get('binning_callout', '')
    sku_subtitle = cfg.get('sku_subtitle', 'Active variants.')
    resource_subtitle = cfg.get('resource_subtitle', 'For restoration architects and designers.')

    skus_js = '[\n' + '\n'.join(sku_row(s) for s in skus) + '\n]'
    trust_html = '\n'.join(f'        <span class="ed-trust-badge">{b}</span>' for b in trust_badges)
    install_html = ''
    for inst in installs:
        install_html += f"""      <div style="background:var(--ed-cream);padding:1.5rem;border:1px solid rgba(26,19,10,0.1);">
        <p class="ed-callout-ey" style="margin-bottom:0.75rem;">{inst['register']}</p>
        <h3 class="ed-serif-text" style="font-size:1.25rem;margin-bottom:0.75rem;">{inst['h3']}</h3>
        <p style="font-size:0.85rem;line-height:1.7;opacity:0.85;font-family:var(--ed-serif);">{inst['p']}</p>
      </div>\n"""

    spec_color = specs['color']
    spec_elec = specs['electrical']
    spec_dim = specs['dimming']
    spec_mat = specs['materials']
    spec_comp = specs['compliance']

    sisters_html = sister_cards(slug, VINTAGE_SISTERS)

    page = f"""---
/**
 * {title_full} \u2014 Vintage D\u00e9cor Family Detail Page
 * v2.7.12 \u2014 migrated to Edison pattern
 * Route: /collections/vintage-decor/{slug}
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
    icon: 'PDF',
    title: 'Installation Sheet',
    desc: 'Per-SKU install instructions',
    url: null,
    family: '{title_full}',
    resource: 'Installation Sheet',
  }},
  {{
    icon: 'IES',
    title: 'IES Files',
    desc: 'Photometric data \u00b7 per glass and filament suffix',
    url: null,
    family: '{title_full}',
    resource: 'IES Files',
  }},
  {{
    icon: 'PDF',
    title: 'ALG D\u00e9cor Lamps \u00b7 Product Guide \u00b7 Q2 2026',
    desc: 'Full D\u00e9cor lamp catalog',
    url: null,
    family: '{title_full}',
    resource: 'Product Guide',
  }},
];

const skus = {skus_js};

const dimmers = {DIMMERS_JS};
---
<BaseLayout
  title="{title_full} \u2014 Vintage D\u00e9cor | Archipelago Lighting Group"
  description="{meta_desc}"
  bodyClass="page-{slug}-family"
>
<style>{VINTAGE_CSS}</style>

<div class="ed-breadcrumb">
  <div class="ed-breadcrumb__inner">
    <a href="/">HOME</a> \u203a
    <a href="/products/">PRODUCTS</a> \u203a
    <a href="/products/lamps/">LAMPS</a> \u203a
    <a href="/collections/vintage-decor/">VINTAGE D\u00c9COR</a> \u203a
    {title_full.upper()}
  </div>
</div>

<main id="main">

<!-- HERO -->
<section class="ed-cream" aria-labelledby="{slug}-hero-h1">
  <div style="max-width:1536px;margin:0 auto;padding:4rem 1.5rem;display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:center;" class="{slug}-hero-grid">
    <div class="ed-photo-ph">
      <div class="ed-photo-ph-text">LIFESTYLE PHOTOGRAPHY<br><span style="opacity:0.6;">\u2014 ROOSTER CREATIVE DELIVERABLE \u2014</span><br><br><span style="opacity:0.5;">{photo_label}</span></div>
    </div>
    <div>
      <p class="ed-eyebrow ed-eyebrow-rule" style="opacity:0.6;margin-bottom:1.5rem;"><span class="ed-brick-text">SERIES \u00b7</span> VINTAGE D\u00c9COR \u00b7 {sub_register}</p>
      <h1 id="{slug}-hero-h1" class="ed-h1" style="font-size:clamp(2.5rem,5vw,4rem);margin-bottom:1rem;">{title_full}</h1>
      <p class="ed-serif-text" style="font-size:1.25rem;font-style:italic;margin-bottom:1.5rem;opacity:0.9;">{tagline}</p>
      <p class="ed-serif-text" style="font-size:1rem;line-height:1.75;margin-bottom:2rem;opacity:0.85;max-width:36rem;">{description}</p>
      <dl style="display:grid;grid-template-columns:1fr 1fr;gap:1.25rem 2rem;margin-bottom:2rem;">
        <div><dd class="ed-stat-num">{watts}</dd><dt class="ed-stat-label">Input wattage range</dt></div>
        <div><dd class="ed-stat-num">{lumens}</dd><dt class="ed-stat-label">Lumen output</dt></div>
        <div><dd class="ed-stat-num">{cct}</dd><dt class="ed-stat-label">CCT</dt></div>
        <div><dd class="ed-stat-num">{cri}</dd><dt class="ed-stat-label">Color fidelity</dt></div>
      </dl>
      <div style="display:flex;flex-wrap:wrap;gap:8px;margin-bottom:1.5rem;">
{trust_html}
      </div>
      <div style="display:flex;flex-wrap:wrap;gap:12px;">
        <a href="/support/sample-request?subject={title_full.replace(' ', '+').replace('The+', '')}+Spec" class="ed-btn ed-btn-primary">SPECIFY THIS LAMP</a>
        <a href="/support/sample-request?subject={title_full.replace(' ', '+').replace('The+', '')}+Sample" class="ed-btn ed-btn-outline">REQUEST SAMPLE</a>
        <a href="#resources" class="ed-btn ed-btn-ghost">DOCUMENTATION \u2193</a>
      </div>
    </div>
  </div>
</section>
<style>
  @media (max-width: 768px) {{ .{slug}-hero-grid {{ grid-template-columns: 1fr !important; }} }}
</style>

<!-- WHERE IT BELONGS -->
<section class="ed-cream2" aria-labelledby="{slug}-belongs-h2">
  <div style="max-width:1536px;margin:0 auto;padding:5rem 1.5rem;">
    <p class="ed-eyebrow ed-eyebrow-rule ed-brick-text" style="margin-bottom:1.5rem;">WHERE THE {title_full.upper()} BELONGS</p>
    <h2 id="{slug}-belongs-h2" class="ed-h2" style="font-size:clamp(1.75rem,3.5vw,3rem);margin-bottom:3rem;">Three install registers. One lamp.</h2>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem;" class="{slug}-belongs-grid">
{install_html}    </div>
    <style>
      @media (max-width: 768px) {{ .{slug}-belongs-grid {{ grid-template-columns: 1fr !important; }} }}
    </style>
  </div>
</section>

{filament_section}

<!-- STRUCTURED SPECS -->
<section class="ed-cream" aria-labelledby="{slug}-specs-h2">
  <div style="max-width:1536px;margin:0 auto;padding:5rem 1.5rem;">
    <p class="ed-eyebrow ed-eyebrow-rule ed-brick-text" style="margin-bottom:1.5rem;">FULL SPECIFICATIONS</p>
    <h2 id="{slug}-specs-h2" class="ed-h2" style="font-size:clamp(1.5rem,3vw,2.5rem);margin-bottom:3rem;">Spec sheet for the lamp \u00b7 restoration-grade detail.</h2>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:3rem;" class="{slug}-spec-grid">
      <article id="spec-color">
        <p class="ed-spec-block-num" style="margin-bottom:0.5rem;">01</p>
        <h3 class="ed-serif-text" style="font-size:1.5rem;margin-bottom:1rem;">Color &amp; Filament</h3>
        <dl>
{spec_rows(spec_color.items())}
        </dl>
      </article>
      <article id="spec-electrical">
        <p class="ed-spec-block-num" style="margin-bottom:0.5rem;">02</p>
        <h3 class="ed-serif-text" style="font-size:1.5rem;margin-bottom:1rem;">Electrical</h3>
        <dl>
{spec_rows(spec_elec.items())}
        </dl>
      </article>
      <article id="spec-dimming">
        <p class="ed-spec-block-num" style="margin-bottom:0.5rem;">03</p>
        <h3 class="ed-serif-text" style="font-size:1.5rem;margin-bottom:1rem;">Dimming &amp; Controls</h3>
        <dl>
{spec_rows(spec_dim.items())}
        </dl>
      </article>
      <article id="spec-materials">
        <p class="ed-spec-block-num" style="margin-bottom:0.5rem;">04</p>
        <h3 class="ed-serif-text" style="font-size:1.5rem;margin-bottom:1rem;">Materials &amp; Finish</h3>
        <dl>
{spec_rows(spec_mat.items())}
        </dl>
      </article>
      <article id="spec-compliance" style="grid-column:1/-1;">
        <p class="ed-spec-block-num" style="margin-bottom:0.5rem;">05</p>
        <h3 class="ed-serif-text" style="font-size:1.5rem;margin-bottom:1rem;">Compliance &amp; Warranty</h3>
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

<!-- DIMMER COMPATIBILITY TABLE -->
<section class="ed-cream2" aria-labelledby="{slug}-dim-h2">
  <div style="max-width:1536px;margin:0 auto;padding:5rem 1.5rem;">
    <p class="ed-eyebrow ed-eyebrow-rule ed-brick-text" style="margin-bottom:1.5rem;">DIMMER COMPATIBILITY</p>
    <h2 id="{slug}-dim-h2" class="ed-h2" style="font-size:clamp(1.5rem,3vw,2.5rem);margin-bottom:1rem;">The Nostalgic &amp; Vintage GEN-2 dimmer list.</h2>
    <p style="opacity:0.7;max-width:40rem;margin-bottom:2rem;font-size:0.9rem;font-family:var(--ed-serif);">Tested and confirmed on the following control systems. All pass at 5% minimum dim level with no flicker, buzz, or pop-on.</p>
    <div style="overflow-x:auto;">
      <table class="ed-sku-table" style="min-width:520px;">
        <thead>
          <tr>
            <th>MODEL</th><th>BRAND</th><th style="text-align:center;">TYPE</th><th style="text-align:center;">PASS</th><th>SERIES</th>
          </tr>
        </thead>
        <tbody>
          {{dimmers.map(d => (
            <tr>
              <td style="font-weight:600;">{{d.model}}</td>
              <td>{{d.brand}}</td>
              <td style="text-align:center;">{{d.type}}</td>
              <td style="text-align:center;color:#16a34a;font-weight:700;">\u2713</td>
              <td>{{d.series}}</td>
            </tr>
          ))}}
        </tbody>
      </table>
    </div>
    <p style="font-family:var(--ed-mono);font-size:0.65rem;letter-spacing:0.12em;opacity:0.6;margin-top:1rem;">\u25b8 MATRIX UPDATED 2026.Q2 \u00b7 SUBMIT YOUR CONTROL FOR TESTING</p>
  </div>
</section>

{binning_callout}

<!-- SKU TABLE -->
<section class="ed-cream2" aria-labelledby="{slug}-sku-h2">
  <div style="max-width:1536px;margin:0 auto;padding:5rem 1.5rem;">
    <p class="ed-eyebrow ed-eyebrow-rule ed-brick-text" style="margin-bottom:1.5rem;">ORDERABLE VARIANTS</p>
    <h2 id="{slug}-sku-h2" class="ed-h2" style="font-size:clamp(1.5rem,3vw,2.5rem);margin-bottom:0.75rem;">{sku_subtitle}</h2>
    <p class="ed-serif-text" style="opacity:0.8;max-width:40rem;margin-bottom:2rem;font-size:0.9rem;">All E26 medium-base unless noted. Standard-warranty 3-year / 25,000-hour rated life per datasheet. JA8-2022-E and T20-compliant variants available where required.</p>
    <div style="overflow-x:auto;">
      <table class="ed-sku-table spec-table" style="min-width:700px;">
        <thead>
          <tr>
            <th>SKU</th><th>FINISH / ENVELOPE</th><th style="text-align:center;">BASE</th><th style="text-align:center;">WATTS</th><th style="text-align:center;">EQ.</th><th style="text-align:center;">LUMENS</th><th style="text-align:center;">CCT</th><th style="text-align:center;">CRI</th><th>CERT</th>
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
    <p style="font-family:var(--ed-mono);font-size:0.65rem;letter-spacing:0.12em;opacity:0.6;margin-top:1rem;">\u25b8 {sku_note}</p>
  </div>
</section>

<!-- RESOURCES -->
<section class="ed-cream" id="resources" aria-labelledby="{slug}-resources-h2">
  <div style="max-width:1536px;margin:0 auto;padding:4rem 1.5rem;">
    <p class="ed-eyebrow ed-eyebrow-rule ed-brick-text" style="margin-bottom:1.5rem;">RESOURCES</p>
    <h2 id="{slug}-resources-h2" class="ed-h2" style="font-size:clamp(1.25rem,2.5vw,2rem);margin-bottom:2rem;">{resource_subtitle}</h2>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;" class="{slug}-resources-grid">
      {{resources.map(r => <ResourceCard {{...r}} />)}}
    </div>
    <style>
      @media (max-width: 768px) {{ .{slug}-resources-grid {{ grid-template-columns: 1fr 1fr !important; }} }}
      @media (max-width: 480px) {{ .{slug}-resources-grid {{ grid-template-columns: 1fr !important; }} }}
    </style>
  </div>
</section>

<!-- SISTER LAMPS -->
<section class="ed-cream2" aria-labelledby="{slug}-sister-h2">
  <div style="max-width:1536px;margin:0 auto;padding:4rem 1.5rem;">
    <p class="ed-eyebrow ed-eyebrow-rule ed-brick-text" style="margin-bottom:1.5rem;">SISTER LAMPS IN VINTAGE D\u00c9COR</p>
    <h2 id="{slug}-sister-h2" class="ed-h2" style="font-size:clamp(1.25rem,2.5vw,2rem);margin-bottom:2rem;">Five more named lamps. Same series register.</h2>
    <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:0.75rem;" class="{slug}-sister-grid">
{sisters_html}
    </div>
    <style>
      @media (max-width: 900px) {{ .{slug}-sister-grid {{ grid-template-columns: 1fr 1fr !important; }} }}
    </style>
  </div>
</section>

<!-- DARK CTA -->
<section style="background:#1C0F06;">
  <div style="max-width:1280px;margin:0 auto;padding:5rem 1.5rem;text-align:center;color:#EFE6D2;">
    <h2 class="ed-h1" style="font-size:clamp(1.75rem,3.5vw,2.75rem);margin-bottom:1.5rem;">Specify the {title_full}. Honor the room.</h2>
    <p class="ed-serif-text" style="opacity:0.7;max-width:40rem;margin:0 auto 2rem;line-height:1.7;">Restoration architects answered same business day. Heritage binning kits shipped 5-day. Custom filament geometries quoted within 48 hours.</p>
    <div style="display:flex;justify-content:center;gap:12px;flex-wrap:wrap;">
      <a href="/support/sample-request?subject={title_full.replace(' ', '+').replace('The+', '')}+Spec" class="ed-btn ed-btn-primary">SPECIFY THIS LAMP</a>
      <a href="/support/sample-request?subject={title_full.replace(' ', '+').replace('The+', '')}+Sample" class="ed-btn" style="background:transparent;color:#EFE6D2;border:1.5px solid rgba(239,230,210,0.3);">REQUEST SAMPLE</a>
      <a href="https://algportal.archipelagolighting.com" class="ed-btn" style="background:transparent;color:#EFE6D2;border:1.5px solid rgba(239,230,210,0.3);" target="_blank" rel="noopener">SHOP STOCK &amp; BUY</a>
    </div>
  </div>
</section>

</main>
</BaseLayout>
"""
    return page


# ─── PRODUCT DATA ─────────────────────────────────────────────────────────────

HERITAGE_BINNING = """<!-- HERITAGE BINNING CALLOUT -->
<section class="ed-cream">
  <div style="max-width:1536px;margin:0 auto;padding:3rem 1.5rem;">
    <div style="background:#E5D9C0;border:1px solid rgba(26,19,10,0.1);padding:2rem;">
      <p class="ed-callout-ey" style="margin-bottom:0.75rem;">\u2014 HERITAGE BINNING KIT</p>
      <h3 class="ed-h2" style="font-size:1.5rem;margin-bottom:0.75rem;">For the restoration that requires the right lamp, not just any lamp.</h3>
      <p class="ed-serif-text" style="font-size:1rem;opacity:0.9;line-height:1.7;max-width:48rem;">Heritage binning kits ship 50 lamps from the same production run with verified 3-step MacAdam consistency and matching filament geometry. For restoration architects specifying 200+ lamps in a single heritage interior \u2014 the lobby chandelier, the corridor sconces, the bar pendants \u2014 where period accuracy and visual consistency across the entire space are non-negotiable.</p>
    </div>
  </div>
</section>"""

PAGES = [
    {
        'slug': 'victorian',
        'title_full': 'The Belgravia Victorian',
        'sub_register': 'VICTORIAN REVIVAL',
        'tagline': 'The lamp Belgravia townhouses were lit by, rebuilt for today.',
        'description': 'The lamp Belgravia townhouses were lit by, rebuilt for today. The Belgravia Victorian captures the refined residential warmth of Victorian-era London \u2014 A19 silhouette, amber or smoked finish, squirrel-cage and spiral filament options, and a 2200K glow that reads as candlelight from across the room. For hospitality spaces, residential dining rooms, and any application where the lamp sets the mood before the food arrives.',
        'meta_desc': 'The Belgravia Victorian: CRI 90+, 2200K, A19 silhouette, amber/smoked glass, dimmable to 5%. Victorian revival lamp for hospitality and residential dining.',
        'watts': '3.5\u20134.5W',
        'lumens': '250\u2013350 lm',
        'cct': '2200K',
        'cri': 'CRI 90+',
        'trust_badges': ['CRI 90+', 'UL LISTED', 'CEC TITLE 24 JA8', 'DIMMABLE TO 5%'],
        'photo_label': 'BELGRAVIA VICTORIAN IN DINING ROOM SETTING\nWARM EVENING REGISTER \u00b7 CANDLELIGHT REGISTER',
        'installs': [
            {'register': 'RESIDENTIAL \u00b7 DINING ROOM', 'h3': 'The lamp that sets the mood before the food.', 'p': 'Dining room pendants, sideboard sconces, and formal living room fixtures. The Victorian A19 silhouette is familiar; the 2200K glow is the register of candlelight, not fluorescent.'},
            {'register': 'HOSPITALITY \u00b7 BOUTIQUE HOTEL', 'h3': 'Period accuracy at property scale.', 'p': 'Boutique hotels in Victorian and Edwardian buildings where the lamp must match the architecture. Heritage binning kits ensure 3-step MacAdam consistency across the entire property.'},
            {'register': 'RESTAURANT \u00b7 FINE DINING', 'h3': 'The lamp that earns the Michelin star.', 'p': 'Fine-dining ambient lighting, private dining rooms, and wine-cellar fixtures. The 2200K CCT renders the second-half-of-evening register that fine dining requires.'},
        ],
        'specs': {
            'color': {'CCT': '2200K (candle-hour)', 'CRI': '\u226590', 'Filament geometry': 'Squirrel-cage \u00b7 spiral (per SKU)', 'Glass options': 'Amber \u00b7 Smoked', 'Envelope': 'A19 (60mm)'},
            'electrical': {'Input voltage': '120V AC \u00b7 60Hz', 'Wattage range': '3.5W \u2013 4.5W (per SKU)', 'Lumen output': '250 \u2013 350 lm (per SKU)', 'L70 life': '25,000 hours'},
            'dimming': {'Dimming types': 'TRIAC \u00b7 ELV \u00b7 CL', 'Dim-to': '5% (smooth, flicker-free)', 'Compatible systems': 'Lutron \u00b7 Leviton \u00b7 Legrand \u00b7 Forbes &amp; Lomax \u00b7 Cooper'},
            'materials': {'Base': 'E26 medium screw base', 'Filament suffix': 'V (squirrel-cage) \u00b7 S (spiral)', 'MOL': '~4.8" (122mm)'},
            'compliance': {'Safety': 'UL Listed', 'Energy code': 'CEC Title 24 JA8-2022-E \u00b7 T20 (on JA8 variants)', 'Warranty': '3 years / 25,000 hours', 'RoHS': 'Compliant'},
        },
        'skus': [
            {'sku': 'LTVA19V35022MB', 'finish': 'Amber \u00b7 A19 \u00b7 Squirrel-cage', 'base': 'E26', 'watts': '3.5W', 'eq': '40W', 'lumens': '250', 'cct': '2200K', 'cri': '90+', 'cert': '\u2014'},
            {'sku': 'LTVA19V45022MB', 'finish': 'Amber \u00b7 A19 \u00b7 Squirrel-cage', 'base': 'E26', 'watts': '4.5W', 'eq': '40W', 'lumens': '350', 'cct': '2200K', 'cri': '90+', 'cert': '\u2014'},
            {'sku': 'LTVA19V45022MB/JA8', 'finish': 'Amber \u00b7 A19 \u00b7 Spiral', 'base': 'E26', 'watts': '4.5W', 'eq': '40W', 'lumens': '350', 'cct': '2200K', 'cri': '90+', 'cert': 'JA8 \u00b7 T20'},
            {'sku': 'LTVA19S35022MB', 'finish': 'Smoked \u00b7 A19 \u00b7 Squirrel-cage', 'base': 'E26', 'watts': '3.5W', 'eq': '40W', 'lumens': '250', 'cct': '2200K', 'cri': '90+', 'cert': '\u2014'},
            {'sku': 'LTVA19S45022MB', 'finish': 'Smoked \u00b7 A19 \u00b7 Squirrel-cage', 'base': 'E26', 'watts': '4.5W', 'eq': '40W', 'lumens': '350', 'cct': '2200K', 'cri': '90+', 'cert': '\u2014'},
            {'sku': 'LTVA19S45022MB/JA8', 'finish': 'Smoked \u00b7 A19 \u00b7 Spiral', 'base': 'E26', 'watts': '4.5W', 'eq': '40W', 'lumens': '350', 'cct': '2200K', 'cri': '90+', 'cert': 'JA8 \u00b7 T20'},
        ],
        'binning_callout': HERITAGE_BINNING,
        'sku_subtitle': 'Nine datasheet variants. Amber and Smoked glass. Two filament geometries.',
        'resource_subtitle': 'For restoration architects and designers.',
    },
    {
        'slug': 'tubular',
        'title_full': 'The Brighton Tubular',
        'sub_register': 'REGENCY REVIVAL',
        'tagline': 'Regency theatricality in a T9 form factor.',
        'description': "Regency theatricality in a T9 form factor. The Brighton Tubular brings the architectural drama of Brighton Pavilion's glass-and-light tradition to a compact T9 shape \u2014 clear or amber finish, spiral filament options, and a 2200K warmth that works in vanity strips, bathroom sconces, and decorative wall fixtures. Slim enough to disappear into the fixture. Warm enough to define the room.",
        'meta_desc': 'The Brighton Tubular: CRI 90+, 2200K, T9 tubular, clear/amber glass, dimmable to 5%. Regency revival lamp for vanity strips, bathroom sconces, and wall fixtures.',
        'watts': '2\u20133.5W',
        'lumens': '150\u2013280 lm',
        'cct': '2200K',
        'cri': 'CRI 90+',
        'trust_badges': ['CRI 90+', 'UL LISTED', 'CEC TITLE 24 JA8', 'DIMMABLE TO 5%'],
        'photo_label': 'BRIGHTON TUBULAR IN VANITY SCONCE SETTING\nWARM REGISTER \u00b7 BATHROOM CONTEXT',
        'installs': [
            {'register': 'RESIDENTIAL \u00b7 BATHROOM SCONCE', 'h3': 'The tubular that frames the mirror.', 'p': 'Bathroom wall sconces, vanity strips, and powder-room fixtures. The T9 tubular silhouette adds architectural interest; the 2200K warmth flatters skin tones in the mirror register.'},
            {'register': 'HOSPITALITY \u00b7 GUEST BATH', 'h3': 'Consistent across the property.', 'p': 'Hotel bathroom sconces and vanity strips where the lamp must match across a full property renovation. Heritage binning kits ensure 3-step MacAdam consistency.'},
            {'register': 'RESTAURANT \u00b7 WALL SCONCE', 'h3': 'The slim lamp that earns its place.', 'p': 'Restaurant wall sconces, bar back-lighting, and decorative wall fixtures. The T9 tubular silhouette is slim enough to disappear into the fixture; the 2200K warmth creates the atmosphere.'},
        ],
        'specs': {
            'color': {'CCT': '2200K (candle-hour)', 'CRI': '\u226590', 'Filament geometry': 'Spiral (standard) \u00b7 squirrel-cage (select SKUs)', 'Glass options': 'Clear \u00b7 Amber', 'Envelope': 'T9 (29mm diameter)'},
            'electrical': {'Input voltage': '120V AC \u00b7 60Hz', 'Wattage range': '2W \u2013 3.5W (per SKU)', 'Lumen output': '150 \u2013 280 lm (per SKU)', 'L70 life': '25,000 hours'},
            'dimming': {'Dimming types': 'TRIAC \u00b7 ELV \u00b7 CL', 'Dim-to': '5% (smooth, flicker-free)', 'Compatible systems': 'Lutron \u00b7 Leviton \u00b7 Legrand \u00b7 Forbes &amp; Lomax \u00b7 Cooper'},
            'materials': {'Base': 'E26 medium screw base', 'Filament suffix': 'V (squirrel-cage) \u00b7 S (spiral)', 'MOL': '~5.5" (140mm)'},
            'compliance': {'Safety': 'UL Listed', 'Energy code': 'CEC Title 24 JA8-2022-E \u00b7 T20 (on JA8 variants)', 'Warranty': '3 years / 25,000 hours', 'RoHS': 'Compliant'},
        },
        'skus': [
            {'sku': 'LTT9C20022MB', 'finish': 'Clear \u00b7 T9 \u00b7 Spiral', 'base': 'E26', 'watts': '2.0W', 'eq': '25W', 'lumens': '150', 'cct': '2200K', 'cri': '90+', 'cert': '\u2014'},
            {'sku': 'LTT9C35022MB', 'finish': 'Clear \u00b7 T9 \u00b7 Spiral', 'base': 'E26', 'watts': '3.5W', 'eq': '40W', 'lumens': '280', 'cct': '2200K', 'cri': '90+', 'cert': '\u2014'},
            {'sku': 'LTT9C35022MB/JA8', 'finish': 'Clear \u00b7 T9 \u00b7 Spiral', 'base': 'E26', 'watts': '3.5W', 'eq': '40W', 'lumens': '280', 'cct': '2200K', 'cri': '90+', 'cert': 'JA8 \u00b7 T20'},
            {'sku': 'LTT9V20022MB', 'finish': 'Amber \u00b7 T9 \u00b7 Squirrel-cage', 'base': 'E26', 'watts': '2.0W', 'eq': '25W', 'lumens': '150', 'cct': '2200K', 'cri': '90+', 'cert': '\u2014'},
            {'sku': 'LTT9V35022MB', 'finish': 'Amber \u00b7 T9 \u00b7 Squirrel-cage', 'base': 'E26', 'watts': '3.5W', 'eq': '40W', 'lumens': '280', 'cct': '2200K', 'cri': '90+', 'cert': '\u2014'},
            {'sku': 'LTT9V35022MB/JA8', 'finish': 'Amber \u00b7 T9 \u00b7 Spiral', 'base': 'E26', 'watts': '3.5W', 'eq': '40W', 'lumens': '280', 'cct': '2200K', 'cri': '90+', 'cert': 'JA8 \u00b7 T20'},
        ],
        'binning_callout': HERITAGE_BINNING,
        'sku_subtitle': 'Active T9 tubular variants. Clear and Amber glass.',
        'resource_subtitle': 'For restoration architects and designers.',
    },
    {
        'slug': 'globe',
        'title_full': 'The Provence Globe',
        'sub_register': 'BISTRO GLOBE',
        'tagline': "Warm light in a shape you can't ignore.",
        'description': "Warm light in a shape you can't ignore. The Provence Globe brings the amber glow of a Proven\u00e7al farmhouse to G25 and G40 pendants \u2014 a round silhouette that reads as decorative even when unlit, and a 2200K warmth that turns any table into a gathering place. For bistro pendants, globe strings, and open-shade fixtures where the lamp is the fixture.",
        'meta_desc': 'The Provence Globe: CRI 90+, 2200K, G25/G40 globe, amber/smoked glass, dimmable to 5%. Bistro globe lamp for pendant fixtures and open-shade applications.',
        'watts': '2\u20133.5W',
        'lumens': '150\u2013280 lm',
        'cct': '2200K',
        'cri': 'CRI 90+',
        'trust_badges': ['CRI 90+', 'UL LISTED', 'CEC TITLE 24 JA8', 'DIMMABLE TO 5%'],
        'photo_label': 'PROVENCE GLOBE IN BISTRO PENDANT SETTING\nWARM EVENING REGISTER \u00b7 OUTDOOR DINING CONTEXT',
        'installs': [
            {'register': 'RESTAURANT \u00b7 BISTRO PENDANT', 'h3': 'The globe that defines the table.', 'p': 'Bistro pendant fixtures, open-shade pendants, and restaurant ambient lighting. The G25/G40 globe silhouette is the fixture; the 2200K warmth creates the gathering-place register.'},
            {'register': 'HOSPITALITY \u00b7 OUTDOOR DINING', 'h3': 'Globe strings above the terrace.', 'p': 'Hotel and restaurant outdoor dining terraces, rooftop bars, and courtyard string lights. The Provence Globe in G40 creates the outdoor bistro register that hospitality spaces require.'},
            {'register': 'RESIDENTIAL \u00b7 PENDANT', 'h3': 'The globe that earns the kitchen island.', 'p': 'Kitchen island pendants, dining room open-shade fixtures, and living room accent lighting. The round silhouette reads as decorative even when unlit.'},
        ],
        'specs': {
            'color': {'CCT': '2200K (candle-hour)', 'CRI': '\u226590', 'Filament geometry': 'Squirrel-cage \u00b7 spiral (per SKU)', 'Glass options': 'Amber \u00b7 Smoked', 'Envelope': 'G25 (80mm) \u00b7 G40 (127mm)'},
            'electrical': {'Input voltage': '120V AC \u00b7 60Hz', 'Wattage range': '2W \u2013 3.5W (per SKU)', 'Lumen output': '150 \u2013 280 lm (per SKU)', 'L70 life': '25,000 hours'},
            'dimming': {'Dimming types': 'TRIAC \u00b7 ELV \u00b7 CL', 'Dim-to': '5% (smooth, flicker-free)', 'Compatible systems': 'Lutron \u00b7 Leviton \u00b7 Legrand \u00b7 Forbes &amp; Lomax \u00b7 Cooper'},
            'materials': {'Base': 'E26 medium screw base', 'Filament suffix': 'V (squirrel-cage) \u00b7 S (spiral)', 'MOL (G25)': '~4.8" (122mm)', 'MOL (G40)': '~6.5" (165mm)'},
            'compliance': {'Safety': 'UL Listed', 'Energy code': 'CEC Title 24 JA8-2022-E \u00b7 T20 (on JA8 variants)', 'Warranty': '3 years / 25,000 hours', 'RoHS': 'Compliant'},
        },
        'skus': [
            {'sku': 'LTG25V20022MB', 'finish': 'Amber \u00b7 G25 \u00b7 Squirrel-cage', 'base': 'E26', 'watts': '2.0W', 'eq': '25W', 'lumens': '150', 'cct': '2200K', 'cri': '90+', 'cert': '\u2014'},
            {'sku': 'LTG25V35022MB', 'finish': 'Amber \u00b7 G25 \u00b7 Squirrel-cage', 'base': 'E26', 'watts': '3.5W', 'eq': '40W', 'lumens': '280', 'cct': '2200K', 'cri': '90+', 'cert': '\u2014'},
            {'sku': 'LTG25V35022MB/JA8', 'finish': 'Amber \u00b7 G25 \u00b7 Spiral', 'base': 'E26', 'watts': '3.5W', 'eq': '40W', 'lumens': '280', 'cct': '2200K', 'cri': '90+', 'cert': 'JA8 \u00b7 T20'},
            {'sku': 'LTG25S35022MB', 'finish': 'Smoked \u00b7 G25 \u00b7 Squirrel-cage', 'base': 'E26', 'watts': '3.5W', 'eq': '40W', 'lumens': '280', 'cct': '2200K', 'cri': '90+', 'cert': '\u2014'},
            {'sku': 'LTG40V35022MB', 'finish': 'Amber \u00b7 G40 \u00b7 Squirrel-cage', 'base': 'E26', 'watts': '3.5W', 'eq': '40W', 'lumens': '280', 'cct': '2200K', 'cri': '90+', 'cert': '\u2014'},
            {'sku': 'LTG40S35022MB', 'finish': 'Smoked \u00b7 G40 \u00b7 Squirrel-cage', 'base': 'E26', 'watts': '3.5W', 'eq': '40W', 'lumens': '280', 'cct': '2200K', 'cri': '90+', 'cert': '\u2014'},
        ],
        'binning_callout': HERITAGE_BINNING,
        'sku_subtitle': 'Eleven datasheet variants. G25 and G40 envelopes. Amber and Smoked glass.',
        'resource_subtitle': 'For bistro designers and restoration architects.',
    },
    {
        'slug': 'radio',
        'title_full': 'The Marconi Radio',
        'sub_register': 'ART DECO REVIVAL',
        'tagline': 'The tubular lamp with a wireless-era pedigree.',
        'description': 'The tubular lamp with a wireless-era pedigree. The Marconi Radio takes the T10 and T14 radio-bulb form \u2014 long, slender, unmistakably vintage \u2014 and pairs it with 2200K amber warmth and a 92 CRI option for spaces where color accuracy matters as much as atmosphere. For wall sconces, art-deco pendants, and any fixture that calls for a lamp with a story.',
        'meta_desc': 'The Marconi Radio: CRI 90+, 2200K, T10/T14 radio-style tubular, dimmable to 5%. Art Deco revival lamp for wall sconces and decorative pendants.',
        'watts': '3.5W',
        'lumens': '250\u2013280 lm',
        'cct': '2200K',
        'cri': 'CRI 90+',
        'trust_badges': ['CRI 90+', 'UL LISTED', 'CEC TITLE 24 JA8', 'DIMMABLE TO 5%'],
        'photo_label': 'MARCONI RADIO IN ART DECO SCONCE SETTING\nWARM REGISTER \u00b7 WALL FIXTURE CONTEXT',
        'installs': [
            {'register': 'RESIDENTIAL \u00b7 ART DECO SCONCE', 'h3': 'The lamp that earns the sconce.', 'p': 'Art Deco wall sconces, period-appropriate pendant fixtures, and decorative table lamps where the T10/T14 radio-bulb silhouette is part of the design language.'},
            {'register': 'HOSPITALITY \u00b7 HERITAGE HOTEL', 'h3': 'Period accuracy in the corridor.', 'p': 'Heritage hotel corridors, boutique hotel lobbies, and restaurant bar back-lighting where the radio-bulb silhouette signals period authenticity.'},
            {'register': 'RESTAURANT \u00b7 BAR LIGHTING', 'h3': 'The lamp behind the bar.', 'p': 'Bar back-lighting, speakeasy ambient fixtures, and cocktail-bar wall sconces. The T10/T14 radio-bulb silhouette is the architectural detail; the 2200K warmth creates the atmosphere.'},
        ],
        'specs': {
            'color': {'CCT': '2200K (candle-hour)', 'CRI': '\u226590', 'Filament geometry': 'Squirrel-cage \u00b7 spiral (per SKU)', 'Glass options': 'Amber \u00b7 Clear', 'Envelope': 'T10 (32mm) \u00b7 T14 (44mm)'},
            'electrical': {'Input voltage': '120V AC \u00b7 60Hz', 'Wattage range': '3.5W (per SKU)', 'Lumen output': '250 \u2013 280 lm (per SKU)', 'L70 life': '25,000 hours'},
            'dimming': {'Dimming types': 'TRIAC \u00b7 ELV \u00b7 CL', 'Dim-to': '5% (smooth, flicker-free)', 'Compatible systems': 'Lutron \u00b7 Leviton \u00b7 Legrand \u00b7 Forbes &amp; Lomax \u00b7 Cooper'},
            'materials': {'Base': 'E26 medium screw base', 'Filament suffix': 'V (squirrel-cage) \u00b7 S (spiral)', 'MOL (T10)': '~5.5" (140mm)', 'MOL (T14)': '~6.0" (152mm)'},
            'compliance': {'Safety': 'UL Listed', 'Energy code': 'CEC Title 24 JA8-2022-E \u00b7 T20 (on JA8 variants)', 'Warranty': '3 years / 25,000 hours', 'RoHS': 'Compliant'},
        },
        'skus': [
            {'sku': 'LTT10V35022MB', 'finish': 'Amber \u00b7 T10 \u00b7 Squirrel-cage', 'base': 'E26', 'watts': '3.5W', 'eq': '40W', 'lumens': '250', 'cct': '2200K', 'cri': '90+', 'cert': '\u2014'},
            {'sku': 'LTT10V35022MB/JA8', 'finish': 'Amber \u00b7 T10 \u00b7 Spiral', 'base': 'E26', 'watts': '3.5W', 'eq': '40W', 'lumens': '280', 'cct': '2200K', 'cri': '90+', 'cert': 'JA8 \u00b7 T20'},
            {'sku': 'LTT10C35022MB', 'finish': 'Clear \u00b7 T10 \u00b7 Squirrel-cage', 'base': 'E26', 'watts': '3.5W', 'eq': '40W', 'lumens': '250', 'cct': '2200K', 'cri': '90+', 'cert': '\u2014'},
            {'sku': 'LTT14V35022MB', 'finish': 'Amber \u00b7 T14 \u00b7 Squirrel-cage', 'base': 'E26', 'watts': '3.5W', 'eq': '40W', 'lumens': '280', 'cct': '2200K', 'cri': '90+', 'cert': '\u2014'},
            {'sku': 'LTT14V35022MB/JA8', 'finish': 'Amber \u00b7 T14 \u00b7 Spiral', 'base': 'E26', 'watts': '3.5W', 'eq': '40W', 'lumens': '280', 'cct': '2200K', 'cri': '90+', 'cert': 'JA8 \u00b7 T20'},
            {'sku': 'LTT14C35022MB', 'finish': 'Clear \u00b7 T14 \u00b7 Squirrel-cage', 'base': 'E26', 'watts': '3.5W', 'eq': '40W', 'lumens': '280', 'cct': '2200K', 'cri': '90+', 'cert': '\u2014'},
            {'sku': 'LTT14C35022MB/JA8', 'finish': 'Clear \u00b7 T14 \u00b7 Spiral', 'base': 'E26', 'watts': '3.5W', 'eq': '40W', 'lumens': '280', 'cct': '2200K', 'cri': '90+', 'cert': 'JA8 \u00b7 T20'},
        ],
        'binning_callout': HERITAGE_BINNING,
        'sku_subtitle': 'Seven datasheet variants. T10 and T14 envelopes. Amber and Clear glass.',
        'resource_subtitle': 'For restoration architects and Art Deco designers.',
    },
    {
        'slug': 'candelabra',
        'title_full': 'The Glasgow Candelabra',
        'sub_register': 'CRAFTSMAN REVIVAL',
        'tagline': 'A chandelier lamp that earns its place in the room.',
        'description': 'A chandelier lamp that earns its place in the room. The Glasgow Candelabra draws on the craftsman tradition of the Glasgow School of Art \u2014 hand-blown amber glass, a warm 2200K glow, and a CA10 silhouette that disappears into the fixture and lets the light do the talking. For dining rooms, sconces, and decorative pendants where the bulb is part of the composition.',
        'meta_desc': 'The Glasgow Candelabra: CRI 90+, 2200K, CA10 vintage candelabra, amber glass, dimmable to 5%. Craftsman revival candelabra for chandeliers and decorative sconces.',
        'watts': '2\u20134.5W',
        'lumens': '180\u2013350 lm',
        'cct': '2200K',
        'cri': 'CRI 90+',
        'trust_badges': ['CRI 90+', 'UL LISTED', 'CEC TITLE 24 JA8', 'DIMMABLE TO 5%'],
        'photo_label': 'GLASGOW CANDELABRA IN CHANDELIER SETTING\nWARM EVENING REGISTER \u00b7 DINING ROOM CONTEXT',
        'installs': [
            {'register': 'RESIDENTIAL \u00b7 CHANDELIER', 'h3': 'The candelabra that earns the chandelier.', 'p': 'Dining room chandeliers, foyer pendants, and living-room sconce clusters. The Glasgow Candelabra in amber glass creates the craftsman warmth that Arts and Crafts interiors require.'},
            {'register': 'HOSPITALITY \u00b7 HERITAGE LOBBY', 'h3': 'Period accuracy at property scale.', 'p': 'Heritage hotel lobby chandeliers and corridor sconces where the lamp must match the architecture. Heritage binning kits ensure 3-step MacAdam consistency across the entire property.'},
            {'register': 'RESTAURANT \u00b7 AMBIENT', 'h3': 'The candelabra above the table.', 'p': 'Restaurant ambient chandeliers, bar sconces, and private dining room fixtures. The CA10 silhouette is familiar; the 2200K amber warmth creates the gathering-place register.'},
        ],
        'specs': {
            'color': {'CCT': '2200K (candle-hour)', 'CRI': '\u226590', 'Filament geometry': 'Squirrel-cage \u00b7 spiral (per SKU)', 'Glass options': 'Amber', 'Envelope': 'CA10 flame-tip (32mm diameter)'},
            'electrical': {'Input voltage': '120V AC \u00b7 60Hz', 'Wattage range': '2W \u2013 4.5W (per SKU)', 'Lumen output': '180 \u2013 350 lm (per SKU)', 'L70 life': '25,000 hours'},
            'dimming': {'Dimming types': 'TRIAC \u00b7 ELV \u00b7 CL', 'Dim-to': '5% (smooth, flicker-free)', 'Compatible systems': 'Lutron \u00b7 Leviton \u00b7 Legrand \u00b7 Forbes &amp; Lomax \u00b7 Cooper'},
            'materials': {'Base': 'E12 candelabra screw base', 'Filament suffix': 'V (squirrel-cage) \u00b7 S (spiral)', 'MOL': '~4.0" (102mm)'},
            'compliance': {'Safety': 'UL Listed', 'Energy code': 'CEC Title 24 JA8-2022-E \u00b7 T20 (on JA8 variants)', 'Warranty': '3 years / 25,000 hours', 'RoHS': 'Compliant'},
        },
        'skus': [
            {'sku': 'LTCA10V20022MB', 'finish': 'Amber \u00b7 CA10 \u00b7 Squirrel-cage', 'base': 'E12', 'watts': '2.0W', 'eq': '25W', 'lumens': '180', 'cct': '2200K', 'cri': '90+', 'cert': '\u2014'},
            {'sku': 'LTCA10V35022MB', 'finish': 'Amber \u00b7 CA10 \u00b7 Squirrel-cage', 'base': 'E12', 'watts': '3.5W', 'eq': '40W', 'lumens': '280', 'cct': '2200K', 'cri': '90+', 'cert': '\u2014'},
            {'sku': 'LTCA10V45022MB', 'finish': 'Amber \u00b7 CA10 \u00b7 Squirrel-cage', 'base': 'E12', 'watts': '4.5W', 'eq': '40W', 'lumens': '350', 'cct': '2200K', 'cri': '90+', 'cert': '\u2014'},
            {'sku': 'LTCA10V45022MB/JA8', 'finish': 'Amber \u00b7 CA10 \u00b7 Spiral', 'base': 'E12', 'watts': '4.5W', 'eq': '40W', 'lumens': '350', 'cct': '2200K', 'cri': '90+', 'cert': 'JA8 \u00b7 T20'},
            {'sku': 'LTCA10S35022MB', 'finish': 'Smoked \u00b7 CA10 \u00b7 Squirrel-cage', 'base': 'E12', 'watts': '3.5W', 'eq': '40W', 'lumens': '280', 'cct': '2200K', 'cri': '90+', 'cert': '\u2014'},
            {'sku': 'LTCA10S45022MB/JA8', 'finish': 'Smoked \u00b7 CA10 \u00b7 Spiral', 'base': 'E12', 'watts': '4.5W', 'eq': '40W', 'lumens': '350', 'cct': '2200K', 'cri': '90+', 'cert': 'JA8 \u00b7 T20'},
        ],
        'binning_callout': HERITAGE_BINNING,
        'sku_subtitle': 'Six datasheet variants. Amber and Smoked glass. Two filament geometries.',
        'resource_subtitle': 'For restoration architects and craftsman designers.',
    },
]


if __name__ == '__main__':
    out_dir = os.path.join(BASE, 'src', 'pages', 'collections', 'vintage-decor')
    for cfg in PAGES:
        slug = cfg['slug']
        path = os.path.join(out_dir, f'{slug}.astro')
        content = build_vintage_page(cfg)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        size = len(content.encode('utf-8'))
        print(f'  wrote {slug}.astro ({size:,} bytes)')
    print('Done.')
