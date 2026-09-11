# QA: Dashboard Overview

## Article and sources

- **Article name:** Dashboard Overview
- **Old title:** unchanged. "Dashboard Overview" already matches the approved `<Page> Overview` naming pattern
- **Article type:** Overview
- **Old Notion page:** https://app.notion.com/p/30c8b9e0143880208fcfff65955d4f83 (Master Article List, read only)
- **Intercom article ID:** 13903062 | **Content ID:** 16154239
- **Mirror path:** `docs/help-center/baldwin/dashboard-overview.md`
- **Shared across help centers:** no. Article 13903062 appears in `baldwin/` only
- **Draft:** `workstreams/help-center-overhaul/outputs/drafts/2026-09-10-dashboard-overview-rewrite.md`
- **Notion draft:** https://app.notion.com/p/3d78b9e0143881438489e44b4242a40c

Scored by Claude for Tara, September 10, 2026, using the **September 10, 2026 check set, revision 2**.

**Revised after Tara's review, September 10, 2026.** Three changes to the draft:

- "change which widgets appear" became "adjust which widgets display" in the opening paragraph, and "how to change your layout" became "how to adjust your layout" in the description. Tara's preference is for verbs that put the member in control of the product rather than describing what happens on screen
- The list in "What you do on the Dashboard" was missing tags, so it promised four areas while the article delivered five sections. Tags added
- Confirmed the section order follows that list exactly: market activity, contacts, saved searches, tags, listings, matching the Hot Sheets, Contacts, Saved Searches, Tags, and Listings widget sections in order

Both preferences were then written into `docs/standards/content-standards.md` and became scorecard checks, creating revision 2 of the check set: Retrieval signals check 7 (list order) and Accuracy and confidence check 5 (member-controlled verbs). The tables below are rescored on revision 2. The rewrite held at 96.4 at this point, since it already had full marks in both affected dimensions; it reached 100.0 later the same day when the integrations rewrite closed the last check. **The original drops from 51.0 to 46.3 and changes band**, because the live article fails both new checks: its lead sentence lists hot sheets, listings, saved searches, and contact information while the sections run Hot Sheets, Contacts, Saved Searches, Tags, Listings, and it says "allows you to" six times.

**Revised again after Tara's prose review, September 10, 2026.** Four passages reworded for a more active, less abstract voice. The score does not move; it was already 100.0 and stays there.

- Description: "Find your way around the Perchwell Dashboard: what each widget shows, how to adjust your layout, and which integrations launch from it" became "Get familiar with the Perchwell Dashboard: understand what each widget shows, customize your layout, and access integrations". Tara's proposed version ran 153 characters, over Intercom's 140 cap and outside the 120 to 140 the scorecard requires, so the closing "directly from the Dashboard" was cut. It repeated a word already in the sentence. The result is 125 characters
- Opening paragraph: now "Use this article to get familiar with the Perchwell Dashboard, understand what each widget shows, customize which widgets display, and access the workflows available from the Dashboard". Tara proposed "customize which widgets appear" and chose "display" instead when asked, for consistency with the member-controlled-verb rule she set earlier the same day
- "What you do on the Dashboard": now "so you see what has changed without running individual searches". Tara's proposed "so you can quickly see what has changed" contained "you can", which the content standard bans and which became Accuracy and confidence check 5 earlier the same day, so only "can" was dropped. The speed idea is already carried by "in one view"
- "What each Dashboard widget shows": now "Each Dashboard widget is a tile that displays a specific type of information. Together they give you a quick view across several areas of Perchwell." Two adjustments to Tara's version. "Activity" was dropped because only the Hot Sheets and Listings widgets show activity, while Contacts holds people, Saved Searches holds searches, and Tags holds folders of listings. The trailing ", giving you a quick view" became its own sentence, since a trailing present participle is the shape the humanizer skill flags under superficial -ing endings. Removing this sentence's "which means" clause is safe: the Hot Sheets and integrations sections still carry one each, which is what Answer completeness check 3 looks for

**Hot Sheets section reworked, September 10, 2026.** Tara proposed a rewrite and asked for an evaluation. Most of it was adopted; the score is unchanged at 100.0, and her version would very likely have held there too, so these were accuracy and consistency calls rather than points.

Adopted: "tracks new and updated listings" over the abstract "tracks listing activity"; "without rerunning a search" over "without anyone running the search again"; "two types of Hot Sheets", which matches the sources, since CRMLS heads its section "Types of Hot Sheets" and Baldwin says "Hot Sheet types"; "listing status" over a bare "status"; and "across the MLS", dropping a possessive with no loss.

Not adopted, with reasons:

- Her version opened "The Hot Sheets widget tracks ...", dropping "on the Dashboard". All five widget sections open with the same shape, which keeps each self-identifying if Fin loses the heading from the HTML. Tara chose to keep it in all five when asked
- Her ", providing an up-to-date view of listing activity" replaced "updates automatically, which means ...". That drops an explicit system-behavior fact stated in both help centers, at `baldwin/dashboard-overview.md:35` and `crmls/the-dashboard-page-overview.md:39`; "up-to-date view" implies automatic refresh without stating it. The trailing present participle is also the shape split out of the widget-tile sentence in the previous revision. Only two "which means" clauses remain in the article and Answer completeness check 3 looks for that construction on system terms, so this one stays
- Her Saved Search bullet said "criteria" twice and defined a Saved Search in terms of itself: "activity that matches the criteria of a specific Saved Search, such as ... another defined set of criteria". Now "monitors activity within one Saved Search, such as one you saved for a client, a city, or another set of criteria"
- Her bullets carried terminal periods. None of the article's six bullets do, and neither do the model articles. Tara chose to keep the article convention when asked

One knock-on fix: the paragraph below the bullets still read "walks through both kinds step by step" after the list became "two types", so it now reads "both types".

**Source note.** The live Intercom article was last updated 2026-07-02. The old Notion page was last edited 2026-07-17 with `Update Status: Transfer to Intercom`, which means the Notion revision was written and never pushed to Intercom. Usual source precedence is inverted here: Notion is the newer source and wins on the facts it states, and the mirror wins on the mobile constraint that the Notion revision dropped.

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1. disambiguation | Fail | Pass | Old article used the 📖 emoji as a pointer in six callouts, which the factor bans outright. New article has no emoji |
| 2. visual_content_text | Pass | Pass | Old article carries no images at all, so nothing is missing alt text. Seven screenshots exist on the Notion page and were never transferred. New article carries seven placeholders, each with the alt text the image will use |
| 3. undefined_terms | Fail | Pass | Old article names CRS, RPR, and BR Announcements with no expansion, and never says what a widget is. New article defines the widget and spells out Realtors Property Resource. CRS and BR Announcements are no longer named at all, since the integrations section was genericized |
| 4. structured_enumeration | Pass | Pass | Old article's integration list is a bullet list. New article adds a numbered Steps block for opening the Integrations panel, which the old article described in prose |
| 5. query_answer_symmetry | Fail | Pass | Every old heading is a bare noun ("Dashboard widgets", "Contacts Widget", "Integrated tools access"). Every new heading names what the section answers |
| 6. self_contained_sections | Pass | Pass | Neither article uses "as described above" or opens on "Then". New article restates the navigation inside step 1 rather than pointing back |
| 7. audience_specification | Pass | Pass | Neither article claims every member has the Dashboard. New article encodes the one real gate in the Listings widget wording ("a listing that belongs to you") instead of stating a role. See Open items |
| 8. entity_distribution | Fail | Pass | Old widget sections drop the Dashboard entirely and the opening falls back to "It". New article carries "Dashboard" in every heading and in the first sentence of every section |
| 9. semantic_chunk_boundaries | Pass | Pass | One widget per section in both. New article groups the five widgets under one parent section and splits layout and integrations out |
| 10. restate_questions | Pass | Pass | No tables in either. New article's integration bullet list carries an intro line |
| 11. overview_jtbd | Fail | Pass | Old body has no opening paragraph and starts cold at a heading; its only intro lives in the Intercom description field. New article opens "Use this article to ..." |
| 12. instruction_completeness | Fail | Pass | Old article has no complete instructions anywhere, and the integrations passage says to hover without saying what follows. New Steps block ends with "The integration opens outside Perchwell, so the Dashboard stays as you left it" |
| 13. limitations_workarounds | Pass | Pass | Both state the mobile constraint specifically with the alternative. New article adds the Listings widget position behavior and the separate-credentials note |
| 14. numerical_clarity | Pass | Pass | Neither article states a vague quantity. New article routes the Hot Sheet count and timeframe numbers to Dashboard FAQ, which is their canonical home, rather than restating them loosely |

**Old gate:** failed on 6 factors (1, 3, 5, 8, 11, 12).
**New gate:** all 14 pass, with no open confirm markers. Both were closed on September 10, 2026.

## Dimension scores

Revision 2 of the September 10, 2026 check set. Retrieval signals carries seven checks and Accuracy and confidence carries five.

| Dimension | Weight | Old | New | Delta |
|---|---|---|---|---|
| Retrieval signals | 30 | 4.3 (1/7) | 30.0 (7/7) | +25.7 |
| Chunk independence | 25 | 16.7 (4/6) | 25.0 (6/6) | +8.3 |
| Answer completeness | 25 | 14.3 (4/7) | 25.0 (7/7) | +10.7 |
| Fin-parsable formatting | 10 | 5.0 (4/8) | 10.0 (8/8) | +5.0 |
| Accuracy and confidence | 10 | 6.0 (3/5) | 10.0 (5/5) | +4.0 |
| **Total** | **100** | **46.3** | **100.0** | **+53.7** |

| | Old | New |
|---|---|---|
| Score | 46.3 | 100.0 |
| Band | Not retrievable as written | Fin-ready |
| Gate | Failed, 6 factors | Passed |

Answer completeness reached 7 of 7 when the integrations section was genericized on September 10, 2026. Check 6, abbreviations defined on first use, was the last one failing, held open by CRS. Dropping the product names removed the only undefined abbreviations in the article, so the check passes and the confirm marker that stood in for it is gone.

Under revision 1 the original scored 51.0, in the Needs rewrite band. The two checks added in revision 2 both fail on the live article, which moves it into the bottom band.

### Checks the old article failed

- **Retrieval signals:** description runs 152 characters, over Intercom's 140 cap; no "Use this article to" opening; every heading is a bare noun; heading echoes missing under "Dashboard widgets" and "Integrated tools access"; the section heading "Dashboard overview" duplicates the article title; the lead sentence lists hot sheets, listings, saved searches, and contact information while the sections run Hot Sheets, Contacts, Saved Searches, Tags, Listings, so the list is out of order against the article and omits Tags entirely
- **Chunk independence:** the opening falls back to "It" and the widget sections drop the Dashboard; every section is an H1, competing with the title
- **Answer completeness:** the one procedural passage does not say what happens after the hover; no system behavior and no "which means" clause anywhere; CRS, RPR, and BR undefined
- **Fin-parsable formatting:** the procedural content is prose rather than a numbered list; six callouts are emoji-led bold lines with no **Note:** or **Tip:** label; bold is applied throughout the body; 📖 appears six times
- **Accuracy and confidence:** "allows you to" appears six times, once in every widget section and again in the integrations lead, which is the pattern revision 2's verb check exists to catch

### Checks the new article fails

None. All 35 checks in revision 2 pass, and the gate passes.

The last one to close was Answer completeness 6, abbreviations defined on first use, which CRS held open because no source in the repo expands it. The genericization removed CRS from the body entirely. RPR came back when the three common integrations were named, and it is spelled out in place as Realtors Property Resource, so the check still passes. MLS is the only other abbreviation, and the glossary says not to define it.

### Genericizing the integrations section, September 10, 2026

Tara asked for the integrations list to be rewritten so the article can serve every MLS. The mirror shows why a fixed list cannot: the two help centers overlap on only half their integrations.

| Integration | Baldwin | CRMLS |
|---|---|---|
| ShowingTime | yes | yes |
| SentriLock | yes | yes |
| RPR | yes | yes |
| BR Announcements | yes | no |
| Infosparks | yes | no |
| CRS | yes | no |
| Realist | no | yes |
| Down Payment Resource | no | yes |
| Cloud CMA | no | yes |

Sources: `docs/help-center/baldwin/integration-tools-on-the-dashboard.md` and `docs/help-center/crmls/integration-tools-on-the-dashboard.md`, both live and both last updated 2026-07-02.

The section names the three integrations both in-scope help centers demonstrably have, ShowingTime, SentriLock, and RPR, as commonly connected rather than guaranteed. It then says the panel lists only what the member's own MLS has enabled, points at the panel as the authoritative list, and routes to each MLS's own Integration Tools on the Dashboard article for detail. The nine products that exist in only one help center are not named.

Revised again on September 10, 2026 after Tara's review. An earlier version named no products at all and closed with "a member at a different MLS may see a different set". That clause was writer-facing reasoning in member-facing text: a member has no use for what another MLS sees, only for what is in their own panel. Naming the three common tools also gives Fin something concrete to match when a member types "ShowingTime" or "SentriLock", which the category-only version could not do.

The two live articles also conflict on the outcome. Baldwin says an integration opens "in a new window"; CRMLS says "in a new browser tab". The rewrite says it opens "outside Perchwell, so the Dashboard stays as you left it", which is true in both and avoids picking a side that would be wrong for one MLS.

## Fin test questions

| Question a member may type | Old answers from one section | New answers from one section |
|---|---|---|
| Where do I find the Dashboard in Perchwell? | No. The location is not in the live article at all | Yes. "What you do on the Dashboard" |
| How do I change which widgets show on my Dashboard? | Partly. The Manage widgets sentence sits under a bare "Dashboard widgets" heading with no page context | Yes. "Choose and arrange your Dashboard widgets" |
| What are the two types of Hot Sheet? | No. The live article does not mention types | Yes. "Hot Sheets widget on the Dashboard" |
| Can I sort the Contacts widget on my Dashboard? | No. Sort options are not in the live article | Yes. "Contacts widget on the Dashboard" |
| Why can't I move the Listings widget? | No | Yes. "Listings widget on the Dashboard", as a **Note:** |
| How do I open ShowingTime from Perchwell? | Partly. "Hover over the right side of the screen" with no numbered steps and no outcome | Yes. "Launch third-party integrations from the Dashboard" |
| Is the Dashboard available on the mobile app? | Yes. "Things to Know" | Yes. "Things to Know" |
| Do I need a separate login for RPR? | No | Yes. "Launch third-party integrations from the Dashboard", as a **Note:** |

## Open items

**Confirm markers in the draft**

None. Both were closed on September 10, 2026.

- `[confirm: what CRS stands for]` was removed with the product names when the integrations section was genericized. Nothing in the article now needs a first-use definition
- `[confirm: whether the on-screen options are still labeled New Hot Sheet and From Saved Search]` was resolved by checking the CRMLS counterpart. `crmls/adding-a-hot-sheet-to-the-dashboard.md` names the on-screen options 'New Hot Sheet' and 'From Saved Search', exactly as `baldwin/add-a-hot-sheet-to-the-dashboard.md` does. Two independent live articles agree, so the draft's labels stand and the marker is gone.

  The old Notion page was not wrong, it was answering a different question. "Quick Hot Sheet" is the name of the *type*, which CRMLS uses in prose ("Quick Hot Sheets"), while "New Hot Sheet" is the *button* the member clicks. Baldwin's article calls the same type "New Hot Sheets". The draft names the button, which is what a member looking at the screen needs

**Universality: the integrations section is done, the article is not**

The integrations rewrite makes that one section MLS-neutral. Seven other things in this article are still Baldwin-specific, and each needs a decision before the body can serve both help centers. **None of them is a defect in the current Baldwin draft**, which is complete and scores 100.0; they are the remaining scope of "universal" if the team takes that route.

1. **The widget lineup is not a blocker.** Investigated in full on September 10, 2026; see `audit/dashboard-widget-lineup-2026-09-10.md`. All five widgets this article covers, Hot Sheets, Contacts, Saved Searches, Tags, and Listings, exist in CRMLS as well, so the five widget sections are universal as written. The only divergence is CRMLS's Days on Market widget, which has its own CRMLS articles. Scope is Baldwin and CRMLS only; NYC is out, confirmed by Tara on September 10, 2026. The Presentations widget is not a divergence either, because Listing Presentations has been removed from CRMLS and was never a Baldwin feature.

   Two things this file previously got wrong. **It said CRMLS has no Tags widget**; CRMLS does have one, and the claim came from `crmls/the-dashboard-page-overview.md`, which omits Tags, rather than from `crmls/customizing-your-dashboard.md`, which owns the Manage Widgets enumeration and lists it. An overview article's silence is not evidence a feature is absent. **It also treated the Presentations widget as a live divergence**, which it is not
2. **Hot Sheet limits differ by MLS.** `crmls/adding-a-hot-sheet-to-the-dashboard.md` states a maximum of 5 Hot Sheets per Dashboard. `baldwin/dashboard-faq.md` answers the same question with "There is no limit. You can add as many as you'd like." Either the cap is CRMLS-specific or one article is stale. This draft routes the question to Baldwin's Dashboard FAQ, which is correct for a Baldwin row, but a shared body cannot point at an answer that is wrong for the other MLS
3. **Quick Hot Sheet filters differ by MLS.** This draft says a New Hot Sheet monitors by property type, timeframe, and status, which matches Baldwin's article. CRMLS's article says Quick Hot Sheets can be filtered "by property type or location, depending on the MLS", and the old Notion row notes "Quick Hotsheet for CRMLS has the city and county". A shared body needs the location filter handled conditionally
4. **Sort options conflict.** This draft says the Contacts and Saved Searches widgets sort by Name or Recently Created, from the Notion source. CRMLS's overview says Contacts filters by Recently Created or New, and Saved Searches sorts by Name or Recently Updated. Either the widgets differ by MLS or one source is stale
5. **Two linked articles have no CRMLS equivalent.** `New Terminology` and `Listings Widget Overview` exist only in Baldwin. A universal body would need those sentences to degrade gracefully where the target article does not exist
6. **Three linked articles have different titles per MLS.** Baldwin `Add a Hot Sheet to the Dashboard` is CRMLS `Adding a Hot Sheet to the Dashboard`; Baldwin `Customize Your Dashboard` is CRMLS `Customizing Your Dashboard`; Baldwin `Dashboard FAQ` has no CRMLS counterpart beyond a general `Frequently Asked Questions`. Link text is the article title by standard, so the text itself changes per MLS, not just the URL. `Create and Manage Your Contacts in Perchwell`, `Manage Your Saved Searches`, and `Tags Page Overview` match in both and are safe
7. **The mobile constraint is sourced from Baldwin only.** "The Dashboard and Hot Sheets are not available in the Perchwell mobile app" traces to `baldwin/dashboard-faq.md` and the live Baldwin article. No CRMLS source states it, and `docs/product-context.md` claims web and mobile parity. Publishing it in a CRMLS help center would be an unverified claim

There is also a schema problem underneath all of this: `MLS/AOR` in the new database is a single select, so a genuinely universal article has no row that represents "all MLSs." That is the same open question already on the project status page about the 26 shared articles, and this article is now a second instance of it.

**Decisions the team owes**

- **The Arcade walkthrough is known stale.** The draft carries `https://app.arcade.software/share/uP0zdXgQGkrqA3tt5lpo` per the migration rule, but the old row reads `Video: Update Required` and `Support / Training Updates: update arcade with new framing`. Decide whether to ship the draft with the current Arcade, hold for the re-record, or drop the embed
- **Seven screenshots already exist and were never transferred.** They are on the Notion page as expiring S3 URLs, so the draft carries placeholders rather than image links. Six map to existing Notion images (Manage widgets, two Hot Sheet types, Contacts, Saved Searches, Tags, Listings); the full-Dashboard shot in the first section is a new ask. The old row's `Screenshot: Done` refers to the Notion images, not to anything live
- **MLS-specific integrations.** The old row says "Small tweaks needed to remove MLS specific integrations." This row is `MLS/AOR: Baldwin`, so BR Announcements and Baldwin REALTORS stay. A CRMLS version needs its own row and its own integration list. The same note adds "Quick Hotsheet for CRMLS has the city and county", which is a CRMLS behavior difference to capture when that row is created
- **Invited clients and the Dashboard.** The old row's `Roles` reads "All - but client", carried across as `All Except Client`. No source in the repo states that invited clients cannot reach the Dashboard, so the draft asserts nothing about it rather than inventing a restriction. Confirm whether a role gates the page; if it does, the body needs an audience line
- **Listings widget scope options conflict.** The old Notion page lists them as MLS Listings, My Brokerage, My Office, My Listings and calls them sort options. `Listings Widget Overview` calls them scope filters named MLS Listings, Brokerage Listings, My Listings, Office listings. The draft describes the scope and links out rather than restating a contested enumeration. `Listings Widget Overview` needs correcting or confirming when it is migrated

**Standards changes this article surfaced, now applied**

Both were written into the standards on September 10, 2026, creating revision 2 of the check set:

- **List order governs section order.** `content-standards.md`, under Structure and heading levels, "Enumerations set the section order", with a pointer from Opening paragraph and a line in the quality checklist. Scorecard: Retrieval signals check 7
- **Member-controlled verbs.** `content-standards.md`, under Voice and terminology, plus a quality checklist line. Scorecard: Accuracy and confidence check 5

Outstanding: the Universal Search Bar QA file is still on revision 1. Its current draft passes both new checks and rises from 95.0 to 95.7, but its live-article and September 9 columns have not been rechecked. Worth doing when that article next comes up rather than as its own task.

**Link corrections made in the draft**

- The live Contacts link points at article 8955819, which no longer resolves. Repointed to 14790755, `Create and Manage Your Contacts in Perchwell`
- The live Listings link points at `Manage Listings Page Overview` (13623016). Repointed to `Listings Widget Overview` (13903171), which is the widget's own article
- "Inforsparks" corrected to "Infosparks" in both sources, matching `Integration Tools on the Dashboard` and the product's real name
- Seven of the nine outbound links use the default help center path (`support.perchwell.com/en/...`) rather than `/baldwin/en/...`, because that is how the mirror records them. Only New Terminology and Tags Page Overview carry a `/baldwin/en/` path. Flag all seven at Intercom transfer to confirm each resolves for Baldwin members. An earlier version of this file said six, which was a miscount
