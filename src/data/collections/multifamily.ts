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
  description: 'Multifamily, garden-style, and mid-rise developments need lighting that works on a per-door budget — and still passes the code inspector on the first walk-through. multi-f<span class="aa">Ⓐ</span>MILY is the ALG line that ships value-engineered ECO and code-compliant PRO downlights, hallway fixtures, and unit basics with the per-door affordability developers run on.',
  pillRow: ['VALUE-ENGINEERED', 'CODE-COMPLIANT', 'JA8 / TITLE 24', '48-HR LAYOUTS', '5-YR WARRANTY'],
  statStrip: [
    { value: '~$12',label: '/ door' },
    { value: '5-yr',label: 'Warranty' },
    { value: 'JA8', label: 'Title 24' },
    { value: '48-hr',label: 'Layouts' },
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
      name: 'Common Areas',
      slug: 'common-areas',
      skuCount: 15,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M12 12v10M8 18l4 4 4-4"/></svg>',
    },
    {
      name: 'Inside the unit',
      slug: 'inside-the-unit',
      skuCount: 41,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M12 12v10M8 18l4 4 4-4"/></svg>',
    },
    {
      name: 'Code & Inspection',
      slug: 'code-and-inspection',
      skuCount: 4,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 3"/></svg>',
    },
  ],
  featured: [
    {
      family: 'Nebula-II',
      subCategory: 'Commercial Recess Can',
      displayEchelon: 'ECO' as const,
      maxWattage: 20,
      skuCount: 12,
      dlc: true,
      lineDrawing: null,
    },
    {
      family: 'Eclipse-II',
      subCategory: 'Downlight',
      displayEchelon: 'PRO' as const,
      maxWattage: 18,
      skuCount: 16,
      dlc: true,
      lineDrawing: null,
    },
    {
      family: 'Radius SafeZone',
      subCategory: 'Hallway / Common Area',
      displayEchelon: 'PRO' as const,
      maxWattage: 15,
      skuCount: 4,
      dlc: true,
      lineDrawing: null,
    },
  ],
  familiesHeadline: 'Lighting for the buildings people live in.',
  familiesSubhead: 'Multifamily, garden-style, and mid-rise developments need lighting that works on a per-door budget — and still passes the code inspector on the first walk-through.',
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
