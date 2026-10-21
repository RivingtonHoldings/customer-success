# QA: Tags in the Perchwell Mobile App

- **Article:** Tags in the Perchwell Mobile App. Old title: Tags Overview.
- **Sources:** live Intercom article 14786075, content 17381417 (Baldwin, Mobile collection), body confirmed current with `get_article`, October 21, 2026; mirror `docs/help-center/baldwin/tags-overview.md`; old Master Article List rows [Tags Overview on an Apple Device](https://app.notion.com/p/34f8b9e01438804fb6d8e86ee85e333d) and [Tags Overview on an Android Device](https://app.notion.com/p/37c8b9e014388005845bd9637e28d708), both word for word the live text, no video; the three live screenshots, read October 21, 2026; teammate product answers, October 21, 2026.
- **Sibling drafts read:** Search in the Perchwell Mobile App, Listing Detail Page in the Perchwell Mobile App, Mobile App FAQ; Tag facts from `docs/product-context.md` and the Tags set QA files.
- **Scored by:** Claude, for Kevin, October 21, 2026. Scorecard revision 2.

## Golden questions

| # | Factor | Old | New | Note |
|---|---|---|---|---|
| 1 | disambiguation | Pass | Pass | |
| 2 | visual_content_text | Fail | Pass | Live images had no alt text; placeholders carry alt text |
| 3 | undefined_terms | Pass | Pass | |
| 4 | structured_enumeration | Fail | Pass | Nested numbered sub-lists in steps were option lists |
| 5 | query_answer_symmetry | Fail | Pass | "Tips", "Tag Alert Management" were bare nouns |
| 6 | self_contained_sections | Fail | Pass | Configure Tag Alerts started at the three dots with no screen named |
| 7 | audience_specification | Pass | Pass | No role gates the workflow |
| 8 | entity_distribution | Fail | Pass | No heading named the mobile app |
| 9 | semantic_chunk_boundaries | Fail | Pass | Alert email H1 held the Tag settings steps |
| 10 | restate_questions | Pass | Pass | No tables |
| 11 | overview_jtbd | Fail | Pass | No "Use this article to" opening |
| 12 | instruction_completeness | Fail | Pass | Share and alert steps stopped at the click |
| 13 | limitations_workarounds | Pass | Pass | |
| 14 | numerical_clarity | Pass | Pass | |

## Plain language gate

Pass. "Tag folder" and "tag alerts" capitalization fixed to Tag. "Tagged items", "My Tags", "Shared with client", and "Other Tags" are on-screen labels, named where the member meets them.

## Scores

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.6 (2/7) | 30.0 (7/7) | +21.4 |
| Chunk independence (25) | 8.3 (2/6) | 25.0 (6/6) | +16.7 |
| Answer completeness (25) | 10.7 (3/7) | 25.0 (7/7) | +14.3 |
| Fin-parsable formatting (10) | 2.5 (2/8) | 10.0 (8/8) | +7.5 |
| Accuracy and confidence (10) | 8.0 (4/5) | 10.0 (5/5) | +2.0 |
| **Total** | **38.1** | **100.0** | **+61.9** |

Old band: Not retrievable as written. New band: Fin-ready, gate passed; one `[confirm: ...]` marker must be resolved before transfer.

Old failures: title one word off Tags Page Overview; description opens "In this article"; no jobs opening; multiple H1s and H4s; bold, emoji tips, horizontal rules; no alt text; "Tag Alerts notify agents only" stated twice; Tag settings options repeated across two sections; no links to the Tag articles.

## Fin test questions

| Question | Old, one section | New, one section |
|---|---|---|
| How do I add a listing to a tag on my phone? | Yes | Yes |
| Can I add listings to more than one tag at once in the app? | No | Yes |
| How do I create a new tag in the Perchwell app? | Partly ("create a new one") | Yes |
| Where do I see the listings in my tags on mobile? | Yes, with steps that select by name | Yes |
| How do I copy a tag link in the app? | Yes | Yes |
| How do I turn off tag alerts on my phone? | Partly, in a tip | Yes |
| How do I delete a tag in the Perchwell app? | No, only named in a list | Yes |

## Source differences

The live article and both old rows are identical, so no source difference to settle. Where the teammate's answers differ from all three:

- Tapping a Tag's name selects it; it does not open the Tag. Steps rewritten.
- The listings open on a Tagged items page.
- My Tags has two lists, Shared with client and Other Tags.
- The bell icon toggles alerts. On the web Tags page the bell is a readout.
- The three-dots menu holds Edit tag, Turn off alerts, and Copy link.
- Adding listings notifies the Tag's contacts, while price and status alerts go to the agent only. The live article said only that Tag alerts notify agents.

## Open items

- Notion: https://app.notion.com/p/4008b9e0143881aeb69bff5765c91029, created October 21, 2026, as a Draft. Owners copied from the newest Mobile rows; no due dates or Tracker ID yet.

- `[confirm: the button that saves your changes]` on the Edit tag screen.
- Resolved by the teammate, October 21, 2026:
  - Tapping a Tag in the Add tag list adds the listings at once, with no finish button.
  - A Tag is under Shared with client once a client is added, whether or not it was sent.
  - Tag alerts go to the agent only.
  - The menu reads Turn on alerts when alerts are off.
  - The alerts on Edit tag are Price increase, Price decrease, and Status change. The live article's New Listings alert is gone.
  - Edit tag has Tag name, Alerts, and Information.
  - Delete Tag is in the lower left of Edit tag, and Delete confirms.
- Alerts are off by default on mobile (teammate, October 21, 2026). `docs/product-context.md` says Tag notifications start on in the browser's Create a new tag window. Confirm whether the two really differ, or whether one source is out of date.
- Still unanswered: what the Information section on Edit tag holds. The draft does not mention it.
- "A message confirms it" was dropped from the add outcome. It had no source; the teammate's "add a general message" meant a general outcome sentence.
- Duplicate: the live article lists Delete or Duplicate on Edit tag. Left out until confirmed. If it is gone, the bare-deficit exception may apply, since the live article promised it.
- Not yet answered: whether a Tag can be created without listings, sent to contacts, or have a listing removed, in the mobile app. Left out of the draft.
- Search mobile and Listing Detail Page mobile drafts link "How to Tag Individual Listings" for adding to a Tag. Once this article is live, they could link here instead.
- Links point at Notion drafts of Share a Tag with Clients and Create and Edit a Tag; replace with public URLs at transfer.
- Contact notification on add: the browser notifies only Tags under Invited. Confirm whether mobile follows the same rule, and narrow the outcome sentence if so.
- Legacy sentence: Kelly's open question on "Listing Carts" applies here too, as in the six Tag drafts.
- **Privacy, replace now:** all three live screenshots are published today. Group 94 lists Tags named for what look like client names; IMG_2323 and IMG_2324 show an agent's name, email, and photo, and a client-named Tag. Replace them in Intercom now, not at port.
- Shared status: the article sits in two parents (19615962, 19637741); the mirror shows Baldwin only.
