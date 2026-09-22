# QA: Open Your MLS Integrations from the Dashboard

Old title: Integration Tools on the Dashboard. Retitled 2026-09-22 by Tara. Scored by Claude on 2026-09-21, check set revision 2, at Tara's request; rescored 2026-09-22 after the retitle.

## Sources

| Source | Reference |
|---|---|
| Old Notion page | https://app.notion.com/p/30a8b9e01438800c8c14d12b92c67987 (Master Article List) |
| Intercom article | 13903183, content ID 16154445 |
| Mirror | `docs/help-center/baldwin/integration-tools-on-the-dashboard.md` |
| Screenshots | Dashboard panel revealed, Dashboard panel collapsed, listing Actions menu with Integrations open. Supplied by Tara 2026-09-21 |
| Sibling, desktop | `docs/help-center/baldwin/listing-detail-page-overview.md` (14074994) |
| Sibling, integrations | `docs/help-center/baldwin/offer-manager-integration.md` (16777012) |

## Golden questions

| # | Factor | Old | New | Note |
|---|---|---|---|---|
| 1 | disambiguation | Fail | Pass | "Use the list below" removed; the emoji callout is gone |
| 2 | visual_content_text | Pass | Pass | Old article had no images at all. New carries three placeholders with alt text |
| 3 | undefined_terms | Pass | Pass | RPR was defined; CRS is now defined as Courthouse Retrieval System |
| 4 | structured_enumeration | Pass | Pass | |
| 5 | query_answer_symmetry | Fail | Pass | Six bare-noun headings replaced with headings naming what each answers |
| 6 | self_contained_sections | Fail | Pass | Each section now names its surface |
| 7 | audience_specification | Pass | Pass | Silent in both; no role gates the workflow |
| 8 | entity_distribution | Pass | Pass | |
| 9 | semantic_chunk_boundaries | Pass | Pass | |
| 10 | restate_questions | Pass | Pass | No tables in either |
| 11 | overview_jtbd | Fail | Pass | The old article had no opening paragraph; its description used the banned "you will learn how to" form |
| 12 | instruction_completeness | Pass | Pass | |
| 13 | limitations_workarounds | Fail | Pass | Five "(when available)" hedges named nothing and offered no route. Removed |
| 14 | numerical_clarity | Fail | Pass | "Some integrations" twice, plus the five hedges |

Old gate: failed on 1, 5, 6, 11, 13, 14. New gate: 14 of 14 pass.

## Plain language gate

New article: pass, all five checks. The old article fails checks 1 and 5: "What you can do from Listing Details" as a heading, and "Use the list below to choose the right tool" as a lead.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 4.3 | 30.0 | +25.7 |
| Chunk independence (25) | 12.5 | 25.0 | +12.5 |
| Answer completeness (25) | 10.7 | 25.0 | +14.3 |
| Fin-parsable formatting (10) | 7.5 | 10.0 | +2.5 |
| Accuracy and confidence (10) | 4.0 | 10.0 | +6.0 |
| **Total** | **39.0** | **100.0** | **+61.0** |

Old band: Not retrievable as written. New band: Fin-ready.

**The retitle is what closed the last check.** Scored on 2026-09-21 the rewrite was 95.7, failing Retrieval signals 1: "Integration Tools on the Dashboard" names a thing rather than an outcome, and the same check fails on the old article. Tara retitled it on 2026-09-22 and cut the listing procedure down to a pointer, which is what makes the narrower title accurate. The article had grown a second co-equal `Steps:` block for the listing surface, and a title naming only the Dashboard would have under-described it.

The title landed in three moves, and the last two are worth recording because they turn on rules that pull against each other. "Open an Integration from the Dashboard" fixed the outcome problem but used a singular no on-screen label uses; the panel reads `Integrations`. "Open MLS Integrations from the Dashboard" fixed that and added a term members type, but introduced a compound noun no live article uses and could be read as integrations with the MLS rather than from it. The possessive settles both: it matches how every live article already phrases this ("the tools your MLS connects to Perchwell", "integrations your MLS has enabled for your account"), and "your" earns its place under the rule that keeps it where it separates the member's things from everyone else's.

Two knock-on edits the retitle forced:

- The first section heading was "Open an integration from the Dashboard", identical to the new title, which would have handed Fin two chunks with the same label. It is now "Open an integration from the Integrations panel".
- The opening paragraph promised three outcomes and now promises two, matching the two sections that deliver them. The listing section is a closing pointer with no matching item in the opening list, which the order rule allows: every item in the list needs a section, not the reverse.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I open ShowingTime from Perchwell? | Partly. Steps exist but never name an integration | Yes |
| Where are the integrations on the Dashboard? | Yes | Yes |
| What is CRS? | No. Not mentioned anywhere | Yes |
| Do I need a separate login for these tools? | Partly. The callout says "may require" | Yes |
| Does an integration open in a new tab or a new window? | No. The old article says new window, which is wrong | Yes |
| How do I open RPR for one specific listing? | No. The Listing Details section lists no tools | Partly. The section says where they are and names the tools, and sends the steps to Listing Detail Page Overview |
| Which integrations does my MLS give me? | No | Yes |

## Open items

1. **`[confirm: ...]` in the draft, one marker.** SentriLock is listed in the Dashboard integrations but does not appear in the current Baldwin panel. Tara asked to write it as though it belongs there while the team investigates. The marker names the claim itself, not a detail beside it.
2. **Screenshots are placeholders.** Three images exist and are attached to the session but have no stable URL yet, so the draft carries placeholders with their alt text. The listing screenshot must be the cropped version; the full-browser capture shows a listing address, the listing agent's photo and license number, and a bookmarks bar, and cannot go in the article or the repo.
3. **Collection settled as `Dashboard`** by Tara on 2026-09-22, and the title follows from it. Baldwin also has an `Integrations` collection (19737537) holding Dotloop Integration, ListTrac Integration, and Offer Manager Integration, which stays the alternative if the team revisits it.
4. **CRMLS has a twin article**, 13921493, titled "Integration Tools on the Dashboard", in its own `Dashboard` collection. It is a separate article, not a shared record, so the Baldwin retitle does not touch it and the pair now diverges by name until CRMLS is migrated.
5. **One inbound link uses the old title as its link text.** Offer Manager Integration (16777012) links here as "Integration Tools on the Dashboard". The link resolves by article ID so it will not break, but the text is stale and wants updating when that article is next touched.
6. **Two live Baldwin articles share the title "Listing Detail Page Overview":** 14074994, desktop, in Listing Maintenance, and 14784837, mobile, in Mobile. Identical titles put them in competition for the same query. The draft links 14074994, the desktop one, because that is the surface the screenshots show.
7. **Both Listing Detail Page Overview URLs are default help center links** (`/en/`, not `/baldwin/en/`), so they are flagged for confirmation at transfer per the linking standard.
8. **Sibling article 14074994 is stale on the same facts.** Its Integrations list reads RPR, ShowingTime, Sentrilock, InfoSparks, CRS integrations, Down Payment Resource. The current listing menu shows ShowingTime, CRS Property Report, Report a Listing, CRS Comparables, CRS Demographic, CRS Parcel Map, InfoSparks, RPR, RPR Market Trends, Dotloop, Offer Manager. Neither Sentrilock nor Down Payment Resource appears.
9. **The live Dashboard Overview carries the same SentriLock error.** It names ShowingTime, SentriLock, and RPR as commonly connected integrations. If SentriLock is not on the Baldwin panel, that article needs the same correction.
10. **Still manual after transfer:** Fin labels per `docs/standards/fin-labeling.md`, and MLS audience. The connector cannot write tags.
