/**
 * BR Flood family detail data
 * Collection: utility-signature
 * v2.7.0
 */
const br_lampData = {
  slug: 'br-lamp',
  name: 'BR Flood',
  collectionSlug: 'utility-signature',
  collectionName: 'Utility sign<span class="aa">Ⓐ</span>TURE',
  collectionTitleAscii: 'Utility signATURE',
  collectionHeadlineLine: 'Utility sign<span class="aa">Ⓐ</span>TURE',
  collectionAesthetic: 'utility' as const,
  tagline: 'BR40 flood lamps for recessed and track lighting.',
  description: 'BR40 flood lamps for recessed and track lighting.',
  heroImage: '',
  echelon: undefined,
  keySpecs: {
    inputWatts: '9–12W',
    lumens: '800–1100lm',
    lmPerW: '80–100',
    cri: '80+',
  },
  certifications: ['UL Listed', 'FCC'],
  datasheetUrl: undefined,
  installGuideUrl: undefined,
  comingSoon: false,
  isTubularArch: false,
};

export const siblingFamilies = [
    {
      slug: 'a-lamp',
      name: 'A-Lamp',
      tagline: 'A19 utility LED lamps for everyday commercial replacement.',
      skuCount: 4,
    },
    {
      slug: 'par-lamp',
      name: 'PAR Reflector',
      tagline: 'PAR38 reflector lamps for outdoor and commercial applications.',
      skuCount: 2,
    },
    {
      slug: 'hid-retrofit',
      name: 'HID Retrofit',
      tagline: 'HID retrofit lamps for metal halide and high-pressure sodium fixtures.',
      skuCount: 0,
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
      slug: 'planoarch',
      name: 'plano<span class="aa">Ⓐ</span>RCH',
      vertical: 'Indoor',
      description: 'Commercial indoor lighting for offices, retail, and healthcare.',
      status: 'live' as const,
    }
  ];

export const getStarted = {
  layoutCopy: 'Submit a fixture schedule and we return a utility lamp recommendation for each row.',
  sampleCopy: 'Request a physical sample of any active Utility sign<span class="aa">Ⓐ</span>TURE family. Ships within 3 business days.',
  distributorCopy: 'Find a stocking distributor near your project site.',
  repCopy: 'Connect with a local sales rep for specification support and pricing.',
};

export default br_lampData;
