/**
 * The Brighton Tubular — Vintage Décor family detail data
 * Collection: vintage-decor
 * v2.7.x — Named product, narrative copy, SKU data from Item.xlsx
 */
const tubularData = {
  slug: 'tubular',
  name: 'The Brighton Tubular',
  collectionSlug: 'vintage-decor',
  collectionName: 'Vintage Décor',
  collectionTitleAscii: 'VINT<span class="aa">Ⓐ</span>GE',
  collectionHeadlineLine: 'Décor | vint<span class="aa">Ⓐ</span>GE',
  collectionAesthetic: 'vintage' as const,
  tagline: 'Regency theatricality in a T9 form factor.',
  description: 'Regency theatricality in a T9 form factor. The Brighton Tubular brings the architectural drama of Brighton Pavilion\'s glass-and-light tradition to a compact T9 shape — clear or amber finish, spiral filament options, and a 2200K warmth that works in vanity strips, bathroom sconces, and decorative wall fixtures. Slim enough to disappear into the fixture. Warm enough to define the room.',
  heroImage: '',
  echelon: undefined,
  keySpecs: {
    inputWatts: '2–3.5W',
    lumens: '150–280lm',
    lmPerW: '70–80',
    cri: '80+',
  },
  certifications: ['UL Listed', 'Dimmable', '120V', 'RoHS Compliant'],
  datasheetUrl: undefined,
  installGuideUrl: undefined,
  comingSoon: false,
  isTubularArch: false,
};
export default tubularData;
export const siblingFamilies = [
  { slug: 'candelabra', name: 'The Glasgow Candelabra', skuCount: 6, tagline: 'CA10 vintage candelabra in amber finish.' },
  { slug: 'edison', name: 'The Foundry Edison', skuCount: 18, tagline: 'ST19 Edison in clear, amber, and smoked.' },
  { slug: 'globe', name: 'The Provence Globe', skuCount: 11, tagline: 'G25 and G40 globe in amber and smoked.' },
  { slug: 'radio', name: 'The Marconi Radio', skuCount: 7, tagline: 'T10 and T14 radio-style tubular.' },
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
