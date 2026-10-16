---
title: "Carbon Fiber Fitment Data for Amazon Sellers: ACES & SKU Checklist"
description: "Build evidence-based vehicle fitment records for carbon fiber listings; understand ACES and PIES and verify current Amazon submission requirements."
keywords: ["Amazon ACES fitment", "Amazon automotive fitment data", "Amazon auto parts listing carbon fiber", "ACES XML carbon fiber parts", "Amazon Part Finder", "Amazon vehicle fitment seller", "Auto Care Association ACES"]
date: 2026-10-15
draft: false
cover:
  image: "/automotive-carbon-fiber-guide/images/posts/amazon-aces-fitment-cover.jpg"
  alt: "Amazon automotive Part Finder showing year make model fitment results for carbon fiber car parts"
lastmod: 2026-10-16
relatedGuides: ["carbon-fiber-parts-bmw-m3-m4-g80-g82", "carbon-fiber-sample-evaluation", "how-to-start-carbon-fiber-automotive-parts-business"]
---

**Treat fitment as a maintained SKU record, not a phrase such as “fits BMW 2021+.”** Identify the exact vehicle configuration, component revision, installation method and supporting evidence before publishing compatibility. Marketplace acceptance of data does not prove physical fitment.

## ACES and PIES: different jobs

The Auto Care Association defines ACES as a standard for communicating product fitment information and PIES as a standard for product information. See its [data standards overview](https://www.autocare.org/data-standards) and current documentation for supported versions, reference databases and licensing.

| Record | Purpose | Examples of buyer-maintained information |
|---|---|---|
| Fitment / ACES workflow | Communicate vehicle applications in a structured format | Vehicle attributes, qualifiers and exclusions |
| Product / PIES workflow | Communicate product information | Part identity, attributes and package content |
| Physical verification file | Support the application claim | Test-fit vehicle, component revision, measurements and photos |

ACES is an XML-based communication standard supported by reference databases. A spreadsheet may be your working input, but it is not automatically a valid ACES submission. The [official ACES page](https://www.autocare.org/aces) explains the standard and access to its supporting databases.

## Verify the marketplace route before creating a feed

Check the current Automotive fitment instructions in your Amazon Seller Central marketplace or with your authorized data provider. Confirm category eligibility, accepted format/version, submission method, account permissions, processing feedback and update/deletion procedures.

Requirements may vary by region and account. This guide does not claim that every seller can upload an ACES file directly, that a specific portal is available to every account, or that any data provider guarantees listing approval. Verify eBay's requirements separately rather than assuming the Amazon workflow applies there.

## Minimum fitment record for each carbon fiber SKU

| Field | What to record |
|---|---|
| Identity | Internal SKU, supplier reference and product revision |
| Vehicle | Make, model, generation, body style, production-date limits and market |
| Relevant options | Bumper/trim package, mirror housing, exhaust layout or equipment affecting the part |
| Part scope | Replacement or overlay; individual component, pair or kit |
| Installation | Hardware, adhesive, drilling and modification requirements |
| Evidence | Test-fit configuration, date, photos, reviewer and any limitations |
| Exclusions | Configurations not supported or not yet verified |
| Maintenance | Record owner, last review and change history |

Keep customer vehicle identifiers in your internal support record where appropriate; do not publish personal data in listing content.

## Worked example: a front lip with limited evidence

Suppose a supplier has verified a front lip on one particular bumper configuration. That evidence supports the recorded configuration, not every car sharing the same model name. Before expanding compatibility, ask which mounting surfaces, production changes and optional packages were checked.

Keep proposed applications separate from verified ones. If a qualifier cannot be represented clearly in the channel's accepted fields, resolve the limitation before publishing a broader fitment claim. Do not rely on a small note to contradict an expansive compatibility table.

## Before publishing or updating a listing

- [ ] Product photos correspond to the actual SKU and revision.
- [ ] Title, description and compatibility records agree.
- [ ] Unverified years, trims and body styles have not been added for traffic.
- [ ] Supplied hardware, kit contents and modifications are disclosed.
- [ ] Construction and weight claims match documented evidence.
- [ ] Feed validation and marketplace processing feedback have been reviewed.
- [ ] A process exists to remove or correct affected applications after a fitment complaint.

Use [sample inspection]({{< relref "posts/carbon-fiber-sample-evaluation.md" >}}) and the [BMW G80/G82 sourcing checklist]({{< relref "posts/carbon-fiber-parts-bmw-m3-m4-g80-g82.md" >}}) to build the evidence file before mapping it to marketplace fields.

## Frequently asked questions

### Does a valid ACES file prove that a part fits?

No. Format validation and physical verification solve different problems. Retain the evidence behind each published application.

### Can my supplier provide an Amazon-ready feed?

Ask what is available: raw fitment records, a spreadsheet or a validated feed. Confirm ownership, licensing, update responsibilities and the destination's requirements. Do not assume CCF or another supplier provides a marketplace integration without confirmation.

### What should happen after a fitment complaint?

Record the customer's configuration and the supplied revision, review the evidence and suspend questionable applications while investigating. Update both the source record and each affected sales channel.
