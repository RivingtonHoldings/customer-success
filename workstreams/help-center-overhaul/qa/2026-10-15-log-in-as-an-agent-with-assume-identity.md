# QA: Log In as an Agent with Assume Identity

- Old title: Assume Identity
- Old Notion row: https://app.notion.com/p/3a58b9e0143880f588a5c2536cc825f1 (Master Article List, read only)
- Intercom article ID 16053168, content ID 19292838
- Mirror: `docs/help-center/baldwin/assume-identity.md` (Baldwin only, not shared)
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-10-15-log-in-as-an-agent-with-assume-identity-rewrite.md`
- Scored by Claude for Kevin, October 15, 2026, scorecard revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Fail | Pass | Old steps ended in bare colons before images; "the steps below" |
| 2 visual_content_text | Fail | Pass | No alt text on any of 11 images; every image and placeholder now carries alt text |
| 3 undefined_terms | Pass | Pass | Assume Identity defined with a which-means clause in the opening |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | Bold paragraphs instead of headings |
| 6 self_contained_sections | Fail | Pass | "Follow the instructions below" |
| 7 audience_specification | Pass | Pass | Each route names who uses it; Admin/Broker in Roles |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Fail | Pass | Old admin section mixed requesting permission, granting access, and logging in |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | Old opened with "What is Assuming Identity?" |
| 12 instruction_completeness | Fail | Pass | Each Steps block now ends with the Dashboard opening in the same tab, or the save and emails |
| 13 limitations_workarounds | Pass | Pass | Office-only list and web-only availability stated where met |
| 14 numerical_clarity | Pass | Pass | |

Old: 7 of 14. New: 14 of 14.

## Plain language gate

Pass. No do-not-list terms. "Can login as me", "Log in as", "Search users", "Search all", "Assume identity", and "Stop assuming identity" are control labels named where the member acts on them; the heading over the grant section says "log in as you" rather than the label. "Masquerading" is kept out per `docs/product-context.md`.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.6 (2/7) | 30.0 (7/7) | +21.4 |
| Chunk independence (25) | 8.3 (2/6) | 25.0 (6/6) | +16.7 |
| Answer completeness (25) | 17.9 (5/7) | 25.0 (7/7) | +7.1 |
| Fin-parsable formatting (10) | 1.3 (1/8) | 10.0 (8/8) | +8.7 |
| Accuracy and confidence (10) | 8.0 (4/5) | 10.0 (5/5) | +2.0 |
| Total | 44.0 | 100.0 | +56.0 |

Old band: Not retrievable as written. New band: Fin-ready, gate passed, one `[confirm: ...]` open.

Old failures: bare-noun title; description 170 characters in the "you will learn" form; no headings; list order (opening promised brokers then admins, body opened with setup); "below" reference; duplicated Stop assuming identity instruction; no outcomes after steps; emoji callouts, bold UI labels, horizontal rules, an em dash, no alt text; "allows", "can use", "you will be able to".

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I log in as one of my agents? | Partly | Yes |
| How do I let my assistant log in to my account? | Partly | Yes |
| Why can't I find an agent under Log in as? | No | Yes |
| How do I get back to my own account after assuming identity? | Yes | Yes |
| Can I assume identity on the mobile app? | No | Yes |
| Who gets an email when I give someone access to my account? | Yes | Yes |
| Can I add someone from another office to Can login as me? | No | Yes |
| Where do I land after I click Assume identity? | No | Yes |

## Source differences and decisions

- Live article wins over the old Notion row, which predates it: the row has no setup section and no admin step 4.
- Kevin answered eight product questions on October 15, 2026: office admins and MLS staff also see Assume identity on Agent details; Log in as lists only people who added you under Can login as me; the admin route is for an agent's or broker's admin and still needs the MLS request; Can login as me is office-only, takes multiple people, and saves automatically; landing is the Dashboard in the same tab; history stays a plain statement; nothing here works in the mobile app; title approved.
- MLS email corrected from `mls@baldwinreatls.com` (live typo) to `mls@baldwinrealtors.com`, confirmed by Kevin.
- Legacy-platform sentence omitted: New Terminology maps Paragon "Assume Identity" to Perchwell, but Perchwell's own button reads "Assume identity", so the member's word is already on screen.
- Live article contradicted itself: setup said the person granted access has "the same abilities as your account"; Things to Know said changes happen "within your permission level". The draft keeps only the permission-level sentence, which the Manage People FAQ draft also uses.
- Dropped one image: the admin route's profile-icon screenshot duplicated the grant section's step 1 image.

## Open items

- `[confirm: how to remove a person from the Can login as me list, such as clicking their name again or clicking an x]`
- "Admins for an agent or broker" is the draft's wording for Kevin's "agent or broker admin". Confirm the phrasing members would recognize, and whether that matches a role name in Manage People (the screenshot shows roles such as Agent L1 and Broker/Admin (Individual Office)).
- Whether a person granted Can login as me acts with their own permission level or the granting agent's (see the contradiction above).
- Privacy, replace now in the live article: the Agent details screenshot shows a real member's full name and office; the Search users screenshot shows a contact with an email address. The draft uses placeholders for both.
- Optional: two live images show a CS teammate's photo and MLS ID, and two show Kevin's name. Staff, not members; worth swapping when the screenshots are retaken.
- Set: the unpublished Intercom draft "Masquerade an Agent's Account" (8391759) covers the same task with labels the July screenshots no longer show. Recommend marking it Deprecated rather than migrating.
- Set: the Manage People FAQ draft (Notion, October 15) says "Brokers and admins can assume an agent's identity" and that a broker does it from Manage People. Office admins and MLS staff also have the Manage People route; offered as a fix. It also writes "Assume Identity button"; the button reads "Assume identity".
