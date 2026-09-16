# QA: Find Listings in the Listings Widget

Old title: **Listings Widget Overview**. Retitled on Tara's approval, September 16, 2026; record the old title for the Intercom redirect.

**The title was settled twice.** The first proposal, "Find and Manage Listings in the Listings Widget", was withdrawn after Tara flagged that Manage Listings could confuse both members and Fin. Checking it out made the case stronger than the collection name alone: **Manage Listings is a page in Perchwell**, reached from the main menu, with its own article, [Manage Listings Page Overview](http://support.perchwell.com/en/articles/13623016-manage-listings-page-overview) (Intercom 13623016, Listing Maintenance collection). Its description reads "open Manage Listings, add or update a listing, schedule an open house, and use filters to find the listings you need."

The proposed title would have competed with that article on *manage listings*, *find listings*, *filter listings*, and *edit a listing*, for two different surfaces. "Find Listings in the Listings Widget" collides with it on nothing, keeps the exact feature name a member types, and still passes golden question 5. Dashboard queries are covered by the description and by three of the six headings.

**Also surfaced while checking.** The pencil icon appears in four Baldwin articles for four different controls: contacts, draft listings, Manage Listings, and messages. This article names it as "the pencil icon next to a listing" inside the Listings widget, which is specific enough, but the icon alone is not a distinguishing detail anywhere in the help center.

## Sources

- Live Intercom article 13903171, content ID 16154426, updated 2026-07-02. Mirror: `docs/help-center/baldwin/listings-widget-overview.md`, synced 2026-09-04
- Old Notion page: https://app.notion.com/p/2ca8b9e0143880a58589ee63af4af579, Master Article List, last edited 2026-07-17, `Update Status: Transfer to Intercom`
- Tara's product screenshots, September 16, 2026: the Listings widget with the scope menu open, and the filter row scrolled right
- Baldwin only. The `intercom_id` appears in no CRMLS mirror file, so this is not a shared article
- Notion Draft created 2026-09-16: https://app.notion.com/p/3dd8b9e01438813ea9f6cdadffa18871

Scored by Claude for Tara, September 16, 2026, using the **September 10, 2026 check set, revision 2**, plus the plain language gate added September 15, 2026.

**Source precedence, and a case where both documents lost.** The Notion page is newer than the live article by two weeks and is marked `Transfer to Intercom`, which records an intention rather than a fact, so the live article wins under the standard. On the filter list both lost anyway: each names Recently Added and neither names Active Under Contract, and Tara's September 16 screenshots show the opposite. A product observation from today beats two documents from July.

## Where the sources disagreed, and what won

| Fact | Live article | Notion page | Product, Sep 16 | Taken |
|---|---|---|---|---|
| Quick Edit icon | pen icon | pencil icon | pencil | **pencil**. Three sources to one; also closes the defect logged in `audit/notes.md` 2026-09-11 |
| Filter list | 8, includes Recently Added | same 8 | 8, no Recently Added, adds Active Under Contract | **product**. Recently Added dropped, Active Under Contract added |
| Scope order | MLS, Brokerage, My, Office | same | MLS, My, Brokerage, Office | **product**, per the rule that an ordered pair follows the product's controls |
| Office listings | lowercase l | lowercase l | Office Listings | **product** |
| Coming soon | lowercase s | lowercase s | Coming Soon | **product** |
| Scope permissions | "your MLS permissions" | "your user permissions" | not visible | **live article** |
| Filter section framing | "Narrow by listing type", filters | "Sort by listing status or activity" | filters, not statuses | **live article**, confirmed by Tara. Notion was wrong twice: they neither sort nor are they all statuses |
| Quick Edit bullet label | Quick Edit | Edit | icon only, no text label | **Quick Edit**, which the live article uses consistently in both places; Notion contradicts itself |

The Notion page did contribute the one thing it was right about: `pencil icon`.

## The three confirm markers, all closed the same day

Tara answered all three on September 16, 2026, from the product. No marker remains in the draft.

1. **What the Search field does.** Resolved: the field takes any text, the intended use is an address the way a member would type one into the Universal Search Bar, and matches appear as you type. The draft says that and links the Universal Search Bar article. It deliberately does **not** say the field matches on anything other than an address: accepting any text and matching on any field are different claims, and only the first was confirmed.
2. **Whether Brokerage Admins have Quick Edit.** Resolved: they do. The live article's quick actions bullet was right and its callout was incomplete, which is the opposite of what the bullet-versus-callout conflict suggested.
3. **Which icons appear on a given listing.** Resolved for the pencil: it appears on a member's own listings, and on every listing for a Brokerage Admin. That is the same fact as the role gate, so the two merged into one **Note:** that answers the question a member actually asks, which is why they cannot see a pencil.

**What the resolutions changed in the draft.** The Search field's confirmation moved it from an aside into one of three narrowing methods, so the section lead now reads "in three ways" and the opening paragraph collapsed to three outcomes that map one-to-one onto the three H2s. The audience note went from an availability claim carrying a marker to a plain statement of when the control appears.

**One sourced sentence was dropped rather than kept.** The live article and the Notion page both say "MLS staff and administrators may have broader access to edit other agents' listings." It is hedged, it does not say which role or how much, and it now sits next to a precise statement about Brokerage Admins. Keeping both would leave a member less certain than keeping one. Recorded here rather than deleted silently.

## Second round of Tara's answers, September 16, 2026

Four more corrections after the first three markers closed. One of them changes what the article documents rather than how it says it.

**The Tag quick action no longer exists.** The live article lists Tag as one of three quick actions, with two bullets under it, and the old Notion page says the same. Tara confirms the icon is gone from the widget. The bullet and the Tags Page Overview link that hung off it were both removed, and "tag" came out of the description and the opening paragraph. **This is a live wrong-answer risk, not just a stale line:** Fin answers from the published article today, so a member who asks how to tag a listing from the Dashboard is being told to click a control that is not there.

**I misread the first screenshot.** The QA record said the September 16 screenshots "show a tag icon on some listings and the pencil and ShowingTime icons on others". The pencil and ShowingTime halves were right and Tara has since confirmed both. The tag half was my reading of a small glyph and it was wrong. Corrected here rather than left standing, because that sentence was the evidence for a marker that no longer exists.

**Brokerage Admins are scoped to their brokerage.** The earlier note read "on every listing", which was the looser of the two readings flagged in Open items. Now "on every listing in their brokerage".

**Search is scoped.** It looks only at the listings currently chosen, so the section states it as the route forward: "To search every listing in your MLS, pick MLS Listings first." This closes the third open item.

**The default and the persistence are now stated**, which closes the fourth. The widget starts on MLS Listings and afterwards keeps whichever listings and filter were chosen last. It sits in one **Note:** under the parent section, because it governs both controls and splitting it across the two subsections would state one fact twice.

No score change: nothing here touches a scored check, and the description was retrimmed to 137 characters after "tag" came out of it.

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1. disambiguation | Fail | Pass | Old article leads its Quick Edit callout with a 💡 emoji, which the factor bans outright. New article has no emoji |
| 2. visual_content_text | Fail | Pass | Old article's one image carries the alt text "image". New article carries two screenshot placeholders, each with the alt text the image will use |
| 3. undefined_terms | Fail | Pass | Old article names Quick Edit, ShowingTime, Tag, and "listing management form" with no gloss. New article defines each by what it does and links Tags Page Overview |
| 4. structured_enumeration | Pass | Pass | Both use bullets for options and lists |
| 5. query_answer_symmetry | Fail | Pass | Every old heading is a bare noun: "Listings Widget location", "Listings Widget filters", "Listings Widget quick actions". Every new heading names what the section answers |
| 6. self_contained_sections | Fail | Pass | Old subsection opens "Refine the results further with the other filters", where "further" and "other" both point outside the section Fin would retrieve. New leads stand alone |
| 7. audience_specification | Fail | Pass | Old article states the Quick Edit audience twice and contradicts itself, so a member cannot tell who has it. New article states it once, confirmed by Tara, and frames it as when the pencil icon appears |
| 8. entity_distribution | Pass | Pass | "Listings widget" appears in every section of both |
| 9. semantic_chunk_boundaries | Pass | Pass | One topic per section in both. New article splits the three controls into H3 subsections |
| 10. restate_questions | Pass | Pass | No tables in either. Every new list carries an intro line |
| 11. overview_jtbd | Fail | Pass | Old body has no opening paragraph and starts cold at a heading; its only intro is the description field, which opens "In this article, you will learn how to" |
| 12. instruction_completeness | Fail | Pass | Old article's location steps stop at "Look for the Listings Widget" with no outcome, and ShowingTime and Tag describe capabilities with no mechanism. New article gives each action its click and its result |
| 13. limitations_workarounds | Pass | Pass | Old states the Quick Edit limit. New states it, adds that scope options depend on MLS permissions, and adds the mobile constraint with desktop as the route forward |
| 14. numerical_clarity | Pass | Pass | Neither states a vague quantity |

**Old gate:** failed on 7 factors (1, 2, 3, 5, 6, 11, 12).
**New gate:** all 14 pass, with no open confirm markers.

## The pencil opens Add/Edit, and that closed three things at once

The draft carried "Click the pencil icon next to a listing to open the listing management form" verbatim from the live article and the old Notion page. It was sourced, and it was still the weakest sentence in the article. Tara confirmed on September 16, 2026: **the pencil opens the Add/Edit form in a new tab.**

That one answer fixed three separate problems.

- **The term was wrong, against a rule that names this exact case.** `docs/product-context.md` reads: "Use the label the member sees on screen, spelled exactly as the UI spells it, and do not bold it. **'Add/Edit,' not 'the listing form.'**" Both sources had written around the product's own name for the screen, and the rewrite inherited it because it was sourced. Sourced and wrong is the failure mode the scorecard cannot see, recorded twice before in this project.
- **It was the last Manage Listings collision in the article.** "Listing management" is "Manage Listings" turned around. It is gone.
- **A missing link appeared.** Add/Edit has its own article, [Add and Edit Listings](http://support.perchwell.com/en/articles/13627189-add-and-edit-listings) (Intercom 13627189, Listing Maintenance). The bullet now hands off to it: "covers the fields and the save step once Add/Edit opens." Answer completeness check 7 was already passing, but a member who clicks the pencil and lands in an unfamiliar form now has somewhere to go.

**The new tab detail earned its own clause**, matching how the set states click behavior: Dashboard Overview says "Clicking one opens the Listing Detail Page in a new tab" and "opens their Contact Detail Page in a new tab". Here it is "in a new tab, so the Dashboard stays as you left it", which also lets the section lead drop "without opening the listing", a phrase that was no longer true once the pencil was known to open something.

One "manage" survives in the body: "manage upcoming showings when your MLS supports it". That is ShowingTime's own hedged claim about showings rather than listings, no collision, and the hedge is kept as the source wrote it.

**A pattern worth carrying into the audit.** The Manage Listings page has a pencil that opens Add/Edit too, and its own article links out to Add and Edit Listings for the same reason. Two surfaces, one destination. Any article describing a pencil next to a listing should name Add/Edit and link that article rather than inventing a name for the screen.

## Plain language gate

**Pass**, all five checks.

1. No term from the do-not list, in the sense it bans. Zero hits
2. The article names listings, filters, and the scope rather than a category standing in for them
3. Title, description, opening, and all six headings read as an agent would say them out loud
4. No sentence restates a procedure in the abstract
5. "Filter", "search", "edit", "tag", and "schedule a showing" each appear in the section that covers that task, not only in a link title

One term was checked and kept: **Tag**, capitalized, which is the Perchwell feature name and carries a terminology rule.

**One term the gate passed and Tara caught: "scope".** The draft used it as its own vocabulary, in an H3 ("Choose the listing scope"), in a lead ("The scope sets whose listings the widget shows"), and in a control name ("the scope button"). Check 3 passed it because "Scope by" is the label on the menu, so it read as an on-screen term rather than jargon. Tara's objection was the right one: an agent seeing a button labeled MLS Listings does not know that the word for it is "scope", and nothing on screen calls it a scope button.

The fix keeps the label and drops the vocabulary. "Scope by" now appears exactly once in the body, at the moment the member has to find it on the menu, and once in an alt text. Everywhere else the article says what the control does: the H3 is "Choose whose listings you see", the lead is "Choose whose listings the Listings widget shows from the button in its top right", and the description and opening both say "choose whose listings" rather than "by scope". The control is identified by position rather than by a name, because its label changes with the selection and there is no fixed name for it on screen.

**The rule this surfaces.** An exact on-screen label licenses naming the control at the point of use. It does not license adopting the word as the article's own noun throughout. The plain language gate's check 3 cannot catch this on its own, because the term passes the "is it on screen" test; it needs the second question, which is whether a member would use the word when the control is not in front of them. Worth adding to `content-standards.md` under the check-a-candidate rule.

## Dimension scores

| Dimension | Weight | Old | New | Delta |
|---|---|---|---|---|
| Retrieval signals | 30 | 8.6 (2/7) | 30.0 (7/7) | +21.4 |
| Chunk independence | 25 | 12.5 (3/6) | 25.0 (6/6) | +12.5 |
| Answer completeness | 25 | 7.1 (2/7) | 25.0 (7/7) | +17.9 |
| Fin-parsable formatting | 10 | 5.0 (4/8) | 10.0 (8/8) | +5.0 |
| Accuracy and confidence | 10 | 8.0 (4/5) | 10.0 (5/5) | +2.0 |
| **Total** | **100** | **41.2** | **100.0** | **+58.8** |

Band: **Not retrievable as written** to **Fin-ready**.

**Checks the old article failed.** Retrieval: bare-noun title; description runs 172 characters against Intercom's 140 cap; no opening paragraph; three bare-noun headings; two sections jump from heading to content without echoing the heading. Chunk independence: three sections are H1, competing with the title; subsections carry no feature name; one subsection depends on the one before it. Answer completeness: no Steps block ends with an outcome; the Quick Edit audience contradicts itself; no "which means" clause; no default stated; four product terms undefined; the article links to nothing at all despite Tag and listing statuses each having their own article. Formatting: emoji-led callout with no bold label; bold on every UI element; alt text reads "image". Accuracy: "Use the widget filters", "so you can manage listings".

**Two defects were caught in the rewrite's own self-review**, not in the original: the three controls were enumerated in two sections, which fails Chunk independence check 6, and the draft carried no "which means" clause, which fails Answer completeness check 3. Both were fixed before scoring. A third, larger one is recorded above: the description, opening, and section lead all asserted that the Search field narrows the list, which no source supports.

**Ready to move to `Ready to Transfer`** once the two screenshots are placed. The score is in the Fin-ready band, both gates pass, and no confirm marker is open.

## Fin test questions

| Question a member may type | Old answers from one section | New answers from one section |
|---|---|---|
| How do I see only my own listings on the Dashboard? | Partly | Yes. "Choose the listing scope" |
| Where is the Listings widget? | Yes | Yes. "Find the Listings widget on the Dashboard" |
| How do I filter the Dashboard listings by price drop? | Partly | Yes. "Filter by listing type" |
| Why can't I edit a listing from the Dashboard? | Partly | Yes. "Take action on a listing from the Listings widget", subject to the open marker |
| How do I schedule a showing from the Dashboard? | No | Yes. "Take action on a listing from the Listings widget" |
| What do Active Under Contract and Pending mean? | No | Yes. "Filter by listing type" links Listing Statuses in Perchwell |
| Can I see brokerage listings instead of just mine? | Partly | Yes. "Choose the listing scope" |
| Can I do this on my phone? | No | Yes. "Things to Know" |

## Open items

None blocking. Every one of these is a question for review rather than a gap in the draft.

1. **The live Baldwin article still documents the Tag quick action**, which no longer exists in the product. Fin answers from it today. That is a correction to a published article, outside this migration's scope, and it should be logged in `audit/notes.md` and fixed on its own
2. **Whether the Search field also respects the listing type filter**, not just the listings chosen. Tara confirmed it is scoped to the listings shown; the filter interaction was not asked and is not claimed
3. The old Notion row has `CRMLS?: 100% Applicable` while `Which HC is it in` reads Baldwin and no CRMLS mirror file carries this `intercom_id`. Whether CRMLS should get this article is a question for Tara and Kelly, not something this migration decides
4. The live article's one Intercom CDN image was dropped rather than carried. The old Notion row reads `Screenshot: Update Required`, and the image predates the current filter row, which no longer has Recently Added and now has Active Under Contract. Tara's two September 16 screenshots are what the two placeholders describe
5. The live article says the widget sits "on the right side of the page". The September 16 screenshots do not show enough of the Dashboard to confirm it, so the claim was dropped rather than repeated. Nothing in the draft depends on it
6. Links to Dashboard Overview, Customize Your Dashboard, and Dashboard FAQ point at the default help center (`support.perchwell.com/en/...`) because that is what the mirror carries. Flag at transfer and confirm they resolve for Baldwin members
