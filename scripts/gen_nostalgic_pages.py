#!/usr/bin/env python3
"""
v2.7.12 — Generate Nostalgic Décor family pages using the A19 pattern.
Pages: a15, b10, ca10, g16, g25, s14
"""
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NOSTALGIC_CSS = """
  :root {
    --a19-amber: #C17B2A;
    --a19-warm: #F5EFE3;
    --a19-warm2: #EDE5D3;
    --a19-ink: #1A140C;
    --a19-umber: #2C1A0A;
    --a19-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    --a19-serif: 'Georgia', 'Times New Roman', serif;
    --a19-mono: 'JetBrains Mono', ui-monospace, monospace;
  }
  .a19-warm  { background: var(--a19-warm); color: var(--a19-ink); }
  .a19-warm2 { background: var(--a19-warm2); color: var(--a19-ink); }
  .a19-umber { background: var(--a19-umber); color: #EFE6D2; }
  .a19-eyebrow { font-family: var(--a19-mono); font-size: 0.68rem; letter-spacing: 0.18em; text-transform: uppercase; }
  .a19-eyebrow-rule::before { content: ""; display: inline-block; width: 28px; height: 1px; background: var(--a19-amber); vertical-align: middle; margin-right: 12px; }
  .a19-amber-text { color: var(--a19-amber); }
  .a19-h1 { font-family: var(--a19-serif); font-weight: 700; letter-spacing: -0.01em; line-height: 1.05; }
  .a19-h2 { font-family: var(--a19-serif); font-weight: 700; letter-spacing: -0.01em; line-height: 1.1; }
  .a19-serif-text { font-family: var(--a19-serif); }
  .a19-stat-num { font-family: var(--a19-sans); font-weight: 900; font-size: 1.5rem; letter-spacing: -0.02em; line-height: 1; color: var(--a19-amber); }
  .a19-stat-label { font-family: var(--a19-mono); font-size: 0.6rem; letter-spacing: 0.14em; text-transform: uppercase; opacity: 0.65; margin-top: 4px; }
  .a19-btn { display: inline-flex; align-items: center; gap: 6px; padding: 12px 24px; font-size: 0.78rem; font-weight: 700; letter-spacing: 0.06em; text-decoration: none; cursor: pointer; border: none; transition: background 0.15s; font-family: var(--a19-mono); }
  .a19-btn-primary { background: var(--a19-amber); color: white; }
  .a19-btn-primary:hover { background: #a06520; }
  .a19-btn-outline { background: transparent; color: var(--a19-ink); border: 1.5px solid rgba(26,20,12,0.3); }
  .a19-btn-outline:hover { border-color: var(--a19-ink); }
  .a19-btn-ghost { background: transparent; color: var(--a19-ink); }
  .a19-btn-ghost:hover { text-decoration: underline; }
  .a19-trust-badge { font-family: var(--a19-mono); font-size: 0.6rem; letter-spacing: 0.12em; text-transform: uppercase; padding: 4px 10px; border: 1px solid rgba(26,20,12,0.2); display: inline-block; }
  .a19-photo-ph { background: #2C1A0A; aspect-ratio: 4/3; display: flex; align-items: center; justify-content: center; }
  .a19-photo-ph-text { font-family: var(--a19-mono); font-size: 10px; letter-spacing: 0.14em; text-transform: uppercase; text-align: center; padding: 2rem; border: 1px dashed rgba(245,239,227,0.15); margin: 2rem; color: rgba(245,239,227,0.4); }
  .a19-spec-row { display: grid; grid-template-columns: 1fr 2fr; gap: 1rem; padding: 0.75rem 0; border-bottom: 1px solid rgba(26,20,12,0.08); font-size: 0.875rem; }
  .a19-spec-row dt { font-family: var(--a19-mono); font-size: 0.7rem; letter-spacing: 0.08em; opacity: 0.7; }
  .a19-spec-row dd { margin: 0; font-family: var(--a19-serif); }
  .a19-spec-block-num { font-family: var(--a19-mono); font-size: 0.6rem; letter-spacing: 0.18em; color: var(--a19-amber); }
  .a19-sku-table { width: 100%; background: white; border: 1px solid rgba(26,20,12,0.1); font-family: var(--a19-mono); font-size: 0.68rem; }
  .a19-sku-table th { padding: 0.75rem 1rem; text-align: left; border-bottom: 1px solid rgba(26,20,12,0.1); font-weight: 700; letter-spacing: 0.1em; opacity: 0.7; }
  .a19-sku-table td { padding: 0.6rem 1rem; border-bottom: 1px solid rgba(26,20,12,0.06); }
  .a19-sku-table tr:hover td { background: rgba(193,123,42,0.04); }
  .a19-sister-card { display: block; padding: 1.25rem; border: 1px solid rgba(26,20,12,0.1); background: var(--a19-warm); text-decoration: none; color: inherit; transition: border-color 0.15s; }
  .a19-sister-card:hover { border-color: var(--a19-amber); }
  .a19-breadcrumb { border-bottom: 1px solid rgba(26,20,12,0.1); background: white; }
  .a19-breadcrumb__inner { max-width: 1536px; margin: 0 auto; padding: 12px 24px; font-family: var(--a19-mono); font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase; opacity: 0.7; }
  .a19-breadcrumb a { color: inherit; text-decoration: none; }
  .a19-breadcrumb a:hover { color: var(--a19-amber); opacity: 1; }
  .a19-callout-ey { font-family: var(--a19-mono); font-size: 0.65rem; letter-spacing: 0.18em; text-transform: uppercase; color: #8a5a10; }
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

# Sister lamps section (same for all nostalgic pages)
NOSTALGIC_SISTERS = [
    ('a15', 'A15', 'The Saarinen', 'Small-format accent \u00b7 vanity strips'),
    ('a19', 'A19', 'The Eames', 'Standard A19 \u00b7 residential and hospitality'),
    ('b10', 'B10', 'The Knoll', 'Blunt-tip candelabra \u00b7 decorative chandeliers'),
    ('ca10', 'CA10', 'The Bauer', 'Flame-tip candelabra \u00b7 entryway and formal sconces'),
    ('g16', 'G16', 'The Heath', 'Small globe \u00b7 vanity strips'),
    ('g25', 'G25', 'The Eichler', 'Medium globe \u00b7 pendant fixtures'),
    ('s14', 'S14', 'The Marshall', 'Commercial-grade string light \u00b7 outdoor'),
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
        cards.append(f"""      <a href="/collections/nostalgic-decor/{slug}/" class="a19-sister-card">
        <p style="font-family:var(--a19-mono);font-size:0.65rem;letter-spacing:0.12em;opacity:0.6;margin-bottom:0.5rem;">{shape}</p>
        <h3 class="a19-serif-text" style="font-size:1.1rem;margin-bottom:0.25rem;">{name}</h3>
        <p style="font-size:0.8rem;opacity:0.7;font-family:var(--a19-serif);">{tagline}</p>
      </a>""")
    return '\n'.join(cards)


def build_nostalgic_page(cfg):
    slug = cfg['slug']
    title_full = cfg['title_full']
    designer = cfg['designer']
    shape_code = cfg['shape_code']
    sub_register = cfg['sub_register']
    tagline = cfg['tagline']
    description = cfg['description']
    meta_desc = cfg['meta_desc']
    watts = cfg['watts']
    lumens = cfg['lumens']
    cri = cfg['cri']
    skus = cfg['skus']
    trust_badges = cfg.get('trust_badges', ['CRI 90+', 'UL LISTED', 'CEC TITLE 24 JA8', 'DIMMABLE TO 5%'])
    installs = cfg['installs']  # list of 3 dicts: {register, h3, p}
    specs = cfg['specs']  # dict with keys: color, electrical, dimming, materials, compliance
    photo_label = cfg.get('photo_label', f'{title_full.upper()} IN SETTING')
    sku_note = cfg.get('sku_note', 'ALTERNATIVE CCTS AVAILABLE AS SPECIAL ORDER \u00b7 CONTACT SALES@ARCHIPELAGOLIGHTING.COM')
    datasheet_url = cfg.get('datasheet_url', 'null')
    coming_soon = cfg.get('coming_soon', False)

    skus_js = '[\n' + '\n'.join(sku_row(s) for s in skus) + '\n]'
    trust_html = '\n'.join(f'        <span class="a19-trust-badge">{b}</span>' for b in trust_badges)
    install_html = ''
    for inst in installs:
        install_html += f"""      <div style="background:var(--a19-warm);padding:1.5rem;border:1px solid rgba(26,20,12,0.1);">
        <p class="a19-callout-ey" style="margin-bottom:0.75rem;">{inst['register']}</p>
        <h3 class="a19-serif-text" style="font-size:1.25rem;margin-bottom:0.75rem;">{inst['h3']}</h3>
        <p style="font-size:0.85rem;line-height:1.7;opacity:0.85;font-family:var(--a19-serif);">{inst['p']}</p>
      </div>\n"""

    spec_color = specs['color']
    spec_elec = specs['electrical']
    spec_dim = specs['dimming']
    spec_mat = specs['materials']
    spec_comp = specs['compliance']

    def spec_rows(items):
        return '\n'.join(f'          <div class="a19-spec-row"><dt>{k}</dt><dd>{v}</dd></div>' for k, v in items)

    sisters_html = sister_cards(slug, NOSTALGIC_SISTERS)

    # Coming-soon CTA override
    if coming_soon:
        cta_section = f"""<!-- COMING SOON CTA -->
<section style="background:#1A140C;" data-content-pending="true">
  <div style="max-width:1280px;margin:0 auto;padding:5rem 1.5rem;text-align:center;color:#F5EFE3;">
    <h2 class="a19-h1" style="font-size:clamp(1.75rem,3.5vw,2.75rem);margin-bottom:1.5rem;">Coming soon — request samples.</h2>
    <p class="a19-serif-text" style="opacity:0.7;max-width:40rem;margin:0 auto 2rem;line-height:1.7;">Full product data is being finalized. Request a sample or contact sales for availability.</p>
    <div style="display:flex;justify-content:center;gap:12px;flex-wrap:wrap;">
      <a href="/support/sample-request?subject={slug.upper()}+Sample" class="a19-btn a19-btn-primary">REQUEST SAMPLE</a>
      <a href="/support/sample-request?subject={slug.upper()}+Info" class="a19-btn" style="background:transparent;color:#F5EFE3;border:1.5px solid rgba(245,239,227,0.3);">CONTACT SALES</a>
    </div>
  </div>
</section>"""
    else:
        cta_section = f"""<!-- DARK CTA -->
<section style="background:#1A140C;">
  <div style="max-width:1280px;margin:0 auto;padding:5rem 1.5rem;text-align:center;color:#F5EFE3;">
    <h2 class="a19-h1" style="font-size:clamp(1.75rem,3.5vw,2.75rem);margin-bottom:1.5rem;">Specify the {designer}. Deliver the room.</h2>
    <p class="a19-serif-text" style="opacity:0.7;max-width:40rem;margin:0 auto 2rem;line-height:1.7;">Interior designers answered same business day. Hospitality binning kits shipped 5-day. Custom CCT requests quoted within 48 hours.</p>
    <div style="display:flex;justify-content:center;gap:12px;flex-wrap:wrap;">
      <a href="/support/sample-request?subject={designer.replace(' ', '+')}+Spec" class="a19-btn a19-btn-primary">SPECIFY THIS LAMP</a>
      <a href="/support/sample-request?subject={designer.replace(' ', '+')}+Sample" class="a19-btn" style="background:transparent;color:#F5EFE3;border:1.5px solid rgba(245,239,227,0.3);">REQUEST SAMPLE</a>
      <a href="https://algportal.archipelagolighting.com" class="a19-btn" style="background:transparent;color:#F5EFE3;border:1.5px solid rgba(245,239,227,0.3);" target="_blank" rel="noopener">SHOP STOCK &amp; BUY</a>
    </div>
  </div>
</section>"""

    page = f"""---
/**
 * {title_full} \u2014 Nostalgic D\u00e9cor Family Detail Page
 * v2.7.12 \u2014 migrated to A19 pattern
 * Route: /collections/nostalgic-decor/{slug}
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
    desc: 'Photometric data \u00b7 per CCT and glass finish',
    url: null,
    family: '{title_full}',
    resource: 'IES Files',
  }},
  {{
    icon: 'PDF',
    title: 'ALG D\u00e9cor Lamps \u00b7 Product Guide \u00b7 Q2 2026',
    desc: 'Full D\u00e9cor lamp catalog \u00b7 Nostalgic + Vintage series',
    url: null,
    family: '{title_full}',
    resource: 'Product Guide',
  }},
];

const skus = {skus_js};

const dimmers = {DIMMERS_JS};
---
<BaseLayout
  title="{title_full} \u2014 Nostalgic D\u00e9cor | Archipelago Lighting Group"
  description="{meta_desc}"
  bodyClass="page-{slug}-family"
>
<style>{NOSTALGIC_CSS}</style>

<div class="a19-breadcrumb">
  <div class="a19-breadcrumb__inner">
    <a href="/">HOME</a> \u203a
    <a href="/products/">PRODUCTS</a> \u203a
    <a href="/products/lamps/">LAMPS</a> \u203a
    <a href="/collections/nostalgic-decor/">NOSTALGIC D\u00c9COR</a> \u203a
    THE {title_full.upper()}
  </div>
</div>

<main id="main">

<!-- HERO -->
<section class="a19-warm" aria-labelledby="{slug}-hero-h1">
  <div style="max-width:1536px;margin:0 auto;padding:4rem 1.5rem;display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:center;" class="{slug}-hero-grid">
    <div class="a19-photo-ph">
      <div class="a19-photo-ph-text">LIFESTYLE PHOTOGRAPHY<br><span style="opacity:0.6;">\u2014 ROOSTER CREATIVE DELIVERABLE \u2014</span><br><br><span style="opacity:0.5;">{photo_label}</span></div>
    </div>
    <div>
      <p class="a19-eyebrow a19-eyebrow-rule" style="opacity:0.6;margin-bottom:1.5rem;"><span class="a19-amber-text">SERIES \u00b7</span> NOSTALGIC D\u00c9COR \u00b7 {sub_register}</p>
      <h1 id="{slug}-hero-h1" class="a19-h1" style="font-size:clamp(2.5rem,5vw,4rem);margin-bottom:1rem;">{title_full}</h1>
      <p class="a19-serif-text" style="font-size:1.25rem;font-style:italic;margin-bottom:1.5rem;opacity:0.9;">{tagline}</p>
      <p class="a19-serif-text" style="font-size:1rem;line-height:1.75;margin-bottom:2rem;opacity:0.85;max-width:36rem;">{description}</p>
      <dl style="display:grid;grid-template-columns:1fr 1fr;gap:1.25rem 2rem;margin-bottom:2rem;">
        <div><dd class="a19-stat-num">{watts}</dd><dt class="a19-stat-label">Input wattage range</dt></div>
        <div><dd class="a19-stat-num">{lumens}</dd><dt class="a19-stat-label">Lumen output</dt></div>
        <div><dd class="a19-stat-num">{cri}</dd><dt class="a19-stat-label">Color rendering</dt></div>
        <div><dd class="a19-stat-num">25,000h</dd><dt class="a19-stat-label">L70 rated life</dt></div>
      </dl>
      <div style="display:flex;flex-wrap:wrap;gap:8px;margin-bottom:1.5rem;">
{trust_html}
      </div>
      <div style="display:flex;flex-wrap:wrap;gap:12px;">
        <a href="/support/sample-request?subject={designer.replace(' ', '+')}+Spec" class="a19-btn a19-btn-primary">SPECIFY THIS LAMP</a>
        <a href="/support/sample-request?subject={designer.replace(' ', '+')}+Sample" class="a19-btn a19-btn-outline">REQUEST SAMPLE</a>
        <a href="#resources" class="a19-btn a19-btn-ghost">DOCUMENTATION \u2193</a>
      </div>
    </div>
  </div>
</section>
<style>
  @media (max-width: 768px) {{ .{slug}-hero-grid {{ grid-template-columns: 1fr !important; }} }}
</style>

<!-- WHERE IT BELONGS -->
<section class="a19-warm2" aria-labelledby="{slug}-belongs-h2">
  <div style="max-width:1536px;margin:0 auto;padding:5rem 1.5rem;">
    <p class="a19-eyebrow a19-eyebrow-rule a19-amber-text" style="margin-bottom:1.5rem;">WHERE THE {designer.upper()} BELONGS</p>
    <h2 id="{slug}-belongs-h2" class="a19-h2" style="font-size:clamp(1.75rem,3.5vw,3rem);margin-bottom:3rem;">Three install registers. One lamp.</h2>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem;" class="{slug}-belongs-grid">
{install_html}    </div>
    <style>
      @media (max-width: 768px) {{ .{slug}-belongs-grid {{ grid-template-columns: 1fr !important; }} }}
    </style>
  </div>
</section>

<!-- STRUCTURED SPECS -->
<section class="a19-warm" aria-labelledby="{slug}-specs-h2">
  <div style="max-width:1536px;margin:0 auto;padding:5rem 1.5rem;">
    <p class="a19-eyebrow a19-eyebrow-rule a19-amber-text" style="margin-bottom:1.5rem;">FULL SPECIFICATIONS</p>
    <h2 id="{slug}-specs-h2" class="a19-h2" style="font-size:clamp(1.5rem,3vw,2.5rem);margin-bottom:3rem;">Spec sheet for the lamp \u00b7 designer-grade detail.</h2>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:3rem;" class="{slug}-spec-grid">
      <article id="spec-color">
        <p class="a19-spec-block-num" style="margin-bottom:0.5rem;">01</p>
        <h3 class="a19-serif-text" style="font-size:1.5rem;margin-bottom:1rem;">Color &amp; Optical</h3>
        <dl>
{spec_rows(spec_color.items())}
        </dl>
      </article>
      <article id="spec-electrical">
        <p class="a19-spec-block-num" style="margin-bottom:0.5rem;">02</p>
        <h3 class="a19-serif-text" style="font-size:1.5rem;margin-bottom:1rem;">Electrical</h3>
        <dl>
{spec_rows(spec_elec.items())}
        </dl>
      </article>
      <article id="spec-dimming">
        <p class="a19-spec-block-num" style="margin-bottom:0.5rem;">03</p>
        <h3 class="a19-serif-text" style="font-size:1.5rem;margin-bottom:1rem;">Dimming &amp; Controls</h3>
        <dl>
{spec_rows(spec_dim.items())}
        </dl>
      </article>
      <article id="spec-materials">
        <p class="a19-spec-block-num" style="margin-bottom:0.5rem;">04</p>
        <h3 class="a19-serif-text" style="font-size:1.5rem;margin-bottom:1rem;">Materials &amp; Finish</h3>
        <dl>
{spec_rows(spec_mat.items())}
        </dl>
      </article>
      <article id="spec-compliance" style="grid-column:1/-1;">
        <p class="a19-spec-block-num" style="margin-bottom:0.5rem;">05</p>
        <h3 class="a19-serif-text" style="font-size:1.5rem;margin-bottom:1rem;">Compliance &amp; Warranty</h3>
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
<section class="a19-warm2" aria-labelledby="{slug}-dim-h2">
  <div style="max-width:1536px;margin:0 auto;padding:5rem 1.5rem;">
    <p class="a19-eyebrow a19-eyebrow-rule a19-amber-text" style="margin-bottom:1.5rem;">DIMMER COMPATIBILITY</p>
    <h2 id="{slug}-dim-h2" class="a19-h2" style="font-size:clamp(1.5rem,3vw,2.5rem);margin-bottom:1rem;">The Nostalgic &amp; Vintage GEN-2 dimmer list.</h2>
    <p style="opacity:0.7;max-width:40rem;margin-bottom:2rem;font-size:0.9rem;font-family:var(--a19-serif);">Tested and confirmed on the following control systems. All pass at 5% minimum dim level with no flicker, buzz, or pop-on.</p>
    <div style="overflow-x:auto;">
      <table class="a19-sku-table" style="min-width:520px;">
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
    <p style="font-family:var(--a19-mono);font-size:0.65rem;letter-spacing:0.12em;opacity:0.6;margin-top:1rem;">\u25b8 MATRIX UPDATED 2026.Q2 \u00b7 NEW DIMMERS ADDED QUARTERLY \u00b7 SUBMIT YOUR CONTROL FOR TESTING</p>
  </div>
</section>

<!-- SKU TABLE -->
<section class="a19-warm" aria-labelledby="{slug}-sku-h2">
  <div style="max-width:1536px;margin:0 auto;padding:5rem 1.5rem;">
    <p class="a19-eyebrow a19-eyebrow-rule a19-amber-text" style="margin-bottom:1.5rem;">ORDERABLE VARIANTS</p>
    <h2 id="{slug}-sku-h2" class="a19-h2" style="font-size:clamp(1.5rem,3vw,2.5rem);margin-bottom:0.75rem;">Active {shape_code} variants.</h2>
    <p class="a19-serif-text" style="opacity:0.8;max-width:40rem;margin-bottom:2rem;font-size:0.9rem;">Standard-warranty 3-year / 25,000-hour rated life per datasheet. JA8-2022-E and T20-compliant variants available where required.</p>
    <div style="overflow-x:auto;">
      <table class="a19-sku-table spec-table" style="min-width:700px;">
        <thead>
          <tr>
            <th>SKU</th><th>FINISH</th><th style="text-align:center;">BASE</th><th style="text-align:center;">WATTS</th><th style="text-align:center;">EQ.</th><th style="text-align:center;">LUMENS</th><th style="text-align:center;">CCT</th><th style="text-align:center;">CRI</th><th>CERT</th>
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
    <p style="font-family:var(--a19-mono);font-size:0.65rem;letter-spacing:0.12em;opacity:0.6;margin-top:1rem;">\u25b8 {sku_note}</p>
  </div>
</section>

<!-- RESOURCES -->
<section class="a19-warm2" id="resources" aria-labelledby="{slug}-resources-h2">
  <div style="max-width:1536px;margin:0 auto;padding:4rem 1.5rem;">
    <p class="a19-eyebrow a19-eyebrow-rule a19-amber-text" style="margin-bottom:1.5rem;">RESOURCES</p>
    <h2 id="{slug}-resources-h2" class="a19-h2" style="font-size:clamp(1.25rem,2.5vw,2rem);margin-bottom:2rem;">For designers and spec writers.</h2>
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
<section class="a19-warm" aria-labelledby="{slug}-sister-h2">
  <div style="max-width:1536px;margin:0 auto;padding:4rem 1.5rem;">
    <p class="a19-eyebrow a19-eyebrow-rule a19-amber-text" style="margin-bottom:1.5rem;">SISTER LAMPS IN NOSTALGIC D\u00c9COR</p>
    <h2 id="{slug}-sister-h2" class="a19-h2" style="font-size:clamp(1.25rem,2.5vw,2rem);margin-bottom:2rem;">More named lamps. Same series register.</h2>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;" class="{slug}-sister-grid">
{sisters_html}
    </div>
    <style>
      @media (max-width: 768px) {{ .{slug}-sister-grid {{ grid-template-columns: 1fr 1fr !important; }} }}
    </style>
  </div>
</section>

{cta_section}

</main>
</BaseLayout>
"""
    return page


# ─── PRODUCT DATA ─────────────────────────────────────────────────────────────

PAGES = [
    {
        'slug': 'a15',
        'title_full': 'The Saarinen A15',
        'designer': 'Saarinen',
        'shape_code': 'LTA15',
        'sub_register': 'MID-CENTURY ACCENT',
        'tagline': 'The accent lamp that Saarinen would have specified.',
        'description': 'The small-format A15 shape — the lamp of vanity strips, accent fixtures, and appliance sockets — given a frosted amber finish and 2700K warmth that reads as warm-white without the yellow cast of older incandescent replacements. For bathroom vanity strips, accent lighting, and any fixture where the lamp is visible but not the centerpiece.',
        'meta_desc': 'The Saarinen A15: CRI 80+, 2400K\u20132700K, frosted/clear glass, dimmable to 5%. Small-format A15 for vanity strips, accent fixtures, and appliance sockets.',
        'watts': '3.5\u20134.5W',
        'lumens': '280\u2013350 lm',
        'cri': 'CRI 80+',
        'trust_badges': ['CRI 80+', 'UL LISTED', 'CEC TITLE 24 JA8', 'DIMMABLE TO 5%'],
        'photo_label': 'SAARINEN A15 IN VANITY STRIP SETTING\nSOFT MORNING REGISTER \u00b7 BATHROOM CONTEXT',
        'installs': [
            {'register': 'RESIDENTIAL \u00b7 BATHROOM VANITY', 'h3': 'The lamp that frames the mirror.', 'p': 'Bathroom vanity strips, Hollywood-style mirror bars, and powder-room sconces. The A15 silhouette disappears into a vanity strip and lets the warm amber glow do the work.'},
            {'register': 'HOSPITALITY \u00b7 GUEST BATH', 'h3': 'Consistent across 200 vanity strips.', 'p': 'Hotel bathroom vanity strips where 6\u20138 lamps per fixture must match in CCT and output. 3-step MacAdam binning across the entire order so no two adjacent lamps read differently.'},
            {'register': 'RESTAURANT \u00b7 ACCENT', 'h3': 'Small lamp, big atmosphere.', 'p': 'Accent fixtures, display lighting, and small decorative pendants where a compact lamp profile is required but warm-amber atmosphere is non-negotiable.'},
        ],
        'specs': {
            'color': {'CCT options': '2400K \u00b7 2700K', 'CRI': '\u226580', 'MacAdam binning': '3-step (standard) \u00b7 matched binning kits available', 'Glass options': 'Frosted \u00b7 Clear', 'Beam distribution': 'Omnidirectional \u00b7 360\u00b0'},
            'electrical': {'Input voltage': '120V AC \u00b7 60Hz', 'Wattage range': '3.5W \u2013 4.5W (per SKU)', 'Lumen output': '280 \u2013 350 lm (per SKU)', 'Efficacy': '~75\u201380 lm/W (typ.)', 'L70 life': '25,000 hours'},
            'dimming': {'Dimming types': 'TRIAC \u00b7 ELV \u00b7 CL (leading/trailing edge)', 'Dim-to': '5% (smooth, flicker-free)', 'Compatible systems': 'Lutron \u00b7 Leviton \u00b7 Legrand \u00b7 Forbes &amp; Lomax \u00b7 Cooper', 'Dim-to-warm': 'Not applicable (fixed CCT per SKU)'},
            'materials': {'Base': 'E26 medium screw base', 'Envelope': 'A15 (47mm diameter)', 'Glass': 'Frosted \u00b7 Clear (per SKU)', 'Filament style': 'Spiral (per SKU)', 'MOL': '3.8" (97mm)'},
            'compliance': {'Safety': 'UL Listed', 'Energy code': 'CEC Title 24 JA8-2022-E \u00b7 T20 (on JA8 variants)', 'Warranty': '3 years / 25,000 hours', 'RoHS': 'Compliant'},
        },
        'skus': [
            {'sku': 'LTA15F35024MB', 'finish': 'Frosted', 'base': 'E26', 'watts': '3.5W', 'eq': '40W', 'lumens': '280', 'cct': '2400K', 'cri': '80+', 'cert': '\u2014'},
            {'sku': 'LTA15F45027MB', 'finish': 'Frosted', 'base': 'E26', 'watts': '4.5W', 'eq': '40W', 'lumens': '350', 'cct': '2700K', 'cri': '80+', 'cert': '\u2014'},
            {'sku': 'LTA15F45027MB/JA8', 'finish': 'Frosted', 'base': 'E26', 'watts': '4.5W', 'eq': '40W', 'lumens': '350', 'cct': '2700K', 'cri': '80+', 'cert': 'JA8 \u00b7 T20'},
            {'sku': 'LTA15C35024MB', 'finish': 'Clear', 'base': 'E26', 'watts': '3.5W', 'eq': '40W', 'lumens': '280', 'cct': '2400K', 'cri': '80+', 'cert': '\u2014'},
            {'sku': 'LTA15C45027MB', 'finish': 'Clear', 'base': 'E26', 'watts': '4.5W', 'eq': '40W', 'lumens': '350', 'cct': '2700K', 'cri': '80+', 'cert': '\u2014'},
            {'sku': 'LTA15C45027MB/JA8', 'finish': 'Clear', 'base': 'E26', 'watts': '4.5W', 'eq': '40W', 'lumens': '350', 'cct': '2700K', 'cri': '80+', 'cert': 'JA8 \u00b7 T20'},
        ],
    },
    {
        'slug': 'b10',
        'title_full': 'The Knoll B10',
        'designer': 'Knoll',
        'shape_code': 'LTB10',
        'sub_register': 'MID-CENTURY CANDELABRA',
        'tagline': 'The candelabra lamp that belongs in a Knoll showroom.',
        'description': 'The blunt-tip candelabra shape — the lamp of chandeliers, wall sconces, and decorative pendants — given the refined materiality that Knoll brought to mid-century furniture: clean lines, warm amber finish, and a 2700K glow that reads as sophisticated without trying. For chandeliers, sconces, and decorative fixtures where the lamp is part of the design language.',
        'meta_desc': 'The Knoll B10: CRI 80+, 2700K, blunt-tip candelabra, dimmable to 5%. The mid-century candelabra lamp for chandeliers and decorative sconces.',
        'watts': '3.5\u20134.5W',
        'lumens': '280\u2013350 lm',
        'cri': 'CRI 80+',
        'trust_badges': ['CRI 80+', 'UL LISTED', 'CEC TITLE 24 JA8', 'DIMMABLE TO 5%'],
        'photo_label': 'KNOLL B10 IN CHANDELIER SETTING\nWARM EVENING REGISTER \u00b7 DINING ROOM CONTEXT',
        'installs': [
            {'register': 'RESIDENTIAL \u00b7 CHANDELIER', 'h3': 'Eight lamps. One consistent glow.', 'p': 'Dining room chandeliers, foyer pendants, and living-room sconce clusters where all lamps must match in CCT and output. 3-step MacAdam binning across the full order.'},
            {'register': 'HOSPITALITY \u00b7 LOBBY', 'h3': 'Hundreds of lamps. One bin.', 'p': 'Hotel lobby chandeliers and corridor sconces where 50\u2013500 lamps must be consistent across an entire property. Binning kit ships 50 lamps from the same production run.'},
            {'register': 'RESTAURANT \u00b7 AMBIENT', 'h3': 'The lamp that sets the mood.', 'p': 'Restaurant ambient chandeliers and bar sconces. ELV/TRIAC dim-to-5% performance verified on Lutron, Leviton, Cooper, and Legrand control systems for restaurant-grade smoothness.'},
        ],
        'specs': {
            'color': {'CCT options': '2700K', 'CRI': '\u226580', 'MacAdam binning': '3-step (standard) \u00b7 matched binning kits available', 'Glass options': 'Frosted \u00b7 Clear', 'Beam distribution': 'Omnidirectional \u00b7 360\u00b0'},
            'electrical': {'Input voltage': '120V AC \u00b7 60Hz', 'Wattage range': '3.5W \u2013 4.5W (per SKU)', 'Lumen output': '280 \u2013 350 lm (per SKU)', 'Efficacy': '~75\u201380 lm/W (typ.)', 'L70 life': '25,000 hours'},
            'dimming': {'Dimming types': 'TRIAC \u00b7 ELV \u00b7 CL (leading/trailing edge)', 'Dim-to': '5% (smooth, flicker-free)', 'Compatible systems': 'Lutron \u00b7 Leviton \u00b7 Legrand \u00b7 Forbes &amp; Lomax \u00b7 Cooper', 'Dim-to-warm': 'Not applicable (fixed CCT per SKU)'},
            'materials': {'Base': 'E12 candelabra screw base', 'Envelope': 'B10 blunt-tip (32mm diameter)', 'Glass': 'Frosted \u00b7 Clear (per SKU)', 'Filament style': 'Spiral (per SKU)', 'MOL': '3.6" (91mm)'},
            'compliance': {'Safety': 'UL Listed', 'Energy code': 'CEC Title 24 JA8-2022-E \u00b7 T20 (on JA8 variants)', 'Warranty': '3 years / 25,000 hours', 'RoHS': 'Compliant'},
        },
        'skus': [
            {'sku': 'LTB10F35027MB', 'finish': 'Frosted', 'base': 'E12', 'watts': '3.5W', 'eq': '40W', 'lumens': '280', 'cct': '2700K', 'cri': '80+', 'cert': '\u2014'},
            {'sku': 'LTB10F45027MB', 'finish': 'Frosted', 'base': 'E12', 'watts': '4.5W', 'eq': '40W', 'lumens': '350', 'cct': '2700K', 'cri': '80+', 'cert': '\u2014'},
            {'sku': 'LTB10F45027MB/JA8', 'finish': 'Frosted', 'base': 'E12', 'watts': '4.5W', 'eq': '40W', 'lumens': '350', 'cct': '2700K', 'cri': '80+', 'cert': 'JA8 \u00b7 T20'},
            {'sku': 'LTB10C35027MB', 'finish': 'Clear', 'base': 'E12', 'watts': '3.5W', 'eq': '40W', 'lumens': '280', 'cct': '2700K', 'cri': '80+', 'cert': '\u2014'},
            {'sku': 'LTB10C45027MB', 'finish': 'Clear', 'base': 'E12', 'watts': '4.5W', 'eq': '40W', 'lumens': '350', 'cct': '2700K', 'cri': '80+', 'cert': '\u2014'},
            {'sku': 'LTB10C45027MB/JA8', 'finish': 'Clear', 'base': 'E12', 'watts': '4.5W', 'eq': '40W', 'lumens': '350', 'cct': '2700K', 'cri': '80+', 'cert': 'JA8 \u00b7 T20'},
        ],
    },
    {
        'slug': 'ca10',
        'title_full': 'The Bauer CA10',
        'designer': 'Bauer',
        'shape_code': 'LTCA10',
        'sub_register': 'MID-CENTURY FLAME-TIP',
        'tagline': 'The flame-tip candelabra for entryway and formal sconces.',
        'description': 'The flame-tip CA10 shape — the lamp of entryway chandeliers, formal sconces, and decorative pendants — given a warm 2700K amber glow and the refined materiality of California mid-century design. The Bauer CA10 takes its name from the California pottery tradition: warm, handcrafted, and built to last. For formal entryways, dining rooms, and any fixture where the flame-tip silhouette is part of the composition.',
        'meta_desc': 'The Bauer CA10: CRI 80+, 2700K, flame-tip candelabra, dimmable to 5%. The mid-century flame-tip for entryway chandeliers and formal sconces.',
        'watts': '3.5\u20134.5W',
        'lumens': '280\u2013350 lm',
        'cri': 'CRI 80+',
        'trust_badges': ['CRI 80+', 'UL LISTED', 'CEC TITLE 24 JA8', 'DIMMABLE TO 5%'],
        'photo_label': 'BAUER CA10 IN ENTRYWAY SCONCE SETTING\nFORMAL EVENING REGISTER \u00b7 FOYER CONTEXT',
        'installs': [
            {'register': 'RESIDENTIAL \u00b7 ENTRYWAY', 'h3': 'The lamp that greets the room.', 'p': 'Entryway chandeliers, foyer sconces, and formal pendant fixtures. The flame-tip silhouette adds visual interest while the 2700K glow creates a warm welcome.'},
            {'register': 'HOSPITALITY \u00b7 FORMAL DINING', 'h3': 'Formal dining, consistent light.', 'p': 'Hotel formal dining rooms and ballroom chandeliers where the lamp silhouette is part of the design specification. Binning kits available for large-quantity orders.'},
            {'register': 'RESTAURANT \u00b7 FINE DINING', 'h3': 'The finishing touch on a fine-dining table.', 'p': 'Fine-dining ambient chandeliers and wall sconces. The flame-tip shape signals formality; the 2700K CCT delivers the warm glow that fine-dining environments require.'},
        ],
        'specs': {
            'color': {'CCT options': '2700K', 'CRI': '\u226580', 'MacAdam binning': '3-step (standard) \u00b7 matched binning kits available', 'Glass options': 'Frosted \u00b7 Clear', 'Beam distribution': 'Omnidirectional \u00b7 360\u00b0'},
            'electrical': {'Input voltage': '120V AC \u00b7 60Hz', 'Wattage range': '3.5W \u2013 4.5W (per SKU)', 'Lumen output': '280 \u2013 350 lm (per SKU)', 'Efficacy': '~75\u201380 lm/W (typ.)', 'L70 life': '25,000 hours'},
            'dimming': {'Dimming types': 'TRIAC \u00b7 ELV \u00b7 CL (leading/trailing edge)', 'Dim-to': '5% (smooth, flicker-free)', 'Compatible systems': 'Lutron \u00b7 Leviton \u00b7 Legrand \u00b7 Forbes &amp; Lomax \u00b7 Cooper', 'Dim-to-warm': 'Not applicable (fixed CCT per SKU)'},
            'materials': {'Base': 'E12 candelabra screw base', 'Envelope': 'CA10 flame-tip (32mm diameter)', 'Glass': 'Frosted \u00b7 Clear (per SKU)', 'Filament style': 'Spiral (per SKU)', 'MOL': '4.0" (102mm)'},
            'compliance': {'Safety': 'UL Listed', 'Energy code': 'CEC Title 24 JA8-2022-E \u00b7 T20 (on JA8 variants)', 'Warranty': '3 years / 25,000 hours', 'RoHS': 'Compliant'},
        },
        'skus': [
            {'sku': 'LTCA10F35027MB', 'finish': 'Frosted', 'base': 'E12', 'watts': '3.5W', 'eq': '40W', 'lumens': '280', 'cct': '2700K', 'cri': '80+', 'cert': '\u2014'},
            {'sku': 'LTCA10F45027MB', 'finish': 'Frosted', 'base': 'E12', 'watts': '4.5W', 'eq': '40W', 'lumens': '350', 'cct': '2700K', 'cri': '80+', 'cert': '\u2014'},
            {'sku': 'LTCA10F45027MB/JA8', 'finish': 'Frosted', 'base': 'E12', 'watts': '4.5W', 'eq': '40W', 'lumens': '350', 'cct': '2700K', 'cri': '80+', 'cert': 'JA8 \u00b7 T20'},
            {'sku': 'LTCA10C35027MB', 'finish': 'Clear', 'base': 'E12', 'watts': '3.5W', 'eq': '40W', 'lumens': '280', 'cct': '2700K', 'cri': '80+', 'cert': '\u2014'},
            {'sku': 'LTCA10C45027MB', 'finish': 'Clear', 'base': 'E12', 'watts': '4.5W', 'eq': '40W', 'lumens': '350', 'cct': '2700K', 'cri': '80+', 'cert': '\u2014'},
            {'sku': 'LTCA10C45027MB/JA8', 'finish': 'Clear', 'base': 'E12', 'watts': '4.5W', 'eq': '40W', 'lumens': '350', 'cct': '2700K', 'cri': '80+', 'cert': 'JA8 \u00b7 T20'},
        ],
    },
    {
        'slug': 'g16',
        'title_full': 'The Heath G16',
        'designer': 'Heath',
        'shape_code': 'LTG16',
        'sub_register': 'MID-CENTURY GLOBE',
        'tagline': 'The small globe for vanity strips and decorative pendants.',
        'description': 'The G16 small globe shape \u2014 the lamp of bathroom vanity strips, Hollywood mirrors, and small decorative pendants \u2014 given a warm amber glow and the clean materiality of California mid-century ceramics. Full product data is being finalized. Request a sample or contact sales for availability.',
        'meta_desc': 'The Heath G16: small globe lamp for vanity strips and decorative pendants. Nostalgic D\u00e9cor series. Contact sales for availability.',
        'watts': '3.5\u20134.5W',
        'lumens': '280\u2013350 lm',
        'cri': 'CRI 80+',
        'trust_badges': ['CRI 80+', 'UL LISTED', 'DIMMABLE TO 5%'],
        'photo_label': 'HEATH G16 IN VANITY STRIP SETTING\n\u2014 ROOSTER CREATIVE DELIVERABLE \u2014',
        'coming_soon': True,
        'installs': [
            {'register': 'RESIDENTIAL \u00b7 VANITY STRIP', 'h3': 'The globe that frames the mirror.', 'p': 'Bathroom vanity strips and Hollywood-style mirror bars. The G16 globe shape adds decorative interest while the warm amber glow flatters skin tones.'},
            {'register': 'HOSPITALITY \u00b7 GUEST BATH', 'h3': 'Consistent across the property.', 'p': 'Hotel bathroom vanity strips and powder-room fixtures. 3-step MacAdam binning ensures all lamps match across a full property renovation.'},
            {'register': 'RESTAURANT \u00b7 DECORATIVE', 'h3': 'Small globe, strong statement.', 'p': 'Decorative pendant clusters and accent fixtures in restaurant environments where the globe shape is part of the visual composition.'},
        ],
        'specs': {
            'color': {'CCT options': '2700K (additional CCTs on request)', 'CRI': '\u226580', 'MacAdam binning': '3-step (standard)', 'Glass options': 'Frosted \u00b7 Clear', 'Beam distribution': 'Omnidirectional \u00b7 360\u00b0'},
            'electrical': {'Input voltage': '120V AC \u00b7 60Hz', 'Wattage range': '3.5W \u2013 4.5W (per SKU)', 'Lumen output': '280 \u2013 350 lm (per SKU)', 'Efficacy': '~75\u201380 lm/W (typ.)', 'L70 life': '25,000 hours'},
            'dimming': {'Dimming types': 'TRIAC \u00b7 ELV \u00b7 CL (leading/trailing edge)', 'Dim-to': '5% (smooth, flicker-free)', 'Compatible systems': 'Lutron \u00b7 Leviton \u00b7 Legrand \u00b7 Cooper', 'Dim-to-warm': 'Not applicable (fixed CCT per SKU)'},
            'materials': {'Base': 'E12 candelabra screw base', 'Envelope': 'G16 globe (51mm diameter)', 'Glass': 'Frosted \u00b7 Clear (per SKU)', 'Filament style': 'Spiral (per SKU)', 'MOL': '3.5" (89mm)'},
            'compliance': {'Safety': 'UL Listed', 'Energy code': 'CEC Title 24 JA8 (on applicable variants)', 'Warranty': '3 years / 25,000 hours', 'RoHS': 'Compliant'},
        },
        'skus': [
            {'sku': 'LTG16F45027MB', 'finish': 'Frosted', 'base': 'E12', 'watts': '4.5W', 'eq': '40W', 'lumens': '350', 'cct': '2700K', 'cri': '80+', 'cert': '\u2014'},
            {'sku': 'LTG16C45027MB', 'finish': 'Clear', 'base': 'E12', 'watts': '4.5W', 'eq': '40W', 'lumens': '350', 'cct': '2700K', 'cri': '80+', 'cert': '\u2014'},
        ],
        'sku_note': 'FULL VARIANT LIST IN PROGRESS \u00b7 CONTACT SALES@ARCHIPELAGOLIGHTING.COM FOR AVAILABILITY',
    },
    {
        'slug': 'g25',
        'title_full': 'The Eichler G25',
        'designer': 'Eichler',
        'shape_code': 'LTG25',
        'sub_register': 'MID-CENTURY GLOBE',
        'tagline': 'The globe lamp that Eichler would have hung in the atrium.',
        'description': 'The G25 medium globe shape \u2014 the lamp of pendant fixtures, exposed-bulb chandeliers, and decorative table lamps \u2014 given the warm amber glow and clean lines of California mid-century design. The Eichler G25 takes its name from the California developer who brought mid-century modernism to the American suburb: open plans, natural light, and lamps that were meant to be seen. For pendant fixtures, exposed-bulb chandeliers, and any application where the globe shape is part of the composition.',
        'meta_desc': 'The Eichler G25: CRI 80+, 2700K, medium globe, dimmable to 5%. Mid-century G25 for pendant fixtures, exposed-bulb chandeliers, and decorative table lamps.',
        'watts': '4.5\u20136.5W',
        'lumens': '350\u2013500 lm',
        'cri': 'CRI 80+',
        'trust_badges': ['CRI 80+', 'UL LISTED', 'CEC TITLE 24 JA8', 'DIMMABLE TO 5%'],
        'photo_label': 'EICHLER G25 IN PENDANT FIXTURE SETTING\nWARM EVENING REGISTER \u00b7 ATRIUM CONTEXT',
        'installs': [
            {'register': 'RESIDENTIAL \u00b7 PENDANT', 'h3': 'The globe that defines the room.', 'p': 'Exposed-bulb pendant fixtures, decorative table lamps, and open-plan living spaces where the lamp silhouette is a design element. The G25 globe reads as modern without trying.'},
            {'register': 'HOSPITALITY \u00b7 LOBBY BAR', 'h3': 'Statement lighting at scale.', 'p': 'Hotel lobby bars, restaurant pendant clusters, and hospitality spaces where exposed-bulb fixtures are part of the design language. Binning kits available for large-quantity orders.'},
            {'register': 'RESTAURANT \u00b7 AMBIENT', 'h3': 'Warm globe clusters above the bar.', 'p': 'Restaurant ambient pendant clusters and bar overhead fixtures. The G25 globe shape creates visual warmth at scale; the 2700K CCT delivers the amber glow that hospitality environments require.'},
        ],
        'specs': {
            'color': {'CCT options': '2700K', 'CRI': '\u226580', 'MacAdam binning': '3-step (standard) \u00b7 matched binning kits available', 'Glass options': 'Frosted \u00b7 Clear', 'Beam distribution': 'Omnidirectional \u00b7 360\u00b0'},
            'electrical': {'Input voltage': '120V AC \u00b7 60Hz', 'Wattage range': '4.5W \u2013 6.5W (per SKU)', 'Lumen output': '350 \u2013 500 lm (per SKU)', 'Efficacy': '~70\u201380 lm/W (typ.)', 'L70 life': '25,000 hours'},
            'dimming': {'Dimming types': 'TRIAC \u00b7 ELV \u00b7 CL (leading/trailing edge)', 'Dim-to': '5% (smooth, flicker-free)', 'Compatible systems': 'Lutron \u00b7 Leviton \u00b7 Legrand \u00b7 Forbes &amp; Lomax \u00b7 Cooper', 'Dim-to-warm': 'Not applicable (fixed CCT per SKU)'},
            'materials': {'Base': 'E26 medium screw base', 'Envelope': 'G25 globe (80mm diameter)', 'Glass': 'Frosted \u00b7 Clear (per SKU)', 'Filament style': 'Spiral (per SKU)', 'MOL': '4.8" (122mm)'},
            'compliance': {'Safety': 'UL Listed', 'Energy code': 'CEC Title 24 JA8-2022-E \u00b7 T20 (on JA8 variants)', 'Warranty': '3 years / 25,000 hours', 'RoHS': 'Compliant'},
        },
        'skus': [
            {'sku': 'LTG25F45027MB', 'finish': 'Frosted', 'base': 'E26', 'watts': '4.5W', 'eq': '40W', 'lumens': '350', 'cct': '2700K', 'cri': '80+', 'cert': '\u2014'},
            {'sku': 'LTG25F65027MB', 'finish': 'Frosted', 'base': 'E26', 'watts': '6.5W', 'eq': '60W', 'lumens': '500', 'cct': '2700K', 'cri': '80+', 'cert': '\u2014'},
            {'sku': 'LTG25F65027MB/JA8', 'finish': 'Frosted', 'base': 'E26', 'watts': '6.5W', 'eq': '60W', 'lumens': '500', 'cct': '2700K', 'cri': '80+', 'cert': 'JA8 \u00b7 T20'},
            {'sku': 'LTG25C45027MB', 'finish': 'Clear', 'base': 'E26', 'watts': '4.5W', 'eq': '40W', 'lumens': '350', 'cct': '2700K', 'cri': '80+', 'cert': '\u2014'},
            {'sku': 'LTG25C65027MB', 'finish': 'Clear', 'base': 'E26', 'watts': '6.5W', 'eq': '60W', 'lumens': '500', 'cct': '2700K', 'cri': '80+', 'cert': '\u2014'},
            {'sku': 'LTG25C65027MB/JA8', 'finish': 'Clear', 'base': 'E26', 'watts': '6.5W', 'eq': '60W', 'lumens': '500', 'cct': '2700K', 'cri': '80+', 'cert': 'JA8 \u00b7 T20'},
        ],
    },
    {
        'slug': 's14',
        'title_full': 'The Marshall S14',
        'designer': 'Marshall',
        'shape_code': 'LTS14',
        'sub_register': 'COMMERCIAL STRING LIGHT',
        'tagline': "The string lamp that Marshall Field's would have hung.",
        'description': "The S14 string lamp shape \u2014 the lamp of commercial string light installations, outdoor bistro strings, and hospitality patio lighting \u2014 given a warm 2400K to 2700K amber glow that works in any environment where warmth and longevity matter equally. The Marshall S14 draws on the commercial nostalgia of mid-century department store lighting. For commercial string light installations, outdoor patio strings, and hospitality spaces where the lamp is the decoration.",
        'meta_desc': 'The Marshall S14: CRI 80+, 2400K\u20132700K, S14 string lamp, dimmable. Commercial-grade string light for outdoor bistro strings and hospitality patio lighting.',
        'watts': '1.5\u20132W',
        'lumens': '100\u2013160 lm',
        'cri': 'CRI 80+',
        'trust_badges': ['CRI 80+', 'UL LISTED', 'WET LOCATION RATED', 'DIMMABLE'],
        'photo_label': 'MARSHALL S14 IN OUTDOOR STRING LIGHT SETTING\nWARM EVENING REGISTER \u00b7 PATIO CONTEXT',
        'installs': [
            {'register': 'COMMERCIAL \u00b7 OUTDOOR STRING', 'h3': 'Hundreds of lamps. One consistent amber.', 'p': 'Commercial bistro string light installations, outdoor patio strings, and event lighting. The S14 shape is the standard for commercial string light applications; the 2400K CCT delivers the warmest amber glow in the Nostalgic series.'},
            {'register': 'HOSPITALITY \u00b7 PATIO', 'h3': 'The lamp that extends the season.', 'p': 'Hotel and restaurant patio lighting, rooftop bar string lights, and outdoor hospitality spaces. Wet-location rated for year-round outdoor use.'},
            {'register': 'RESTAURANT \u00b7 AMBIENT', 'h3': 'String lights above the tables.', 'p': 'Restaurant ambient string light canopies and outdoor dining area lighting. The S14 string lamp is the standard for restaurant outdoor ambient lighting.'},
        ],
        'specs': {
            'color': {'CCT options': '2400K \u00b7 2700K', 'CRI': '\u226580', 'MacAdam binning': '3-step (standard)', 'Glass options': 'Clear \u00b7 Frosted', 'Beam distribution': 'Omnidirectional \u00b7 360\u00b0'},
            'electrical': {'Input voltage': '120V AC \u00b7 60Hz', 'Wattage range': '1.5W \u2013 2W (per SKU)', 'Lumen output': '100 \u2013 160 lm (per SKU)', 'Efficacy': '~70\u201380 lm/W (typ.)', 'L70 life': '25,000 hours'},
            'dimming': {'Dimming types': 'TRIAC \u00b7 CL (leading/trailing edge)', 'Dim-to': '10% (smooth)', 'Compatible systems': 'Lutron \u00b7 Leviton \u00b7 Legrand', 'Wet location': 'UL Wet Location Rated'},
            'materials': {'Base': 'E17 intermediate screw base', 'Envelope': 'S14 (44mm diameter)', 'Glass': 'Clear \u00b7 Frosted (per SKU)', 'Filament style': 'Spiral (per SKU)', 'MOL': '3.9" (99mm)'},
            'compliance': {'Safety': 'UL Listed \u00b7 Wet Location Rated', 'Energy code': 'CEC compliant', 'Warranty': '3 years / 25,000 hours', 'RoHS': 'Compliant'},
        },
        'skus': [
            {'sku': 'LTS14C15024MB', 'finish': 'Clear', 'base': 'E17', 'watts': '1.5W', 'eq': '15W', 'lumens': '100', 'cct': '2400K', 'cri': '80+', 'cert': '\u2014'},
            {'sku': 'LTS14C20027MB', 'finish': 'Clear', 'base': 'E17', 'watts': '2.0W', 'eq': '25W', 'lumens': '160', 'cct': '2700K', 'cri': '80+', 'cert': '\u2014'},
            {'sku': 'LTS14F15024MB', 'finish': 'Frosted', 'base': 'E17', 'watts': '1.5W', 'eq': '15W', 'lumens': '100', 'cct': '2400K', 'cri': '80+', 'cert': '\u2014'},
            {'sku': 'LTS14F20027MB', 'finish': 'Frosted', 'base': 'E17', 'watts': '2.0W', 'eq': '25W', 'lumens': '160', 'cct': '2700K', 'cri': '80+', 'cert': '\u2014'},
        ],
    },
]


if __name__ == '__main__':
    out_dir = os.path.join(BASE, 'src', 'pages', 'collections', 'nostalgic-decor')
    for cfg in PAGES:
        slug = cfg['slug']
        path = os.path.join(out_dir, f'{slug}.astro')
        content = build_nostalgic_page(cfg)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        size = len(content.encode('utf-8'))
        print(f'  wrote {slug}.astro ({size:,} bytes)')
    print('Done.')
