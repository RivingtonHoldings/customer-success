# QA: Add Listings to a Tag

- **Article:** Add Listings to a Tag
- **Old title:** How to Tag Individual Listings
- **Sources:** Intercom article 16221347, content 19552103; mirror `docs/help-center/baldwin/how-to-tag-individual-listings.md` (Baldwin only, not shared); Tara's six Listing Detail Page screenshots, October 20, 2026; sibling drafts Create and Edit a Tag, Link a Saved Search to a Tag, Share a Tag with Clients, Search Page Overview, Share Listings with Clients from Search, Contacts Page Overview
- **Scored by:** Claude, for Tara, October 20, 2026
- **Check set:** scorecard revision 2

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | |
| 2 visual_content_text | Pass | Pass | Old had no images; new placeholders carry alt text |
| 3 undefined_terms | Fail | Pass | Tag defined in the opening |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Pass | Pass | |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | No role gates the workflow |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | Pass | Pass | Notification behavior split into its own section |
| 10 restate_questions | Pass | Pass | |
| 11 overview_jtbd | Fail | Pass | Old article had no opening paragraph |
| 12 instruction_completeness | Fail | Pass | Both old Steps blocks ended at Save |
| 13 limitations_workarounds | Pass | Pass | |
| 14 numerical_clarity | Pass | Pass | |

## Plain language gate

New: pass. Old: "populate" (in the saved search bullet) would fail check 1; replacement is "are added".

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 17.1 (4/7: title says "Individual" but covers multiple, description 165 characters, no opening) | 30.0 | +12.9 |
| Chunk independence (25) | 25.0 | 25.0 | 0 |
| Answer completeness (25) | 10.7 (3/7: no outcomes, notification behavior missing, Tag undefined, saved search re-explained instead of linked) | 25.0 | +14.3 |
| Fin-parsable formatting (10) | 5.0 (4/8: bold, terminal periods in steps, horizontal rules) | 10.0 | +5.0 |
| Accuracy and confidence (10) | 6.0 (3/5: Tags tab, Add to Tag button, and Property Detail page contradict the current product; "using") | 10.0 | +4.0 |
| **Total** | **63.8, Needs rewrite** | **100.0, Fin-ready** | **+36.2** |

The new score assumes the three open `[confirm: ...]` markers resolve as written.

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| How do I add a listing to a tag? | Yes, with the wrong controls | Yes |
| Can I add several listings to a tag at once from my search? | Yes, with the wrong controls | Yes |
| Can I add a listing to more than one tag at the same time? | No | Yes |
| Why didn't my client get an email when I added a listing to their tag? | No | Yes |
| How do I make a new tag while I'm adding listings? | Partly | Yes |
| Where do I add a listing to a tag from the listing page? | Yes, wrong (Add to Tag button) | Yes |
| If a listing stops matching my saved search, does it stay in my tag? | Yes | Yes |
| How do I remove a listing from a tag? | No | Yes, by link |

## Source differences and resolution

- Listing Detail Page route: live article said an Add to Tag button. Tara's screenshot shows Actions, then Share, then the via Tag section. Screenshot wins.
- Search route: live article said a Tags tab and Save. Search Page Overview draft and Tara's screenshots show via Tag, Next, then Add Listings. Screenshots win.
- Multiple Tags, the Invited and Uninvited groups, the Invite contacts to Tag and notify checkbox, the Message fields, the Listings added! window, and the no-eligible-clients message: all new, from Tara's screenshots.
- Preview: Tara confirmed it reaches the same window.
- Dashboard Listings widget tag icon: currently opens the old Tags page (bug reported by Tara); written as intended per Tara.
- Saved search section: cut to one short section linking Link a Saved Search to a Tag.

## Open items

- Dashboard tag icon: marker removed October 20, 2026, at Tara's request. She is tracking the bug and the icon's intended destination herself.
- Resolved October 20, 2026, from Tara's screenshot: Add Listings | Send opens a Listings sent! window (same count line, each Tag's row marked Sent, Close) and a "Your message has been sent." message in the lower right. The outcome names both windows. No confirm markers remain.
- Resolved October 20, 2026, from Tara: Invite contacts to Tag and notify sends the Welcome to Your Tag email with a View Tag button; Edit next to Listings opens Edit Listings (reorder arrows, trash can, open full listing); the x beside a Tag's name on the Listing Detail Page removes the listing from that Tag even when it has a reaction. All three are in the draft.
- The cause given for the "no eligible clients could be notified" message (every selected Tag under Uninvited) comes from one screenshot: an uninvited Tag with Invite contacts to Tag and notify left clear. Kept, rewritten from a bare readout, after a reviewer proposed cutting it, because members may paste the message into chat.
- Set consistency: Link a Saved Search to a Tag says a reacted saved search listing leaves the Tag only once the reaction is removed, and Create and Edit a Tag names only the Tags page route for removing a listing. Neither mentions the Listing Detail Page x. Offered to Tara as a follow-up.
- `docs/product-context.md` says adding a listing to a Tag emails the agent with the Tag's contacts copied when Tag notifications are on. The Share via Tag window says uninvited contacts are not notified. Which wins for uninvited contacts with Tag notifications on is unconfirmed; the draft states only the on-screen behavior.
- Loom (3dcc11372b634f93a35935b9d7785f8e, about three months old) kept at Tara's request; she is checking whether it shows the old Tags tab.
- Tracker ID pending from Tara.
- Title change: the live URL slug stays "how-to-tag-individual-listings" until the port; sibling drafts link that URL with the old title as link text, matching the set convention.
- MLS: the article lives only in the Baldwin help center. CRMLS has its own "Saving Listings with Tags" with different controls; the team should decide whether this article replaces it for CRMLS.
- Tara's working screenshots show contact and agent names; they are context only and are not to be used as article images.
