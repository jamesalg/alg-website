/**
 * The Heath G16.5 — Nostalgic Décor family detail data
 * Collection: nostalgic-decor
 * v2.7.x — Named product, narrative copy, SKU data from Item.xlsx
 */
const g16_5Data = {
  slug: 'g16-5',
  name: 'The Heath G16.5',
  collectionSlug: 'nostalgic-decor',
  collectionName: 'Nostalgic Décor',
  collectionTitleAscii: 'NOST<span class="aa">Ⓐ</span>LGIC',
  collectionHeadlineLine: 'Décor | nost<span class="aa">Ⓐ</span>LGIC',
  collectionAesthetic: 'nostalgic' as const,
  tagline: 'The vanity globe that Heath Ceramics would have stocked.',
  description: 'The vanity globe that Heath Ceramics would have stocked. The Heath G16.5 brings the warm matte finish of Heath\'s Sausalito studio to a G16.5 globe shape — a small, round lamp with a 2700K to 2400K glow that reads as warm-white in vanity strips and as amber in decorative pendants. For bathroom vanity strips, globe pendants, and any fixture where a small round lamp needs to do big atmospheric work.',
  heroImage: '',
  echelon: undefined,
  keySpecs: {
    inputWatts: '3.5–4.5W',
    lumens: '280–350lm',
    lmPerW: '75–80',
    cri: '80+',
  },
  certifications: ['UL Listed', 'Dimmable', '120V', 'RoHS Compliant'],
  datasheetUrl: undefined,
  installGuideUrl: undefined,
  comingSoon: false,
  isTubularArch: false,
};
export default g16_5Data;
export const siblingFamilies = [
  { slug: 'a15', name: 'The Saarinen A15', skuCount: 24, tagline: 'Small-format A15 for accent and vanity.' },
  { slug: 'a19', name: 'The Eames A19', skuCount: 24, tagline: 'Standard A19 for residential and hospitality.' },
  { slug: 'b10', name: 'The Knoll B10', skuCount: 42, tagline: 'Blunt-tip candelabra for chandeliers and sconces.' },
  { slug: 'ca10', name: 'The Bauer CA10', skuCount: 36, tagline: 'Flame-tip candelabra for decorative fixtures.' },
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
