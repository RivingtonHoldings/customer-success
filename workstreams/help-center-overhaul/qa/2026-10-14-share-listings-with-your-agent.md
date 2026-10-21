# QA: Share Listings with Your Agent

- **Article:** Share Listings with Your Agent (title unchanged)
- **Sources:** old Notion page https://app.notion.com/p/1e78b9e014388003b8c4fc128092b347; unpublished NYC + CRMLS page https://app.notion.com/p/3458b9e014388025a41ce6408eb21027; Intercom article 11373849, content 12304821; mirror `docs/help-center/baldwin/share-listings-with-your-agent.md` and `docs/help-center/crmls/share-listings-with-your-agent.md` (shared article); two screenshots from a test client account and the teammate's answers, October 14, 2026
- **Scored by:** Claude for Kevin, October 14, 2026, scorecard revision 2

## Golden questions

| # | Factor | Old | New | Note |
|---|---|---|---|---|
| 1 | disambiguation | Pass | Pass | |
| 2 | visual_content_text | Pass | Pass | Old had no images; new placeholders carry alt text |
| 3 | undefined_terms | Pass | Pass | New defines Messages, CC, and BCC in context |
| 4 | structured_enumeration | Pass | Pass | |
| 5 | query_answer_symmetry | Fail | Pass | Old: "Listing sharing purpose", "Send by Email" |
| 6 | self_contained_sections | Fail | Pass | Old Listing Detail Page email and Messages sections began at a menu option the reader had not opened |
| 7 | audience_specification | Fail | Pass | Old never said it is for invited clients |
| 8 | entity_distribution | Fail | Pass | Old subsections named neither listings nor the agent |
| 9 | semantic_chunk_boundaries | Fail | Pass | Old carried an unrelated Create communication templates section |
| 10 | restate_questions | Pass | Pass | No tables |
| 11 | overview_jtbd | Fail | Pass | |
| 12 | instruction_completeness | Fail | Pass | Old stopped at Email and Send |
| 13 | limitations_workarounds | Pass | Pass | |
| 14 | numerical_clarity | Pass | Pass | |

## Plain language gate

New: Pass. No do-not-list terms; "appear" in the Messages outcome has the listings as the subject, so it describes the system.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.6 (2/7) | 30.0 (7/7) | +21.4 |
| Chunk independence (25) | 8.3 (2/6) | 25.0 (6/6) | +16.7 |
| Answer completeness (25) | 10.7 (3/7) | 25.0 (7/7) | +14.3 |
| Fin-parsable formatting (10) | 6.3 (5/8) | 10.0 (8/8) | +3.7 |
| Accuracy and confidence (10) | 6.0 (3/5) | 10.0 (5/5) | +4.0 |
| **Total** | **39.9, Not retrievable as written** | **100.0, Fin-ready** | **+60.1** |

Old failures: description in the "In this article, you will learn" form; no "Use this article to" opening; bare and duplicated headings (Send by Email and Send by Messages twice each); section titles at H1; no outcomes after steps; no audience; horizontal rules and bolded UI labels; stale labels (Share via Email, Share via Messages, notepad icon, Start Conversation) that the October 14 screenshots show are gone.

## Fin test questions

| Question | Old, one section | New, one section |
|---|---|---|
| How do I send a listing to my agent? | No, labels out of date | Yes |
| How do I email listings to my agent from my search? | No, Share via Email no longer exists | Yes |
| Can I share a listing with my agent from the listing page? | No, Share and Send via Email are out of date | Yes |
| How do I send my agent a home in Messages? | No, labels out of date | Yes |
| Does my agent get notified when I share a listing? | No | Yes |
| Can I CC someone when I email listings? | No | Yes |
| Where do the listings I share in Messages show up? | Partly, "your conversation thread" | Yes, Shared properties |
| How do I share just one listing from the preview? | No | Yes |

## Open items

- `[confirm: Share via email opens the same Share window, on the Email tab]`. Resolved in part October 14, 2026: a client screenshot of the Listing Detail Page Actions menu shows a Share group with Share via email, Copy public link, and Send as in-app message, then Add to: Tag, then Create: Print full report. The window Share via email opens was not shown.
- Resolved October 14, 2026: from search results, Actions, then Share, opens the Share window directly on the Email tab for an invited client (teammate confirmed).
- Copy public link and Add to Tag are in the client's Listing Detail Page Actions menu and are not covered.
- Share via Text and Contact Agent are in the client's Actions menu and are not covered. Decide whether texting listings to the agent belongs in this article; what the client experience is (consent message, 600-character limit, sender number) has not been checked.
- Select a template and Create contact sit in the client's Share window. Left out because neither has been checked for clients.
- Character limit on the Include a message field: 1,000 on the agent side, not checked for clients, so not stated.
- Video: the live Loom (https://www.loom.com/embed/157b29ff2327430396881190dfe8028d) and the old Notion Arcade (https://app.arcade.software/share/0TAXLJjsebpNZr2VUrYT) were both made with the old labels, so the draft carries a video placeholder. Check whether either can be kept.
- Cut: the Create communication templates section and its Loom (https://www.loom.com/embed/f92ed88f2280493ba8da298ea7ad9ce6). It describes an agent feature in User Settings that has its own article.
- No legacy-platform sentence. The legacy mapping (CollabLink) describes how agents shared; this article's readers are clients.
- Shared article: Intercom serves it in Baldwin Client Experience and CRMLS Client Collaboration / Invited Clients. The row takes both MLS/AOR values. Cross-links point at the Baldwin help center.
- The client screenshot of the Actions menu shows a profile photo in the upper right. Capture the final screenshots from a test client account with no real face or name.
