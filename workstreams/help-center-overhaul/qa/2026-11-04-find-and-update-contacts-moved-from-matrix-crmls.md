# QA: Find and Update Contacts Moved from Matrix (CRMLS)

Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-11-04-find-and-update-contacts-moved-from-matrix-crmls.md`. Mirrors the Baldwin article "Find and Update Contacts Moved from Paragon" (Baldwin record 14726035). Source: the Matrix doc "External Then vs Now: CRMLS Matrix → Perchwell". Tracker ID: TRK-133 (next free number at Tara's direction, Nov 4, 2026). Notion row name carries a "(CRMLS)" suffix for now. Original article title left blank in the master sheet: brand-new article.

## Checks run

- Title, description (121 characters), "Use this article to ..." opening, H1/H2/H3 levels, heading echo, `Steps:` block, outcome sentence, bullet list for the four share actions, "For more information:" list for three links, screenshot placeholder with alt text: pass.
- No em dashes, bold, horizontal rules, "you can": pass.
- Legacy platform named (Matrix), allowed for Then vs. Now: pass.
- Fin-readiness score and the 14 golden questions: not run. Three confirm markers remain.

## Differences from the Baldwin article, on purpose

- Baldwin says contacts "arrived uninvited" and that some moved without an email. The Matrix doc says contacts arrive with an email address and does not say whether they are invited, so the draft claims neither. The email section stays, marked, in case some contacts lack one; delete it if V6 confirms none do.
- Baldwin's "one-time transfer the week before your access date" is replaced by the doc's "start of your Perchwell member training", with a marker.
- Added from the doc's OneHome table: uninvited contacts can open shared listings with no login, and contacts can be invited one at a time, by CSV file, or up to 100 at once.
- Baldwin's Sample Emails link is dropped. No CRMLS version exists; it is optional article #8.

## Open items

| Marker | Question | Notes |
|---|---|---|
| V4 | Is the move one-time, and do later Matrix changes reach Perchwell? | Also on the hub and saved-search drafts |
| V6 | Does any moved contact lack an email address, and do contacts arrive uninvited? | Decides whether the add-email section stays |
| V10 | How does a member invite up to 100 contacts at once? | The doc states 100 with no route. It may be the CSV upload; confirm the number and the path |

## Judgment calls to confirm

- The Edit profile steps, the My Contacts tab, the Email column, and the lock after invitation come from Baldwin's Perchwell behavior and the CRMLS Create and Manage Your Contacts draft, not the Matrix doc. They need a CRMLS screenshot check.
- The lock list (first name, last name, email, phone) is from the CRMLS Create and Manage Your Contacts draft, which is more specific than Baldwin's "email address is locked".
- All three links point at published CRMLS records. Create and Manage Your Contacts also has a CRMLS draft (18232928) that will replace record 8955819 after the port; repoint then.

## Screenshots

One placeholder (My Contacts tab with moved contacts). `Media Update Needed` is set to Yes so the row reaches the production board.

## Fin test questions

1. Did my Matrix contacts move to Perchwell?
2. Why is a contact missing from my share list?
3. How do I invite my clients to Perchwell?
4. Can I invite many clients to Perchwell at once?
5. Can clients see listings I share without a Perchwell account?
6. How do I change a contact's email after inviting them?

## Review results, Nov 4, 2026

Scored by Claude against `docs/standards/fin-readiness-scorecard.md` (check set revision 2, plain language gate), after the draft-quality pass in `.claude/skills/article-rewrite`. Self-scored, so a second reviewer's read is still pending. New article: no old score to compare.

### Golden questions

| Factor | Result | Note |
|---|---|---|
| 1 disambiguation | Pass | No "this screen", "above", or emoji pointers. |
| 2 visual_content_text | Pass | Placeholders carry alt text. |
| 3 undefined_terms | Pass | Abbreviations defined at first use after review. |
| 4 structured_enumeration | Pass | Steps and sequences are numbered; sets are bulleted or tabled. |
| 5 query_answer_symmetry | Pass | Headings name what each section answers, per the house reading of factor 5. |
| 6 self_contained_sections | Pass | No dependence on earlier sections; navigation named where a step needs it. |
| 7 audience_specification | Pass | Open to all members; Notion Roles is All. Silence is correct. |
| 8 entity_distribution | Pass | Feature and product names repeat in each section. |
| 9 semantic_chunk_boundaries | Pass | One topic per section. |
| 10 restate_questions | Pass | Every table has an intro sentence. |
| 11 overview_jtbd | Pass | "Use this article to ..." opening. |
| 12 instruction_completeness | Pass | Each Steps block ends with an outcome sentence. |
| 13 limitations_workarounds | Pass | Gaps are stated once with the route forward, or marked. |
| 14 numerical_clarity | Pass | Exact numbers or a marker for unknowns. |

All 14 pass as drafted, with confirm markers still open. Markers must clear before the row moves to Ready to Transfer.

### Plain language gate

Pass. The "entry" in "listing entry" and "above" in "above your search results" are the product's own sense, not the banned one.

### Dimension scores (new article)

| Dimension | Checks passed | Score |
|---|---|---|
| Retrieval signals | 7 of 7 | 30.0 of 30 |
| Chunk independence | 6 of 6 | 25.0 of 25 |
| Answer completeness | 7 of 7 | 25.0 of 25 |
| Fin-parsable formatting | 8 of 8 | 10.0 of 10 |
| Accuracy and confidence | 5 of 5 | 10.0 of 10 |

Total 100.0 of 100, band Fin-ready. The score does not count open confirm markers against accuracy, so it will not move when they clear.

### Changes the review made

- Split a 27-word outcome sentence after the email steps.
- Defined CSV (comma-separated values) at first use (factor 3).

## Markers resolved, Nov 5, 2026

- Move timing (V4): same answer as the hub, one time. "Contacts moved in a one-time transfer ..." plus "Changes made in Matrix afterward are not in Perchwell" (an inference from one-time; confirm). Marker removed.

## Markers resolved, Nov 5, 2026

- Invite options (V10): Tara said bulk upload takes a CSV of 100 contacts at a time and asked for the section to be rewritten. Rewritten from the published CRMLS articles: Bulk Upload Contacts from a CSV File (upload no more than 100 contacts at a time; the invitation toggle during upload) and Invite Clients to Perchwell and Resend Invitations (invite from a profile; invite up to 100 selected contacts at once from the Actions menu with Invite to Perchwell). The Actions menu route is an addition to what Tara said; it is the route that fits contacts already moved to Perchwell, since bulk upload adds contacts and does not re-invite existing ones (the Upload Contacts window does not send invitations; the toggle does at upload). The link lines now describe each article by what it covers. Marker removed.
- Missing email (V6): Tara was unsure whether any moved contact lacks an email. The section no longer claims any did: "Add an email address to any contact that has none." The consequence (left out of the contact list) is Perchwell behavior from Baldwin and the CRMLS contacts drafts. Delete the whole section if migration confirms every contact has an email. The same open question remains on Review Your Data (V6).

## Contact markers resolved, Nov 5, 2026

- Uninvited: the Invite section now opens "Contacts moved from Matrix arrived uninvited, which means they do not have access to Perchwell until you invite them." (Tara; mirrors Baldwin). The Find section's field list now matches the Review Your Data hub, using the Transfer Guide's rule that only contacts with a valid first name, last name, and email address were imported.
- Consequence for the Add an email address section: if every moved contact has an email, the section applies to no moved contact. Tara chose to keep it earlier, before this source; revisit.

## Row name, Nov 5, 2026

The "(CRMLS)" suffix was removed from this article's Notion Article Name at Tara's request, so the row now carries the exact article title for the port. The master sheet's title columns were not changed.

## Contact fields reworded, Nov 5, 2026

- Same rewording as the hub for the field list. The Add an email address section stays, written conditionally ("any contact that has none"), with a marker: whether Matrix contacts without an email address moved. If they are excluded, delete the section; if they come over, keep it. The marker blocks the port until Tara confirms.

## Synced from Notion, Nov 5, 2026

Notion was ahead of the repo. Kelly is the Article Reviewer on all nine rows, Article Due is Nov 12, 2026, Article Status is Ready to Transfer, and Roles is All Except Client, all set by Tara or the team. Article Review Status is still Not Started; the CRMLS port needs Review Finished or Complete. Sam added the CRMLS screenshot. The contacts marker is cleared: Tara said contacts are handled as in Baldwin, so the Add an email address section follows Baldwin's wording (a contact that moved without an email; Perchwell requires one to create a contact). Marker removed.
