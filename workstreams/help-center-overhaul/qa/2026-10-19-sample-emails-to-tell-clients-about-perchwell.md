# QA: Sample Emails to Tell Clients About Perchwell

- **Article:** Sample Emails to Tell Clients About Perchwell
- **Old title:** Agent-to-Client Transition Email Templates
- **Old Notion page:** https://app.notion.com/p/3818b9e01438802cabc2d3e8bee6aac1 (Master Article List, read only)
- **Intercom:** article 15521036, content 18496654, collection Then vs. Now (Baldwin only)
- **Mirror:** `docs/help-center/baldwin/agent-to-client-transition-email-templates.md`
- **Notion draft:** https://app.notion.com/p/3fe8b9e01438818aa60aec33a3051665
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-10-19-sample-emails-to-tell-clients-about-perchwell-rewrite.md`
- **Scored by:** Claude for Kevin, October 19, 2026, scorecard revision 2

## Decisions taken with Kevin

- Title changed to avoid "Email Templates", which Create Communication Templates, Create Email Templates, and Create Brokerage Email Templates already use for the Settings feature.
- Paragon replaced in the email copy with a [PREVIOUS SYSTEM] placeholder, per the old row's MLS update note "Remove Paragon and add previous provider".
- Email copy moved to past tense, since Baldwin cut over on August 3, 2026.
- Template 1 "Your searches are waiting for you in the Search tab" softened to the client portal, and "favorite listings" changed to liking listings with the heart icon.

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Pass | Pass | No images in either version |
| 3 undefined_terms | Fail | Pass | "portal" was undefined; client portal is now defined in the email |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Fail | Pass | Template numbers replaced with task headings |
| 6 self_contained_sections | Fail | Pass | "Use this for ..." leads now name the sample email and the client |
| 7 audience_specification | Pass | Pass | Agent-facing, no role gate |
| 8 entity_distribution | Fail | Pass | Perchwell and "sample email" in every heading and lead |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | |
| 11 overview_jtbd | Fail | Pass | Opening is now "Use this article to ..." |
| 12 instruction_completeness | Pass | Pass | No Steps blocks |
| 13 limitations_workarounds | Pass | Pass | |
| 14 numerical_clarity | Pass | Pass | |

## Plain language gate

Pass. The verb "use" appears only inside the email copy, as the agent's own "the system I use", which is not a stand-in for a real action.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 4.3 | 30.0 | +25.7 |
| Chunk independence (25) | 8.3 | 25.0 | +16.7 |
| Answer completeness (25) | 17.9 | 25.0 | +7.1 |
| Fin-parsable formatting (10) | 7.5 | 10.0 | +2.5 |
| Accuracy and confidence (10) | 2.0 | 10.0 | +8.0 |
| **Total** | **40.0, Not retrievable as written** | **100.0, Fin-ready** | **+60.0** |

Old failures: title collides on "Email Templates"; description opens "In this article:" and uses "you can"; no jobs opening; headings are template numbers and bold link-only H2s; multiple H1s; resource list repeated; "portal" undefined; both resource links pointed at Notion, one at this page itself; bold and horizontal rules; Paragon named; "Search tab" claim unsourced.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| Is there an email I can send my clients about switching to Perchwell? | Partly, no section names the job | Yes |
| What should I email my buyers before I invite them to Perchwell? | Yes, Template 1 | Yes |
| How do I tell a seller their listing is still on Zillow after the switch? | Yes, Template 3 | Yes |
| Do you have an email for past clients about the new alerts? | Yes, Template 4 | Yes |
| What do I put in place of the brackets in the sample emails? | No | Yes |
| Can I tell clients about Perchwell without inviting them? | Yes, Template 2 | Yes |

## Open items

- `[confirm: where shared saved searches appear for a client in the Perchwell mobile app]` in Template 1, step 3.
- Two links were cut from the email copy: "Quick Guide: Getting Started in Perchwell" is an agent guide, not one for clients, and both resource links in the live article pointed at Notion pages. Template 2 also linked Accept Your Agent's Perchwell Invitation, which contradicts an email for clients who are not invited.
- "Zillow, Homes, and Realtor" normalized to Zillow, Homes.com, and Realtor.com. Confirm the team is comfortable with this syndication claim in agent copy.
- Sibling drafts disagree on the invitation email subject: Invite Clients to Perchwell and Resend Invitations says "You've been invited to join Perchwell"; Accept Your Agent's Perchwell Invitation says "Start your home search on Perchwell". This article names neither.
- The seller link points at article 13903326, live as Share Multiple Listings in Perchwell and drafted as Share Listings with Clients from Search. Confirm the link text matches the title at port.
- The live article is linked from Quick Guide: Getting Clients Started in Perchwell as "creating email templates", which is the wrong target; the Set Up Your Clients in Perchwell draft that replaces it no longer links here.
- Intercom redirect: old title Agent-to-Client Transition Email Templates.
