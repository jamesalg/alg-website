/**
 * scripts/build-sku-index.mjs
 *
 * v2.7.1 — collection-aware family resolution for Bucket B lamp collections.
 *
 * Reads data/Item.xlsx (Zoho export) and emits src/data/sku-index.json
 * for use by CollectionAllFamilies.astro and LampFamilyDetailPageLayout.astro.
 *
 * Relevant Item.xlsx columns (1-indexed):
 *   24  Status
 *   56  CF.Wattage (W):
 *   84  CF.Collection
 *   85  CF.Commercial Grade
 *   88  CF.Family
 *
 * Bucket B collections and their family-resolution strategy:
 *   tubulⒶRCH       → shape from CF.Commercial Grade (T5/T5HE/T5HO/T8/PL/PLL/U6)
 *                       UL tier from CF.Family (UL-A / UL A+B / UL-B)
 *   Décor nostⒶLGIC → shape from CF.Commercial Grade; A-Lamp split by wattage threshold
 *   Décor vintⒶGE   → shape from CF.Commercial Grade (direct 1:1)
 *   Utility signⒶTURE → family from CF.Family (A-Lamp / BR-Lamp / Husk Series / PAR-Lamp)
 *   Décor signⒶTURE → EXCLUDED (discontinued line per James direction)
 *
 * Bucket A collections (luxoarch, planoarch) still read from
 * data/SKU_Attributes_Template_v1.xlsx (legacy path, unchanged).
 */

import { writeFileSync, mkdirSync, existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import XLSX from 'xlsx';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..');

const XLSX_PATH_A = join(ROOT, 'data', 'SKU_Attributes_Template_v1.xlsx');
const XLSX_PATH_B = join(ROOT, 'data', 'Item.xlsx');
const OUT_PATH    = join(ROOT, 'src', 'data', 'sku-index.json');

// Collections to exclude entirely (discontinued)
const EXCLUDED_COLLECTIONS = new Set(['Décor signⒶTURE']);

// Coming-soon families — SKUs count toward collection total but don't render in detail pages
const COMING_SOON_FAMILIES = new Set([
  'utility-signature/a-lamp',
  'utility-signature/br-lamp',
  'utility-signature/par-lamp',
]);

// ── helpers ───────────────────────────────────────────────────────────────────
function parsePipeList(val) {
  if (!val || String(val).trim() === '' || String(val).trim() === 'n/a') return [];
  return String(val).split('|').map(s => s.trim()).filter(Boolean);
}
function parseDlc(dlcListing) {
  if (!dlcListing) return null;
  const tokens = String(dlcListing).split(',').map(s => s.trim());
  const dlcToken = tokens.find(t => t.startsWith('DLC'));
  if (!dlcToken) return null;
  if (dlcToken.includes('Premium')) return 'Premium';
  if (dlcToken.includes('Standard')) return 'Standard';
  return null;
}
function parseWattages(val) {
  return parsePipeList(val)
    .map(s => parseInt(s.replace(/W$/i, ''), 10))
    .filter(n => !isNaN(n));
}
function parseMountTypes(val) {
  if (!val || String(val).trim() === '' || String(val).trim() === 'n/a') return [];
  return String(val).split(' | ').map(s => s.trim()).filter(Boolean);
}
function parseTaa(val) {
  if (typeof val === 'boolean') return val;
  if (typeof val === 'string') return val.toUpperCase() === 'TRUE';
  return false;
}
function collectionSlug(raw) {
  return raw.replace(/Ⓐ/g, 'a').replace(/RCH/g, 'rch').toLowerCase().replace(/[^a-z]/g, '');
}

// ── Bucket B: Nostalgic shape map ─────────────────────────────────────────────
function nostalgicShapeMap(commercialGrade, wattageStr) {
  if (commercialGrade === 'A-Lamp') {
    const watt = parseFloat(wattageStr || '0');
    return watt < 5 ? 'a15' : 'a19';
  }
  const directMap = {
    'Candle | Blunt-Tip': 'b10',
    'Candle | Flame-Tip': 'ca10',
    'Globe G16.5':        'g16-5',
    'Globe G25':          'g25',
    'Globe':              'g25',
    'Globe 40':           'g25',
    'S14':                's14',
  };
  if (directMap[commercialGrade]) return directMap[commercialGrade];
  console.warn(`[BUCKET-B] Unmapped Nostalgic Décor commercial_grade: '${commercialGrade}'`);
  return null;
}

// ── Bucket B: collection-aware family resolution ──────────────────────────────
function resolveFamily(collRaw, commGrade, cfFamily, wattageStr) {
  switch (collRaw) {
    case 'tubulⒶRCH': {
      const rolledUp = ['T5HE', 'T5HO'].includes(commGrade) ? 'T5' : commGrade;
      const familySlug = rolledUp.toLowerCase();
      const tier = cfFamily ? cfFamily.replace('UL A+B', 'UL-A+B').trim() : null;
      return { familySlug, capabilityTier: tier, rawShape: commGrade };
    }
    case 'Décor nostⒶLGIC': {
      const slug = nostalgicShapeMap(commGrade, wattageStr);
      return { familySlug: slug, capabilityTier: null, rawShape: commGrade };
    }
    case 'Décor vintⒶGE': {
      const vintMap = {
        'Candle':    'candelabra',
        'Edison':    'edison',
        'Globe':     'globe',
        'Radio':     'radio',
        'Tubular':   'tubular',
        'Victorian': 'victorian',
      };
      const slug = vintMap[commGrade] || commGrade.toLowerCase();
      return { familySlug: slug, capabilityTier: null, rawShape: commGrade };
    }
    case 'Utility signⒶTURE': {
      const famMap = {
        'A-Lamp':      'a-lamp',
        'BR-Lamp':     'br-lamp',
        'PAR-Lamp':    'par-lamp',
        'Husk Series': 'husk-hid',
      };
      const slug = famMap[cfFamily] || null;
      return { familySlug: slug, capabilityTier: null, rawShape: commGrade };
    }
    default:
      return { familySlug: null, capabilityTier: null, rawShape: commGrade };
  }
}

// ── Bucket A: build collection output from rows ───────────────────────────────
function buildCollectionOutput(skus) {
  const familyMap = {};
  for (const sku of skus) {
    const key = sku.family;
    if (!familyMap[key]) {
      familyMap[key] = {
        family: sku.family, sub_category: sku.sub_category,
        display_echelon: sku.display_echelon, max_wattage: 0, sku_count: 0,
        dlc: false, ccts: new Set(), voltages: new Set(), mount_types: new Set(), taa: false,
      };
    }
    const fam = familyMap[key];
    fam.sku_count++;
    if (sku.wattages.length) {
      const maxW = Math.max(...sku.wattages);
      if (maxW > fam.max_wattage) fam.max_wattage = maxW;
    }
    if (sku.dlc) fam.dlc = true;
    if (sku.taa) fam.taa = true;
    sku.ccts.forEach(c => fam.ccts.add(c));
    if (sku.voltage) fam.voltages.add(sku.voltage);
    sku.mount_types.forEach(m => fam.mount_types.add(m));
  }
  const families = Object.values(familyMap).map(f => ({
    family: f.family, sub_category: f.sub_category, display_echelon: f.display_echelon,
    max_wattage: f.max_wattage, sku_count: f.sku_count, dlc: f.dlc,
    ccts: [...f.ccts].sort(), voltages: [...f.voltages].sort(),
    mount_types: [...f.mount_types].sort(), taa: f.taa,
  }));
  const TIER = { ECO: 0, PRO: 1, 'PRO+': 2 };
  families.sort((a, b) => {
    const sd = a.sub_category.localeCompare(b.sub_category);
    if (sd !== 0) return sd;
    const td = (TIER[a.display_echelon] ?? 99) - (TIER[b.display_echelon] ?? 99);
    return td !== 0 ? td : a.family.localeCompare(b.family);
  });
  return { skus, families };
}

// ── Read Bucket A ─────────────────────────────────────────────────────────────
let collectionsA = {};
if (existsSync(XLSX_PATH_A)) {
  const wbA = XLSX.readFile(XLSX_PATH_A);
  const wsA = wbA.Sheets[wbA.SheetNames[0]];
  const rowsA = XLSX.utils.sheet_to_json(wsA, { header: 1, defval: '' });
  const dataRowsA = rowsA.slice(2);
  const byCollA = {};
  for (const row of dataRowsA) {
    const collRaw = String(row[0]).trim();
    if (!collRaw) continue;
    const slug = collectionSlug(collRaw);
    if (!byCollA[slug]) byCollA[slug] = [];
    byCollA[slug].push({
      sku: String(row[3]).trim(), family: String(row[2]).trim(),
      sub_category: String(row[1]).trim(), display_echelon: String(row[6]).trim(),
      wattages: parseWattages(row[7]), ccts: parsePipeList(row[8]),
      voltage: String(row[9]).trim(), mount_types: parseMountTypes(row[13]),
      dlc: parseDlc(row[15]), taa: parseTaa(row[16]),
    });
  }
  for (const [slug, skus] of Object.entries(byCollA)) {
    collectionsA[slug] = buildCollectionOutput(skus);
  }
}

// ── Read Bucket B ─────────────────────────────────────────────────────────────
let collectionsB = {};
if (existsSync(XLSX_PATH_B)) {
  const wbB = XLSX.readFile(XLSX_PATH_B);
  const wsB = wbB.Sheets[wbB.SheetNames[0]];
  const rowsB = XLSX.utils.sheet_to_json(wsB, { header: 1, defval: '' });

  const hdrs = rowsB[0];
  const ci = {};
  hdrs.forEach((h, i) => { if (h) ci[String(h).trim()] = i; });

  const STATUS_COL    = ci['Status']               ?? 23;
  const WATTAGE_COL   = ci['CF.Wattage (W):']      ?? 55;
  const COLL_COL      = ci['CF.Collection']         ?? 83;
  const COMMGRADE_COL = ci['CF.Commercial Grade']   ?? 84;
  const FAMILY_COL    = ci['CF.Family']             ?? 87;
  const ITEM_NAME_COL = ci['Item Name']             ?? 0;

  const BUCKET_B = new Set(['tubulⒶRCH', 'Décor nostⒶLGIC', 'Décor vintⒶGE', 'Utility signⒶTURE']);

  const byCollB = {};
  for (const row of rowsB.slice(1)) {
    const collRaw = String(row[COLL_COL] ?? '').trim();
    if (!collRaw) continue;
    if (EXCLUDED_COLLECTIONS.has(collRaw)) continue;
    if (!BUCKET_B.has(collRaw)) continue;
    const status = String(row[STATUS_COL] ?? '').trim();
    if (status !== 'Active') continue;

    const wattageStr = String(row[WATTAGE_COL] ?? '').trim();
    const commGrade  = String(row[COMMGRADE_COL] ?? '').trim();
    const cfFamily   = String(row[FAMILY_COL] ?? '').trim();
    const itemName   = String(row[ITEM_NAME_COL] ?? '').trim();

    const { familySlug, capabilityTier, rawShape } = resolveFamily(collRaw, commGrade, cfFamily, wattageStr);
    if (!familySlug) continue;

    const collSlug = collRaw === 'tubulⒶRCH'        ? 'tubulararch'
                   : collRaw === 'Décor nostⒶLGIC'   ? 'nostalgic-decor'
                   : collRaw === 'Décor vintⒶGE'     ? 'vintage-decor'
                   : collRaw === 'Utility signⒶTURE' ? 'utility-signature'
                   : collRaw.toLowerCase();

    if (!byCollB[collSlug]) byCollB[collSlug] = {};
    if (!byCollB[collSlug][familySlug]) byCollB[collSlug][familySlug] = [];

    const watt = parseFloat(wattageStr.replace(/W$/i, ''));
    byCollB[collSlug][familySlug].push({
      sku: itemName, family: familySlug,
      sub_category: rawShape || familySlug,
      display_echelon: capabilityTier || '',
      wattages: isNaN(watt) ? [] : [watt],
      ccts: [], voltage: '', mount_types: [], dlc: null, taa: false,
      comingSoon: COMING_SOON_FAMILIES.has(`${collSlug}/${familySlug}`),
    });
  }

  for (const [collSlug, familyMap] of Object.entries(byCollB)) {
    const allSkus = [];
    const families = [];
    for (const [famSlug, skus] of Object.entries(familyMap)) {
      const isComingSoon = COMING_SOON_FAMILIES.has(`${collSlug}/${famSlug}`);
      const maxWatt = skus.reduce((m, s) => { const w = s.wattages[0] ?? 0; return w > m ? w : m; }, 0);
      families.push({
        family: famSlug, sub_category: skus[0]?.sub_category || famSlug,
        display_echelon: skus[0]?.display_echelon || '',
        max_wattage: maxWatt, sku_count: skus.length, dlc: false,
        ccts: [], voltages: [], mount_types: [], taa: false, comingSoon: isComingSoon,
      });
      allSkus.push(...skus);
    }
    collectionsB[collSlug] = { skus: allSkus, families };
  }
}

// ── Hard-fail assertion ───────────────────────────────────────────────────────
const FAMILIES_REQUIRING_SKUS = [
  'tubulararch/t5', 'tubulararch/t8', 'tubulararch/pl', 'tubulararch/pll', 'tubulararch/u6',
  'nostalgic-decor/a15', 'nostalgic-decor/a19', 'nostalgic-decor/b10', 'nostalgic-decor/ca10',
  'nostalgic-decor/g16-5', 'nostalgic-decor/g25', 'nostalgic-decor/s14',
  'vintage-decor/candelabra', 'vintage-decor/edison', 'vintage-decor/globe',
  'vintage-decor/radio', 'vintage-decor/tubular', 'vintage-decor/victorian',
  'utility-signature/husk-hid',
];

for (const path of FAMILIES_REQUIRING_SKUS) {
  const [collSlug, famSlug] = path.split('/');
  const coll = collectionsB[collSlug];
  const fam = coll?.families?.find(f => f.family === famSlug);
  if (!fam || fam.sku_count === 0) {
    throw new Error(`[BUILD] Family ${path} has 0 SKUs — fix data resolution before shipping`);
  }
}
console.log('[build-sku-index] Hard-fail assertion: all expected-live families have ≥1 SKU ✓');

// ── Merge and write ───────────────────────────────────────────────────────────
const collections = { ...collectionsA, ...collectionsB };
mkdirSync(join(ROOT, 'src', 'data'), { recursive: true });
writeFileSync(OUT_PATH, JSON.stringify({ collections }, null, 2), 'utf8');

for (const [slug, col] of Object.entries(collections)) {
  console.log(`[build-sku-index] ${slug}: ${col.skus.length} SKUs, ${col.families.length} families`);
}
console.log(`[build-sku-index] Wrote ${OUT_PATH}`);
