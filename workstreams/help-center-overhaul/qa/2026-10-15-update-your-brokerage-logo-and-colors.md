# QA: Update Your Brokerage Logo and Colors

- **Article:** Update Your Brokerage Logo and Colors
- **Old title:** Add Branding to a Brokerage
- **Old Notion page:** https://app.notion.com/p/1c78b9e0143880b1ab63ef75e659f2a9 (Master Article List, read only)
- **Intercom:** article 14057465, content 16369988, collection User Settings, Baldwin
- **Mirror:** `docs/help-center/baldwin/add-branding-to-a-brokerage.md` (mirror last run September 29, 2026; body checked against `get_article` on October 15, 2026, unchanged)
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-15-update-your-brokerage-logo-and-colors-rewrite.md`
- **Notion:** https://app.notion.com/p/3fa8b9e0143881dbb01ce096c18b27b9
- **Scored by:** Claude for Kevin, October 15, 2026, scorecard revision 2

## Golden questions

| # | Factor | Old | New | Note |
|---|---|---|---|---|
| 1 | disambiguation | Fail | Pass | "From this page" pointed back at the previous section |
| 2 | visual_content_text | Fail | Pass | Live images had no alt text; kept images and placeholders now carry it |
| 3 | undefined_terms | Fail | Pass | Hex code is now defined |
| 4 | structured_enumeration | Pass | Pass | |
| 5 | query_answer_symmetry | Fail | Pass | "Tips" was a bare noun heading |
| 6 | self_contained_sections | Fail | Pass | Color sections started at Edit Settings with no place named; each section now carries its own navigation |
| 7 | audience_specification | Fail | Pass | Broker admin gate stated in the opening and before the first steps |
| 8 | entity_distribution | Fail | Pass | Logo and email sections never named Branding or My brokerage |
| 9 | semantic_chunk_boundaries | Pass | Pass | |
| 10 | restate_questions | Pass | Pass | No tables |
| 11 | overview_jtbd | Fail | Pass | Live article had no opening paragraph |
| 12 | instruction_completeness | Fail | Pending | Live color steps had no save step. The logo outcome carries a confirm marker on whether it saves right away |
| 13 | limitations_workarounds | Pass | Pass | |
| 14 | numerical_clarity | Pass | Pass | 8 visualization colors and 6 report colors, from the screenshots |

Old: 5 of 14. New: 13 of 14, with factor 12 passing once the logo marker is answered.

## Plain language gate

Pass. "Visualization colors" and "Reports customization" appear only as the on-screen section labels the member clicks under; the title, description, opening, and headings say "colors", "charts", and "reports". Hex code is defined where it first appears.

## Dimension scores

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 8.6 (2/7: description 159 characters and "you will learn", no opening, "Tips" heading, no heading echo, sections out of the opening list's order) | 30.0 | +21.4 |
| Chunk independence (25) | 8.3 (2/6: sections start with no place named, feature name dropped, section headings were H1, "manage colors, logos, reports, and templates" restated the opening list) | 25.0 | +16.7 |
| Answer completeness (25) | 3.6 (1/7: no outcomes or save step, no role, no defaults, constraint only in Tips, hex undefined, no link to the templates article) | 25.0 | +21.4 |
| Fin-parsable formatting (10) | 5.0 (4/8: labels in title case against sentence-case screens, bold, no alt text, horizontal rules) | 10.0 | +5.0 |
| Accuracy and confidence (10) | 4.0 (2/5: unsourced tips, nothing marked unconfirmed, "you can") | 10.0 | +6.0 |
| **Total** | **29.5, Not retrievable as written** | **100.0, Fin-ready** | **+70.5** |

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I change my brokerage logo? | No; no place named | Yes |
| How do I change the colors on our CMAs? | No; no place named, no save step | Yes |
| Why aren't my new brand colors showing on an old report? | No | Yes |
| Can agents change the brokerage colors? | No | Yes |
| What is a hex code? | No | Yes |
| Where is My brokerage? | Yes | Yes |
| How do I create an email template for my brokerage? | Yes, with stale steps | Yes, by link to Create Communication Templates for your Brokerage |

## Source differences and decisions

- Save step added. The live article and old Notion page ended every color procedure at picking a color; the internal Brokerage Branding troubleshooting guide (June 25, 2026 screenshots) showed Save settings, and Kevin confirmed it, October 15, 2026. The page's helper text still reads "Click 'Save profile'", which does not match the button.
- Labels corrected to the screen's sentence case: My brokerage, Edit settings, Save settings, Reports customization (live article: "Report Customization").
- Logo: Kevin confirmed you click the logo and a file window opens. "Find Brokerage Details" from the live article was dropped; Brokerage details is a separate left-panel item, and the logo sits at the top of the left panel.
- Font style: shown in the February 2026 Branding screenshot's right-hand menu; Kevin confirmed it is not an option. Not documented, and that screenshot is replaced with a placeholder.
- Email templates: moved to Communication templates in My brokerage (Kevin, with a screenshot of the Share with Contact section). The section is cut to one sentence and a link to Create Communication Templates for your Brokerage, which owns the workflow.
- Access: broker admins only (Kevin). Roles property set to Admin/Broker.
- Visualization colors cover charts and analytics only; color changes apply to new reports only (Kevin).
- All four Tips cut (Kevin): off-hours editing, saving hex codes, checking a sample report, and removing a template.
- Title changed from Add Branding to a Brokerage to Update Your Brokerage Logo and Colors. No collision found in the mirror, collection names, or page names.

## Open items

- `[confirm: whether the new logo saves right away or only after clicking Save settings]`. Also unknown and left out of the body: whether Edit settings is needed before clicking the logo, accepted file types and size, and where the logo shows up (reports, emails).
- Which report types take the Reports customization colors. The draft says only "reports", with Preview CMA and Preview show sheet named from the screen.
- Confirm the left-panel label reads Communication templates; the February screenshot shows "Email copy templates".
- The sibling Create Communication Templates for your Brokerage is out of date against Kevin's screenshot: it does not mention the Edit, Delete, or Default controls, and it carries emoji callouts and bold. It needs its own migration; the link sentence here describes only what that article covers today.
- The kept profile-menu screenshot shows a Perchwell staff member's name and photo, not a member. Replace at the media owner's discretion.
- Video: the old row says Video Done with no link, and the live article has none. No placeholder added.
