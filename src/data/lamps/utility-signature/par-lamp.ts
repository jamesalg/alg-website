/**
 * PAR Reflector family detail data
 * Collection: utility-signature
 * v2.7.0
 */
const par_lampData = {
  slug: 'par-lamp',
  name: 'PAR Reflector',
  collectionSlug: 'utility-signature',
  collectionName: 'Utility sign<span class="aa">Ⓐ</span>TURE',
  collectionTitleAscii: 'UTILITY SIGN<span class="aa">Ⓐ</span>TURE',
  collectionHeadlineLine: 'Utility sign<span class="aa">Ⓐ</span>TURE',
  collectionAesthetic: 'utility' as const,
  tagline: 'PAR38 reflector lamps for outdoor and commercial applications.',
  description: 'PAR38 reflector lamps for outdoor and commercial applications.',
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
  { slug: 'a-lamp', name: 'A-Lamp', skuCount: 6, tagline: '' },
  { slug: 'br-lamp', name: 'BR-Lamp', skuCount: 5, tagline: '' },
  { slug: 'husk-hid', name: 'Hid Retrofit', skuCount: 0, tagline: '' },
];

export const relatedCollections = [
  { slug: 'luxoarch', vertical: 'Commercial', name: 'luxoⒶRCH', description: 'Commercial-grade LED luminaires.', status: 'live' as const },
  { slug: 'planoarch', vertical: 'Commercial', name: 'planoⒶRCH', description: 'Flat-panel LED for commercial spaces.', status: 'live' as const },
];

export const getStarted = {
  layoutCopy: 'Submit a fixture schedule and we return a utility lamp recommendation for each row.',
  sampleCopy: 'Request a physical sample of any active Utility sign<span class="aa">Ⓐ</span>TURE family. Ships within 3 business days.',
  distributorCopy: 'Find a stocking distributor near your project site.',
  repCopy: 'Connect with a local sales rep for specification support and pricing.',
};

export default par_lampData;
