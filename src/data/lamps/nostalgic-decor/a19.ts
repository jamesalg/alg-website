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
  collectionTitleAscii: 'Nostalgic Decor',
  collectionHeadlineLine: 'Nostalgic Décor',
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
  { slug: 'a15', vertical: 'General', name: 'A15' },
  { slug: 'a19', vertical: 'General', name: 'A19' },
  { slug: 'b10', vertical: 'General', name: 'B10' },
  { slug: 'ca10', vertical: 'General', name: 'CA10' },
  { slug: 'candle-blunt-tip', vertical: 'General', name: 'Candle Blunt-Tip' },
  { slug: 'candle-flame-tip', vertical: 'General', name: 'Candle Flame-Tip' },
  { slug: 'globe-g16-5', vertical: 'General', name: 'Globe G16.5' },
  { slug: 'globe-g25', vertical: 'General', name: 'Globe G25' },
  { slug: 's14', vertical: 'General', name: 'S14' },
];

export const relatedCollections = [
  { slug: 'vintage-decor', vertical: 'Decorative', name: 'Vintage Décor', href: '/collections/vintage-decor/' },
  { slug: 'consumer', vertical: 'Consumer', name: 'Consumer & Retail', href: '/collections/consumer/' },
];

export const getStarted = {
  sampleCopy: 'Request a sample of the A19 family from our Nostalgic Décor collection.',
  distributorCopy: 'Contact your ALG distributor to place an order for the A19 family.',
  repCopy: 'Find your local ALG rep for the Nostalgic Décor collection.',
  layoutCopy: 'Download the planogram layout guide for Nostalgic Décor.',
};
