# QA: Share Listings with Clients from Search

- Article name: Share Listings with Clients from Search
- Old titles: Share Multiple Listings in Perchwell (Intercom); How to Share Multiple Listings Without Client Access to Perchwell (old Notion row)
- Old Notion page: https://app.notion.com/p/2f68b9e0143880a1be92e664408b6145
- Intercom article ID 13903326, content ID 16154688
- Mirror: `docs/help-center/baldwin/share-multiple-listings-in-perchwell.md` (Baldwin only, not shared with CRMLS)
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-10-06-share-listings-with-clients-from-search-rewrite.md`
- Scored by Claude with Tara, October 6, 2026. Check set: September 10, 2026, revision 2

## Source note

The live article and the old Notion page both described a Share window with Email, Text, and Public Link tabs. Tara's screenshots of October 6, 2026 show a redesigned window: a via Tag section and a via Public Link section, where Email or Text opens a second window with Email and Text tabs. The screenshots won. The Text tab labels also changed: Select a contact, Create Contact, and Send Text replace Select or create new contact, New Contact, and Share Listings.

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Fail | Pass | Old used emoji pointers |
| 2 visual_content_text | Fail | Pass | Old images had the alt text "image"; new placeholders carry alt text |
| 3 undefined_terms | Pass | Pass | CC and BCC defined in the new draft |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Pass | Pass | |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | Silence; Roles property records All Except Client |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | Old had no opening paragraph |
| 12 instruction_completeness | Fail | Pass | Old steps stopped at choosing a tab and at Share Listings |
| 13 limitations_workarounds | Pass | Pass | |
| 14 numerical_clarity | Pass | Pass | Sending hours hedged to match the source |

## Plain language gate

New: Pass. No terms from the do-not list. "via Tag", "via Public Link", and "Copy sharable link" are on-screen labels, named only where the member acts on them.

## Dimension scores

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 17.1 (4/7: description 186 characters, no opening, "Tips" heading and no echo) | 30.0 (7/7) | +12.9 |
| Chunk independence (25) | 16.7 (4/6: H1 used for sections, Tips repeats facts) | 25.0 (6/6) | +8.3 |
| Answer completeness (25) | 21.4 (6/7: steps stop at the last click) | 25.0 (7/7) | +3.6 |
| Fin-parsable formatting (10) | 3.75 (3/8: step periods, "Good to know" labels, bold, emoji, alt text) | 10.0 (8/8) | +6.25 |
| Accuracy and confidence (10) | 6.0 (3/5: "makes it easy to browse", "you can") | 10.0 (5/5) | +4.0 |
| Total | 65.0, Needs rewrite | 100.0, Fin-ready | +35.0 |

The old score does not count the fact that the live article describes a Share window that no longer exists. The scorecard measures sourcing, not currency, so the old article is worse than 65 suggests.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I share listings with a client who doesn't have Perchwell? | Partly (Public Link section) | Yes |
| How do I copy a link to listings? | Yes, with an outdated control | Yes |
| How do I text listings to a client? | Yes, with an outdated path | Yes |
| Why can't I select a contact when texting listings? | Yes | Yes |
| What time do listing texts send? | Yes | Yes |
| Can my client see the listing agent's information? | Yes | Yes |
| Can I use a template when emailing listings? | Partly (link only) | Yes |
| How do I share listings on Facebook? | No | Yes |

## Open items

- Facebook, LinkedIn, and X each open a new post with the public link, confirmed by Tara October 7, 2026
- Share via Text confirmed October 7, 2026: it opens a Share window on the Text tab. That window has four tabs (Email, Text, Tags, Public link), unlike the two-section Share 1 Listing window. The draft documents the UI as it is today and names Share via Text only as a shortcut to the Text tab. Tara asked the product team on October 7, 2026 whether the Share via Text window will be updated; no answer yet. If it changes, recheck the Text section and its screenshot
- Sending hours are approximate per Tara (about 8am and 8pm, in the member's time zone). The draft keeps the hedge rather than stating exact times; numerical clarity passes on the source, but product may want to state the exact window
- Title collision to note: CRMLS has "Sharing Listings with Clients" in its own help center
- Message Clients in Perchwell link points at the default help center (`/en/`); flag at transfer
- The old Notion page's Loom (b39567cba22e48ae8944d27de72930c5) shows RLS, not Baldwin, per Tara. Replaced with a video placeholder
- Search Page Overview draft describes this article as covering "email, text message (SMS), or public link" and links the old title; update the link text after transfer
- Live Multi-Listing Actions on the Search Page still says Share sends "by Email or generate a Public Link"; needs its own pass
- Pending Tara (product): whether the YES opt-in for texts applies per phone number across Perchwell or per agent. The draft keeps the source wording, "The first time you text a new number", until that is answered
- Reviewed October 7, 2026: a second reviewer's tightening pass was merged; edits that dropped the invited-client condition, the icon shape, "greyed out", or the clear-the-box clause, or that added "you can" or an unsourced contacts-only rule, were not taken
