# QA: MLS Rules and Compliance FAQ

Article name: MLS Rules and Compliance FAQ. Old title: Top Compliance Questions. The new title is the proposal from this migration; the teammate has not yet chosen between it and the old one.

Sources:

- Old Notion page: https://app.notion.com/p/3498b9e01438803e9ab2d905fa84c064 (Master Article List, last edited July 13, 2026). Body matches the live article apart from an `In this article:` line and one extra horizontal rule
- Intercom article ID 14710094, content ID 17269251. Live body checked with `get_article` October 15, 2026; it matches the mirror, last updated July 2, 2026
- Mirror: `docs/help-center/baldwin/top-compliance-questions.md` (Baldwin only)
- Sibling live articles read for conflicts: Most Common Questions Asked to MLS Staff (14710059), Listing Maintenance FAQ (15199904), Listing Statuses in Perchwell (14709241)
- New Notion draft: https://app.notion.com/p/3fa8b9e0143881d89687cd3a2590d212
- Sibling Notion draft read: Listing Maintenance FAQ (https://app.notion.com/p/3f88b9e0143881d7931ed6337abf85cf, fetched October 15, 2026)
- Product answers from Kevin, October 15, 2026: Coming Soon listings syndicate through the same channels and stay in Coming Soon for up to 30 days; enter a listing within 3 business days of obtaining all required signatures or authorization, with no 24-hour rule; VRM is disclosed in both Public and Agent remarks, with supporting documentation submitted to compliance; Limited Service listings are clearly identified so cooperating brokers understand their responsibilities; the orphaned sentence describes the Listing Date; reactivation rules go to MLS staff; Expired listings are relisted with Duplicate; the Add/Edit field is Equitable Interest with a Yes option; "Use GPS" is not in the product and is cut; Baldwin publishes no exact bedroom standards; Brokerage Exclusive is a listing type visible to the brokerage only; the Member Portal has no URL to link; the buyer agreement hedges stay

Scored by Claude for Kevin, October 15, 2026. Check set: September 10, 2026, revision 2.

## Merge from Most Common Questions Asked to MLS Staff, October 15, 2026

Most Common Questions Asked to MLS Staff (Intercom 14710059, mirror `docs/help-center/baldwin/most-common-questions-asked-to-mls-staff.md`, old Notion page https://app.notion.com/p/3498b9e0143880e89fa6fe457f10bcf0) was folded into this FAQ at Kevin's direction, after checking with the TRK-031 owner. It gets no row of its own and is to be deprecated when this FAQ is ported. Its live score was 53.4 (Needs rewrite), and it failed golden questions 3, 4, 11, 12, 13, and 14.

Six questions were added: Who can see Days on Market?, Which listing statuses accumulate Days on Market?, the two new construction questions under a new New construction questions group, the Rental type options, and comp-only listings. One existing answer changed on Kevin's answers: the compliance contact. The MLS entry deadline was briefly changed to 24 hours, then restored to 3 business days. The Equitable interest field label was corrected to the on-screen spelling from Kevin's screenshot, and the description now names new construction.

Product answers from Kevin for the merge: new construction does not accrue DOM for up to 365 days, and the agent changes Construction Status; all members and invited clients see DOM and CDOM; Active accrues DOM, Pending and Withdrawn do not; comp-only listings take FOR COMP PURPOSES ONLY in Agent remarks, with no compliance notification; Rental type offers Short term, Long term, and Vacation (screenshot); Garage is a subtype under Residential-Single Family; the contacts are info@baldwinrealtors.com, 251-947-3777, and the MLS direct line 251-270-0328.

Where the other 14 questions went:

| MLS Staff question | Where it lives now |
|---|---|
| Other class (Boat Slip, Fractional Ownership, Garage) | What Each Property Type Includes draft |
| Active New Construction status | What Each Listing Status Means draft, plus the legacy sentence here |
| DOM reset after Expired, Withdrawn, Canceled (two questions) | Already here |
| Equitable Interest Pending, VRM, Limited Service | Already here |
| Then vs. Now | Cut; the Then vs. Now collection carries it |
| Residential to Lease | Not yet placed. Belongs in the Listing Maintenance FAQ; Kevin confirmed a property type can be changed after submission |
| Invited client email address | Not yet placed. Belongs in the Client Collaboration FAQ |
| Area search | Not yet placed. Belongs in the Search FAQ, with the map tools link |

Rescore after the merge: 100.0, Fin-ready, on the same check set. The golden question gate holds at 14 of 14 only once the four markers below are resolved; until then, factor 14 (numerical clarity) is pending on the 365-day question.

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | **Fail** | Pass | Old had an orphaned "This is the date ..." with no heading for "This". New gives it a What is the Listing Date? question |
| 2 visual_content_text | Pass | Pass | No images in either |
| 3 undefined_terms | **Fail** | Pass | Old used ANSI undefined. New defines DOM, CDOM, AUC, VRM, and ANSI |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Pass | Pass | Question headings in both |
| 6 self_contained_sections | **Fail** | Pass | Old answers opened with "This is considered ..." and depended on the heading. New answers name their subject |
| 7 audience_specification | Pass | Pass | Every answer applies to all non-client roles |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | **Fail** | Pass | Old put the Listing Date inside the CDOM answer and the Listing Agreement Date under Coming Soon. New groups both under Listing entry questions |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | **Fail** | Pass | Old had no opening paragraph. New uses the single-job opening for a many-question FAQ |
| 12 instruction_completeness | Pass | Pass | Old "copy/cloned" had no route; new links the Listing Maintenance FAQ for Duplicate |
| 13 limitations_workarounds | **Fail** | Pass | Old "depending on timing and rules". New sends the member to Baldwin MLS staff to confirm |
| 14 numerical_clarity | **Fail** | Pass | Old omitted the 30-day Coming Soon limit and gave a deadline that conflicts with another live article. New states 30 days and the confirmed deadline. Bedroom "minimum size" stays unnumbered, because Baldwin publishes no standard (see Open items) |

Old: 7 of 14. New: 14 of 14, with no `[confirm: ...]` markers.

## Plain language gate

Old: Pass. No term from the do-not list. "copy/cloned" is a legacy label, which new handles with the legacy-platform sentence.

New: Pass. Checks 1 through 5 clear. Check 5: "advertise", "enter", "duplicate", "relist" (as "back on the market"), "amend", and "contact" each appear in the answer that covers them.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 12.86 | 30.00 | +17.14 |
| Chunk independence (25) | 8.33 | 25.00 | +16.67 |
| Answer completeness (25) | 10.71 | 25.00 | +14.29 |
| Fin-parsable formatting (10) | 7.50 | 10.00 | +2.50 |
| Accuracy and confidence (10) | 4.00 | 10.00 | +6.00 |
| **Total** | **43.40** | **100.00** | **+56.60** |

Old band: Not retrievable as written. New band: Fin-ready.

Old failures by dimension:

- Retrieval: "Top Compliance Questions" does not follow the "\<Area\> FAQ" pattern; description is 104 characters, uses the "In this article" form, and does not name the area; no opening paragraph; answers such as "No. This is considered branding" do not echo the question
- Chunk independence: answers fall back to "This"; the Listing Date sentence sits inside the CDOM answer; every group heading is an H1
- Answer completeness: reactivation "depending on timing and rules" with no route; Coming Soon 30-day limit missing; ANSI undefined; nothing linked
- Formatting: bold on values and phrases throughout; horizontal rules between groups
- Accuracy: Coming Soon "not syndicated to public websites", the entry deadline's 24-hour rule, and "disclosed in remarks" for VRM all contradicted other live articles and were wrong; "You can upload"

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| Will my Coming Soon listing show up on public websites? | No, and its answer was wrong | Yes |
| How long can a listing stay Coming Soon? | No | Yes |
| How long does a withdrawn listing have to be off market before DOM resets? | Yes | Yes |
| How many days do I have to enter a listing in the MLS? | Yes, with the wrong rule | Yes |
| Who do I contact about a compliance violation email? | No | Yes |
| What is the Listing Date? | No | Yes |
| How do I relist an expired listing with DOM at zero? | Partly; "copy/cloned" with no route | Yes, with the Listing Maintenance FAQ link |
| Can I put my phone number in public remarks? | Split across two questions | Yes |
| Can my clients see days on market? | No (MLS Staff article: wrong, named a legacy platform) | Yes |
| How do I stop DOM counting on a new construction listing? | No (MLS Staff article: 180 days, wrong) | Yes |
| What's the difference between short term and long term rental? | Split across three questions in the MLS Staff article | Yes |
| How do I enter a closed listing just for comps? | Partly; no field named, no outcome | Yes, with one marker |

## Open items

- **Title.** MLS Rules and Compliance FAQ is proposed; the old title is Top Compliance Questions. The teammate has not chosen. Collision check: no mirror article, Perchwell page, or collection uses "rules and compliance"
- **The live article is wrong today.** It tells members and Fin that Coming Soon listings are not syndicated to public websites. Until this draft is ported, Fin may give that answer
- **Listing Maintenance FAQ draft.** Its Coming Soon answer now overlaps this article. Recommended: cut it to "the Coming Soon rules are unchanged in Perchwell" plus a link here, so the 30-day, marketing, and syndication facts have one home
- **Entry deadline, settled.** Kevin answered "24 hours" during the merge, then confirmed the same day that the rule is 3 business days of obtaining all required signatures or authorization, with no 24-hour rule. The draft says 3 business days, and the marker is removed
- **Open markers from the merge:** whether DOM and CDOM appear on public websites (the live MLS Staff article said never syndicated); whether DOM starts at zero when Construction Status changes; what happens at 365 days with Construction Status still Under Construction; the name of the status field in Add/Edit for comp-only listings
- **Compliance contact.** Replaced Compliance@BaldwinRealtors.com and 251-270-2725 with info@baldwinrealtors.com, 251-947-3777, and 251-270-0328 on Kevin's answer. Confirm these are the right contacts for a compliance email rather than general MLS contacts. The Search FAQ draft gives mls@baldwinrealtors.com for the same direct line
- **Deprecate Most Common Questions Asked to MLS Staff (14710059)** when this FAQ is ported, and redirect it here. Until then the live article tells members and Fin that DOM is viewable only in a legacy platform and that new construction pauses DOM for 180 days, both wrong
- **Three MLS Staff questions still need homes** in the Listing Maintenance, Client Collaboration, and Search FAQ drafts; see the table above
- **Status spelling across the set.** This FAQ writes Cancelled and Coming Soon; What Each Listing Status Means writes Canceled and Coming soon, the on-screen forms. Settle by counting across the set
- **Listing Statuses in Perchwell** (live) defines Coming Soon as "The purchase agreement has been fulfilled and the title transferred", which reads as the Closed definition. Its Active New Construction row says 365 days, while the MLS Staff article says 180. Neither is in this article; both are worth fixing in their own migrations
- **Compliance contact question** was added from the MLS Staff article, so the member who is told to contact MLS staff has the details in this article. Its contacts were replaced in the merge; see the compliance contact item above
- **Legacy-platform sentence** for Equitable Interest Pending comes from the MLS Staff article's "What happened to the Equitable Interest Pending status?"
- **Bedroom standards** stay hedged ("generally", "standards such as") with no numbers, because Baldwin publishes no exact standard, per Kevin. The buyer agreement hedges ("Generally no", "Typically no") stay by request
- **"Can I use 'Use GPS' in directions?"** was cut; the control is not in the product
- **Member Portal** has no URL to link
- **"Specific timeframes"** in the buyer agreement list became "specific time periods", since timeframe is reserved for Hot Sheets
