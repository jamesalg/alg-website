/**
 * Candle (Flame-Tip) family detail data
 * Collection: nostalgic-decor
 * v2.7.0
 */
const candle_flame_tipData = {
  slug: 'candle-flame-tip',
  name: 'Candle (Flame-Tip)',
  collectionSlug: 'nostalgic-decor',
  collectionName: 'Nostalgic Décor',
  collectionTitleAscii: 'Nostalgic Decor',
  collectionHeadlineLine: 'Nostalgic Décor',
  collectionAesthetic: 'nostalgic' as const,
  tagline: 'CA10 flame-tip candelabra lamps for decorative fixtures.',
  description: 'CA10 flame-tip candelabra lamps for decorative fixtures.',
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
    {
      slug: 'vintage-decor',
      name: 'Vintage Décor',
      vertical: 'Lamps',
      description: 'Old-world filament lamps with modern efficiency.',
      status: 'live' as const,
    },
    {
      slug: 'tubulararch',
      name: 'tubul<span class="aa">Ⓐ</span>RCH',
      vertical: 'Lamps',
      description: 'LED lamp retrofits for T5, T8, PL, PLL, and U6 fixtures.',
      status: 'live' as const,
    },
    {
      slug: 'utility-signature',
      name: 'Utility sign<span class="aa">Ⓐ</span>TURE',
      vertical: 'Lamps',
      description: 'Utility LED lamps for everyday replacement.',
      status: 'live' as const,
    },
    {
      slug: 'planoarch',
      name: 'plano<span class="aa">Ⓐ</span>RCH',
      vertical: 'Indoor',
      description: 'Commercial indoor lighting for offices, retail, and healthcare.',
      status: 'live' as const,
    }
  ];

export const getStarted = {
  layoutCopy: 'Submit a fixture schedule and we return a lamp recommendation for each row.',
  sampleCopy: 'Request a physical sample of any active Nostalgic Décor family. Ships within 3 business days.',
  distributorCopy: 'Find a stocking distributor near your project site.',
  repCopy: 'Connect with a local sales rep for specification support and pricing.',
};

export default candle_flame_tipData;
