# QA: Client Collaboration FAQ

Article name: Client Collaboration FAQ. Title unchanged.

Sources:

- Old Notion page: https://app.notion.com/p/3658b9e01438802ebe1fd9b383fa07e6 (Master Article List, last edited July 13, 2026), including Kelly Miragliotta's resolved comment on the listing agent question
- Intercom article ID 15201114, content ID 17971183, read with `get_article` on October 9, 2026. The live body was edited around October 6, after the mirror's September 14 sync
- Mirror: `docs/help-center/baldwin/client-collaboration-faq.md` (Baldwin only; not in the CRMLS mirror). Stale: it still carries the parallel-period sentences the live article removed
- Sibling sources: Notion drafts Message Clients in Perchwell, Share Listings with Clients from Search, Set Up Your Clients in Perchwell, Export Contacts to a CSV File; live articles Search FAQ (Bridge), Contacts Page Overview- Mobile, Accept Your Agent's Perchwell Invitation, How to Share a Tag, Share Multiple Listings in Perchwell
- New Notion draft: https://app.notion.com/p/3f48b9e014388188aa17c6b043449e91
- Teammate answers, October 9, 2026: contacts can be added in the mobile app; the CRM answer follows the Search FAQ; two questions from the old Notion page come back (login, invited client); title kept

Scored by Claude for Kevin Liang, October 9, 2026. Check set: September 10, 2026, revision 2.

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Pass | Pass | No images in either |
| 3 undefined_terms | **Fail** | Pass | Old used CRM undefined. New defines CRM and CSV on first use |
| 4 structured_enumeration | Pass | Pass | New lists invited-client capabilities and the two CRM routes as bullets |
| 5 query_answer_symmetry | Pass | Pass | Question headings in both |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | **Fail** | Pass | Old sent every member to Bridge; the feed is broker-only, now stated |
| 8 entity_distribution | **Fail** | Pass | Old answers such as "Not at this time." named nothing |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | **Fail** | Pass | Old had no opening paragraph |
| 12 instruction_completeness | Pass | Pass | No procedures; answers link to the workflow articles |
| 13 limitations_workarounds | **Fail** | Pass | Old "Not at this time" answers had no route forward. New gives Re-Share for Tags, the saved-search update behavior, and the Messages page for conversations |
| 14 numerical_clarity | Pass | Pass | 600 characters in both |

Old: 9 of 14. New: 14 of 14.

## Plain language gate

Old: **Fail**, on checks 1 and 3.

| Term flagged | Replacement |
|---|---|
| "the platform", in a heading | "Perchwell" |
| "contact interactions" | "conversations with clients" |
| "realtor" | "agent" |
| "Perchwell is not in the middle" | a plain statement of how contacts and listing data each reach a CRM |

New: **Pass**. Checks 1 to 5 clear. "appears" in the email answer has the system as its real subject.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.57 | 25.71 | +17.14 |
| Chunk independence (25) | 16.67 | 25.00 | +8.33 |
| Answer completeness (25) | 10.71 | 25.00 | +14.29 |
| Fin-parsable formatting (10) | 8.75 | 10.00 | +1.25 |
| Accuracy and confidence (10) | 4.00 | 10.00 | +6.00 |
| **Total** | **48.70** | **95.71** | **+47.01** |

Old band: Not retrievable as written. New band: Fin-ready.

Old failures: no description of length, no opening, a heading without the product name, answers that do not echo their heading (Retrieval 2 to 5); questions set as H1s, answers that drop the entity (Chunk 2, 5); Bridge role, bare deficits, CRM undefined, no links (Completeness 2, 4, 6, 7); bold Text (Formatting 3); a false "no" on mobile contacts and a typo that inverted the listing-agent answer, Paragon named, three "you can" (Accuracy 2, 4, 5).

The rewrite does not reach 100 because Retrieval check 1 fails on the `<Area> FAQ` title pattern, the open question already logged in `project-status.md` and recorded the same way for Dashboard FAQ.

## Fin test questions

| Question, as a member would type it | Old answers from one section | New answers from one section |
|---|---|---|
| do my clients need to log in to see listings I send | No | Yes |
| can I add a contact from the mobile app | No, and the old answer was wrong | Yes |
| can the listing agent see who I sent their listing to | Partial; the typo reads "contact your listing agent" | Yes |
| does my client get notified when I add listings to a tag | Yes, with no next step | Yes |
| how do I get my contacts into my CRM | Partial | Yes |
| will my clients keep getting their old saved search emails | Yes, by naming the legacy platform | Partial. The section no longer names the platform, so Fin matches on "saved search alerts" and "legacy platform" |
| is there an app for my clients | Yes | Yes |
| what email address do Perchwell emails come from | Yes | Yes |

## Open items

1. `[confirm: Perchwell has no direct CRM integration]`. The live article says only "Perchwell is not in the middle"; the draft states it plainly and marks it.
2. **Contacts Page Overview- Mobile wins over this FAQ.** The live FAQ has told members since May that contacts cannot be added from a phone. Confirmed wrong October 9, 2026.
3. **Bridge wording follows the Search FAQ.** The live answer here sent every member to Bridge; the Search FAQ says the feed is broker-only, free, and set up through MLS staff.
4. **Export Contacts to a CSV File has no live URL yet.** The CRM answer links its Notion draft; replace it at transfer.
5. **Old Notion questions left out:** the spouse email question (a product test was still open in May), the first-alert recap (unverified), the opted-out-contact question, and contact groups (owned by the Contacts articles).
6. **Set overlap.** The texting answer restates two facts from the texting section of Share Multiple Listings and its draft replacement, Share Listings with Clients from Search. The FAQ keeps a short answer and links out.
7. **Links use the Baldwin help center form.** Seven mirror entries (Invite Clients, Accept invitation, Message Clients, Set Up Email Alerts, Add an Invited Client, Contacts Page Overview- Mobile, Share Multiple Listings) show `/en/` URLs; `/port-to-intercom` checks the stored links.
8. **Manual after transfer:** Fin labels per `docs/standards/fin-labeling.md`, MLS audience, and publishing.
