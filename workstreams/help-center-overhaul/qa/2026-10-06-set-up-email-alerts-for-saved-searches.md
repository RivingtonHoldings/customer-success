# QA: Set Up Email Alerts for Saved Searches

Title unchanged. Scored October 6, 2026 by Claude for Tara, against scorecard revision 2.

## Sources

- Old Notion page: https://app.notion.com/p/1c88b9e01438801f94aef8977a2c9ff4 (Master Article List, read only)
- Intercom article ID 11112420, content ID 11986197
- Mirror: `docs/help-center/baldwin/set-up-email-alerts-for-saved-searches.md` and `docs/help-center/crmls/set-up-email-alerts-for-saved-searches.md` (shared article, identical bodies)
- Tara's screenshots of the Edit Search window, October 6, 2026: Alerts off, Alerts on, Recipient dropdown open, Frequency Daily with Time of day open, Frequency Weekly with Day
- Tara's answers on October 6, 2026: Recipient and Frequency options, Day and Day of Month dropdowns, the New match tooltip, Price covering increases and drops, the icon names (Tara later confirmed neither the bell nor the pencil has a hover label, so the article names both by shape only), the Saved Searches button label, contacts receiving alerts without the see-and-edit toggle, and dropping the rollout duplicate-email note
- Example alert email image on the old Notion page, captured July 4, 2026
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-10-06-set-up-email-alerts-for-saved-searches-rewrite.md`

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Pass | Pass | Old had no images; new placeholders carry alt text |
| 3 undefined_terms | Pass | Pass | CC and BCC defined on first use |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | Old headings were bare nouns: Alert types, Alert recipients, Contact alerts |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | No role gate; silence |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables; Frequency options are a labeled list (Tara, October 6, 2026) |
| 11 overview_jtbd | Fail | Pass | Old article had no opening paragraph |
| 12 instruction_completeness | Fail | Pass | Old Alert settings steps stop at Update. New blocks state what Update does |
| 13 limitations_workarounds | Pass | Pass | |
| 14 numerical_clarity | Pass | Pass | Monthly days 29 to 31 send on the last day of a shorter month |

## Plain language gate

Pass. CC contact and BCC contact are exact on-screen labels on the Recipient dropdown, defined on first use. No term from the do-not list.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 12.9 (3/7: description over 140 characters, no opening, bare-noun headings, no heading echo) | 30.0 | +17.1 |
| Chunk independence (25) | 16.7 (4/6: sections at H1, "Contacts must be added" stated twice) | 25.0 | +8.3 |
| Answer completeness (25) | 14.3 (4/7: steps stop at Update, no defaults stated, no related links) | 25.0 | +10.7 |
| Fin-parsable formatting (10) | 6.3 (5/8: step labels wrong and one terminal period, bold throughout, horizontal rules) | 10.0 | +3.7 |
| Accuracy and confidence (10) | 8.0 (4/5: Search Settings, the alert type names, the recipient names, and the 1 to 28 day range no longer match the product) | 10.0 | +2.0 |
| **Total** | **58.2, Needs rewrite** | **100.0, Fin-ready** | **+41.8** |

No `[confirm: ...]` markers remain.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I set up email alerts on a saved search? | Partly; split across two sections with wrong labels | Yes |
| Can I get an alert when a listing's price goes up? | No; says Price Drop only | Yes |
| How do I send saved search alerts to my client without getting them myself? | Partly; option names are wrong | Yes |
| Can my client get a weekly email on Mondays? | Yes | Yes |
| Does my client need "Allow added contacts to see and edit this search" on to get alerts? | No | Yes |
| Why didn't my weekly alert include a listing that came back on the market? | No | Yes |
| What is the difference between CC contact and BCC contact? | No | Partly; spells out carbon copy and blind carbon copy and leaves the email behavior to common knowledge, by Tara's call |

## Open items

- Resolved by the team via Tara, October 6, 2026: a Monthly alert set to day 29, 30, or 31 sends on the last day of a shorter month. The Alerts toggle, like the bell, restores the previous alert settings when alerts were on before; the article now states this once for both.
- Resolved by Tara, October 6, 2026: Update saves the changes to the saved search; the bell turns green when alerts are on and defaults to Only me and Immediately, or to the last alert settings used; CC lists every recipient and BCC shows each recipient only their own address; Immediately checks every hour; Morning and Evening send around 8:00 AM and 8:00 PM; contacts cannot be created from the Contacts dropdown. The bell section and a route to creating a contact were added from these answers.
- Tara's revision, October 6, 2026, applied to Notion and the repo with fixes: bold bullet labels removed, the table intro sentence restored, CC and BCC spelled out again, step 7 changed back to "and", the section lead no longer says "receive" (it is 23 words and wrong for contact-only recipients), the duplicated "add contacts first" lead and toggle sentence collapsed, and the first-time settings stated once for the toggle and the bell (option a). Kept from her revision: the bell heading, "The bell turns green when alerts are on", "change the alert settings", "not sent as new matches", "adds an upcoming open house", the CC and BCC behavior as its own paragraph, and the "since the last alert" fact kept in the email section only.
- Shared article: the same Intercom article sits in both the Baldwin and CRMLS help centers. Proposed as one row with both MLS/AOR values, per the September 17, 2026 rule in `notion-publishing.md`.
- Video: the live Loom is carried as is; the team is re-recording videos. The old row's Arcade and second Loom are not carried.
- Neighbors carrying stale alert facts, for when they are next touched: Manage Your Saved Searches (Search Settings, Save button, alert type names), Search FAQ (alert type names), Set-up Automatic Emails and Search Alerts, and Set up Search Alert for a Status Change. The last two say "a more streamlined approach is coming soon", and the checkboxes may already be that approach.
