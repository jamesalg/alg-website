/**
 * B10 family detail data
 * Collection: nostalgic-decor
 * v2.7.1
 */
const b10Data = {
  slug: 'b10',
  name: 'B10',
  collectionSlug: 'nostalgic-decor',
  collectionName: 'Nostalgic Décor',
  collectionTitleAscii: 'NOST<span class="aa">Ⓐ</span>LGIC',
  collectionHeadlineLine: 'Décor | nost<span class="aa">Ⓐ</span>LGIC',
  collectionAesthetic: 'nostalgic' as const,
  tagline: 'Blunt-tip candelabra shape for chandeliers and decorative fixtures.',
  description: 'Blunt-tip candelabra shape for chandeliers and decorative fixtures.',
  heroImage: '',
  echelon: undefined,
  keySpecs: {
    inputWatts: '2–5W',
    lumens: '150–450lm',
    lmPerW: '70–90',
    cri: '80+',
  },
  certifications: ['UL Listed', 'FCC', 'Dimmable'],
  datasheetUrl: undefined,
  installGuideUrl: undefined,
  comingSoon: false,
  isTubularArch: false,
};

export default b10Data;

export const siblingFamilies = [
  { slug: 'a15', name: 'A15', skuCount: 33, tagline: '' },
  { slug: 'a19', name: 'A19', skuCount: 33, tagline: '' },
  { slug: 'ca10', name: 'CA10', skuCount: 33, tagline: '' },
  { slug: 'candle-blunt-tip', name: 'Candle Blunt-Tip', skuCount: 33, tagline: '' },
  { slug: 'candle-flame-tip', name: 'Candle Flame-Tip', skuCount: 33, tagline: '' },
  { slug: 'g16-5', name: 'Globe G16.5', skuCount: 33, tagline: '' },
  { slug: 'g25', name: 'Globe G25', skuCount: 33, tagline: '' },
  { slug: 's14', name: 'S14', skuCount: 33, tagline: '' },
];

export const relatedCollections = [
  { slug: 'luxoarch', vertical: 'Commercial', name: 'luxoⒶRCH', description: 'Commercial-grade LED luminaires.', status: 'live' as const },
  { slug: 'planoarch', vertical: 'Commercial', name: 'planoⒶRCH', description: 'Flat-panel LED for commercial spaces.', status: 'live' as const },
];

export const getStarted = {
  sampleCopy: 'Request a sample of the B10 family from our Nostalgic Décor collection.',
  distributorCopy: 'Contact your ALG distributor to place an order for the B10 family.',
  repCopy: 'Find your local ALG rep for the Nostalgic Décor collection.',
  layoutCopy: 'Download the planogram layout guide for Nostalgic Décor.',
};
