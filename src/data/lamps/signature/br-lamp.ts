/**
 * BR Flood family detail data
 * Collection: signature
 * v2.7.0
 */
const br_lampData = {
  slug: 'br-lamp',
  name: 'BR Flood',
  collectionSlug: 'signature',
  collectionName: 'sign<span class="aa">Ⓐ</span>TURE',
  collectionTitleAscii: 'SIGN<span class="aa">Ⓐ</span>TURE',
  collectionHeadlineLine: 'sign<span class="aa">Ⓐ</span>TURE',
  collectionAesthetic: 'utility' as const,
  tagline: 'BR40 flood lamps for recessed and track lighting.',
  description: 'BR40 flood lamps for recessed and track lighting.',
  heroImage: '',
  echelon: undefined,
  keySpecs: {
    inputWatts: '9–12W',
    lumens: '800–1100lm',
    lmPerW: '80–100',
    cri: '80+',
  },
  certifications: ['UL Listed', 'FCC'],
  datasheetUrl: undefined,
  installGuideUrl: undefined,
  comingSoon: true,
  isTubularArch: false,
};

export const siblingFamilies = [
  { slug: 'a-lamp', name: 'A-Lamp', skuCount: 5, tagline: '' },
  { slug: 'husk-hid', name: 'Hid Retrofit', skuCount: 5, tagline: '' },
  { slug: 'par-lamp', name: 'PAR-Lamp', skuCount: 5, tagline: '' },
];

export const relatedCollections = [
  { slug: 'luxoarch', vertical: 'Commercial', name: 'luxoⒶRCH', description: 'Commercial-grade LED luminaires.', status: 'live' as const },
  { slug: 'planoarch', vertical: 'Commercial', name: 'planoⒶRCH', description: 'Flat-panel LED for commercial spaces.', status: 'live' as const },
];

export const getStarted = {
  layoutCopy: 'Submit a fixture schedule and we return a utility lamp recommendation for each row.',
  sampleCopy: 'Request a physical sample of any active sign<span class="aa">Ⓐ</span>TURE family. Ships within 3 business days.',
  distributorCopy: 'Find a stocking distributor near your project site.',
  repCopy: 'Connect with a local sales rep for specification support and pricing.',
};

export default br_lampData;
