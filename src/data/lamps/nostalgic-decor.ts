/**
 * Nostalgic Décor collection data
 * v2.7.0 — Bucket B lamp collection
 * CF.Collection: 'Décor nost<span class="aa">Ⓐ</span>LGIC'
 */
const nostalgicDecorData = {
  slug: 'nostalgic-decor',
  name: 'Nostalgic Décor',
  titleAscii: 'Nostalgic Decor',
  parentVertical: 'Indoor' as const,
  parentSubVertical: 'Lamps',
  headlineLine: 'Nostalgic Décor',
  description: 'Classic filament-style LED lamps. A-lamps, globe shapes, candelabra, and S14 string lamp replacements with warm amber glow. Dimmable, long-life, energy-efficient.',
  aesthetic: 'nostalgic' as const,
  pillRow: ['A-Lamp · Globe · Candle · S14', 'Warm Amber Glow', 'Dimmable', 'Long Life'],
  families: [
    {
      slug: 'a-lamp',
      name: 'A-Lamp',
      tagline: 'Classic A19 and A21 shapes with nostalgic frosted or silver-tip finish.',
      heroImage: '',
      skuCount: 39,
      comingSoon: false,
    },
    {
      slug: 'candle-blunt-tip',
      name: 'Candle (Blunt-Tip)',
      tagline: 'B10 blunt-tip candelabra lamps for chandeliers and sconces.',
      heroImage: '',
      skuCount: 33,
      comingSoon: false,
    },
    {
      slug: 'candle-flame-tip',
      name: 'Candle (Flame-Tip)',
      tagline: 'CA10 flame-tip candelabra lamps for decorative fixtures.',
      heroImage: '',
      skuCount: 22,
      comingSoon: false,
    },
    {
      slug: 'globe',
      name: 'Globe',
      tagline: 'G40 globe lamps for vanity and pendant applications.',
      heroImage: '',
      skuCount: 3,
      comingSoon: false,
    },
    {
      slug: 'globe-g16-5',
      name: 'Globe G16.5',
      tagline: 'G16.5 small globe lamps for bathroom vanity strips.',
      heroImage: '',
      skuCount: 23,
      comingSoon: false,
    },
    {
      slug: 'globe-g25',
      name: 'Globe G25',
      tagline: 'G25 medium globe lamps for vanity and decorative pendants.',
      heroImage: '',
      skuCount: 11,
      comingSoon: false,
    },
    {
      slug: 's14',
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
