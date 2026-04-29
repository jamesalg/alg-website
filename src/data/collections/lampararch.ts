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
  description: 'Linear high-bay, low-bay, vapor-tight, and linear strip — DLC Premium-listed across the catalog, project-specified for warehouse, manufacturing, and distribution-center installs where lumen efficiency and 80,000+ hours of L80 matter. lamparⒶRCH is the ALG line that ships when the photometric layout is the conversation.',
  pillRow: ['DLC PREMIUM', 'HIGH LUMEN EFFICIENCY', 'LONG PHOTOMETRIC THROW', 'PROJECT-SPECIFIED', '80,000-HR L80'],
  statStrip: [
    { value: '88.5k',label: 'up to lm' },
    { value: '150', label: 'lm/W' },
    { value: '80k-hr',label: 'L80' },
    { value: '48-hr',label: 'Layouts' },
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
      name: 'Warehouse & Distribution',
      slug: 'warehouse-distribution',
      skuCount: 56,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="10" r="4"/><path d="M12 2v2M12 18v4M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M2 10h2M20 10h2M4.22 15.78l1.42-1.42M18.36 5.64l1.42-1.42"/><path d="M8 14l-2 6h12l-2-6"/></svg>',
    },
    {
      name: 'Manufacturing',
      slug: 'manufacturing',
      skuCount: 46,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="8" width="20" height="8" rx="1"/><line x1="6" y1="8" x2="6" y2="16"/><line x1="12" y1="8" x2="12" y2="16"/><line x1="18" y1="8" x2="18" y2="16"/></svg>',
    },
    {
      name: 'Big-box retail / commercial',
      slug: 'big-box-retail',
      skuCount: 15,
      icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="3" y1="15" x2="21" y2="15"/><line x1="9" y1="3" x2="9" y2="21"/><line x1="15" y1="3" x2="15" y2="21"/></svg>',
    },
  ],
  featured: [
    {
      family: 'Titan-II',
      subCategory: 'Linear High-Bay',
      displayEchelon: 'PRO+' as const,
      maxWattage: 600,
      skuCount: 20,
      dlc: true,
      lineDrawing: null,
    },
    {
      family: 'Jupiter-II',
      subCategory: 'Linear Low-Bay',
      displayEchelon: 'PRO' as const,
      maxWattage: 200,
      skuCount: 12,
      dlc: true,
      lineDrawing: null,
    },
    {
      family: 'Icarus-III',
      subCategory: 'Vapor Tight',
      displayEchelon: 'PRO' as const,
      maxWattage: 150,
      skuCount: 12,
      dlc: true,
      lineDrawing: null,
    },
  ],
  familiesHeadline: 'The PRO line that earns the warehouse.',
  familiesSubhead: 'Linear high-bay, low-bay, vapor-tight, and linear strip — DLC Premium-listed across the catalog, project-specified for warehouse, manufacturing, and distribution-center installs.',
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
