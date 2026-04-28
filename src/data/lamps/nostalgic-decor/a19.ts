/**
 * The Eames A19 — Nostalgic Décor family detail data
 * Collection: nostalgic-decor
 * v2.7.x — Named product, narrative copy, SKU data from Item.xlsx
 */
const a19Data = {
  slug: 'a19',
  name: 'The Eames A19',
  collectionSlug: 'nostalgic-decor',
  collectionName: 'Nostalgic Décor',
  collectionTitleAscii: 'NOST<span class="aa">Ⓐ</span>LGIC',
  collectionHeadlineLine: 'Décor | nost<span class="aa">Ⓐ</span>LGIC',
  collectionAesthetic: 'nostalgic' as const,
  tagline: 'The standard-bearer of mid-century domestic light.',
  description: 'The standard-bearer of mid-century domestic light. The Eames A19 is the lamp Charles and Ray Eames would have used in the Case Study House — a standard A19 silhouette with a warm nostalgic finish, 2700K to 2400K CCT options, and a frosted or smoked glass that softens the filament into a warm ambient glow. For residential living rooms, hospitality bedside tables, and any application where the lamp is the last thing you see before the lights go out.',
  heroImage: '',
  echelon: undefined,
  keySpecs: {
    inputWatts: '4.5–7.5W',
    lumens: '350–800lm',
    lmPerW: '75–100',
    cri: '80+',
  },
  certifications: ['UL Listed', 'Dimmable', '120V', 'RoHS Compliant'],
  datasheetUrl: undefined,
  installGuideUrl: undefined,
  comingSoon: false,
  isTubularArch: false,
};
export default a19Data;
export const siblingFamilies = [
  { slug: 'a15', name: 'The Saarinen A15', skuCount: 24, tagline: 'Small-format A15 for accent and vanity.' },
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
