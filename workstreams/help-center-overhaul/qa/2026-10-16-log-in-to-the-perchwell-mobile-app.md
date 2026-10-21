# QA: Log In to the Perchwell Mobile App

- Article name: Log In to the Perchwell Mobile App (old title: How to Log in to the Perchwell Mobile App)
- Old Notion page: https://app.notion.com/p/3068b9e01438808e9a9fd82357faf3ec
- Intercom article ID 15280170, content ID 18095235
- Mirror: `docs/help-center/baldwin/how-to-log-in-to-the-perchwell-mobile-app.md` (Baldwin only, not shared with CRMLS). Live body and image read from Intercom `get_article`
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-10-16-log-in-to-the-perchwell-mobile-app-rewrite.md`
- New Notion page: https://app.notion.com/p/3fb8b9e014388159b8b8c7c557bdf6d4
- Scored by Claude for Kevin, October 16, 2026, against scorecard revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Fail | Pass | Live image had no alt text; replaced by a placeholder with alt text |
| 3 undefined_terms | Fail | Pass | Relevate and "Baldwin authentication page" were never explained; now "your Baldwin portal, Relevate", and SSO carries a which-means clause |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | "Before you start" and "Reminders" replaced with task headings |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | Baldwin Realtors members named in the opening; invited clients routed to their own article |
| 8 entity_distribution | Fail | Pass | Reminders never named the mobile app; every section now does |
| 9 semantic_chunk_boundaries | Fail | Pass | Reminders mixed three topics; split into email change and help |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | "Use this article" opening added |
| 12 instruction_completeness | Fail | Pass | Step 4 hid the username-and-password step; outcome now names the Search page |
| 13 limitations_workarounds | Fail | Pass | Download step added (iPhone and Android); "contact Baldwin Realtors" now gives the phone and email |
| 14 numerical_clarity | Pass | Pass | |

## Plain language gate

Pass on the rewrite. No do-not-list terms. "Baldwin portal" matches the Login and Troubleshooting FAQ draft; "Relevate" is kept beside it because members and the live articles call it that. "Tap" follows the live mobile articles. "Can't log in" is a condition, not the banned permissive "you can".

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 12.9 | 30.0 | +17.1 |
| Chunk independence (25) | 8.3 | 25.0 | +16.7 |
| Answer completeness (25) | 14.3 | 25.0 | +10.7 |
| Fin-parsable formatting (10) | 2.5 | 10.0 | +7.5 |
| Accuracy and confidence (10) | 10.0 | 10.0 | 0.0 |
| Total | 48.0 | 100.0 | +52.0 |

Old: Not retrievable as written. New: Fin-ready, 14 of 14 golden questions, plain language gate passed, no `[confirm: ...]` markers.

Old failures: 152-character description that did not name the mobile app; no opening; H1 section headings; bare-noun headings; bold Continue; emoji callout with no label; horizontal rules; no alt text; "no separate password" and "keep your email current" each stated twice; step 4 combined several actions; no download step; no contact details; no links.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I log in to the Perchwell app on my phone? | Partly | Yes |
| Is there a Perchwell app for Android? | No | Yes |
| What email do I enter in the Perchwell app? | Yes | Yes |
| Do I need a separate Perchwell password for the app? | Yes | Yes |
| I changed my email, how do I log in to the app now? | Partly | Yes |
| Who do I contact if I can't log in to the Perchwell app? | Partly | Yes |
| I'm a client, how do I log in to the Perchwell app? | No | Yes |

## Open items

- **Replace the live screenshot now, not at transfer.** The published image is a printed handout from May 2026. It shows an event's WiFi network name and password, says the Android app is "coming in June" (now false), and carries an iPhone App Store QR code. No member identifiers. The draft drops it for a placeholder of the app's login screen.
- Kevin's product answers, October 16, 2026: the Android app is on Google Play; the app is named Perchwell in both stores; the first screen has an Email field and a Continue button; the Baldwin portal login page takes the Relevate username and password; the app opens to the Search page; members update their email in Relevate and contact MLS staff if that fails; Baldwin MLS staff are the contact; invited clients get one sentence and a link.
- Not answered, so left out: whether the app keeps a member logged in between sessions.
- Source conflict resolved: the live article said to update your email in Relevate; User Settings FAQs (16180793) says MLS staff manage emails. Kevin: update in Relevate, contact MLS staff if there are issues. User Settings FAQs should match when it is migrated.
- Links: Accept Your Agent's Perchwell Invitation (15521326) is stored with a default help center `/en/` URL; the draft links the `/baldwin/en/` form, so confirm it resolves at transfer. The FAQ link points at the live 14710265 URL under its new draft title, Login and Troubleshooting FAQ, which has not been ported yet.
- Title collision check: "Log In to Perchwell" is a Baldwin collection name; "Log In to the Perchwell Mobile App" adds the surface and matches no article, page, or collection. The Login and Troubleshooting FAQ draft answers "How do I log in to the Perchwell mobile app?" in two sentences and links here, so this article owns the steps.
- Properties: Collection User Settings (the live article's parent collection; the old row said General). Roles All Except Client. MLS/AOR Baldwin. Old row had no video.
- The Baldwin MLS staff phone and email are organization contacts, not member identifiers.
