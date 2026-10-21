# QA: Login and Troubleshooting FAQ

- Article name: Login and Troubleshooting FAQ (old title: Login, Access & Troubleshooting Guide and FAQ)
- Old Notion page: https://app.notion.com/p/3498b9e0143880d885bacbeaba5d0b2f
- Intercom article ID 14710265, content ID 17269443
- Mirror: `docs/help-center/baldwin/login-access-troubleshooting-guide-and-faq.md` (Baldwin only, not shared with CRMLS). Live body read from Intercom `get_article`, since the mirror file was synced September 4, 2026
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-10-15-login-and-troubleshooting-faq-rewrite.md`
- New Notion page: https://app.notion.com/p/3fa8b9e0143881669ae2e6c1b983631c
- Scored by Claude for Kevin, October 15, 2026, against scorecard revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Fail | Pass | Old description pointed at "the table below" |
| 2 visual_content_text | Pass | Pass | Old had no images; new carries one placeholder with alt text |
| 3 undefined_terms | Fail | Pass | MMSI, BR, and DevTools were never defined; SSO now carries a which-means clause, and the Console and Network tabs are explained |
| 4 structured_enumeration | Fail | Pass | Troubleshooting checks were run-on prose; now lists and numbered steps |
| 5 query_answer_symmetry | Fail | Pass | "Reporting a Bug", "Clearing Cache and Cookies" became question headings |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | Opening now names Baldwin Realtors members, since the Baldwin portal login gates the workflow |
| 8 entity_distribution | Fail | Pass | "The platform" and "the site" replaced with Perchwell in every section |
| 9 semantic_chunk_boundaries | Pass | Pass | Blank pages and stuck loading merged into one question with ordered fixes |
| 10 restate_questions | Fail | Pass | The browser table had no intro sentence; it is now a labeled list |
| 11 overview_jtbd | Fail | Pass | "Use this article" opening added |
| 12 instruction_completeness | Fail | Pass | Desktop login now ends with Perchwell opening; bug report ends with sending the screenshots |
| 13 limitations_workarounds | Pass | Pass | |
| 14 numerical_clarity | Pass | Pass | 120% zoom kept |

## Plain language gate

Pass on the rewrite. No do-not-list terms. "Quick Links" and "Perchwell" are the on-screen labels in the Baldwin portal screenshot Kevin supplied; the article avoids "tile". "Display" stays in one H2 as the word members use for display problems.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.6 | 30.0 | +21.4 |
| Chunk independence (25) | 8.3 | 25.0 | +16.7 |
| Answer completeness (25) | 10.7 | 25.0 | +14.3 |
| Fin-parsable formatting (10) | 3.8 | 10.0 | +6.2 |
| Accuracy and confidence (10) | 8.0 | 10.0 | +2.0 |
| Total | 39.4 | 100.0 | +60.6 |

Old: Not retrievable as written. New: Fin-ready, 14 of 14 golden questions, plain language gate passed, with two `[confirm: ...]` markers to resolve before transfer.

Old failures: noun-phrase title; 200-character description that describes a table that is not there; no opening; three H1s; bold on every label and heading; horizontal rules; two em dashes; cache clearing explained in five places and Chrome recommended twice; troubleshooting written as five-sentence paragraphs; desktop steps stopping at the click; no links to the mobile login or training articles; "You can also".

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I log in to Perchwell? | Yes | Yes |
| Can I log in to Perchwell without Relevate? | Partly | Yes |
| Perchwell says I need to complete training before I can log in | No | Yes |
| Perchwell is stuck loading, what do I do? | Partly | Yes |
| How do I clear my cache in Safari? | Partly | Yes |
| My export won't download, what do I do? | No | Yes |
| Which browser should I use for Perchwell? | Yes | Yes |
| Who do I contact if something in Perchwell is broken? | No | Yes |

## Open items

- `[confirm: the Remove button in the Manage Website Data window]`: Kevin's Safari Privacy screenshot (October 15, 2026) shows Website data: Manage Website Data..., so the live article's "Remove Website Data" and "Remove All Website Data" were both stale. The window it opens was not captured. The draft clears perchwell.com only rather than Remove All, so members are not logged out of every website.
- Resolved October 15, 2026: Chrome pop-up route from Kevin's screenshots, ending in the Add a site window (Site field, Cancel and Add buttons). Safari's Websites tab lists the open Perchwell site as perchwell.com, so both browsers' steps name perchwell.com.
- `[confirm: the Allow option in Safari's Downloads list]`: Kevin confirmed Export CSV needs downloads allowed. Chrome has no per-site download setting on its Downloads page, so the article asks for downloads in Safari only. Safari's Websites tab lists Downloads and Pop-up Windows (screenshot, October 15, 2026); the options in the Downloads list were not captured. Safari lists only currently open websites, so the steps tell members to open Perchwell in Safari first.
- Resolved October 15, 2026: Safari Console and Network steps from Kevin (Settings, Advanced tab, Show features for web developers, then Cmd + Option + C). Bug report now has separate Chrome and Safari steps.
- Kevin's product answers, October 15, 2026: members always log in through the Baldwin portal (the perchwell.com fallback is cut); the mobile Continue button is current; required training still gates login; every question and bug goes to Baldwin MLS staff; Safari is supported, and Edge, Firefox, and Opera are not mentioned; "Multiple active sessions" and the whole frequent-logouts question are cut; the Email Delivery Issues section is cut; Print and Export CSV are what pop-up blocking affects; Console and Network screenshots stay.
- Scope: option A, one FAQ, taken by default since Kevin answered the product questions without choosing. Mobile login cut to two sentences and a link, because How to Log in to the Perchwell Mobile App (15280170) owns it.
- Cut as redundant: Chrome's DevTools Empty Cache and Hard Reload, Safari's Develop menu Empty Caches, Ctrl + F5, and the separate "Why does clearing cache fix so many issues?" question (its which-means now leads the cache answer).
- Sibling conflict: How to Complete Required Perchwell Training says to contact Perchwell Support if training is done and login still fails. Kevin's answer routes everything to Baldwin MLS staff. Fix the training article when it is migrated.
- The Baldwin MLS staff phone and email come from this article and User Settings FAQs (16180793). They are organization contacts, not member identifiers.
- Screenshot ready: Kevin supplied the Baldwin portal Quick Links screenshot in the session, and it shows no member names. Place it at the placeholder.
- Collection: the live article sits in FAQs & Cheat Sheets, and the old row said FAQs & What's Coming. Both map to FAQs. Roles: All Except Client (the old row had none; invited clients log in from their agent's invitation, not the Baldwin portal). MLS/AOR: Baldwin.
- Title collision check: "Log In to Perchwell" is a Baldwin collection name (User Settings / Log In to Perchwell), so it was not used as a title. "Login and Troubleshooting FAQ" matches no article, page, or collection.
- No other FAQ row in the new database answers these questions. User Settings FAQs (live, unmigrated) owns email changes and the assistant Dashboard-only question; this article links to it.
