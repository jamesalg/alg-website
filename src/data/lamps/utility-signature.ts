/**
 * Utility sign<span class="aa">Ⓐ</span>TURE collection data
 * v2.7.0 — Bucket B lamp collection
 * CF.Collection: 'Utility sign<span class="aa">Ⓐ</span>TURE' + 'Décor sign<span class="aa">Ⓐ</span>TURE' (legacy)
 */
const utilitySignatureData = {
  slug: 'utility-signature',
  name: 'Utility sign<span class="aa">Ⓐ</span>TURE',
  titleAscii: 'Utility signATURE',
  parentVertical: 'Indoor' as const,
  parentSubVertical: 'Lamps',
  headlineLine: 'Utility sign<span class="aa">Ⓐ</span>TURE',
  description: 'Utility LED lamps for everyday replacement: A-lamps, BR floods, PAR reflectors, and HID retrofits. Broad-spectrum coverage for residential and commercial maintenance.',
  aesthetic: 'utility' as const,
  pillRow: ['A-Lamp · BR · PAR · HID', 'Utility Replacement', 'Commercial Maintenance', 'Broad Coverage'],
  families: [
    {
      slug: 'a-lamp',
      name: 'A-Lamp',
      tagline: 'A19 utility LED lamps for everyday commercial replacement.',
      heroImage: '',
      skuCount: 4,
      comingSoon: false,
    },
    {
      slug: 'br-lamp',
      name: 'BR Flood',
      tagline: 'BR40 flood lamps for recessed and track lighting.',
      heroImage: '',
      skuCount: 7,
      comingSoon: false,
    },
    {
      slug: 'par-lamp',
      name: 'PAR Reflector',
      tagline: 'PAR38 reflector lamps for outdoor and commercial applications.',
      heroImage: '',
      skuCount: 2,
      comingSoon: false,
    },
    {
      slug: 'hid-retrofit',
      name: 'HID Retrofit',
      tagline: 'HID retrofit lamps for metal halide and high-pressure sodium fixtures.',
      heroImage: '',
      skuCount: 0,
      comingSoon: true,
    },
  ],
  legacyFamilies: [
    {
      slug: 'husk-series',
      name: 'Husk Series',
      tagline: 'Discontinued wattage-selectable HID retrofit lamps.',
      heroImage: '',
      skuCount: 7,
    },
  ],
  getStarted: {
    layoutCopy: 'Submit a fixture schedule and we return a utility lamp recommendation for each row.',
    sampleCopy: 'Request a physical sample of any active Utility sign<span class="aa">Ⓐ</span>TURE family. Ships within 3 business days.',
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
    },
  ],
};
export default utilitySignatureData;
