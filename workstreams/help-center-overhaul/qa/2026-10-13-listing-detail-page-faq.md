# QA: Listing Detail Page FAQ

- Article name: Listing Detail Page FAQ (old title: Listings FAQ)
- Old Notion page: https://app.notion.com/p/3658b9e01438803da8c1e1604f129493 (Resource Title "Listing Detail Page FAQ")
- Intercom article ID 15200541, content ID 17970338
- Mirror: `docs/help-center/baldwin/listings-faq.md` (live body re-checked with `get_article` October 13, 2026; identical)
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-10-13-listing-detail-page-faq-rewrite.md`
- New Notion page: https://app.notion.com/p/3f88b9e014388145b535c11d52aa3053
- Scored by Claude for Kevin, October 13, 2026, against scorecard revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Pass | Pass | No images in the live article; one placeholder with alt text added |
| 3 undefined_terms | Pass | Pass | HOA and CMA defined on first use |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Pass | Pass | Question headings |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | No role gates the content; Roles property set to All Except Client |
| 8 entity_distribution | Pass | Pass | Listing Detail Page now in every heading |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables |
| 11 overview_jtbd | Fail | Pass | "Use this article to" opening added |
| 12 instruction_completeness | Pass | Pass | No Steps blocks |
| 13 limitations_workarounds | Fail | Pass | "Coming soon" notes answer dropped; missing similar listings section now routes to CMA Subject Property |
| 14 numerical_clarity | Pass | Pass | HOA example uses exact on-screen values |

## Plain language gate

Pass on the rewrite. "Comps" is the member's own word, and "one-pager" was kept once as a member synonym for One Page Report.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 12.9 | 30.0 | +17.1 |
| Chunk independence (25) | 20.8 | 25.0 | +4.2 |
| Answer completeness (25) | 14.3 | 25.0 | +10.7 |
| Fin-parsable formatting (10) | 8.8 | 10.0 | +1.2 |
| Accuracy and confidence (10) | 6.0 | 10.0 | +4.0 |
| Total | 62.8 | 100.0 | +37.2 |

Old: Needs rewrite. New: Fin-ready, 14 of 14 golden questions, plain language gate passed.

Old failures: bare title close to the Listings widget and Listing Maintenance FAQ; 75-character description; no opening; association fee heading without the page name; no heading echo; every question an H1; bold in the body; a roadmap promise ("coming soon") with no route forward; no links; an agent-version QR code claim the product contradicts; a similar listings answer for a section the page no longer has; and an association fee answer awaiting product confirmation since May 2026 with no marker.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| Is the HOA fee on a listing monthly or yearly? | Partly | Yes |
| Why does the top of the listing say $30/mo when the HOA is $355? | No | Yes |
| Where does the QR code on my agent one-pager go? | Yes, but wrong | Yes |
| Where did similar listings go on the listing page? | No, describes a removed section | Yes |
| How do I find comps for a listing? | No | Yes, with a link |
| Can my buyer see my open house remarks? | Yes | Yes |
| Where do other agents see open house remarks? | Yes | Yes |
| Can I add notes on the listing page? | Yes, as a roadmap promise | No; question dropped, see Open items |

## Open items

- Notes question dropped. Neither Kevin nor the sources could locate a notes feature on the Listing Detail Page, and "coming soon" is a roadmap promise with no route forward. If product confirms notes exist on mobile, restore the question with that route.
- Sibling fix: the Create a One Page Report draft says every QR code opens the client-facing page, which Kevin confirmed October 13, 2026. The live Listings FAQ's agent-version claim was wrong. No change needed to the draft.
- Sibling fix: the Listing Detail Page Overview draft lists the header as price, address, beds, baths, square footage, and acreage; the October 13, 2026 screenshot also shows the monthly HOA fee there. The draft also no longer covers the Showings card, so this FAQ is now its only home.
- Common Perchwell FAQs (live) still carries "How are similar listings determined" and "Can I add notes ... coming soon"; flag both for that article's rewrite.
- Links: Create One Page Reports and Manage Listings Page Overview are stored in the mirror as default help center URLs; the draft links the Baldwin form. Confirm at transfer. The Create a One Page Report link text uses the draft's new title.
- Similar listings removal confirmed by Kevin October 13, 2026; Showings card, See All, and Upcoming Showings labels confirmed the same day.
- The building icon beside the monthly HOA fee in the header is not named in the article; ask whether it has a hover label if a later edit needs to point at it.
