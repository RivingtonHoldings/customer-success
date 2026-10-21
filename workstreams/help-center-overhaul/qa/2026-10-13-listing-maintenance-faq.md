# QA: Listing Maintenance FAQ

- **Article:** Listing Maintenance FAQ (title unchanged)
- **Sources:** live Intercom article 15199904, content ID 17969584, read with `get_article` on October 13, 2026 (updated about October 6, 2026, newer than the mirror). Mirror: `docs/help-center/baldwin/listing-maintenance-faq.md` (synced September 4, 2026, stale). No old Master Article List row. Sibling: Add and Edit Listings Notion draft.
- **Product answers:** teammate, October 13, 2026: Expired listings can be duplicated (the old restriction was a bug); the section is Property Details; Add saves open house remarks; the MAAR push is still suspended; Autofill wording matches the sibling; "property description" means Public remarks; the FSBO homeowner field is Agent remarks; mobile path is More, then Manage Listings; multiple listings can be duplicated at once.
- **Scored by:** Claude for Kevin, October 13, 2026
- **Scorecard:** September 10, 2026 check set, revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Fail | Pass | Old "in the last 3 fields:" ended in a colon pointing at an image |
| 2 visual_content_text | Fail | Pass | Three images had no alt text; all now carry alt text, plus one placeholder with alt text |
| 3 undefined_terms | Fail | Pass | MAAR, CRS, and Ocusell were undefined; MAAR defined, CRS kept only in the legacy name, vendor name dropped |
| 4 structured_enumeration | Fail | Pass | Duplicate steps were prose |
| 5 query_answer_symmetry | Pass | Pass | Question headings |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | Opening now states the broker or full-access agent audience, matching Add and Edit Listings |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | No opening paragraph in the old article |
| 12 instruction_completeness | Fail | Pass | Virtual tour steps stopped at the fields; every Steps block now ends with its outcome |
| 13 limitations_workarounds | Pass | Pass | MAAR workaround stated |
| 14 numerical_clarity | Pass | Pass | No MAAR restore date exists yet, so none is stated |

Old: 8 of 14. New: 14 of 14.

## Plain language gate

Pass. No do-not-list terms. "Push" and "syndicate" are kept as words agents use; "push" is the source's own word and the term members may type about MAAR.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 17.1 (4/7: no description length, no opening, no heading echo, duplicated heading) | 30.0 | +12.9 |
| Chunk independence (25) | 8.3 (2/6: one-line paragraphs, all H1, facts stated twice) | 25.0 | +16.7 |
| Answer completeness (25) | 14.3 (4/7: steps without outcome, undefined terms, no links) | 25.0 | +10.7 |
| Fin-parsable formatting (10) | 5.0 (4/8: prose steps, bold, no alt text, horizontal rule) | 10.0 | +5.0 |
| Accuracy and confidence (10) | 2.0 (1/5: wrong labels, "streamline", Paragon named, "you can") | 10.0 | +8.0 |
| **Total** | **46.7, Not retrievable as written** | **100.0, Fin-ready** | **+53.3** |

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| Can I duplicate an expired listing? | No (said it could not) | Yes |
| Can I duplicate more than one listing at once? | No | Yes |
| Where do I put a Matterport link on my listing? | Yes, with wrong field labels | Yes |
| How many characters can public remarks be? | Yes | Yes |
| How do I change the remarks on my open house? | Partly, no steps | Yes |
| How do I get to my listings in the Perchwell app? | No, wrong label (My Listings) | Yes |
| How long can a listing stay Coming Soon? | Yes | Yes |
| Will my Baldwin listing go to the Mobile MLS? | Yes | Yes |

## Open items

- Resolved October 13, 2026: Add confirms the open house save; "Mobile Alabama MLS (MAAR)" stays as written; no restore date for the MAAR push yet. For the peer reviewer: check in the product that Add on an existing open house updates it rather than adding a second one.
- The virtual tour labeled list describes Unbranded and Branded from the labels alone; confirm no MLS rule on branded links belongs here.
- Matrix is named as MAAR's listing system. It is not a platform Baldwin members came from, so it was kept; confirm.
- The live Manage Listings screenshot shows street addresses of draft listings. Listing data, not member identifiers; replace if the team prefers.
- Sibling claims to fix: Add and Edit Listings (Notion) spells the fields Virtual Tour #1, Virtual Tour #2, Branded Virtual Tour in a "Property Detail" section; the screen reads Virtual tour #1 (Unbranded), Virtual tour #2 (Unbranded), Branded virtual tour in Property Details. The repo draft of Manage Listings Page Overview says Expired listings cannot be duplicated, which is now wrong.
- Audience wording differs across siblings: "an agent with full access" (Add and Edit Listings) and "an agent with permission to manage listings" (Manage Listings Page Overview). This FAQ follows Add and Edit Listings; the set should settle on one.
- Mirror is stale for this article; run `/sync-help-center`.
