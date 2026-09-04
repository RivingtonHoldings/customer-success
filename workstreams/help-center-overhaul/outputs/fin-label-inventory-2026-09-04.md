# Fin content label inventory

Built 2026-09-04 from the help center mirror after a fresh `/sync-help-center` (Intercom unchanged since the morning sync: Baldwin 123 articles, CRMLS 85, zero added, updated, or removed). Every article file in both mirrors was read; labels are the Intercom article tags carried in each file's `labels` frontmatter.

Owner of the follow-up: Tara, with Jeff on the Intercom mechanics. Contacts are in `workstreams/help-center-overhaul/docs/project-status.md`.

## What "label" means here

The Intercom connector exposes one labeling mechanism on articles: tags. These are the same workspace tags used on conversations, which means a tag like "How To: Tags" appears on inbox conversations and on articles alike. If Intercom scopes Fin's retrieval with something other than tags (audience rules or help center membership), that layer is not visible through the connector. [decide: Jeff to confirm which mechanism Fin actually reads for Baldwin and CRMLS before the taxonomy below is applied]

Help center membership is the strongest scoping signal we can see: 120 published articles belong to the Baldwin help center (ID 4755399), 71 to CRMLS (4767477), and 26 articles belong to both through shared collections.

## Baldwin (123 articles: 120 published, 3 draft)

Labels in use: 8 distinct labels on 6 articles. 117 articles (95 percent) carry no label.

| Label | Articles | Which |
|---|---|---|
| How To: Manage Listings | 1 | AI Scribe |
| Client Contacts | 1 | Bulk Upload Contacts |
| How To: Contacts | 1 | Bulk Upload Contacts |
| How To: Open House | 1 | Search for Open Houses |
| How to: Search (Open House) | 1 | Search for Open Houses |
| How to: Search (Status + Listing Activity) | 1 | Understand Status and Activity Filter |
| How To: Search | 1 | Universal Search Bar |
| Roadmap | 1 | Upcoming Features |

Collections carrying the unlabeled 117: Search (14), Getting Started Guide (14), Client Collaboration (9), Reports (9), Then vs. Now (8), FAQs & Cheat Sheets (7), Client Experience (6), Dashboard (6), Perchwell Training Sessions (6), Mobile (6), Tags (5), Listing Maintenance (4), User Settings (4), Search / Filters (4), Analytics / Analytics Tools (3), Manage People (3), Integrations (3), nine per-topic FAQ sub-collections (1 or 2 each), What's New in Perchwell (1).

## CRMLS (85 articles: 71 published, 14 draft)

Labels in use: 12 distinct labels on 8 articles. 77 articles (91 percent) carry no label.

| Label | Articles | Which |
|---|---|---|
| How To: Search | 2 | Universal Search Bar; Using the Draw Filter (draft) |
| Client Contacts | 1 | Bulk Upload Contacts |
| How To: Contacts | 1 | Bulk Upload Contacts |
| How To: Tags | 1 | Managing Tag Alerts (draft) |
| How To: Listing Presentations | 1 | Overview of Listing Presentations |
| Feedback: Agents | 1 | Overview of Listing Presentations |
| How To: Open House | 1 | Search for Open Houses |
| How to: Search (Open House) | 1 | Search for Open Houses |
| How To: Dashboard | 1 | The Days Active in the MLS Widget |
| How to: Search (Status + Listing Activity) | 1 | Understand Status and Activity Filter |
| How to: Search (Filters) | 1 | Using the Draw Filter (draft) |
| How To: Filters | 1 | Using the Draw Filter (draft) |

Collections carrying the unlabeled 77: Search (15), Reports (12), Search / Filters (8), Client Collaboration / Invited Clients (7), Client Collaboration / Agents (7), Dashboard (7), Critical Workflows (7), Tags (5), Listings (5), Analytics (4), Webinars (3), FAQ + Tips + What's New (2), Welcome to Perchwell (2), Client Collaboration (1).

## Labels that do not match their collection or content

- **Roadmap** on Upcoming Features (Baldwin, FAQs & Cheat Sheets). A content-type label in a set that is otherwise topic-based. It is the only label of its kind.
- **Feedback: Agents** on Overview of Listing Presentations (CRMLS, Reports). This is a conversation triage tag, not a content label; it says nothing about what the article covers.
- **Search for Open Houses** (both MLSs, Search / Filters) carries two labels for one idea, "How To: Open House" and "How to: Search (Open House)", with different casing.
- **Using the Draw Filter** (CRMLS draft, Search / Filters) carries three overlapping labels: "How To: Search", "How to: Search (Filters)", and "How To: Filters".
- **Bulk Upload Contacts** (both MLSs) carries "Client Contacts" and "How To: Contacts", which overlap.
- **Sibling inconsistency:** AI Scribe is the only Listing Maintenance article labeled "How To: Manage Listings"; Add and Edit Listings and Manage Listings Page Overview, the two articles members actually ask about, carry nothing. The Days Active in the MLS Widget is the only Dashboard article in CRMLS with "How To: Dashboard"; the other six carry nothing. Universal Search Bar is labeled "How To: Search"; the other 13 Search articles in Baldwin are not.
- **Casing drift:** "How To:" and "How to:" both exist. Intercom treats them as different tags, which means a filter on one misses the other.

## Labels used on one MLS but not the other

Labels are workspace-wide, so the four shared articles that carry labels (Bulk Upload Contacts, Search for Open Houses, Understand Status and Activity Filter, Universal Search Bar) carry the same labels in both help centers. The differences come from MLS-specific articles:

| Only in Baldwin | Only in CRMLS |
|---|---|
| How To: Manage Listings (AI Scribe) | How To: Tags (Managing Tag Alerts, draft) |
| Roadmap (Upcoming Features) | How To: Listing Presentations (Overview of Listing Presentations) |
|  | Feedback: Agents (same article) |
|  | How To: Dashboard (The Days Active in the MLS Widget) |
|  | How to: Search (Filters) and How To: Filters (Using the Draw Filter, draft) |

## Labels in the workspace that touch neither help center

For completeness, tags on the other 250 articles (default help center and unfiled drafts): Agents (1), Mobile: Agents (2), Mobile: Client Collaboration/Messages (1), How To: Client Collaboration/Messages (1), How To: Shared Search (1), How To: Saved Searches (1), How to: Manage Listings (Listing details) (1), How To: Filters on two unfiled drafts, and "Cincy - How To: Articles" on 16 CincyMLS drafts. These show the same pattern: one-off labels applied to single articles, several of them conversation tags.

## Summary

- 14 of 208 mirrored articles (7 percent) carry any label; no collection is labeled consistently.
- 17 distinct labels are in use across the two help centers for what amounts to 8 topics.
- Two labels are not content labels at all (Roadmap, Feedback: Agents).
- Nothing in the current labels expresses MLS scope; the help center does that, and 26 articles sit in both.
- The proposed fix is in `docs/standards/fin-labeling.md`: a small controlled vocabulary applied to every article, derived from the collection and the Notion row, with a migration table from these 17 labels.
