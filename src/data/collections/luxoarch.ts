/**
 * src/data/collections/luxoarch.ts
 * Static data for the luxoⒶRCH collection page.
 * Typed against CollectionPageLayout.astro Props['collection'].
 */

const luxoarchData = {
  slug: 'luxoarch',
  parentVertical: 'Outdoor',
  parentSubVertical: 'Commercial',
  name: 'luxoⒶRCH',
  titleAscii: 'LUXOARCH',
  headlineLine: 'luxo<span class="aa">Ⓐ</span>RCH',
  description: 'Outdoor lighting for the commercial perimeter. 22 active families, 142 active SKUs.',
  pillRow: ['DLC PREMIUM', 'TAA AVAILABLE', '5 US WAREHOUSES', '3-DAY DELIVERY', '8 APPLICATIONS'],
  statStrip: [
    { value: '22',  label: 'Fixture Families' },
    { value: '142', label: 'Active SKUs'       },
    { value: '8',   label: 'Applications'      },
    { value: 'DLC', label: 'Premium Listed'    },
  ],
  redBanner: [
    { value: '22',  label: 'Families'     },
    { value: '142', label: 'Active SKUs'  },
    { value: '8',   label: 'Applications' },
    { value: 'DLC', label: 'Premium'      },
    { value: 'TAA', label: 'Available'    },
    { value: '5 US',label: 'Warehouses'   },
  ],
  applications: [
    {
      name: 'Area Light',
      slug: 'area-light',
      skuCount: 29,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>',
    },
    {
      name: 'Canopy',
      slug: 'canopy',
      skuCount: 7,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2C6.48 2 2 6.48 2 12h20c0-5.52-4.48-10-10-10z"/><line x1="12" y1="12" x2="12" y2="22"/></svg>',
    },
    {
      name: 'Cylinder',
      slug: 'cylinder',
      skuCount: 4,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14c0 1.66 4.03 3 9 3s9-1.34 9-3V5"/></svg>',
    },
    {
      name: 'Dock Light',
      slug: 'dock-light',
      skuCount: 2,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M12 2v4M12 18v4M4.22 4.22l2.83 2.83M16.95 16.95l2.83 2.83M2 12h4M18 12h4M4.22 19.78l2.83-2.83M16.95 7.05l2.83-2.83"/></svg>',
    },
    {
      name: 'Flood Light',
      slug: 'flood-light',
      skuCount: 8,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
    },
    {
      name: 'Sports Lighting',
      slug: 'sports-lighting',
      skuCount: 27,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>',
    },
    {
      name: 'String Light',
      slug: 'string-light',
      skuCount: 19,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7c3-2 6-2 9 0s6 2 9 0"/><path d="M3 17c3-2 6-2 9 0s6 2 9 0"/><line x1="6" y1="7" x2="6" y2="17"/><line x1="12" y1="7" x2="12" y2="17"/><line x1="18" y1="7" x2="18" y2="17"/></svg>',
    },
    {
      name: 'Wall Pack',
      slug: 'wall-pack',
      skuCount: 46,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 9h6M9 12h6M9 15h4"/></svg>',
    },
  ],
  featured: [
    {
      family: 'Aura',
      subCategory: 'Cylinder',
      displayEchelon: 'PRO' as const,
      maxWattage: 45,
      skuCount: 4,
      dlc: true,
      lineDrawing: null,
    },
    {
      family: 'Illuminator',
      subCategory: 'Sports Lighting',
      displayEchelon: 'PRO' as const,
      maxWattage: 800,
      skuCount: 11,
      dlc: true,
      lineDrawing: null,
    },
    {
      family: 'Liberty',
      subCategory: 'Area Light',
      displayEchelon: 'PRO' as const,
      maxWattage: 450,
      skuCount: 25,
      dlc: true,
      lineDrawing: null,
    },
    {
      family: 'Nightwatch',
      subCategory: 'Wall Pack',
      displayEchelon: 'PRO' as const,
      maxWattage: null,
      skuCount: 4,
      dlc: true,
      lineDrawing: null,
    },
    {
      family: 'Sentinel',
      subCategory: 'Wall Pack',
      displayEchelon: 'PRO' as const,
      maxWattage: null,
      skuCount: 4,
      dlc: true,
      lineDrawing: null,
    },
  ],
  familiesHeadline: '22 families. One outdoor portfolio.',
  familiesSubhead: 'Filter by application, echelon, wattage, CCT, and more.',
  legacy: {
    headline: 'Discontinued families.',
    body: 'Some earlier LUXOARCH families have been discontinued. Replacement recommendations are available — contact your rep or distributor for guidance.',
    notifyLink: '/contact',
  },
  getStarted: {
    layoutCopy: 'Submit a project address and fixture list. Our team returns a complete photometric layout within 48 hours.',
    sampleCopy: 'Request a physical sample of any active LUXOARCH family. Ships from a US warehouse within 3 business days.',
    distributorCopy: 'Find a stocking distributor near your project site. All 5 US warehouses carry core LUXOARCH SKUs.',
    repCopy: 'Connect with a local sales rep for specification support, pricing, and project tracking.',
  },
  relatedCollections: [
    {
      slug: 'planoarch',
      name: 'plano<span class="aa">Ⓐ</span>RCH',
      vertical: 'Indoor',
      description: 'Commercial indoor lighting for offices, retail, and healthcare.',
      status: 'live' as const,
    },
    {
      slug: 'lampararch',
      name: 'lampar<span class="aa">Ⓐ</span>RCH',
      vertical: 'Industrial',
      description: 'Industrial lighting for warehouses and manufacturing.',
      status: 'live' as const,
    },
    {
      slug: 'cityarch',
      name: 'city<span class="aa">Ⓐ</span>RCH',
      vertical: 'Municipal',
      description: 'Street and area lighting for municipal and utility applications.',
      status: 'live' as const,
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

export default luxoarchData;
