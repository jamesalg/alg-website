/**
 * T5 family detail data
 * Collection: tubulararch
 * v2.7.0
 */
const t5Data = {
  slug: 't5',
  name: 'T5',
  collectionSlug: 'tubulararch',
  collectionName: 'tubul<span class="aa">Ⓐ</span>RCH',
  collectionTitleAscii: 'TUBUL<span class="aa">Ⓐ</span>RCH',
  collectionHeadlineLine: 'tubul<span class="aa">Ⓐ</span>RCH',
  collectionAesthetic: 'utility' as const,
  tagline: 'T5HE and T5HO fluorescent lamp replacements.',
  description: 'T5HE and T5HO fluorescent lamp replacements.',
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
  { slug: 'pl', name: 'Pl', skuCount: 33, tagline: '' },
  { slug: 'pll', name: 'Pll', skuCount: 33, tagline: '' },
  { slug: 't8', name: 'T8', skuCount: 33, tagline: '' },
  { slug: 'u6', name: 'U6', skuCount: 33, tagline: '' },
];

export const relatedCollections = [
  { slug: 'luxoarch', vertical: 'Commercial', name: 'luxoⒶRCH', description: 'Commercial-grade LED luminaires.', status: 'live' as const },
  { slug: 'planoarch', vertical: 'Commercial', name: 'planoⒶRCH', description: 'Flat-panel LED for commercial spaces.', status: 'live' as const },
];

export const getStarted = {
  layoutCopy: 'Submit a fixture schedule and we return a retrofit recommendation with UL type and wattage for each row.',
  sampleCopy: 'Request a physical sample of any active tubul<span class="aa">Ⓐ</span>RCH family. Ships from a US warehouse within 3 business days.',
  distributorCopy: 'Find a stocking distributor near your project site. Core tubul<span class="aa">Ⓐ</span>RCH SKUs are stocked at all 5 US warehouses.',
  repCopy: 'Connect with a local sales rep for specification support, pricing, and project tracking.',
};

export default t5Data;
