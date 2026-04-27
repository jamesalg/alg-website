/**
 * Tubular family detail data
 * Collection: vintage-decor
 * v2.7.0
 */
const tubularData = {
  slug: 'tubular',
  name: 'Tubular',
  collectionSlug: 'vintage-decor',
  collectionName: 'Vintage Décor',
  collectionTitleAscii: 'Vintage Decor',
  collectionHeadlineLine: 'Vintage Décor',
  collectionAesthetic: 'vintage' as const,
  tagline: 'T9 tubular lamps in clear and amber finishes.',
  description: 'T9 tubular lamps in clear and amber finishes.',
  heroImage: '',
  echelon: undefined,
  keySpecs: {
    inputWatts: '2–4.5W',
    lumens: '200–450lm',
    lmPerW: '80–100',
    cri: '90+',
  },
  certifications: ['UL Listed', 'FCC', 'Dimmable'],
  datasheetUrl: undefined,
  installGuideUrl: undefined,
  comingSoon: false,
  isTubularArch: false,
};

export const siblingFamilies = [
    {
      slug: 'candelabra',
      name: 'Candelabra',
      tagline: 'CA10 vintage candelabra lamps in amber finish.',
      skuCount: 2,
    },
    {
      slug: 'edison',
      name: 'Edison',
      tagline: 'ST19 Edison lamps in clear, amber, and smoked finishes.',
      skuCount: 14,
    },
    {
      slug: 'globe',
      name: 'Globe',
      tagline: 'G25 and G40 globe lamps in amber and smoked finishes.',
      skuCount: 11,
    },
    {
      slug: 'radio',
      name: 'Radio',
      tagline: 'T10 and T14 radio-style tubular lamps.',
      skuCount: 7,
    },
    {
      slug: 'victorian',
      name: 'Victorian',
      tagline: 'Victorian A19 lamps in smoked, amber, and squirrel-cage styles.',
      skuCount: 9,
    }
  ];

export const relatedCollections = [
    {
      slug: 'nostalgic-decor',
      name: 'Nostalgic Décor',
      vertical: 'Lamps',
      description: 'Classic filament-style LED lamps with warm amber glow.',
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
  sampleCopy: 'Request a physical sample of any active Vintage Décor family. Ships within 3 business days.',
  distributorCopy: 'Find a stocking distributor near your project site.',
  repCopy: 'Connect with a local sales rep for specification support and pricing.',
};

export default tubularData;
