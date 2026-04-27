/**
 * Nostalgic Décor collection data
 * v2.7.1 — A-Lamp split into A15/A19, Globe removed (routed to Globe G25)
 * CF.Collection: 'Décor nost<span class="aa">Ⓐ</span>LGIC'
 */
const nostalgicDecorData = {
  slug: 'nostalgic-decor',
  name: 'Nostalgic Décor',
  titleAscii: 'Nostalgic Decor',
  parentVertical: 'Indoor' as const,
  parentSubVertical: 'Lamps',
  headlineLine: 'Nostalgic Décor',
  description: 'Classic filament-style LED lamps. A15, A19, candelabra, globe, and S14 string lamp replacements with warm amber glow. Dimmable, long-life, energy-efficient.',
  aesthetic: 'nostalgic' as const,
  pillRow: ['A15 · A19 · Candle · Globe · S14', 'Warm Amber Glow', 'Dimmable', 'Long Life'],
  families: [
    {
      slug: 'a15', vertical: 'General',
      name: 'A15',
      tagline: 'Small-format A15 shape with vintage frosted finish, ideal for accent and vanity fixtures.',
      heroImage: '',
      skuCount: 12,
      comingSoon: false,
    },
    {
      slug: 'a19', vertical: 'General',
      name: 'A19',
      tagline: 'Standard A19 shape with warm nostalgic finish for residential and hospitality applications.',
      heroImage: '',
      skuCount: 27,
      comingSoon: false,
    },
    {
      slug: 'b10', vertical: 'General',
      name: 'B10',
      tagline: 'Blunt-tip candelabra shape for chandeliers and decorative fixtures.',
      heroImage: '',
      skuCount: 33,
      comingSoon: false,
    },
    {
      slug: 'ca10', vertical: 'General',
      name: 'CA10',
      tagline: 'Flame-tip candelabra shape for decorative chandeliers and sconces.',
      heroImage: '',
      skuCount: 22,
      comingSoon: false,
    },
    {
      slug: 'globe-g16-5', vertical: 'General',
      name: 'Globe G16.5',
      tagline: 'G16.5 small globe lamps for bathroom vanity strips.',
      heroImage: '',
      skuCount: 23,
      comingSoon: false,
    },
    {
      slug: 'globe-g25', vertical: 'General',
      name: 'Globe G25',
      tagline: 'G25 medium globe lamps for vanity and decorative pendants.',
      heroImage: '',
      skuCount: 14,
      comingSoon: false,
    },
    {
      slug: 's14', vertical: 'General',
      name: 'S14',
      tagline: 'S14 string lamp replacements for commercial string light installations.',
      heroImage: '',
      skuCount: 16,
      comingSoon: false,
    },
  ],
  legacyFamilies: [],
  getStarted: {
    layoutCopy: 'Submit a fixture schedule and we return a lamp recommendation for each row.',
    sampleCopy: 'Request a physical sample of any active Nostalgic Décor family. Ships within 3 business days.',
    distributorCopy: 'Find a stocking distributor near your project site.',
    repCopy: 'Connect with a local sales rep for specification support and pricing.',
  },
  relatedCollections: [
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
export default nostalgicDecorData;
