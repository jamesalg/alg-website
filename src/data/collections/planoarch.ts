/**
 * src/data/collections/planoarch.ts
 * Static data for the planoⒶRCH collection page.
 * Typed against CollectionPageLayout.astro Props['collection'].
 */

const planoarchData = {
  slug: 'planoarch',
  parentVertical: 'Indoor',
  parentSubVertical: 'Commercial',
  name: 'planoⒶRCH',
  titleAscii: 'PLANOARCH',
  headlineLine: 'PLANO<span class="aa">Ⓐ</span>RCH',
  description: 'Commercial indoor lighting for offices, retail, and healthcare. 15 active families, 125 active SKUs.',
  pillRow: ['DLC PREMIUM', 'TAA AVAILABLE', '5 US WAREHOUSES', '3-DAY DELIVERY', '8 APPLICATIONS'],
  statStrip: [
    { value: '15',  label: 'Fixture Families' },
    { value: '125', label: 'Active SKUs'       },
    { value: '8',   label: 'Applications'      },
    { value: 'DLC', label: 'Premium Listed'    },
  ],
  redBanner: [
    { value: '15',  label: 'Families'     },
    { value: '125', label: 'Active SKUs'  },
    { value: '8',   label: 'Applications' },
    { value: 'DLC', label: 'Premium'      },
    { value: 'TAA', label: 'Available'    },
    { value: '5 US',label: 'Warehouses'   },
  ],
  applications: [
    {
      name: 'Architectural Linear',
      slug: 'architectural-linear',
      skuCount: 11,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="9" width="20" height="6" rx="1"/></svg>',
    },
    {
      name: 'Downlight',
      slug: 'downlight',
      skuCount: 41,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M12 12v10M8 18l4 4 4-4"/></svg>',
    },
    {
      name: 'Panel',
      slug: 'panel',
      skuCount: 19,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="3" y1="15" x2="21" y2="15"/><line x1="9" y1="3" x2="9" y2="21"/><line x1="15" y1="3" x2="15" y2="21"/></svg>',
    },
    {
      name: 'Retrofit Panel',
      slug: 'retrofit-panel',
      skuCount: 6,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 9l6 6M15 9l-6 6"/></svg>',
    },
    {
      name: 'Retrofit Troffer',
      slug: 'retrofit-troffer',
      skuCount: 6,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="6" width="20" height="12" rx="2"/><line x1="2" y1="12" x2="22" y2="12"/></svg>',
    },
    {
      name: 'Track Light',
      slug: 'track-light',
      skuCount: 4,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><line x1="2" y1="6" x2="22" y2="6"/><circle cx="8" cy="6" r="2"/><circle cx="16" cy="6" r="2"/><path d="M8 8v6l-2 4M16 8v6l2 4"/></svg>',
    },
    {
      name: 'Troffer',
      slug: 'troffer',
      skuCount: 21,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="5" width="20" height="14" rx="2"/><line x1="2" y1="12" x2="22" y2="12"/><line x1="12" y1="5" x2="12" y2="19"/></svg>',
    },
    {
      name: 'Wraparound',
      slug: 'wraparound',
      skuCount: 17,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6h16a2 2 0 012 2v8a2 2 0 01-2 2H4a2 2 0 01-2-2V8a2 2 0 012-2z"/><path d="M4 6c0-1.1.9-2 2-2h12a2 2 0 012 2"/></svg>',
    },
  ],
  featured: [
    {
      family: 'Astra',
      subCategory: 'Downlight',
      displayEchelon: 'PRO+' as const,
      maxWattage: 18,
      skuCount: 27,
      dlc: true,
      lineDrawing: null,
    },
    {
      family: 'Luna',
      subCategory: 'Architectural Linear',
      displayEchelon: 'PRO+' as const,
      maxWattage: 50,
      skuCount: 5,
      dlc: true,
      lineDrawing: null,
    },
    {
      family: 'Luxmark',
      subCategory: 'Troffer',
      displayEchelon: 'PRO+' as const,
      maxWattage: 35,
      skuCount: 6,
      dlc: true,
      lineDrawing: null,
    },
    {
      family: 'proARCH-III',
      subCategory: 'Panel',
      displayEchelon: 'PRO+' as const,
      maxWattage: 30,
      skuCount: 13,
      dlc: true,
      lineDrawing: null,
    },
    {
      family: 'Trackstar',
      subCategory: 'Track Light',
      displayEchelon: 'ECO' as const,
      maxWattage: 20,
      skuCount: 4,
      dlc: false,
      lineDrawing: null,
    },
  ],
  familiesHeadline: '15 families. One indoor portfolio.',
  familiesSubhead: 'Filter by application, echelon, wattage, CCT, and more.',
  legacy: {
    headline: 'Discontinued families.',
    body: 'Some earlier PLANOARCH families have been discontinued. Replacement recommendations are available — contact your rep or distributor for guidance.',
    notifyLink: '/contact',
  },
  getStarted: {
    layoutCopy: 'Submit a project address and fixture list. Our team returns a complete photometric layout within 48 hours.',
    sampleCopy: 'Request a physical sample of any active PLANOARCH family. Ships from a US warehouse within 3 business days.',
    distributorCopy: 'Find a stocking distributor near your project site. All 5 US warehouses carry core PLANOARCH SKUs.',
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
      slug: 'lampararch',
      name: 'lampar<span class="aa">Ⓐ</span>RCH',
      vertical: 'Lamp',
      description: 'LED lamp replacements for commercial retrofit.',
      status: 'coming-soon' as const,
    },
    {
      slug: 'cityarch',
      name: 'city<span class="aa">Ⓐ</span>RCH',
      vertical: 'Municipal',
      description: 'Street and area lighting for municipal and utility applications.',
      status: 'coming-soon' as const,
    },
    {
      slug: 'tubularch',
      name: 'tubul<span class="aa">Ⓐ</span>RCH',
      vertical: 'Industrial',
      description: 'High-bay and low-bay lighting for industrial and warehouse spaces.',
      status: 'coming-soon' as const,
    },
  ],
};

export default planoarchData;
