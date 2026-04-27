/**
 * tubul<span class="aa">Ⓐ</span>RCH collection data
 * v2.7.0 — Bucket B lamp collection
 * CF.Collection: 'tubul<span class="aa">Ⓐ</span>RCH'
 */
const tubulararchData = {
  slug: 'tubulararch',
  name: 'tubul<span class="aa">Ⓐ</span>RCH',
  titleAscii: 'tubulARCH',
  parentVertical: 'Indoor' as const,
  parentSubVertical: 'Lamps',
  headlineLine: 'tubul<span class="aa">Ⓐ</span>RCH',
  description: 'LED lamp retrofits for T5, T8, PL, PLL, and U6 fixtures. UL-A (ballast-compatible), UL-A+B (hybrid), and UL-B (ballast-bypass) types for every retrofit scenario.',
  aesthetic: 'utility' as const,
  pillRow: ['T5 · T8 · PL · PLL · U6', 'UL-A · UL-A+B · UL-B', 'Commercial Retrofit', 'DLC Listed'],
  families: [
    {
      slug: 't5',
      name: 'T5',
      tagline: 'T5HE and T5HO fluorescent lamp replacements.',
      heroImage: '',
      skuCount: 27,
      comingSoon: false,
    },
    {
      slug: 't8',
      name: 'T8',
      tagline: 'The most common fluorescent retrofit. 2FT, 4FT, and 8FT.',
      heroImage: '',
      skuCount: 100,
      comingSoon: false,
    },
    {
      slug: 'pl',
      name: 'PL',
      tagline: 'Compact fluorescent PL lamp replacements.',
      heroImage: '',
      skuCount: 6,
      comingSoon: false,
    },
    {
      slug: 'pll',
      name: 'PLL',
      tagline: 'Biax PLL lamp replacements for 2G11 base fixtures.',
      heroImage: '',
      skuCount: 3,
      comingSoon: false,
    },
    {
      slug: 'u6',
      name: 'U6',
      tagline: 'U-bend T8 lamp replacements for 2×2 troffer fixtures.',
      heroImage: '',
      skuCount: 5,
      comingSoon: false,
    },
  ],
  legacyFamilies: [],
  getStarted: {
    layoutCopy: 'Submit a fixture schedule and we return a retrofit recommendation with UL type and wattage for each row.',
    sampleCopy: 'Request a physical sample of any active tubul<span class="aa">Ⓐ</span>RCH family. Ships from a US warehouse within 3 business days.',
    distributorCopy: 'Find a stocking distributor near your project site. Core tubul<span class="aa">Ⓐ</span>RCH SKUs are stocked at all 5 US warehouses.',
    repCopy: 'Connect with a local sales rep for specification support, pricing, and project tracking.',
  },
  relatedCollections: [
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
      description: 'Classic filament-style LED lamps. Edison, globe, and vintage shapes.',
      status: 'live' as const,
    },
    {
      slug: 'vintage-decor',
      name: 'Vintage Décor',
      vertical: 'Lamps',
      description: 'Old-world filament lamps with modern efficiency.',
      status: 'live' as const,
    },
  ],
};
export default tubulararchData;
