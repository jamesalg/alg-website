/**
 * Tubular family detail data
 * Collection: vintage-decor
 * v2.7.0
 */
const tubularData = {
  slug: 'tubular',
  name: 'Tubular',
  collectionSlug: 'vintage-decor',
  collectionName: 'Vintage Décor',
  collectionTitleAscii: 'VINT<span class="aa">Ⓐ</span>GE',
  collectionHeadlineLine: 'Décor | vint<span class="aa">Ⓐ</span>GE',
  collectionAesthetic: 'vintage' as const,
  tagline: 'T9 tubular lamps in clear and amber finishes.',
  description: 'T9 tubular lamps in clear and amber finishes.',
  heroImage: '',
  echelon: undefined,
  keySpecs: {
    inputWatts: '2–4.5W',
    lumens: '200–450lm',
    lmPerW: '80–100',
    cri: '90+',
  },
  certifications: ['UL Listed', 'FCC', 'Dimmable'],
  datasheetUrl: undefined,
  installGuideUrl: undefined,
  comingSoon: false,
  isTubularArch: false,
};

export const siblingFamilies = [
  { slug: 'candelabra', name: 'Candelabra', skuCount: 12, tagline: '' },
  { slug: 'edison', name: 'Edison', skuCount: 12, tagline: '' },
  { slug: 'globe', name: 'Globe', skuCount: 12, tagline: '' },
  { slug: 'radio', name: 'Radio', skuCount: 12, tagline: '' },
  { slug: 'victorian', name: 'Victorian', skuCount: 12, tagline: '' },
];

export const relatedCollections = [
  { slug: 'luxoarch', vertical: 'Commercial', name: 'luxoⒶRCH', description: 'Commercial-grade LED luminaires.', status: 'live' as const },
  { slug: 'planoarch', vertical: 'Commercial', name: 'planoⒶRCH', description: 'Flat-panel LED for commercial spaces.', status: 'live' as const },
];

export const getStarted = {
  layoutCopy: 'Submit a fixture schedule and we return a lamp recommendation for each row.',
  sampleCopy: 'Request a physical sample of any active Vintage Décor family. Ships within 3 business days.',
  distributorCopy: 'Find a stocking distributor near your project site.',
  repCopy: 'Connect with a local sales rep for specification support and pricing.',
};

export default tubularData;
