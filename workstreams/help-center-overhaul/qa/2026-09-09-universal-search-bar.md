# QA scorecard: Universal Search Bar

Scored with `docs/standards/fin-readiness-scorecard.md`. First article through the migration path, and the article whose team review produced the September 10, 2026 revisions to the standard.

Every score below uses the **September 10, 2026 check set**: Chunk independence carries six checks rather than five, Fin-parsable formatting carries eight rather than seven, and two Answer completeness checks were reworded. Scores recorded before that date are not directly comparable.

## Article and sources

- Title: Universal Search Bar (unchanged). The task-led alternative "Find a Listing, Agent, or Contact with the Universal Search Bar" was proposed and Leo chose to keep the existing title on 2026-09-09
- Old Notion page: https://app.notion.com/p/1c78b9e0143880f3b927daf7d2aca4d5 (Master Article List, last edited 2026-07-17, read only)
- Intercom article 11002620, content ID 11821319, updated 2026-08-10, label `How To: Search`
- Mirror: `docs/help-center/baldwin/universal-search-bar.md` and `docs/help-center/crmls/universal-search-bar.md` (shared into both help centers)
- Draft: `workstreams/help-center-overhaul/outputs/drafts/2026-09-09-universal-search-bar-rewrite.md`
- Notion Draft in the Perchwell Help Center Database [Sep 2026]: https://app.notion.com/p/3d68b9e01438810cb386f3ea550d097c (updated 2026-09-10 with the rewritten body; `Article Status` still `Draft`)
- Scored by Claude for Leo Jedynak, 2026-09-09. Rescored 2026-09-10 after Tara's review, and again the same day after a second review narrowed the article's scope.

## What the review changed

The team read the September 9 draft and returned four points: use MLS ID rather than MLS number, cut role-access language that says nothing, stop leading with what the feature will not do, and keep the structure Fin needs without repeating the same facts. Three of the four traced to the standard rather than to the draft: the standard required an audience statement, made a Limitations section the default, and had no rule against restating facts. The standard, the scorecard, and both skills were revised on September 10 and the draft was rewritten against them.

A second pass the same day narrowed the scope. The first rewrite answered the "where do I go instead" question with three routes to the **Search** page, which turned a lookup article into a Search-page article. Tara cut it to one pointer. The section heading "Open the Universal Search Bar and start a search" was also wrong on the facts: the Universal Search Bar looks a record up and opens it, and no search starts there. It is now "Look up a record with the Universal Search Bar", and it carries the multi-MLS-ID answer, since that is the section a member asking it would land in. Its lead sentence states the every-page behavior as what the member gets rather than what they avoid.

A twelfth pass genericized the legacy platform. Tara asked on 2026-09-10 that articles stop naming Paragon, so one article can serve more than one MLS whose members came from different systems. The Things to Know bullet now says "a legacy platform" and keeps Power Search, which is the term a member actually types. The rule went into the root `CLAUDE.md`, `docs/product-context.md`, the content standard, the scorecard's accuracy check 4, and both article skills. Macros are exempt: a conversation is with one member of one MLS, so a macro may name their platform.

One problem this surfaced is still open: the New Terminology link is Baldwin-only, so genericized prose alone does not make a shared article portable. A second, whether to add "Quick Search" alongside Power Search, was raised and closed the same day; it maps to the Search page, not to this feature.

An eleventh pass closed the mobile question and corrected a third invented fact. Tara confirmed on 2026-09-10 that the Universal Search Bar sits at the top of the Search tab in the mobile app, and only on that tab. That falsified the September 9 sentence "The Universal Search Bar works the same way on mobile as in the browser", which the live article never said in any form: it mentions mobile nowhere. The lead sentence also had to be qualified, since "sits on every page in Perchwell" is true in a browser only.

This one failed differently from the other two. The confirm marker was attached to the location, the part that was safe to ask about, while the behavioral claim beside it went unmarked and was the false half. The same shape as the September 9 role sentence, which asserted that every member role has the feature and marked only the invited-client case. The standard had that rule under Audience and permissions; it is now general, in the standard, the scorecard's accuracy check 2, the rewrite skill, and the Notion prompt.

No confirm markers remain in the draft.

A tenth pass closed the last content question. Tara confirmed on 2026-09-10 that matching is always partial, down to a single number, so there is no empty-result state to document. The sentence names both examples she gave, an address matching the street name but not the number and a record matching only a number, which also answers the likelier member question of why unrelated-looking results appear. Answer completeness goes to 7 of 7 and the total to 95.0. Retrieval signals 1 is the only failing check left, and it is Leo's title decision rather than a defect.

A ninth pass documented partial matching. Tara confirmed on 2026-09-10 that the Universal Search Bar returns records sharing partial information, so an address matching the street name but not the street number still appears. That is the near-miss case, and it is almost certainly the more common one for a member who cannot find a listing. It does not settle the literal zero-result state, so the marker was narrowed rather than removed, and answer completeness 3 still fails on that gap.

An eighth pass resolved the exact-address question. Tara confirmed on 2026-09-10 that an exact address returns a direct match, the same as an exact MLS ID. Worth recording why this one mattered beyond the fact: the July Notion page carried it, the August live article had dropped it, and the house rule is that the live article wins on facts. Here the live article was the one missing something true. The rule that saved it is the other one, that every difference between the sources goes to the reviewer and is never merged silently, which is how the question reached Tara at all. No change to the precedence rule; the diff step is what makes it safe.

The test-question table is back to eight, the scorecard's upper bound. "Can I search for a contact by email?" came out: both articles answer it, and the harder question about another agent's client tests the same section.

A seventh pass resolved the contact-scope question. Tara confirmed on 2026-09-10 that contact results come from the agent's own contacts, not the brokerage's. The bullet states it positively and then names what is excluded, since "why can't I find my colleague's client" is the confusion the fact prevents. Added as a Fin test question.

A sixth pass resolved the status question. Tara confirmed on 2026-09-10 that off-market listings appear in results. That also surfaced a second invented fact: the live article says "View listings across statuses like Active, Pending, Closed, and Expired", and the September 9 rewrite turned that hedged example list into "Listings in every status appear". Perchwell has twelve statuses, per [Listing Statuses in Perchwell](http://support.perchwell.com/baldwin/en/articles/14709241-listing-statuses-in-perchwell), so the claim was false as written. The sentence now leads with what a member actually wants to know, that results are not limited to active listings, names off-market as confirmed, gives the rest as examples, and links the statuses article. No confirm marker remains on it.

A fifth pass removed bold from the body and settled the term for a pop-up window. The house style had bolded every UI element since the standard was written; Tara retired that on 2026-09-10. Bold survives on the callout labels, which Intercom names as the signal Fin reads, and on the `**Description:**` line. The bullet lead-in labels in What the Universal Search Bar returns were kept on the same reasoning, a label introducing its own block rather than emphasis inside a sentence. The descriptive "search window" became "modal" throughout, which also retired the confirm marker asking what the window is called.

A fourth pass corrected a factual error. The draft said matches appear "in a panel below the field", which no source supports: the live article says only "Results populate as you type", so the placement was invented during the September 9 rewrite and read plausibly enough to survive two reviews. Clicking the Search field opens a modal in the center of the screen, and that is where the member types and where matches appear. Corrected in the steps, the post-steps line, the returns section, and the second screenshot's alt text.

A third pass removed the inventory of listing-card fields from the Listings bullet. A member reading results is looking at the card; listing its fields back added length and answered nothing. What the section keeps is behavior: how a listing is matched, that an exact MLS ID is a direct match, and which statuses appear. The screenshot alt text still describes the card, because alt text is written for people who cannot see the image.

## Source differences (live wins)

| Where | Old Notion page (July 17) | Live article (August 10) | Draft |
|---|---|---|---|
| Listings bullets | Exact address returns a direct match | Bullet dropped | Confirmed true by Tara on 2026-09-10 and restored |
| Tips | Three bullets | Adds "If you hear Power Search, it refers to the Universal Search Bar" | Merged into one neutral Things to Know bullet |
| Body extras | Click Script toggle, Loom embed, Perchwell banner image | None | Loom kept under the opening; script and banner dropped |
| Headings | H2 with horizontal rules | H1 with horizontal rules | H2 and H3, no rules |
| Images | Two Notion uploads, no alt text | Two Intercom CDN images, no alt text | Live images kept with alt text |
| Identifier | "MLS number" | "MLS ID" at the top, "MLS number" in the body | MLS ID throughout, per the terminology rule added 2026-09-10 |

## Golden questions (gate)

| Factor | Live | Draft | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | Live used a decorative emoji, not a pointer |
| 2 visual_content_text | Fail | Pass | Both images had no alt text; both now describe the screen |
| 3 undefined_terms | Pass | Pass | MLS ID is the settled term and needs no gloss; the September 9 draft's "MLS number (the listing's MLS ID)" parenthetical is gone |
| 4 structured_enumeration | Pass | Pass | |
| 5 query_answer_symmetry | Pass | Pass | Live "Tips" is the sanctioned closing heading; draft headings all carry the feature name |
| 6 self_contained_sections | Fail | Pass | Live Tips said "this feature" with no name in the section |
| 7 audience_specification | Pass | Pass | Read through the house resolution: no role gates this feature, so silence passes. The September 9 draft failed it by claiming every member role has the feature and marking that claim unconfirmed in the same sentence |
| 8 entity_distribution | Pass | Pass | The feature name appears in every section. The September 9 draft repeated the listings/agents/contacts enumeration six times, which the house resolution now names as the wrong reading of this factor |
| 9 semantic_chunk_boundaries | Pass | Pass | |
| 10 restate_questions | Pass | Pass | No tables in either |
| 11 overview_jtbd | Fail | Pass | Live had no opening paragraph; description said "In this article, you will learn" |
| 12 instruction_completeness | Fail | Pass | Live steps stopped at typing; draft steps end at the opened record |
| 13 limitations_workarounds | Fail | Pass | Live said "not saved or filtered searches" with no route forward. The draft points once at Create a Search with Filters for criteria-based searching and has no Limitations section |
| 14 numerical_clarity | Pass | Pass | No numbers needed. The status list is now written as examples rather than as a complete set, matching the source |

Gate: the live article fails 5 of 14 under the house resolutions, factors 2, 6, 11, 12, and 13. The draft passes 14 of 14. All six `[confirm: ...]` markers were resolved by Tara on 2026-09-10; none remain.

## Dimension scores

All three columns on the September 10 check set, so the middle column shows what the review caught.

| Dimension | Weight | Live article | Sept 9 draft | Sept 10 draft |
|---|---|---|---|---|
| Retrieval signals | 30 | 10.0 (2 of 6) | 25.0 (5 of 6) | 25.0 (5 of 6) |
| Chunk independence | 25 | 12.5 (3 of 6) | 20.8 (5 of 6) | 25.0 (6 of 6) |
| Answer completeness | 25 | 14.3 (4 of 7) | 14.3 (4 of 7) | 25.0 (7 of 7) |
| Fin-parsable formatting | 10 | 3.8 (3 of 8) | 8.8 (7 of 8) | 10.0 (8 of 8) |
| Accuracy and confidence | 10 | 10.0 (4 of 4) | 7.5 (3 of 4) | 10.0 (4 of 4) |
| **Total** | 100 | **50.5** | **76.4** | **95.0** |

Bands: live, Needs rewrite. September 9 draft, Ready with fixes. Current draft, Fin-ready, gate passed. The live and September 9 columns both lose a point on the new formatting check 3, since both bolded UI elements under the pre-September 10 house style.

Failed checks, live: title is a bare noun; no "Use this article to" opening; two of three headings lack the feature name; first sentences do not echo every heading; "this feature" in Tips depends on context; body headings at H1; the same enumeration appears in two sections; no "which means" clause; the stated limit has no route forward; no related links; emoji-led tip with no bold label; no alt text; horizontal rules in the live HTML.

Failed checks, September 9 draft: chunk independence 6 (the listings/agents/contacts enumeration in three consecutive sections); answer completeness 2 (an unverified claim that every member role has the feature); answer completeness 4 (a Limitations section for three constraints, none of which is a hard cap or irreversible); accuracy 2 (the availability claim was a guess carrying its own confirm marker); plus the two below.

Failed checks, current draft: retrieval signals 1 only. The title stays a bare noun by Leo's choice, and the description and opening carry the task words instead. This is a decision rather than a defect, so the article is at the practical ceiling for its agreed title.

## Rescore against revision 2, September 15, 2026

This file had been the known straggler, still carrying revision 1 numbers. Rescoring it turned up a check that was failing under both revisions and had never been recorded.

**Fin-parsable formatting check 3 fails: bold in the body.** The three record-type bullets under "What the Universal Search Bar returns" lead with bold labels, `**Listings.**`, `**Agents.**`, and `**Contacts.**`. The content standard allows bold in exactly two places, the callout labels and the `**Description:**` line, and this article has no callouts, so those three are the only bold in it besides the description. The rule exists because Intercom names the bold callout label as the signal Fin carries into an answer; bold used for anything else dilutes it. The pattern came across from the old article's house style, which bolded liberally, and the migration stripped it everywhere except here.

| Dimension | Weight | Recorded | Actual | Note |
|---|---|---|---|---|
| Retrieval signals | 30 | 25.7 (6/7) | 25.7 (6/7) | Check 1 still fails on the bare-noun title |
| Chunk independence | 25 | 25.0 (6/6) | 25.0 (6/6) | |
| Answer completeness | 25 | 25.0 (7/7) | 25.0 (7/7) | |
| Fin-parsable formatting | 10 | 10.0 (8/8) | 8.75 (7/8) | Check 3, bold bullet labels |
| Accuracy and confidence | 10 | 10.0 (5/5) | 10.0 (5/5) | |
| **Total** | **100** | **95.7** | **94.5** | Still Fin-ready |

The gate passes 14 of 14. The fix is to unbold the three labels and keep the sentences as they are.

Kelly's de-jargon feedback on this article is separate and still pending: she flagged "lookup", "record", "returns", "type what identifies the record", and "Partial entries return close matches" as too technical for agents. That is a rewrite of the same section the bold sits in, so both should be done in one pass rather than twice.

### Fixed the same day

The three bold labels were unbolded, so the bullets now read "Listings. Matched on address or MLS ID, ...", and the only bold left in the article is the `**Description:**` line. Fin-parsable formatting returns to 10.0 (8/8) and the **total returns to 95.7**. Check 1 still fails on the bare-noun title, which is Leo's September 9 decision to keep and not a defect.

## De-jargon pass, September 15, 2026

Kelly left six comments, five on specific words and one on the article as a whole. Her reason is retrieval, not only readability: "they will search and type into Perchie those words they know and we want to make sure we show the right answer." Every replacement below was chosen for that test, the word a member would type, rather than for plainness alone.

| Her comment | Was | Now |
|---|---|---|
| "I don't think lookup is a client friendly word for agents" | "It is a lookup tool"; "a lookup is always one click away"; "Each lookup opens one record"; "the lookup works the same way" | "lookup" is gone from the article |
| "Not sure if record is clear. Might want to break it out a bit more" | "record" in the H2, the lead, the steps outcome, and the bullets | "listing, agent, or contact", the three real things, throughout |
| "what does this mean?" on "type what identifies the record" | "It is a lookup tool: type what identifies the record, click the match, and the record opens." | Cut. The mechanics already live in the Steps block, and the section now says what the tool is for instead: "rather than building a list from filters" |
| "a little technical as well" on "returns" | "What the Universal Search Bar returns" | "What you find with the Universal Search Bar" |
| "Might be a better way to explain it" on "Partial entries return close matches" | "Partial entries return close matches, which means ..." | "You do not have to type the whole thing, which means ..." |
| "a little bit technical for our users" on the article | see above | see above |

**The description was left alone.** Her whole-article comment is anchored to it, but the description already reads "Find a listing, agent, or contact from any page in Perchwell by typing an address, MLS ID, name, or email into the Universal Search Bar". It carries no flagged term and it is the plainest sentence in the article. The jargon was in the body.

**"modal" was changed and then changed back.** It appeared three times and in one image's alt text. Kelly did not name it, but she asked for "some of the other terminology" to get the same treatment, so it was replaced with "search window". That was wrong: `docs/product-context.md` already carries a terminology rule reading "A pop-up window that opens over the page is a modal. One word for it, used consistently, so a member and Fin both track the same thing." The rule's stated reason is the same Fin-matching argument Kelly was making, so the change worked against her own goal rather than for it. Reverted in all four places the same day, on Tara's call.

The lesson is narrower than it looks. The de-jargon pass was right to go past Kelly's literal list, since she asked for it. What it skipped was checking each candidate against the terminology rules before changing it, and "modal" was the one candidate with a rule already written against it. The other five had none.

**Two headings changed, which changes what Fin retrieves on.** "Look up a record with the Universal Search Bar" is now "Find a listing, agent, or contact with the Universal Search Bar", and "What the Universal Search Bar returns" is now "What you find with the Universal Search Bar". Both still carry the feature name and both first sentences still echo them, so Retrieval signals checks 4 and 5 hold. The gain is that the procedure heading now contains the three nouns a member actually types.

**A say-once judgment.** "listing, agent, or contact" now appears in the description, the opening, the When to use lead, the procedure heading and its lead, and the What you find lead. That is the replacement for the abstract noun "record", so it functions as the article's vocabulary rather than as a repeated enumeration, which is what factor 8 asks for. The details of how each type is matched stay in one place, the three bullets. Chunk independence check 6 governs capability enumerations, and none is repeated.

**The score does not move.** It stays at 95.7, and the gate stays at 14 of 14. Nothing here touched a scored check: the words were never the problem the scorecard measures, which is the same blind spot recorded for sourced-but-wrong facts. A member-comprehension defect is invisible to it, and Kelly caught this one by reading as an agent would.

**Kelly's five inline threads no longer exist.** Notion deletes an inline discussion when the text it is anchored to is deleted, and this pass removed every word the five were attached to. Checking the page afterward returns one discussion, the whole-article comment anchored to the description, which Tara resolved herself. An earlier version of this file said the five were still on the page and unresolved; that was wrong.

The practical consequence is that Kelly has no thread-level trail showing which comment produced which change. The table above is now the only record of that, so closing the loop with her means telling her directly rather than replying in the page. Worth knowing before the next round of comments: editing the commented text is what destroys the thread, so a reply belongs on the thread before the edit, not after.

## Fin test questions

Questions members may ask, in their words. "One section" means Fin can answer from a single retrieved section without stitching.

| Question a member may ask | Live article, one section | Draft, one section |
|---|---|---|
| How do I look up a listing by MLS ID? | Yes | Yes |
| Where is the search bar to find an agent? | Partly (says "top of your screen") | Yes (Search field, upper right of the top navigation, opening a modal) |
| Why can't I find another agent's client in the search bar? | No | Yes, contact results are scoped to your own contacts |
| What happened to Power Search? | Yes | Yes, with a link to New Terminology |
| Can I search several MLS IDs at once in the top search bar? | No | Yes, from Look up a record, with the MLS ID filter route and a link |
| Does the search bar show closed or expired listings? | Yes | Yes, and it says results are not limited to active listings, with off-market confirmed |
| Why am I seeing listings that are not the address I typed? | No | Yes, partial matching is explained in What the Universal Search Bar returns |
| How do I filter by price? | No | Yes, from When to use, links Create a Search with Filters |

**Coverage note.** Scope was cut on 2026-09-10 to keep the article on the Universal Search Bar, then the multi-MLS-ID answer was put back into the Look up a record section, where a member asking it would land. Saving a search is the one question that left, and its table row was retired on 2026-09-10 in favor of the partial-match question, since the coverage note below already tracks it for Fin testing: [Manage Your Saved Searches](http://support.perchwell.com/en/articles/8955646-manage-your-saved-searches) is its proper home, and Fin testing should confirm it retrieves from there rather than from this article.

## Open items

- The invited-client question is no longer a blocker for the body, since the draft claims nothing about roles. It still matters for the Notion `Roles` property, currently `All`. Tara or Kelly to confirm whether invited clients see the Universal Search Bar.
- **Internal links do not survive sharing.** [New Terminology](http://support.perchwell.com/baldwin/en/articles/14459704-new-terminology) is a Baldwin article on a `/baldwin/en/` URL, and this article is shared into CRMLS. A CRMLS member following it lands in another MLS's help center, and its content maps Paragon terms specifically. Genericizing the prose does not make an article portable on its own; every internal link has to resolve for every MLS that shows the article. This applies to the whole shared set, not just this article, and it needs a decision before more articles are shared.
- **The title was reconsidered and kept.** Tara raised "Universal Search Bar Overview" on 2026-09-15 and settled on keeping "Universal Search Bar" the same day. Adding "Overview" would not have satisfied Retrieval signals check 1, which wants a task-led title, and it would have mislabeled the article type: the standard's Overview pattern is `<Page> Overview` for an article that orients rather than teaches one task, and this article has a single `Steps:` procedure at its center. It would also have collided with the live `Search Page Overview`, which is the article members already confuse this one with. The task-led alternative remains "Find a Listing, Agent, or Contact with the Universal Search Bar", declined by Leo on 2026-09-09 and not revisited. **95.7 is the agreed ceiling for this article**, and check 1 is a decision rather than a defect. Closed, recorded so it is not reopened a third time. If the title is ever revisited, do it inside Kelly's de-jargon pass, which rewrites the same sentences.
- **"Quick Search" was considered and rejected.** `docs/help-center/baldwin/key-workflow-changes.md:27` maps Paragon's Quick Search widget to the Search page and its filter templates, not to the Universal Search Bar. Tara suggested adding it alongside Power Search on 2026-09-10, then confirmed the same day to leave it out. The article names Power Search only, and the existing Quick Search mapping stands. Closed, recorded so it is not reopened.
- Shared article: the same Intercom article sits in the Baldwin and CRMLS help centers. The new database row is Baldwin, per the old row's `MLS` value. Tara to decide whether CRMLS gets its own row or the shared collection carries the update.
- Every link in the draft now points at `/baldwin/en/`. The default help center link to Manage Your Saved Searches went out with the scope cut, so there is nothing to flag at transfer.
