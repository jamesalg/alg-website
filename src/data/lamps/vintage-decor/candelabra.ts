/**
 * The Glasgow Candelabra — Vintage Décor family detail data
 * Collection: vintage-decor
 * v2.7.x — Named product, narrative copy, SKU data from Item.xlsx
 */
const candelabraData = {
  slug: 'candelabra',
  name: 'The Glasgow Candelabra',
  collectionSlug: 'vintage-decor',
  collectionName: 'Vintage Décor',
  collectionTitleAscii: 'VINT<span class="aa">Ⓐ</span>GE',
  collectionHeadlineLine: 'Décor | vint<span class="aa">Ⓐ</span>GE',
  collectionAesthetic: 'vintage' as const,
  tagline: 'A chandelier lamp that earns its place in the room.',
  description: 'A chandelier lamp that earns its place in the room. The Glasgow Candelabra draws on the craftsman tradition of the Glasgow School of Art — hand-blown amber glass, a warm 2200K glow, and a CA10 silhouette that disappears into the fixture and lets the light do the talking. For dining rooms, sconces, and decorative pendants where the bulb is part of the composition.',
  heroImage: '',
  echelon: undefined,
  keySpecs: {
    inputWatts: '2–4.5W',
    lumens: '180–350lm',
    lmPerW: '70–80',
    cri: '90+',
  },
  certifications: ['UL Listed', 'Dimmable', '120V', 'RoHS Compliant'],
  datasheetUrl: undefined,
  installGuideUrl: undefined,
  comingSoon: false,
  isTubularArch: false,
};
export default candelabraData;
export const siblingFamilies = [
  { slug: 'edison', name: 'The Foundry Edison', skuCount: 18, tagline: 'ST19 Edison in clear, amber, and smoked.' },
  { slug: 'globe', name: 'The Provence Globe', skuCount: 11, tagline: 'G25 and G40 globe in amber and smoked.' },
  { slug: 'radio', name: 'The Marconi Radio', skuCount: 7, tagline: 'T10 and T14 radio-style tubular.' },
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
