# Fin labeling strategy

Draft 2026-09-04 by Claude from the label inventory in `workstreams/help-center-overhaul/outputs/fin-label-inventory-2026-09-04.md`. Owner: Tara, with Jeff on Intercom mechanics. Milestone: September 4, 2026. Items marked [decide: ...] need Tara's call before this becomes the standard.

## What this covers

Labels are the Intercom article tags Fin can use to find the right content. Today 14 of the 208 mirrored Baldwin and CRMLS articles carry any label, 17 distinct labels cover about 8 topics, and two of the labels are conversation tags that say nothing about content. This standard replaces that with a small vocabulary every article gets, so a section retrieved on its own still tells Fin which MLS, which topic, and what kind of content it is.

[decide: Jeff to confirm that article tags are the layer Fin reads for scoping. If Fin scopes on help center membership or audience rules instead, the MLS facet below becomes documentation only and the Topic and Type facets stay.]

## Proposed label taxonomy

Three facets. Every article carries exactly one label from each, written exactly as shown (capital first letter, one space after the colon). Nothing else goes on an article.

### Facet 1: MLS

| Label | Use when |
|---|---|
| MLS: Baldwin | The article is in the Baldwin help center only |
| MLS: CRMLS | The article is in the CRMLS help center only |
| MLS: Shared | The article is in both help centers through a shared collection (26 articles today) |

[decide: whether the 26 shared articles should stay shared with one label, or be split into MLS-specific copies once the audit settles shared versus MLS-specific content. If split, MLS: Shared is retired.]

### Facet 2: Topic

One topic per article, taken from its collection. Topics mirror the collection names both help centers already use, so a teammate can read the topic off the help center without a lookup.

| Label | Baldwin collections it covers | CRMLS collections it covers |
|---|---|---|
| Topic: Search | Search, Search / Filters, Search / FAQs | Search, Search / Filters |
| Topic: Listings | Listing Maintenance, Listing Maintenance / FAQs | Listings |
| Topic: Reports | Reports, Reports / FAQ | Reports |
| Topic: Tags | Tags, Tags / FAQs | Tags |
| Topic: Clients | Client Collaboration, Client Experience, Client Collaboration / FAQs | Client Collaboration, Client Collaboration / Agents, Client Collaboration / Invited Clients |
| Topic: Dashboard | Dashboard, Dashboard / FAQs | Dashboard |
| Topic: Analytics | Analytics / Analytics Tools, Analytics / FAQs | Analytics |
| Topic: Mobile | Mobile, Mobile / FAQs | (none yet) |
| Topic: Account | User Settings, User Settings / Log In to Perchwell, Manage People, Manage People / FAQs | (none yet) |
| Topic: Integrations | Integrations | (none yet; Realist Integration sits in Listings) |
| Topic: Transition | Then vs. Now | Welcome to Perchwell / From Legacy to Perchwell |
| Topic: Getting Started | Getting Started Guide, Perchwell Training Sessions | Critical Workflows, Webinars, Welcome to Perchwell |
| Topic: General | FAQs & Cheat Sheets, What's New in Perchwell | FAQ + Tips + What's New in Perchwell |

[decide: whether Contacts deserves its own topic instead of folding into Topic: Clients. Both help centers keep contact articles under Client Collaboration, so the draft follows the collections.]

[decide: whether Topic: General is acceptable or whether every cheat-sheet and FAQ article must be moved into a topic collection first. Keeping General means Fin can still find "Top Compliance Questions" but the label tells it little.]

### Facet 3: Type

| Label | Use when |
|---|---|
| Type: How-to | Numbered steps to complete one task |
| Type: Overview | Orients the reader to a page or feature without one primary task |
| Type: FAQ | Question-and-answer format, including every article in a nested FAQs collection |
| Type: Reference | Definitions, status lists, property types, terminology |
| Type: Training | Recorded sessions, webinars, video libraries |
| Type: Release notes | What's New and Upcoming Features |

[decide: whether Type: Release notes content should be labeled for Fin at all, or excluded from Fin so it never answers with a roadmap item as if it were live.]

### Reserved: never on an article

Conversation triage tags stay on conversations: Feedback: *, Bug: *, FIN: *, Self-Service, Human Action Required, Baldwin VIP, Paragon vs Perchwell, and the How To: * family once migrated. Label the article, not the inbox.

## Rule for assigning labels to a new article

1. The Notion draft row already carries `MLS`, `Collection in Intercom`, and the article type. Labels are read from those three fields, not chosen fresh.
2. MLS label: `MLS` value Baldwin gives MLS: Baldwin, CRMLS gives MLS: CRMLS, both or All Regions gives MLS: Shared.
3. Topic label: look the collection up in the Topic table above. A collection missing from the table is a signal to add a row here first, not to invent a label.
4. Type label: How-to if the article has a Steps section, FAQ if it lives in a FAQs collection or uses question headings throughout, Overview for "<Page> Overview" titles, Reference for definitions and lists, Training for sessions and videos, Release notes for What's New.
5. Apply all three labels when the article is transferred to Intercom, before it is published, so Fin never indexes an unlabeled article. Three labels exactly; a fourth means the article has two topics and should be split.
6. `/sync-help-center` shows the labels in each mirrored file's frontmatter. An article in the mirror with fewer than three labels fails the QA pass.

[decide: who applies the labels in Intercom at transfer. Jeff's open question on whether labels can be applied in bulk or per collection determines whether the migration below is a one-afternoon job or a per-article one.]

## Migration table: current labels to proposed

| Current label | Articles | Proposed | Note |
|---|---|---|---|
| How To: Search | Universal Search Bar; Using the Draw Filter | Topic: Search + Type: How-to | |
| How to: Search (Filters) | Using the Draw Filter | Topic: Search + Type: How-to | Duplicate of the row above; drop |
| How To: Filters | Using the Draw Filter | Topic: Search + Type: How-to | Duplicate; drop |
| How to: Search (Status + Listing Activity) | Understand Status and Activity Filter | Topic: Search + Type: Reference | |
| How To: Open House | Search for Open Houses | Topic: Search + Type: How-to | |
| How to: Search (Open House) | Search for Open Houses | Topic: Search + Type: How-to | Duplicate; drop |
| How To: Manage Listings | AI Scribe | Topic: Listings + Type: How-to | Also label its siblings Add and Edit Listings, Manage Listings Page Overview |
| Client Contacts | Bulk Upload Contacts | Topic: Clients + Type: How-to | |
| How To: Contacts | Bulk Upload Contacts | Topic: Clients + Type: How-to | Duplicate; drop |
| How To: Tags | Managing Tag Alerts | Topic: Tags + Type: How-to | |
| How To: Dashboard | The Days Active in the MLS Widget | Topic: Dashboard + Type: Overview | |
| How To: Listing Presentations | Overview of Listing Presentations | Topic: Reports + Type: Overview | |
| Feedback: Agents | Overview of Listing Presentations | remove | Conversation tag |
| Roadmap | Upcoming Features | Topic: General + Type: Release notes | [decide: keep out of Fin?] |

Every migrated article also gets its MLS label: Bulk Upload Contacts, Search for Open Houses, Understand Status and Activity Filter, and Universal Search Bar are MLS: Shared; AI Scribe and Upcoming Features are MLS: Baldwin; the CRMLS-only ones are MLS: CRMLS.

The 194 articles with no label today get all three labels from the rule above; the collection column in the mirror README is the worklist.

## Maintenance

- A new collection in either help center means a new row in the Topic table before any article in it is transferred.
- `/sync-help-center` refreshes labels with every run; a weekly check of `labels: []` in the mirror catches anything that slipped through.
- The audit's shared-versus-MLS-specific decision may retire MLS: Shared; update this file and the migration table when it lands.
