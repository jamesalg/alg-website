/**
 * Candle (Blunt-Tip) family detail data
 * Collection: nostalgic-decor
 * v2.7.0
 */
const candle_blunt_tipData = {
  slug: 'candle-blunt-tip',
  name: 'Candle (Blunt-Tip)',
  collectionSlug: 'nostalgic-decor',
  collectionName: 'Nostalgic Décor',
  collectionTitleAscii: 'Nostalgic Decor',
  collectionHeadlineLine: 'Nostalgic Décor',
  collectionAesthetic: 'nostalgic' as const,
  tagline: 'B10 blunt-tip candelabra lamps for chandeliers and sconces.',
  description: 'B10 blunt-tip candelabra lamps for chandeliers and sconces.',
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
    {
      slug: 'a-lamp',
      name: 'A-Lamp',
      tagline: 'Classic A19 and A21 shapes with nostalgic frosted or silver-tip finish.',
      skuCount: 39,
    },
    {
      slug: 'candle-flame-tip',
      name: 'Candle (Flame-Tip)',
      tagline: 'CA10 flame-tip candelabra lamps for decorative fixtures.',
      skuCount: 22,
    },
    {
      slug: 'globe',
      name: 'Globe',
      tagline: 'G40 globe lamps for vanity and pendant applications.',
      skuCount: 3,
    },
    {
      slug: 'globe-g16-5',
      name: 'Globe G16.5',
      tagline: 'G16.5 small globe lamps for bathroom vanity strips.',
      skuCount: 23,
    },
    {
      slug: 'globe-g25',
      name: 'Globe G25',
      tagline: 'G25 medium globe lamps for vanity and decorative pendants.',
      skuCount: 11,
    },
    {
      slug: 's14',
      name: 'S14',
      tagline: 'S14 string lamp replacements for commercial string light installations.',
      skuCount: 16,
    }
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

export default candle_blunt_tipData;
