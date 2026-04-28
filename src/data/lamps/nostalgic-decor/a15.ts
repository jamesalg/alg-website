/**
 * The Saarinen A15 — Nostalgic Décor family detail data
 * Collection: nostalgic-decor
 * v2.7.x — Named product, narrative copy, SKU data from Item.xlsx
 */
const a15Data = {
  slug: 'a15',
  name: 'The Saarinen A15',
  collectionSlug: 'nostalgic-decor',
  collectionName: 'Nostalgic Décor',
  collectionTitleAscii: 'NOST<span class="aa">Ⓐ</span>LGIC',
  collectionHeadlineLine: 'Décor | nost<span class="aa">Ⓐ</span>LGIC',
  collectionAesthetic: 'nostalgic' as const,
  tagline: 'The accent lamp that Saarinen would have specified.',
  description: 'The accent lamp that Saarinen would have specified. The Saarinen A15 takes the small-format A15 shape — the lamp of vanity strips, accent fixtures, and appliance sockets — and gives it a frosted amber finish and 2700K warmth that reads as warm-white without the yellow cast of older incandescent replacements. For bathroom vanity strips, accent lighting, and any fixture where the lamp is visible but not the centerpiece.',
  heroImage: '',
  echelon: undefined,
  keySpecs: {
    inputWatts: '3.5–4.5W',
    lumens: '280–350lm',
    lmPerW: '75–80',
    cri: '80–90',
  },
  certifications: ['UL Listed', 'Dimmable', '120V', 'RoHS Compliant'],
  datasheetUrl: undefined,
  installGuideUrl: undefined,
  comingSoon: false,
  isTubularArch: false,
};
export default a15Data;
export const siblingFamilies = [
  { slug: 'a19', name: 'The Eames A19', skuCount: 24, tagline: 'Standard A19 for residential and hospitality.' },
  { slug: 'b10', name: 'The Knoll B10', skuCount: 42, tagline: 'Blunt-tip candelabra for chandeliers and sconces.' },
  { slug: 'ca10', name: 'The Bauer CA10', skuCount: 36, tagline: 'Flame-tip candelabra for decorative fixtures.' },
  { slug: 'g16-5', name: 'The Heath G16.5', skuCount: 33, tagline: 'G16.5 globe for bathroom vanity strips.' },
  { slug: 'g25', name: 'The Eichler G25', skuCount: 21, tagline: 'G25 globe for vanity and decorative pendants.' },
  { slug: 's14', name: 'The Marshall S14', skuCount: 19, tagline: 'S14 string lamp for commercial installations.' },
];
export const relatedCollections = [
  { slug: 'vintage-decor', vertical: 'Lamps', name: 'Vintage Décor', description: 'Old-world filament lamps with modern efficiency.', status: 'live' as const },
  { slug: 'signature', vertical: 'Lamps', name: 'sign<span class="aa">Ⓐ</span>TURE', description: 'Commercial-grade LED lamps for the hardest retrofit jobs.', status: 'live' as const },
  { slug: 'planoarch', vertical: 'Indoor', name: 'plano<span class="aa">Ⓐ</span>RCH', description: 'Commercial indoor lighting for offices, retail, and healthcare.', status: 'live' as const },
];
export const getStarted = {
  layoutCopy: 'Submit a fixture schedule and we return a lamp recommendation for each row.',
  sampleCopy: 'Request a physical sample from our Décor collection. Ships within 3 business days.',
  distributorCopy: 'Find a stocking distributor near your project site.',
  repCopy: 'Connect with a local sales rep for specification support and pricing.',
};
