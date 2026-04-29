/**
 * src/data/collections/tubularch.ts
 * Static data for the tubulⒶRCH collection page.
 * Route: /collections/tubularch/
 * Typed against CollectionPageLayout.astro Props['collection'].
 */
const tubularchData = {
  slug: 'tubularch',
  parentVertical: 'Décor',
  parentSubVertical: 'Heritage',
  name: 'tubul<span class="aa">Ⓐ</span>RCH',
  titleAscii: 'TUBULARCH',
  headlineLine: 'tubul<span class="aa">Ⓐ</span>RCH',
  description: 'Tubular and radio-tube filament LEDs. The lamps that finish the room.',
  pillRow: ['CRI 90+', 'DIMMABLE TO 5%', 'TRIAC + ELV VERIFIED', '25,000-HR L80', 'HERITAGE BINNED'],
  statStrip: [
    { value: '2200K–2700K', label: 'Candle-hour register' },
    { value: 'CRI 90+',     label: 'Color fidelity'       },
    { value: '25,000-hr',   label: 'L80 rated life'       },
    { value: 'Dim to 5%',   label: 'TRIAC + ELV verified' },
  ],
  redBanner: [
    { value: '4',      label: 'Tube Families'    },
    { value: 'CRI 90+', label: 'Color Fidelity'  },
    { value: '2200K',   label: 'Candle-hour'     },
    { value: '5%',      label: 'Dim Floor'       },
    { value: 'T9–T14',  label: 'Envelopes'       },
    { value: 'E26',     label: 'Base'            },
  ],
  applications: [
    {
      name: 'Salon Bars + Craft Cocktail',
      slug: 'salon-bar',
      skuCount: 12,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M8 3H5a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2V5a2 2 0 00-2-2h-3"/><rect x="8" y="3" width="8" height="4" rx="1"/><path d="M12 11v6M9 14h6"/></svg>',
    },
    {
      name: 'Period Restoration',
      slug: 'period-restoration',
      skuCount: 18,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>',
    },
    {
      name: 'Bespoke Sconces + Arrays',
      slug: 'bespoke-sconce',
      skuCount: 8,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>',
    },
  ],
  featured: [
    {
      family: 'The Brighton Tubular T9',
      subCategory: 'Tubular',
      displayEchelon: 'PRO' as const,
      maxWattage: 6,
      skuCount: 8,
      dlc: false,
      lineDrawing: null,
    },
    {
      family: 'The Marconi Radio T10',
      subCategory: 'Radio Tube',
      displayEchelon: 'PRO' as const,
      maxWattage: 8,
      skuCount: 6,
      dlc: false,
      lineDrawing: null,
    },
    {
      family: 'The Volta T14',
      subCategory: 'Long-form Tubular',
      displayEchelon: 'PRO' as const,
      maxWattage: 8,
      skuCount: 4,
      dlc: false,
      lineDrawing: null,
    },
  ],
  familiesHeadline: '4 tube families. One heritage portfolio.',
  familiesSubhead: 'T9, T10, T14, and PL long-form filament envelopes — dimmer-verified, heritage-binned.',
  legacy: {
    headline: 'Discontinued tube families.',
    body: 'Earlier tubul<span class="aa">Ⓐ</span>RCH families have been phased out. Replacement recommendations available — contact your rep.',
    notifyLink: '/contact',
  },
  getStarted: {
    layoutCopy: 'Submit your project details. Our team returns a lamp specification within 24 hours.',
    sampleCopy: 'Request a physical sample of any active tubul<span class="aa">Ⓐ</span>RCH family. Ships from a US warehouse within 3 business days.',
    distributorCopy: 'Find a stocking distributor near your project site.',
    repCopy: 'Connect with a local sales rep for specification support and project tracking.',
  },
  relatedCollections: [
    {
      slug: 'vintage-decor',
      name: 'Vintage Décor',
      vertical: 'Décor',
      description: 'ST19, ST21, and round-envelope filament LEDs for heritage hospitality.',
      status: 'live' as const,
    },
    {
      slug: 'nostalgic-decor',
      name: 'Nostalgic Décor',
      vertical: 'Décor',
      description: 'A19, B10, CA10 and other classic shapes in the Nostalgic register.',
      status: 'live' as const,
    },
    {
      slug: 'lamparch',
      name: 'lampar<span class="aa">Ⓐ</span>RCH',
      vertical: 'Industrial',
      description: 'High-bay and linear strip for warehouses and manufacturing.',
      status: 'live' as const,
    },
  ],
};
export default tubularchData;
