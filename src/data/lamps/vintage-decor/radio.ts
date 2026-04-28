/**
 * The Marconi Radio — Vintage Décor family detail data
 * Collection: vintage-decor
 * v2.7.x — Named product, narrative copy, SKU data from Item.xlsx
 */
const radioData = {
  slug: 'radio',
  name: 'The Marconi Radio',
  collectionSlug: 'vintage-decor',
  collectionName: 'Vintage Décor',
  collectionTitleAscii: 'VINT<span class="aa">Ⓐ</span>GE',
  collectionHeadlineLine: 'Décor | vint<span class="aa">Ⓐ</span>GE',
  collectionAesthetic: 'vintage' as const,
  tagline: 'The tubular lamp with a wireless-era pedigree.',
  description: 'The tubular lamp with a wireless-era pedigree. The Marconi Radio takes the T10 and T14 radio-bulb form — long, slender, unmistakably vintage — and pairs it with 2200K amber warmth and a 92 CRI option for spaces where color accuracy matters as much as atmosphere. For wall sconces, art-deco pendants, and any fixture that calls for a lamp with a story.',
  heroImage: '',
  echelon: undefined,
  keySpecs: {
    inputWatts: '3.5W',
    lumens: '250–280lm',
    lmPerW: '70–80',
    cri: '92',
  },
  certifications: ['UL Listed', 'Dimmable', '120V', 'RoHS Compliant'],
  datasheetUrl: undefined,
  installGuideUrl: undefined,
  comingSoon: false,
  isTubularArch: false,
};
export default radioData;
export const siblingFamilies = [
  { slug: 'candelabra', name: 'The Glasgow Candelabra', skuCount: 6, tagline: 'CA10 vintage candelabra in amber finish.' },
  { slug: 'edison', name: 'The Foundry Edison', skuCount: 18, tagline: 'ST19 Edison in clear, amber, and smoked.' },
  { slug: 'globe', name: 'The Provence Globe', skuCount: 11, tagline: 'G25 and G40 globe in amber and smoked.' },
  { slug: 'tubular', name: 'The Brighton Tubular', skuCount: 22, tagline: 'T9 tubular in clear and amber.' },
  { slug: 'victorian', name: 'The Belgravia Victorian', skuCount: 9, tagline: 'Victorian A19 in smoked, amber, squirrel-cage.' },
];
export const relatedCollections = [
  { slug: 'nostalgic-decor', vertical: 'Lamps', name: 'Nostalgic Décor', description: 'Classic filament-style LED lamps with warm amber glow.', status: 'live' as const },
  { slug: 'signature', vertical: 'Lamps', name: 'sign<span class="aa">Ⓐ</span>TURE', description: 'Commercial-grade LED lamps for the hardest retrofit jobs.', status: 'live' as const },
  { slug: 'planoarch', vertical: 'Indoor', name: 'plano<span class="aa">Ⓐ</span>RCH', description: 'Commercial indoor lighting for offices, retail, and healthcare.', status: 'live' as const },
];
export const getStarted = {
  layoutCopy: 'Submit a fixture schedule and we return a lamp recommendation for each row.',
  sampleCopy: 'Request a physical sample from our Décor collection. Ships within 3 business days.',
  distributorCopy: 'Find a stocking distributor near your project site.',
  repCopy: 'Connect with a local sales rep for specification support and pricing.',
};
