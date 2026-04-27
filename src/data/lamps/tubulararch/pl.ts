/**
 * PL family detail data
 * Collection: tubulararch
 * v2.7.0
 */
const plData = {
  slug: 'pl',
  name: 'PL',
  collectionSlug: 'tubulararch',
  collectionName: 'tubul<span class="aa">Ⓐ</span>RCH',
  collectionTitleAscii: 'tubulARCH',
  collectionHeadlineLine: 'tubul<span class="aa">Ⓐ</span>RCH',
  collectionAesthetic: 'utility' as const,
  tagline: 'Compact fluorescent PL lamp replacements.',
  description: 'Compact fluorescent PL lamp replacements.',
  heroImage: '',
  echelon: undefined,
  keySpecs: {
    inputWatts: 'See specs',
    lumens: 'See specs',
    lmPerW: 'See specs',
    cri: '80+',
  },
  certifications: ['UL Listed', 'FCC', 'DLC Listed'],
  datasheetUrl: undefined,
  installGuideUrl: undefined,
  comingSoon: false,
  isTubularArch: true,
};

export const siblingFamilies = [
    {
      slug: 't5', vertical: 'General',
      name: 'T5',
      tagline: 'T5HE and T5HO fluorescent lamp replacements.',
      skuCount: 27,
    },
    {
      slug: 't8', vertical: 'General',
      name: 'T8',
      tagline: 'The most common fluorescent retrofit. 2FT, 4FT, and 8FT.',
      skuCount: 100,
    },
    {
      slug: 'pll', vertical: 'General',
      name: 'PLL',
      tagline: 'Biax PLL lamp replacements for 2G11 base fixtures.',
      skuCount: 3,
    },
    {
      slug: 'u6', vertical: 'General',
      name: 'U6',
      tagline: 'U-bend T8 lamp replacements for 2×2 troffer fixtures.',
      skuCount: 5,
    }
  ];

export const relatedCollections = [
    {
      slug: 'luxoarch',
      name: 'luxo<span class="aa">Ⓐ</span>RCH',
      vertical: 'Outdoor',
      description: 'Outdoor lighting for the commercial perimeter.',
      status: 'live' as const,
    },
    {
      slug: 'planoarch',
      name: 'plano<span class="aa">Ⓐ</span>RCH',
      vertical: 'Indoor',
      description: 'Commercial indoor lighting for offices, retail, and healthcare.',
      status: 'live' as const,
    },
    {
      slug: 'nostalgic-decor',
      name: 'Nostalgic Décor',
      vertical: 'Lamps',
      description: 'Classic filament-style LED lamps.',
      status: 'live' as const,
    },
    {
      slug: 'vintage-decor',
      name: 'Vintage Décor',
      vertical: 'Lamps',
      description: 'Old-world filament lamps with modern efficiency.',
      status: 'live' as const,
    }
  ];

export const getStarted = {
  layoutCopy: 'Submit a fixture schedule and we return a retrofit recommendation with UL type and wattage for each row.',
  sampleCopy: 'Request a physical sample of any active tubul<span class="aa">Ⓐ</span>RCH family. Ships from a US warehouse within 3 business days.',
  distributorCopy: 'Find a stocking distributor near your project site. Core tubul<span class="aa">Ⓐ</span>RCH SKUs are stocked at all 5 US warehouses.',
  repCopy: 'Connect with a local sales rep for specification support, pricing, and project tracking.',
};

export default plData;
