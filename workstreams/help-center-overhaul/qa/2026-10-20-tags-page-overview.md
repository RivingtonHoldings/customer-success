# QA: Tags Page Overview

- Article: Tags Page Overview (title unchanged)
- Sources: live Baldwin article, Intercom ID 14465546, content ID 16914937, mirror `docs/help-center/baldwin/tags-page-overview.md`. No old Master Article List page supplied. Product facts from Tara's answers and Tags page screenshot, October 20, 2026, plus facts recorded in `docs/product-context.md` and the Tag sibling QA files.
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-10-20-tags-page-overview-rewrite.md`
- Scored by Claude for Tara, October 20, 2026. Scorecard revision 2.
- Scope: option B (orientation plus the Tags page tour, which no sibling covers), chosen by Tara.

## Golden questions

| # | Factor | Old | New | Note |
|---|---|---|---|---|
| 1 | disambiguation | Pass | Pass | |
| 2 | visual_content_text | Fail | Pass | Both live images had alt text "image"; replaced by placeholders with alt text |
| 3 | undefined_terms | Fail | Pass | "public Tag pages" undefined; Tag and public link now defined in the opening |
| 4 | structured_enumeration | Pass | Pass | |
| 5 | query_answer_symmetry | Fail | Pass | "My Tags vs. client Tags", "Example of a Personal Tag" |
| 6 | self_contained_sections | Pass | Pass | |
| 7 | audience_specification | Pass | Pass | No role gate |
| 8 | entity_distribution | Pass | Pass | |
| 9 | semantic_chunk_boundaries | Fail | Pass | First section mixed sources and use cases |
| 10 | restate_questions | Pass | Pass | No tables |
| 11 | overview_jtbd | Fail | Pass | No opening paragraph |
| 12 | instruction_completeness | Pass | Pass | No Steps blocks |
| 13 | limitations_workarounds | Fail | Pass | Contact removal now linked to its route; Save Search entry point corrected |
| 14 | numerical_clarity | Pass | Pass | |

## Plain language gate

Pass. "My Tag", "Not Sent", and "Sent" are Status column readouts, quoted as the member reads them; "Client Tag" is the Create Tag toggle's wording. "Columns menu" is the settled term.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.6 | 30.0 | +21.4 |
| Chunk independence (25) | 20.8 | 20.8 | 0 |
| Answer completeness (25) | 14.3 | 25.0 | +10.7 |
| Fin-parsable formatting (10) | 7.5 | 10.0 | +2.5 |
| Accuracy and confidence (10) | 6.0 | 10.0 | +4.0 |
| Total | 57.2, Needs rewrite | 95.8, Fin-ready | +38.6 |

Chunk independence check 4 fails in the new draft too: five link or orientation paragraphs run one sentence, matching the sibling drafts.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| Can my client add listings to my tag? | Wrong: says clients add by reacting | Yes |
| Why is a listing still in my tag after it stopped matching my saved search? | Yes | Yes |
| What is the difference between a My Tag and a Client Tag? | Yes | Yes |
| What does Not Sent mean on my Tags page? | No | Yes |
| How do I sort or filter my tags? | No | Yes |
| Can I add a saved search to a tag when I save the search? | Wrong: says yes | Yes |
| Where can I see which tags a listing is in? | Partly | Yes |

## Open items

- Notion: https://app.notion.com/p/3ff8b9e0143881b0a4cce4d39512740b, created October 20, 2026.
- Tracker ID: TRK-101 (Tara, October 21, 2026), set in Notion. Article, Visual, and Video Due set to October 22, 2026, and reviewer and owners copied from Add Listings to a Tag, as assumptions; no dates were given.
- Live images, replace now: both August 5, 2026 images show a staff test account's email and phone, and the first shows a first name in the Tag name and message. They are live until the port.
- Truncated column: the Tags page screenshot cuts off a column between Last Modified and Actions (header begins "T"). The draft names no column list, so nothing depends on it.
- Gear icon right of the filter icon on the Tags page: purpose unknown, left out.
- Bare-deficit exception: the live article told members to link a saved search from the Save Search dialog. Tara cut the correction from this overview on October 20, 2026 as troubleshooting rather than overview content; it moved to Link a Saved Search to a Tag as "There is no Tag option when you save a search."
- Review round, October 20, 2026 (Tara): opening rewritten; What a Tag holds restructured, with the reaction exception in its own paragraph and "determines" for "decides".
- Workspaces: only the URL and the Invite to workspace button say "workspace" (Tara, October 20, 2026). The draft does not use the word. Revisit when the terminology changes.
- Left out on purpose, per Tara: the invited client's own Tags tab, mobile, and the Tags header counts (Tags, Invited, Uninvited).
- Video: live Loom 819fcb287f63406fb49f775ae5f33e19 kept at Tara's request.
- Collision: the mobile "Tags Overview" (14786075, Mobile collection) is a near-identical title. Recommend "Mobile" in its title when it is next touched.
- Set: Contacts Page Overview draft says listings shared through a Tag do not appear under Shared Listings; Tara confirmed October 20, 2026 that they do. Fixed in Notion and the repo draft the same day.
- Set: reports can no longer be created from a Tag (Tara, October 20, 2026). Live Create a Quick CMA Report has a "Start From Tags" section, and Create a Show Sheet and Create an Itinerary Report descriptions name Tags. All need fixing.
- Set: Dashboard Overview draft said clicking a Tag opens "the Tag page"; fixed to the public page in Notion and the repo draft, October 20, 2026. The live article still needs a port.
- Links point to live Baldwin URLs with live titles, per the set convention; update at port.
- Shared status: Baldwin mirror only. CRMLS has its own Tags Page Overview (8955795, draft state) describing a retired UI; the team should retire it when this ports. Row set to Baldwin and CRLMS All, matching the Tag set.
- Resolved October 20, 2026 (Tara): the Invite contacts to Tag and notify checkbox in the Share via Tag window also changes the status to Sent. With two routes, the statuses section says "inviting them changes it to Sent" and names neither button.
- Review round, October 20, 2026 (Tara): the second section became My Tags, Client Tags, and Tag statuses. Statuses are defined as invited to the Tag, matching the Invited and Uninvited labels, and Invite to workspace is named only at the click. The open-house My Tag example came back, written in second person.
- Review round, October 20, 2026 (Tara): statuses section reordered to lead with the Status column, because "A My Tag" read unnaturally. My Tag's purpose is in its bullet, and Client Tag is defined after the list. Kelly's comment on "My Tag" in the old lead is now hidden.
- Review round, October 20, 2026 (Tara): sort, filter, and columns section tightened, with "reverse the sort" and no My Tag filter example. Tara confirmed that the first header clicked gets sort order 1, the next 2, and so on.
- Review round, October 21, 2026 (Tara): Actions column section edited. Send covers Tags that already have contacts, and Resend states that every contact receives the email each time.
- Review round, October 21, 2026 (Tara): Where to find Tags was cut to where Tags appear. The widget sort line was dropped, and the Create Tag toggle is named in the Contacts bullet. The Listings widget tag icon is written as intended; its bug is tracked by Tara.
- Kelly's review, October 21, 2026: the heading changed to "Tag listings and find Tags across Perchwell", because members ask "how do I tag a listing". The opening and lead were updated to match. This section may now compete with Add Listings to a Tag for that question; it gives only routes and links out.
- Open team decision (Kelly, October 21, 2026): whether to keep "Members who came from a legacy platform may know Tags as Listing Carts." Kelly says Tags are now closer to a collaboration center. The sentence appears in all six Tag drafts, and New Terminology maps Listing Carts to Tags. Unchanged until the team decides.
