/**
 * Vintage Décor collection data
 * v2.7.0 — Bucket B lamp collection
 * CF.Collection: 'Décor vint<span class="aa">Ⓐ</span>GE'
 */
const vintageDecorData = {
  slug: 'vintage-decor',
  name: 'Vintage Décor',
  titleAscii: 'Vintage Decor',
  parentVertical: 'Indoor' as const,
  parentSubVertical: 'Lamps',
  headlineLine: 'Vintage Décor',
  description: 'Old-world filament lamps with modern efficiency. Edison, Victorian, tubular, radio, globe, and candelabra shapes in amber and smoked finishes. 2200K warm glow.',
  aesthetic: 'vintage' as const,
  pillRow: ['Edison · Victorian · Globe · Radio · Tubular · Candle', '2200K Warm Amber', 'Dimmable', 'Old-World Charm'],
  families: [
    {
      slug: 'candelabra', vertical: 'General',
      name: 'Candelabra',
      tagline: 'CA10 vintage candelabra lamps in amber finish.',
      heroImage: '',
      skuCount: 2,
      comingSoon: false,
    },
    {
      slug: 'edison', vertical: 'General',
      name: 'Edison',
      tagline: 'ST19 Edison lamps in clear, amber, and smoked finishes.',
      heroImage: '',
      skuCount: 14,
      comingSoon: false,
    },
    {
      slug: 'globe', vertical: 'General',
      name: 'Globe',
      tagline: 'G25 and G40 globe lamps in amber and smoked finishes.',
      heroImage: '',
      skuCount: 11,
      comingSoon: false,
    },
    {
      slug: 'radio', vertical: 'General',
      name: 'Radio',
      tagline: 'T10 and T14 radio-style tubular lamps.',
      heroImage: '',
      skuCount: 7,
      comingSoon: false,
    },
    {
      slug: 'tubular', vertical: 'General',
      name: 'Tubular',
      tagline: 'T9 tubular lamps in clear and amber finishes.',
      heroImage: '',
      skuCount: 12,
      comingSoon: false,
    },
    {
      slug: 'victorian', vertical: 'General',
      name: 'Victorian',
      tagline: 'Victorian A19 lamps in smoked, amber, and squirrel-cage styles.',
      heroImage: '',
      skuCount: 9,
      comingSoon: false,
    },
  ],
  legacyFamilies: [],
  getStarted: {
    layoutCopy: 'Submit a fixture schedule and we return a lamp recommendation for each row.',
    sampleCopy: 'Request a physical sample of any active Vintage Décor family. Ships within 3 business days.',
    distributorCopy: 'Find a stocking distributor near your project site.',
    repCopy: 'Connect with a local sales rep for specification support and pricing.',
  },
  relatedCollections: [
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
      description: 'Utility LED lamps for everyday replacement: A-lamps, BR floods, PAR reflectors.',
      status: 'live' as const,
    },
    {
      slug: 'planoarch',
      name: 'plano<span class="aa">Ⓐ</span>RCH',
      vertical: 'Indoor',
      description: 'Commercial indoor lighting for offices, retail, and healthcare.',
      status: 'live' as const,
    },
  ],
};
export default vintageDecorData;
