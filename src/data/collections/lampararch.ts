/**
 * src/data/collections/lampararch.ts
 * Static data for the lamparⒶRCH collection page.
 * Typed against CollectionPageLayout.astro Props['collection'].
 */
const lampararchData = {
  slug: 'lampararch',
  parentVertical: 'Indoor',
  parentSubVertical: 'Industrial',
  name: 'lamparⒶRCH',
  titleAscii: 'LAMPARARCH',
  headlineLine: 'lampar<span class="aa">Ⓐ</span>RCH',
  description: 'Industrial lighting for warehouses, manufacturing, and high-bay environments. 9 active families, 102 active SKUs.',
  pillRow: ['DLC PREMIUM', 'TAA AVAILABLE', '5 US WAREHOUSES', '3-DAY DELIVERY', '2 APPLICATIONS'],
  statStrip: [
    { value: '9',   label: 'Fixture Families' },
    { value: '102', label: 'Active SKUs'       },
    { value: '2',   label: 'Applications'      },
    { value: 'DLC', label: 'Premium Listed'    },
  ],
  redBanner: [
    { value: '9',   label: 'Families'     },
    { value: '102', label: 'Active SKUs'  },
    { value: '2',   label: 'Applications' },
    { value: 'DLC', label: 'Premium'      },
    { value: 'TAA', label: 'Available'    },
    { value: '5 US',label: 'Warehouses'   },
  ],
  applications: [
    {
      name: 'High-Bay',
      slug: 'high-bay',
      skuCount: 56,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="10" r="4"/><path d="M12 2v2M12 18v4M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M2 10h2M20 10h2M4.22 15.78l1.42-1.42M18.36 5.64l1.42-1.42"/><path d="M8 14l-2 6h12l-2-6"/></svg>',
    },
    {
      name: 'Linear Strip',
      slug: 'linear-strip',
      skuCount: 46,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="8" width="20" height="8" rx="1"/><line x1="6" y1="8" x2="6" y2="16"/><line x1="12" y1="8" x2="12" y2="16"/><line x1="18" y1="8" x2="18" y2="16"/></svg>',
    },
  ],
  featured: [
    {
      family: 'Hallmark',
      subCategory: 'Linear Strip',
      displayEchelon: 'PRO+' as const,
      maxWattage: null,
      skuCount: 30,
      dlc: true,
      lineDrawing: null,
    },
    {
      family: 'Titan-II',
      subCategory: 'High-Bay',
      displayEchelon: 'PRO' as const,
      maxWattage: null,
      skuCount: 20,
      dlc: true,
      lineDrawing: null,
    },
    {
      family: 'Icarus-III',
      subCategory: 'High-Bay',
      displayEchelon: 'ECO' as const,
      maxWattage: null,
      skuCount: 12,
      dlc: false,
      lineDrawing: null,
    },
    {
      family: 'Jupiter-II',
      subCategory: 'High-Bay',
      displayEchelon: 'PRO' as const,
      maxWattage: null,
      skuCount: 12,
      dlc: false,
      lineDrawing: null,
    },
    {
      family: 'Vanguard-I',
      subCategory: 'Linear Strip',
      displayEchelon: 'ECO' as const,
      maxWattage: null,
      skuCount: 9,
      dlc: false,
      lineDrawing: null,
    },
  ],
  familiesHeadline: '9 families. One industrial portfolio.',
  familiesSubhead: 'Filter by application, echelon, wattage, CCT, and more.',
  legacy: {
    headline: 'Discontinued families.',
    body: 'Some earlier LAMPARARCH families have been discontinued. Industrial linear high-bay and low-bay luminaires. Replacement recommendations are available — contact your rep or distributor for guidance.',
    notifyLink: '/contact',
  },
  getStarted: {
    layoutCopy: 'Submit a project address and fixture list. Our team returns a complete photometric layout within 48 hours.',
    sampleCopy: 'Request a physical sample of any active LAMPARARCH family. Ships from a US warehouse within 3 business days.',
    distributorCopy: 'Find a stocking distributor near your project site. All 5 US warehouses carry core LAMPARARCH SKUs.',
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
      slug: 'luxoarch',
      name: 'luxo<span class="aa">Ⓐ</span>RCH',
      vertical: 'Outdoor',
      description: 'Outdoor lighting for the commercial perimeter.',
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
      slug: 'tubulararch',
      name: 'tubul<span class="aa">Ⓐ</span>RCH',
      vertical: 'Industrial',
      description: 'High-bay and low-bay lighting for industrial and warehouse spaces.',
      status: 'coming-soon' as const,
    },
  ],
};
export default lampararchData;
