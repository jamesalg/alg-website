/**
 * Globe G16.5 family detail data
 * Collection: nostalgic-decor
 * v2.7.0
 */
const globe_g16_5Data = {
  slug: 'g16-5',
  name: 'Globe G16.5',
  collectionSlug: 'nostalgic-decor',
  collectionName: 'Nostalgic Décor',
  collectionTitleAscii: 'NOST<span class="aa">Ⓐ</span>LGIC',
  collectionHeadlineLine: 'Décor | nost<span class="aa">Ⓐ</span>LGIC',
  collectionAesthetic: 'nostalgic' as const,
  tagline: 'G16.5 small globe lamps for bathroom vanity strips.',
  description: 'G16.5 small globe lamps for bathroom vanity strips.',
  heroImage: '',
  echelon: undefined,
  keySpecs: {
    inputWatts: '1.5–7.5W',
    lumens: '100–800lm',
    lmPerW: '80–110',
    cri: '80+',
  },
  certifications: ['UL Listed', 'FCC', 'JA8 Listed', 'Dimmable'],
  datasheetUrl: undefined,
  installGuideUrl: undefined,
  comingSoon: false,
  isTubularArch: false,
};

export const siblingFamilies = [
  { slug: 'a15', name: 'A15', skuCount: 23, tagline: '' },
  { slug: 'a19', name: 'A19', skuCount: 23, tagline: '' },
  { slug: 'b10', name: 'B10', skuCount: 23, tagline: '' },
  { slug: 'ca10', name: 'CA10', skuCount: 23, tagline: '' },
  { slug: 'candle-blunt-tip', name: 'Candle Blunt-Tip', skuCount: 23, tagline: '' },
  { slug: 'candle-flame-tip', name: 'Candle Flame-Tip', skuCount: 23, tagline: '' },
  { slug: 'g25', name: 'Globe G25', skuCount: 23, tagline: '' },
  { slug: 's14', name: 'S14', skuCount: 23, tagline: '' },
];

export const relatedCollections = [
  { slug: 'luxoarch', vertical: 'Commercial', name: 'luxoⒶRCH', description: 'Commercial-grade LED luminaires.', status: 'live' as const },
  { slug: 'planoarch', vertical: 'Commercial', name: 'planoⒶRCH', description: 'Flat-panel LED for commercial spaces.', status: 'live' as const },
];

export const getStarted = {
  layoutCopy: 'Submit a fixture schedule and we return a lamp recommendation for each row.',
  sampleCopy: 'Request a physical sample of any active Nostalgic Décor family. Ships within 3 business days.',
  distributorCopy: 'Find a stocking distributor near your project site.',
  repCopy: 'Connect with a local sales rep for specification support and pricing.',
};

export default globe_g16_5Data;
