# Asset Inventory — v2.0.0 Foundation

**Audit date:** 2026-04-25
**Source:** v3.14.6 trusted package (last clean state from prior platform) + Featured Family reference images + brand assets from /mnt/project/

## Present in repo (23 production assets)

### Brand (`public/brand/`)
| File | Source | Notes |
|---|---|---|
| `alg-logo-color.png` | `/mnt/project/ALG_LogoColor.png` | Primary logo, color version |
| `alg-logo-white.png` | `/mnt/project/ALG_LogoWhite.png` | White-on-dark variant |
| `alg-brandmark-red.png` | `/mnt/project/Archipelago_brandmark_Red.png` | Standalone Ⓐ mark, red |
| `alg-brandmark-white.png` | `/mnt/project/Archipelago_brandmark_White.png` | Standalone Ⓐ mark, white |

### Hero photography (`public/images/heroes/`) — 5 slides
| File | Subject |
|---|---|
| `hero-illuminator-stadium.jpg` | Sports lighting / stadium with Illuminator |
| `hero-warehouse-highbay.jpg` | Warehouse high-bay installation |
| `hero-outdoor-area.jpg` | Outdoor area lighting |
| `hero-controls-panel.jpg` | Lighting controls / panels |
| `hero-commercial-office.jpg` | Commercial office interior |

### Vertical "installed at" photography (`public/images/verticals/`) — 5 of 8
| File | Vertical | Status |
|---|---|---|
| `vertical-warehouse.jpg` | Warehouse & Logistics | ✓ Present |
| `vertical-manufacturing.jpg` | Industrial & Manufacturing | ✓ Present |
| `vertical-healthcare.jpg` | Healthcare | ✓ Present |
| `vertical-education.jpg` | Education | ✓ Present |
| `vertical-government.jpg` | Government & Military | ✓ Present |
| **(MISSING)** | **Cold Storage & Grocery** | **Need to source** |
| **(MISSING)** | **Data Center** | **Need to source** |
| **(MISSING)** | **Hospitality** | **Need to source** |

Supplemental images present but not directly mapped:
- `_supplemental-parking.jpg`
- `_supplemental-retail.jpg`
- `_supplemental-stadium.jpg`

### Featured Family photography (`public/images/families/`) — 4 of 4
| File | Family | Notes |
|---|---|---|
| `family-illuminator.png` | Illuminator (Sports/Stadium) | High-res FF reference |
| `family-titan.png` | Titan-II (Warehouse High-bay) | Pulled from hero screenshot |
| `family-astra.png` | Astra (Wall Pack / Area) | High-res FF reference |
| `family-contrals.png` | contrⒶLS (Controls & EM) | High-res FF reference |

### Mega-menu preview tiles (`public/images/megamenu/`) — 2 of 3
| File | Category | Status |
|---|---|---|
| `mega-constant.jpg` | constⒶNT (EM driver products) | ✓ Present |
| `mega-controls.jpg` | contrⒶLS (Controls) | ✓ Present |
| **(MISSING)** | **tubulⒶRCH (Linear Specialty)** | **Need to source** |

## Missing / to-source (4 items)

To complete the homepage and persona pages cleanly, these four assets need to be sourced:

1. `vertical-coldstorage.jpg` — cold storage / grocery interior with high-bay LED lighting
2. `vertical-datacenter.jpg` — server room or data center interior
3. `vertical-hospitality.jpg` — hotel lobby / restaurant interior
4. `mega-tubularch.jpg` — tubulⒶRCH linear product close-up or installed scene

**Resolution paths:**
- Use Manus image gen (NanoBanana style — it's what generated the existing photography; consistent style)
- Use DALL-E or similar
- Use licensed stock photography
- Substitute existing photos temporarily (e.g., commercial-office.jpg as placeholder for hospitality)

For Iteration 1 (homepage), the homepage hero + Featured Families do NOT depend on the missing 4. The 8-vertical "Installed at" section CAN proceed with placeholder grey tiles for the 3 missing verticals + a "photography pending" badge — Manus implements this gracefully.
