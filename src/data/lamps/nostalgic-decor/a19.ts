/**
 * A19 family detail data
 * Collection: nostalgic-decor
 * v2.7.1
 */
const a19Data = {
  slug: 'a19',
  name: 'A19',
  collectionSlug: 'nostalgic-decor',
  collectionName: 'Nostalgic Décor',
  collectionTitleAscii: 'NOST<span class="aa">Ⓐ</span>LGIC',
  collectionHeadlineLine: 'Décor | nost<span class="aa">Ⓐ</span>LGIC',
  collectionAesthetic: 'nostalgic' as const,
  tagline: 'Standard A19 shape with warm nostalgic finish for residential and hospitality applications.',
  description: 'Standard A19 shape with warm nostalgic finish for residential and hospitality applications.',
  heroImage: '',
  echelon: undefined,
  keySpecs: {
    inputWatts: '6.5–15W',
    lumens: '500–1100lm',
    lmPerW: '75–100',
    cri: '80+',
  },
  certifications: ['UL Listed', 'FCC', 'Dimmable'],
  datasheetUrl: undefined,
  installGuideUrl: undefined,
  comingSoon: false,
  isTubularArch: false,
};

export default a19Data;

export const siblingFamilies = [
  { slug: 'a15', name: 'A15', skuCount: 14, tagline: '' },
  { slug: 'b10', name: 'B10', skuCount: 14, tagline: '' },
  { slug: 'ca10', name: 'CA10', skuCount: 14, tagline: '' },
  { slug: 'candle-blunt-tip', name: 'Candle Blunt-Tip', skuCount: 14, tagline: '' },
  { slug: 'candle-flame-tip', name: 'Candle Flame-Tip', skuCount: 14, tagline: '' },
  { slug: 'g16-5', name: 'Globe G16.5', skuCount: 14, tagline: '' },
  { slug: 'g25', name: 'Globe G25', skuCount: 14, tagline: '' },
  { slug: 's14', name: 'S14', skuCount: 14, tagline: '' },
];

export const relatedCollections = [
  { slug: 'luxoarch', vertical: 'Commercial', name: 'luxoⒶRCH', description: 'Commercial-grade LED luminaires.', status: 'live' as const },
  { slug: 'planoarch', vertical: 'Commercial', name: 'planoⒶRCH', description: 'Flat-panel LED for commercial spaces.', status: 'live' as const },
];

export const getStarted = {
  sampleCopy: 'Request a sample of the A19 family from our Nostalgic Décor collection.',
  distributorCopy: 'Contact your ALG distributor to place an order for the A19 family.',
  repCopy: 'Find your local ALG rep for the Nostalgic Décor collection.',
  layoutCopy: 'Download the planogram layout guide for Nostalgic Décor.',
};
