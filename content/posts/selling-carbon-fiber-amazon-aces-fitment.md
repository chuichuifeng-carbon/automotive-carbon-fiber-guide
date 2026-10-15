---
title: "Selling Carbon Fiber Parts on Amazon: ACES Fitment Data Guide for Sellers"
description: "Complete guide to listing carbon fiber car parts on Amazon using ACES fitment data — how to build valid vehicle application records, avoid the fitment errors that cause returns and A-to-z claims, and keep your Automotive Account Health green."
keywords: ["Amazon ACES fitment", "Amazon automotive fitment data", "Amazon auto parts listing carbon fiber", "ACES XML carbon fiber parts", "Amazon Part Finder", "Amazon vehicle fitment seller", "Auto Care Association ACES"]
date: 2026-10-15
draft: false
cover:
  image: "/automotive-carbon-fiber-guide/images/posts/amazon-aces-fitment-cover.jpg"
  alt: "Amazon automotive Part Finder showing year make model fitment results for carbon fiber car parts"
---

# Selling Carbon Fiber Parts on Amazon: ACES Fitment Data Guide for Sellers

If you sell carbon fiber car parts on Amazon, the listing text does not decide whether a part fits a customer's car — the fitment data does. Amazon's automotive category uses a structured data standard called **ACES** to power the "Part Finder" garage that asks shoppers for Year, Make, Model, Engine, and Trim before showing any compatible parts. Get your ACES data wrong and your listing shows up for the wrong vehicles, customers buy parts that do not fit, you accumulate A-to-z Guarantee claims, your Automotive Account Health goes red, and Amazon throttles or suspends your seller account.

This guide explains ACES from the perspective of an Amazon seller of carbon fiber parts — what the standard is, how to build correct fitment records, the specific errors that destroy carbon fiber listings, and a pre-submission checklist you can reuse for every SKU. Every standard, database name, and version here is publicly documented by the Auto Care Association and Amazon Seller Central.

## What ACES Actually Is (and Why It Is Not a Spreadsheet)

**ACES — Aftermarket Catalog Enhanced Standard** is an XML-based data standard published and maintained by the **Auto Care Association** (formerly the Automotive Aftermarket Industry Association). Amazon, eBay, Walmart, and most major auto parts retailers consume ACES to determine which vehicles a given part fits.

ACES is not a spreadsheet. A single ACES file contains:

| Element | What it declares | Example for a carbon fiber spoiler |
|---|---|---|
| `Brand` + `PartNumber` | Identifies the SKU | "BrandX CF-G80-LIP-001" |
| `PartTerminology` (from PCdb) | Standardized part type name | "Front Bumper Lip" |
| `BaseVehicle` + `Vehicle` (from VCdb) | Year/Make/Model/Submodel/Engine | "2021 BMW M3 Competition xDrive" |
| `Qualifiers` | Conditional fitment rules | "Excludes carbon ceramic brake package" |
| `MfrLabel` / `MfrPart` | Marketing part name + number | "M3 G80 Pre-LCI Carbon Front Lip" |
| `Quantity` / `Sequence` | How many fit per vehicle / display order | 1 / 1 |
| `PartCategory` (optional) | PCdb category | "Front Bumper" |

The two reference databases every ACES record draws from:

- **VCdb (Vehicle Configuration database)** — every valid Year/Make/Model/Submodel/Engine/trim combination, each with a numeric ID. You do not write "2021 BMW M3" — you write the VCdb ID `1234567` (the actual ID varies by year).
- **PCdb (Part Category database)** — every standardized part type name and category. You do not write "spoiler" — you reference the PCdb term, e.g., `Front Bumper Lip` or `Rear Spoiler`.

This is why sellers cannot "just type" their fitment into Amazon — they must submit records that resolve against VCdb and PCdb IDs. Amazon's Automotive Fitment Manager is the tool that ingests these records.

## How Amazon Ingests ACES: The Fitment Pipeline

| Step | Where it happens | What you do |
|---|---|---|
| 1. Register your brand | Auto Care Association | Get a **Brand ID (BBID)** — without this, your records cannot resolve |
| 2. Build the ACES XML | Catalog tool (your own, or a service) | Generate `<App>`, `<BaseVehicle>`, `<Qualifiers>` per SKU |
| 3. Submit to Amazon | Seller Central → Catalog → Automotive Fitment Manager | Upload the file or use Amazon's template |
| 4. Amazon validates | Amazon back-end | Records that fail validation are rejected silently or flagged |
| 5. Live fitment | Part Finder on the detail page | Shoppers enter garage vehicle; compatible SKUs surface |
| 6. Account Health feedback | Amazon Automotive category dashboard | Returns and claims against the ASIN hit your fitment accuracy score |

Two non-obvious consequences of this pipeline:

1. **A rejected record does not block the listing** — the part still sells, but it will not show in Part Finder for the rejected vehicles. The customer sees the detail page via search, buys on the listing copy, and then discovers the part does not fit when it arrives. This is the worst outcome: a return plus a "not as described" A-to-z claim.
2. **Fitment accuracy is monitored.** Amazon tracks fitment-related returns per ASIN and per seller. High rates trigger Automotive Account Health warnings, listing suppression, and in extreme cases category removal.

## The Carbon Fiber Fitment Mistakes Amazon Punishes Hardest

Carbon fiber is uniquely punishing on Amazon fitment because the parts are expensive, the returns are expensive, and the customers are knowledgeable. Here are the mistakes that generate the most claims in this category:

| Mistake | Why it happens | Customer impact | Amazon consequence |
|---|---|---|---|
| Listing a part for "M3 2021+" without LCI split | Seller uses model-year range, no generation qualifier | Customer with LCI 2025 M3 buys pre-LCI lip → does not fit | A-to-z claim + fitment accuracy hit |
| Missing xDrive qualifier on diffusers | ACES record omits drivetrain qualifier | Customer's xDrive M3 diffuser contacts underbody hardware | Return + negative review + fitment accuracy hit |
| Applying one part to both sedan and coupe | Seller assumes G80/G82 share all fitment | Trunk spoiler ordered for G82 does not fit G80 | A-to-z claim |
| Omitting sensor/camera qualifiers | No qualifier for sensor provision | Customer buys grille that blocks front camera | Return + safety complaint |
| Using "carbon fiber" PartTerminology not in PCdb | Free-text part name instead of PCdb term | Part does not resolve in Part Finder at all | Listing invisible in garage flow |
| Duplicate fitment apps | Same vehicle listed twice in ACES | Conflicting display | Catalog quality flag |
| Brand ID mismatch | ACES brand ID does not match Amazon Brand Registry | Entire file rejected | No fitment goes live |

## Building a Correct ACES Record: A Worked Example

Here is how a carbon fiber front lip for the BMW G80 M3 should be structured. We use the G80 platform because it is the highest-volume carbon fiber listing on Amazon Motors and the one where fitment errors are most visible.

**Product:** Carbon Fiber Front Lip Spoiler, pre-preg, fits pre-LCI G80 M3 sedan and G82 M4 coupe, RWD and Competition. **Does not fit** LCI (2025+), G83 convertible, or CS/CSL special editions.

**Correct ACES application set:**

| App # | BaseVehicle (VCdb) | Qualifier | Applies? |
|---|---|---|---|
| 1 | 2021 BMW M3 Base sedan | "Pre-LCI only. Excludes LCI (2025+). RWD and Competition." | Yes |
| 2 | 2022 BMW M3 Base sedan | (same qualifier) | Yes |
| 3 | 2023 BMW M3 Base sedan | (same) | Yes |
| 4 | 2024 BMW M3 Base sedan | (same) | Yes |
| 5 | 2021 BMW M4 Base coupe | (same) | Yes |
| 6 | 2022 BMW M4 Base coupe | (same) | Yes |
| 7 | 2023 BMW M4 Base coupe | (same) | Yes |
| 8 | 2024 BMW M4 Base coupe | (same) | Yes |

Note what is **not** in this list: 2025+ M3/M4 (would require a separate SKU for the LCI), G83 convertible, M3 CS, M4 CS, M4 CSL. A responsible supplier will tell you whether a part also fits those — if not, omit them. **An absent vehicle is far safer than an incorrect vehicle.**

<figure class="post-inline-figure">
  <img src="/automotive-carbon-fiber-guide/images/posts/amazon-fitment-manager.jpg" alt="Amazon Seller Central Automotive Fitment Manager screen showing year make model vehicle applications for a carbon fiber part" loading="lazy" />
  <figcaption>Amazon's Automotive Fitment Manager ingests your ACES records and displays them as the Part Finder garage. Each row is one vehicle application — the qualifier column is where you encode pre-LCI/LCI, xDrive, and sensor provisions.</figcaption>
</figure>

## Qualifiers: The Field That Saves Your Account

The `Qualifiers` field is the single most important data element in a carbon fiber ACES record. Amazon's Part Finder surfaces qualifiers as sub-text under the compatible vehicle (e.g., "Excludes LCI models"). Without qualifiers, a generic year/make/model record will sell to customers whose specific trim does not fit.

**Qualifier writing rules:**

1. **Be specific and negative when in doubt.** "Excludes LCI (2025+)" is clearer than "Fits most 2021–2024". A customer reading "Excludes" stops; a customer reading "Fits most" assumes theirs fits.
2. **Call out drivetrain.** "RWD and Competition. Not validated for xDrive" is safer than silence.
3. **Call out sensor packages.** "Retains factory PDC sensor holes" or "Blocks front parking camera — verify before ordering" — pick the accurate one.
4. **Call out special editions.** "Excludes CS, CSL" for parts that do not fit the limited-run cars.
5. **No marketing language.** "Premium quality carbon fiber" belongs in the listing copy, not the qualifier. Amazon validation may reject free text.

## PIES: The Other Standard You Need

Amazon's automotive category uses **PIES (Product Information Exchange Standard)** alongside ACES. Where ACES answers "what does this fit?", PIES answers "what is this product?" — dimensions, weight, materials, UPC, hazmat, images, and marketing copy.

| PIES segment | What it carries | Why it matters for carbon fiber |
|---|---|---|
| `Item` | Brand, part number, UPC | Required for ASIN creation |
| `Prices` | Cost / MSRP | Optional but expected |
| `Attributes` | Dimensions, weight, material | Shipping calculation; returns when dimensions mislead |
| `Marketing` | Short/long description, bullets | Listing copy source |
| `DigitalAssets` | Image URLs, image type | Primary image + fitment photos |
| `Packaging` | Carton dimensions, UPC on package | FBA inbound planning |

The most common PIES failure for carbon fiber sellers: **incorrect `Attributes` weight and dimensions**. A carbon fiber hood shipped in a box labeled 5 kg but actually weighing 11 kg triggers Amazon FBA measurement discrepancies and may charge you for oversize shipping. Weigh the packed part, not the bare part, and use a calibrated scale.

## Account Health: How Fitment Errors Become Account Problems

Amazon tracks several metrics for automotive sellers. Fitment errors feed directly into these:

| Metric | What it measures | Fitment-related cause | Threshold for trouble |
|---|---|---|---|
| Order Defect Rate (ODR) | A-to-z claims, negative reviews, chargebacks | "Item not as described" claims from wrong fitment | < 1% to stay healthy |
| Late Shipment Rate | Late confirmations | Usually unrelated to fitment | < 4% |
| Pre-fulfillment cancel rate | Cancellations before ship | Sometimes fitment disputes before ship | < 2.5% |
| Fitment Accuracy (automotive-specific) | Fitment returns per ASIN | Directly from ACES errors | Repeated flags trigger suppression |

**Carbon fiber ASINs are high-value and low-volume**, which means a single A-to-z claim can push your ODR into the red zone. A seller moving 200 carbon fiber spoilers a month with two A-to-z claims from fitment errors has a 1% ODR — already at the edge. Three claims and you are over. This is why fitment accuracy is not a "nice to have" — it is existential.

## Pre-Submission ACES Checklist (Use Before Every Upload)

Before you submit an ACES file for a carbon fiber SKU:

**Identity**
- [ ] Brand ID (BBID) matches Amazon Brand Registry exactly
- [ ] Manufacturer part number matches the physical part's printed label
- [ ] UPC is valid and unique to this SKU

**Part type**
- [ ] PartTerminology uses a valid PCdb term (e.g., "Front Bumper Lip", not "Lip Kit")
- [ ] No free-text part type names

**Vehicle applications**
- [ ] Every BaseVehicle ID is a real VCdb entry for the current model year cycle
- [ ] Submodel specified where the platform has variants (Base, Competition, CS, CSL)
- [ ] Engine qualifier applied where the platform has multiple engines (rare for M cars but common for non-M BMW parts)
- [ ] Drivetrain (RWD vs xDrive) qualified for underbody and diffuser parts
- [ ] Body style (sedan/coupe/convertible) qualified for trunk, roof, and rear parts
- [ ] Generation (pre-LCI vs LCI) qualified where the part is generation-specific
- [ ] Special editions (CS, CSL, GTS) explicitly excluded where they do not fit

**Qualifiers**
- [ ] Every application has a qualifier field, even if it is "Standard fitment, no exclusions"
- [ ] Sensor and camera provisions noted (retain PDC holes, blocks front camera)
- [ ] No marketing language in qualifiers

**Compliance**
- [ ] No vehicle listed that the supplier has not confirmed in writing
- [ ] Test-fit photo on file for every listed vehicle application
- [ ] File validated against the current ACES schema version Amazon accepts

## Working With Your Supplier on Fitment Data

Most fitment errors originate at the supplier because the seller copies the supplier's "fits M3/M4 2021+" language into an ACES record without verification. To prevent this:

1. **Request a written fitment matrix per SKU.** Ask the supplier for a table listing every vehicle the part is confirmed to fit, with body style, generation, drivetrain, and any exclusions. Our [supplier question checklist](/automotive-carbon-fiber-guide/posts/questions-to-ask-carbon-fiber-supplier/) gives you the exact script.
2. **Cross-reference against OEM parts catalogs.** The factory BMW parts catalog and realOEM.com give you the authoritative fitment for OEM parts; a carbon fiber aftermarket part that claims to replace an OEM part should match the OEM fitment unless the supplier documents a deliberate difference.
3. **Test-fit on the actual vehicle.** The [sample evaluation guide](/automotive-carbon-fiber-guide/posts/carbon-fiber-sample-evaluation/) covers the physical checks. A supplier who test-fits on a real car and sends photos is one you can trust with ACES data.
4. **Never extrapolate.** If the supplier confirms 2021–2024 pre-LCI only, do not add 2025 to your ACES record because "it probably fits." It probably does not, and the LCI bumper contour change is the most common fitment break on this platform.

## eBay's Fitment Standard: A Parallel System

If you sell the same carbon fiber parts on eBay, note that eBay uses a different but parallel system: **eBay Parts Compatibility (Fitment)**. eBay accepts up to 1,000 fitment combinations per listing (3,000 for some categories) and participates in the **eBay Assured Fit** program, which refunds buyers if a part does not fit the selected garage vehicle. The data model is similar (year/make/model/submodel/engine + qualifiers) but the upload format differs. A separate guide covers [eBay Motors fitment in depth](/automotive-carbon-fiber-guide/posts/ebay-motors-carbon-fiber-fitment/).

## FAQ

### Do I need ACES if I only sell a few carbon fiber SKUs on Amazon?

Yes, if you list in the Automotive category. Amazon requires fitment data for automotive ASINs — without it, your listing will not surface in Part Finder, the dominant discovery path for car parts buyers. A carbon fiber spoiler with no ACES record sells only to shoppers who find it via keyword search, missing the customers who enter their vehicle in the garage.

### What happens if I list a part as fitting a vehicle it does not fit?

The customer buys it, receives a part that does not fit, and files an A-to-z Guarantee claim for "item not as described." You refund, pay return shipping, and the claim counts against your Order Defect Rate. Repeated claims suppress the ASIN and can revoke your Automotive selling privileges. On high-value carbon fiber parts, a single claim can be hundreds of dollars plus account-level damage.

### Can I fix fitment errors after a listing is live?

Yes — submit an updated ACES file that removes the incorrect vehicle applications and adds qualifiers. Existing customers who already bought against the wrong fitment are still your liability, so fix errors the moment you identify them. Proactive correction also helps in any Account Health appeal.

### How do I get a Brand ID (BBID) for ACES?

Apply through the Auto Care Association. The brand registration process is separate from Amazon Brand Registry, though both require a trademark. Most carbon fiber sellers use either their own registered brand or license a brand from their manufacturer. Budget 2–4 weeks for the Auto Care Association registration.

### Is the supplier's fitment data good enough to submit directly?

Almost never. Suppliers typically provide fitment in human-readable form ("fits G80/G82 2021+"), not in ACES format against VCdb IDs. You or your catalog service must translate the supplier's confirmed fitment into VCdb-coded applications with qualifiers. The [supplier question guide](/automotive-carbon-fiber-guide/posts/questions-to-ask-carbon-fiber-supplier/) gives you the questions whose answers feed this translation.

### What is the difference between ACES and PIES?

ACES answers "what vehicles does this part fit?" PIES answers "what is this product?" Amazon requires both for automotive listings — ACES powers Part Finder, PIES powers the detail page content, dimensions, and images. Submitting ACES without correct PIES leaves you with a fitment-accurate listing that has no usable product information; submitting PIES without ACES leaves you with a listing no one finds in the garage.

## Need a Supplier That Gives You Fitment Data, Not Just Parts?

We supply carbon fiber parts with a written fitment matrix per SKU — body code, generation (pre-LCI/LCI), drivetrain (RWD/xDrive), sensor provisions, and explicit exclusions. Send us your target Amazon catalog and we will return the fitment data structure your catalog service needs to build clean ACES records.

**Website:** [www.ccfrp.com](https://www.ccfrp.com)
**WhatsApp:** +86 134 2769 0360
**Email:** [info@ccfrp.com](mailto:info@ccfrp.com)

*OEM · ODM · Private Label · Wholesale · Automotive E-commerce Sourcing*
