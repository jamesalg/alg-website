/**
 * src/data/collections/multifamily.ts
 * Static data for the multi-fⒶMILY collection page.
 * Typed against CollectionPageLayout.astro Props['collection'].
 *
 * NOTE: Gehry (Commercial Recess Can) has display_echelon: null per James direction.
 */
const multifamilyData = {
  slug: 'multifamily',
  parentVertical: 'Residential',
  parentSubVertical: 'Multi-Family',
  name: 'multi-fⒶMILY',
  titleAscii: 'MULTIFAMILY',
  headlineLine: 'multi-f<span class="aa">Ⓐ</span>MILY',
  description: 'Apartment-grade downlights and ceiling-mount lighting for multi-family residential developments. 9 active families, 60 active SKUs.',
  pillRow: ['DLC PREMIUM', 'TAA AVAILABLE', '5 US WAREHOUSES', '3-DAY DELIVERY', '3 APPLICATIONS'],
  statStrip: [
    { value: '9',   label: 'Fixture Families' },
    { value: '60',  label: 'Active SKUs'       },
    { value: '3',   label: 'Applications'      },
    { value: 'DLC', label: 'Premium Listed'    },
  ],
  redBanner: [
    { value: '9',   label: 'Families'     },
    { value: '60',  label: 'Active SKUs'  },
    { value: '3',   label: 'Applications' },
    { value: 'DLC', label: 'Premium'      },
    { value: 'TAA', label: 'Available'    },
    { value: '5 US',label: 'Warehouses'   },
  ],
  applications: [
    {
      name: 'Commercial Recess Can',
      slug: 'commercial-recess-can',
      skuCount: 8,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="8" rx="8" ry="3"/><path d="M4 8v8c0 1.66 3.58 3 8 3s8-1.34 8-3V8"/></svg>',
    },
    {
      name: 'Downlight',
      slug: 'downlight',
      skuCount: 51,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="9" r="4"/><path d="M12 13v9M8 18l4 4 4-4"/></svg>',
    },
    {
      name: 'Security Flood',
      slug: 'security-flood',
      skuCount: 1,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
    },
  ],
  featured: [
    {
      family: 'Eclipse-II',
      subCategory: 'Downlight',
      displayEchelon: 'PRO' as const,
      maxWattage: null,
      skuCount: 13,
      dlc: true,
      lineDrawing: null,
    },
    {
      family: 'Nebula-II',
      subCategory: 'Downlight',
      displayEchelon: 'ECO' as const,
      maxWattage: null,
      skuCount: 12,
      dlc: false,
      lineDrawing: null,
    },
    {
      family: 'Radius SafeZone',
      subCategory: 'Downlight',
      displayEchelon: 'PRO+' as const,
      maxWattage: null,
      skuCount: 8,
      dlc: true,
      lineDrawing: null,
    },
    {
      family: 'Gehry',
      subCategory: 'Commercial Recess Can',
      displayEchelon: null,
      maxWattage: null,
      skuCount: 8,
      dlc: false,
      lineDrawing: null,
    },
    {
      family: 'Lunar Eclipse',
      subCategory: 'Downlight',
      displayEchelon: 'PRO' as const,
      maxWattage: null,
      skuCount: 3,
      dlc: true,
      lineDrawing: null,
    },
  ],
  familiesHeadline: '9 families. One multi-family portfolio.',
  familiesSubhead: 'Filter by application, echelon, wattage, CCT, and more.',
  legacy: {
    headline: 'Discontinued families.',
    body: 'Some earlier multi-fAMILY families have been discontinued. Replacement recommendations are available — contact your rep or distributor for guidance.',
    notifyLink: '/contact',
  },
  getStarted: {
    layoutCopy: 'Submit a project address and fixture list. Our team returns a complete photometric layout within 48 hours.',
    sampleCopy: 'Request a physical sample of any active multi-fAMILY family. Ships from a US warehouse within 3 business days.',
    distributorCopy: 'Find a stocking distributor near your project site. All 5 US warehouses carry core multi-fAMILY SKUs.',
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
  ],
};
export default multifamilyData;
