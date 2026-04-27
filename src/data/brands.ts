/**
 * brands.ts — Canonical brand display strings for the ALG website.
 *
 * Rules:
 * - Mixed-case form is used EVERYWHERE in rendered body text (H1, breadcrumb, paragraphs, links).
 * - HTML `<title>` tags use ASCII form (no Ⓐ).
 * - The Ⓐ character MUST be wrapped in <span class="aa"> when rendered as HTML.
 * - Use the `html` field when rendering via set:html or innerHTML.
 * - Use the `ascii` field for <title>, meta, and plain-text contexts.
 * - Use the `text` field for plain-text display (no HTML tags).
 *
 * Stems (13): RCH, LS, NT, CS, BLE, RMOR, DAPT, MILY, IM, PTICS, LGIC, GE, TURE
 */

export interface BrandEntry {
  /** Plain text with Ⓐ character — for display in non-HTML contexts */
  text: string;
  /** HTML with <span class="aa">Ⓐ</span> — for set:html / innerHTML */
  html: string;
  /** ASCII fallback — for <title>, meta, and plain-text export */
  ascii: string;
}

export const BRANDS: Record<string, BrandEntry> = {
  luxoarch: {
    text:  'luxoⒶRCH',
    html:  'luxo<span class="aa">Ⓐ</span>RCH',
    ascii: 'luxoARCH',
  },
  planoarch: {
    text:  'planoⒶRCH',
    html:  'plano<span class="aa">Ⓐ</span>RCH',
    ascii: 'planoARCH',
  },
  lampararch: {
    text:  'lamparⒶRCH',
    html:  'lampar<span class="aa">Ⓐ</span>RCH',
    ascii: 'lamparARCH',
  },
  cityarch: {
    text:  'cityⒶRCH',
    html:  'city<span class="aa">Ⓐ</span>RCH',
    ascii: 'cityARCH',
  },
  tubularch: {
    text:  'tubulⒶRCH',
    html:  'tubul<span class="aa">Ⓐ</span>RCH',
    ascii: 'tubulARCH',
  },
  multifamily: {
    text:  'multi-fⒶMILY',
    html:  'multi-f<span class="aa">Ⓐ</span>MILY',
    ascii: 'multi-fAMILY',
  },
  constant: {
    text:  'constⒶNT',
    html:  'const<span class="aa">Ⓐ</span>NT',
    ascii: 'constANT',
  },
  controls: {
    text:  'contrⒶLS',
    html:  'contr<span class="aa">Ⓐ</span>LS',
    ascii: 'contrALS',
  },
  signature: {
    text:  'signⒶTURE',
    html:  'sign<span class="aa">Ⓐ</span>TURE',
    ascii: 'signATURE',
  },
  utilitysignature: {
    text:  'Utility signⒶTURE',
    html:  'Utility sign<span class="aa">Ⓐ</span>TURE',
    ascii: 'Utility signATURE',
  },
  nostalgic: {
    text:  'Nostalgic Décor',
    html:  'Nostalgic D&eacute;cor',
    ascii: 'Nostalgic Decor',
  },
  vintage: {
    text:  'Vintage Décor',
    html:  'Vintage D&eacute;cor',
    ascii: 'Vintage Decor',
  },
};
