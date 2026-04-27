/**
 * A15 family detail data
 * Collection: nostalgic-decor
 * v2.7.1
 */
const a15Data = {
  slug: 'a15',
  name: 'A15',
  collectionSlug: 'nostalgic-decor',
  collectionName: 'Nostalgic Décor',
  collectionTitleAscii: 'Nostalgic Decor',
  collectionHeadlineLine: 'Nostalgic Décor',
  collectionAesthetic: 'nostalgic' as const,
  tagline: 'Small-format A15 shape with vintage frosted finish, ideal for accent and vanity fixtures.',
  description: 'Small-format A15 shape with vintage frosted finish, ideal for accent and vanity fixtures.',
  heroImage: '',
  echelon: undefined,
  keySpecs: {
    inputWatts: '1.5–4.5W',
    lumens: '100–350lm',
    lmPerW: '70–90',
    cri: '80+',
  },
  certifications: ['UL Listed', 'FCC', 'Dimmable'],
  datasheetUrl: undefined,
  installGuideUrl: undefined,
  comingSoon: false,
  isTubularArch: false,
};

export default a15Data;

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
  sampleCopy: 'Request a sample of the A15 family from our Nostalgic Décor collection.',
  distributorCopy: 'Contact your ALG distributor to place an order for the A15 family.',
  repCopy: 'Find your local ALG rep for the Nostalgic Décor collection.',
  layoutCopy: 'Download the planogram layout guide for Nostalgic Décor.',
};
