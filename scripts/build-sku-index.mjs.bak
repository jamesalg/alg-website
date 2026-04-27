/**
 * scripts/build-sku-index.mjs
 *
 * Reads data/SKU_Attributes_Template_v1.xlsx and emits
 * src/data/sku-index.json for use by CollectionAllFamilies.astro.
 *
 * Column order (row 1 headers):
 *   0  collection
 *   1  sub_category
 *   2  family
 *   3  sku
 *   4  sales_description
 *   5  zoho_echelon
 *   6  display_echelon
 *   7  wattage
 *   8  cct
 *   9  voltage
 *  10  finish
 *  11  optics
 *  12  mount_in_sales_desc
 *  13  mount_type
 *  14  ship_status
 *  15  dlc_listing
 *  16  taa_compliant
 *  17  em_driver
 *  18  sensor_bilevel
 *  19  notes_for_james
 *
 * Row 2 is instructions — skipped.
 * Data starts at row 3.
 */

import { readFileSync, writeFileSync, mkdirSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import XLSX from 'xlsx';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..');
const XLSX_PATH = join(ROOT, 'data', 'SKU_Attributes_Template_v1.xlsx');
const OUT_PATH  = join(ROOT, 'src', 'data', 'sku-index.json');

// ── helpers ──────────────────────────────────────────────────────────────────

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
  // 'luxoⒶRCH' → 'luxoarch', 'planoⒶRCH' → 'planoarch'
  return raw.replace(/Ⓐ/g, 'a').replace(/RCH/g, 'rch').toLowerCase().replace(/[^a-z]/g, '');
}

// ── main ─────────────────────────────────────────────────────────────────────

let wb;
try {
  wb = XLSX.readFile(XLSX_PATH);
} catch (e) {
  console.error(`[build-sku-index] ERROR: Cannot read ${XLSX_PATH}`);
  console.error(e.message);
  process.exit(1);
}

const ws   = wb.Sheets[wb.SheetNames[0]];
const rows = XLSX.utils.sheet_to_json(ws, { header: 1, defval: '' });

if (rows.length < 3) {
  console.error('[build-sku-index] ERROR: xlsx has fewer than 3 rows — malformed file.');
  process.exit(1);
}

// rows[0] = headers, rows[1] = instructions, rows[2..] = data
const dataRows = rows.slice(2);

// Group by collection slug
const byCollection = {};

for (const row of dataRows) {
  const collRaw = String(row[0]).trim();
  if (!collRaw) continue;

  const slug = collectionSlug(collRaw);
  if (!byCollection[slug]) byCollection[slug] = [];

  const wattages   = parseWattages(row[7]);
  const ccts       = parsePipeList(row[8]);
  const voltage    = String(row[9]).trim();
  const mountTypes = parseMountTypes(row[13]);
  const dlc        = parseDlc(row[15]);
  const taa        = parseTaa(row[16]);

  byCollection[slug].push({
    sku:             String(row[3]).trim(),
    family:          String(row[2]).trim(),
    sub_category:    String(row[1]).trim(),
    display_echelon: String(row[6]).trim(),
    wattages,
    ccts,
    voltage,
    mount_types: mountTypes,
    dlc,
    taa,
  });
}

// Build per-collection output
const collections = {};

for (const [slug, skus] of Object.entries(byCollection)) {
  // Aggregate families
  const familyMap = {};
  for (const sku of skus) {
    const key = sku.family;
    if (!familyMap[key]) {
      familyMap[key] = {
        family:          sku.family,
        sub_category:    sku.sub_category,
        display_echelon: sku.display_echelon,
        max_wattage:     0,
        sku_count:       0,
        dlc:             false,
        ccts:            new Set(),
        voltages:        new Set(),
        mount_types:     new Set(),
        taa:             false,
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

  // Serialize sets → sorted arrays
  const families = Object.values(familyMap).map(f => ({
    family:          f.family,
    sub_category:    f.sub_category,
    display_echelon: f.display_echelon,
    max_wattage:     f.max_wattage,
    sku_count:       f.sku_count,
    dlc:             f.dlc,
    ccts:            [...f.ccts].sort(),
    voltages:        [...f.voltages].sort(),
    mount_types:     [...f.mount_types].sort(),
    taa:             f.taa,
  }));

  // Sort families: sub A→Z, echelon ECO→PRO→PRO+, name A→Z
  const TIER = { ECO: 0, PRO: 1, 'PRO+': 2 };
  families.sort((a, b) => {
    const sd = a.sub_category.localeCompare(b.sub_category);
    if (sd !== 0) return sd;
    const td = (TIER[a.display_echelon] ?? 99) - (TIER[b.display_echelon] ?? 99);
    return td !== 0 ? td : a.family.localeCompare(b.family);
  });

  collections[slug] = { skus, families };
}

// Write output
mkdirSync(join(ROOT, 'src', 'data'), { recursive: true });
writeFileSync(OUT_PATH, JSON.stringify({ collections }, null, 2), 'utf8');

// Summary
for (const [slug, col] of Object.entries(collections)) {
  console.log(`[build-sku-index] ${slug}: ${col.skus.length} SKUs, ${col.families.length} families`);
}
console.log(`[build-sku-index] Wrote ${OUT_PATH}`);
