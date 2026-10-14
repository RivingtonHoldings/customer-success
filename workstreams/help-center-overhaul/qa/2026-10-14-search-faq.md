# QA: Search FAQ

Article name: Search FAQ. Title unchanged, confirmed by Tara October 14, 2026.

Sources:

- Old Notion page: https://app.notion.com/p/3658b9e014388055841dfb006b8d5074 (Master Article List, last edited July 17, 2026; 8 comment threads, all resolved)
- Intercom article ID 15200328, content ID 17970084 (the old row's Intercom Internal URL carries the content ID, not the article ID). Live body checked with `get_article` October 14, 2026; it matches the mirror, last updated August 31, 2026
- Mirror: `docs/help-center/baldwin/search-faq.md` (Baldwin only)
- Screenshots on the old Notion page, July 4, 2026: Location section school filters, the crossed-out eye icon next to Actions, the street name field
- Screenshots supplied by Tara October 14, 2026: Waterfront Feet Y/N, Named Waterfront Y/N and Waterfront Footage, Lot Description and Water Property Type values, Apx Acreage, the Street name field in the Location section, the Open house filter, and the Listings widget Open Houses tab
- Product answers from Tara, October 14, 2026: Quick Filters update stays a generic 2026 date; saved searches from the legacy platform arrived with alerts off; Start New stays in the same tab and Open New Tab is how to start a search in a new tab; clients hide listings in searches they create and in shared ones, and hiding in a shared search hides the listings in the agent's version too; Export CSV includes any field entered when adding a listing
- New Notion draft: https://app.notion.com/p/3f98b9e0143881ad877ae38e1b822baf
- Sibling drafts read for the set pass: Search Page Overview (Notion, fetched October 14), Client Collaboration FAQ (Notion, fetched October 14), Filter Your Search with Map Tools, Create a Search with Filters, Set Up Email Alerts for Saved Searches, Manage Your Saved Searches, Actions Menu Options on the Search Page, Find Listings in the Listings Widget (repo copies)

Scored by Claude for Tara, October 14, 2026. Check set: September 10, 2026, revision 2.

## Golden questions

| Factor | Old | New | Note |
|---|---|---|---|
| 1 disambiguation | Pass | Pass | Old "eyeball icon" named a shape without a place; new names the crossed-out eye icon next to Actions on the Results tab |
| 2 visual_content_text | **Fail** | Pass | Old closed the Driving Directions answer with a trailing colon and an image with no alt text. New gives that image alt text and adds three placeholders with alt text |
| 3 undefined_terms | **Fail** | Pass | Old used CSV, CRM, and Parallel Period undefined. New defines CSV, CRM, and Apx Acreage; the Parallel Period question is cut |
| 4 structured_enumeration | **Fail** | Pass | Old listed alert frequencies, alert activity, and share options in prose. New gives the share options and the waterfront filters as labeled lists |
| 5 query_answer_symmetry | Pass | Pass | Question headings in both. Old had one empty heading, counted under formatting |
| 6 self_contained_sections | Pass | Pass | |
| 7 audience_specification | Pass | Pass | The CRM answer names brokers in both; every other answer applies to all non-client roles |
| 8 entity_distribution | Pass | Pass | |
| 9 semantic_chunk_boundaries | **Fail** | Pass | Old put an unheaded street name question inside the satellite images answer |
| 10 restate_questions | Pass | Pass | No tables in either |
| 11 overview_jtbd | **Fail** | Pass | Old had no opening paragraph. New uses the single-job opening for a many-question article |
| 12 instruction_completeness | **Fail** | Pass | Old MLS ID steps stopped at "choose Share" with no outcome; new hands sharing to Share Multiple Listings in Perchwell |
| 13 limitations_workarounds | Pass | Pass | School filter plus map boundary states the Or behavior and the workaround in both; new drops "feedback has been shared with the product team" |
| 14 numerical_clarity | **Fail** | Pass | Old "a few options" for sharing. New lists the two options |

Old: 7 of 14. New: 14 of 14, with no open `[confirm: ...]` markers (see Open items).

## Plain language gate

Old: **Fail**, on checks 1 and 3.

| Term flagged | Replacement |
|---|---|
| "Navigate to the Results tab", in the MLS ID steps | Cut with the steps; the answer links Share Multiple Listings in Perchwell |
| "Parallel Period" and "Paragon", in a heading and answer | Question rewritten for the agent: "Why are alerts off on saved searches from a legacy platform?" |
| "eyeball icon" | "crossed-out eye icon", the shape on screen and the Search Page Overview wording |
| "cadence", in the satellite answer | "schedule" |

New: **Pass**. Checks 1 through 5 clear. Check 5: "search", "unhide", "share", "export", "hide", and "turn on alerts" each appear in the answer that covers them, not only in link titles.

## Dimensions

| Dimension | Old | New | Delta |
|---|---|---|---|
| Retrieval signals (30) | 12.86 | 30.00 | +17.14 |
| Chunk independence (25) | 12.50 | 25.00 | +12.50 |
| Answer completeness (25) | 7.14 | 25.00 | +17.86 |
| Fin-parsable formatting (10) | 6.25 | 10.00 | +3.75 |
| Accuracy and confidence (10) | 4.00 | 10.00 | +6.00 |
| **Total** | **42.75** | **100.00** | **+57.25** |

Old band: Not retrievable as written. New band: Fin-ready, with every confirm marker resolved.

Old failures by dimension:

- Retrieval: description 104 characters; no opening paragraph; one empty heading; answers that do not echo their question ("Click the eyeball icon")
- Chunk independence: every heading at H1; an orphan question inside another answer; three questions asked twice (multiple searches, street name, MLS ID)
- Answer completeness: MLS ID steps end without an outcome; undefined terms; "a few options"; the MLS ID and share procedure re-explained instead of linked
- Formatting: bold UI labels, steps with terminal periods, an image with no alt text
- Accuracy: Paragon named; "planned for Q3 2026" stale; the Paragon answer contradicts itself on alerts; "you can" throughout

## Fin test questions

| Question | Old answers from one section | New answers from one section |
|---|---|---|
| Can I search by school district? | Yes, vaguely ("school-related filters") | Yes, names the four school filters |
| How do I search one street without getting partial matches? | Split across two sections, and wrong (quotation marks) | Yes |
| I drew around the waterfront, how do I get rid of listings that aren't on the water? | Partly; names filters that are not on screen | Yes |
| How do I get hidden listings back? | Yes | Yes |
| Can saved search alerts come by text? | Yes | Yes |
| How do I open a second search in another tab? | Wrong: says Start New opens a new tab | Yes |
| How do I find open houses this weekend? | No | Yes |
| Why can't I click Driving Directions? | Yes | Yes |

## Source differences and how each was settled

| Question | Live article | Old Notion page | Settled |
|---|---|---|---|
| School zone | "school-related filters" | School filters under Location, with screenshot | Notion screenshot names the four filters |
| Unhide | "eyeball icon" | Eye icon next to Actions, with screenshot | Screenshot and Search Page Overview |
| Street name | "Street field", plus an orphan answer under satellite images | Same, screenshot shows the field in Property Details | Tara's screenshots: the Street name field under Location is a pick list, so the live quotation-mark advice is wrong; corrected October 14, 2026 |
| Quick Filters | Planned for Q3 2026 | Planned for later in 2026 | Date dropped in review, approved by Tara: the answer says No and gives a route forward |
| Alerts | Frequencies and activity listed | "each time a new listing matches" | Live, trimmed to a link to Set Up Email Alerts |
| Waterfront exclusion | "waterfront and direct bay front view filters" | "Names Waterfront = No", Water Property Type with Not | Tara's screenshots: five filters, two with Or, And, and Not |
| Share multiple listings | Email, public link, Tag | Adds Tag landing page detail | Actions menu options from the set |
| School plus map | Or, draw a radius | Adds "filter via the column" | Live. The column suggestion is dropped: a column filter becomes a search filter, which would combine as Or with the boundary again |
| MLS ID | Comma | Comma and a space | Both examples carry a space; written "separated by commas" with the example |
| Multiple searches | Start New opens a new tab | New Perchwell tab | Tara: Open New Tab in the Unsaved Changes window; a browser tab otherwise |
| Open houses | Not present | Filters and Dashboard Open House tab | Tara's screenshots: Open house filter in Listing Details; Open Houses tab in the Listings widget |
| Paragon alerts | Adds "turn off alerts in Paragon" | Without it | Client-side question already in the Client Collaboration FAQ draft; agent-side question kept, per Tara: alerts arrived off |

## Scope decisions

- Merged: two multiple-searches questions, two street name questions, two MLS ID questions
- Cut, answered in the Client Collaboration FAQ draft: "Will I receive a notification if my client changes the search criteria?" and "Will contacts who have existing saved search emails from Paragon still receive those alerts?"
- Kept, rewritten for the agent: why alerts are off on saved searches from a legacy platform
- Added from the old Notion page: open houses
- Grouped into five H2s with question H3s: filters, map, results, sharing and exporting, saved searches and alerts
- Review round, October 14, 2026: removed "in Perchwell" from the opening, and removed the lead sentence under all five group H2s, per a reviewer. The second change added an FAQ exception to the parent-H2 rule in `content-standards.md` and to Retrieval signals check 5 in the scorecard, both awaiting Kelly and Rafe. Score unchanged at 100
- Review round, October 14, 2026: filter groups named "under <heading> on the Filters tab" in all five answers, matching the on-screen panel headings and the set's "under Listing Visibility & Access"; "Waterfront under Lot Description" became "the Waterfront option in Lot Description" so "under" keeps one sense; the school filters placeholder and alt text no longer repeat the four names from the answer. Score unchanged at 100
- Review round, October 14, 2026: the Street name field is a pick list (type, then select a match), per Tara's screenshot, so the quotation-mark advice is cut. A sentence saying quotation marks are not needed was added, then cut at the reviewer's suggestion: the bare-deficit exception covers a promised capability the product lacks, not a technique the pick list makes unnecessary, and once this article replaces the live one Fin has no published source left that says to type them. The Common Perchwell FAQs mirror (draft state) carries the same advice and should lose it when migrated
- Review round, October 14, 2026: acreage answer says what From and To take ("Enter the minimum in the From field and the maximum in the To field") instead of "the range of acres", per a reviewer. The reviewer's "minimum and maximum acreage" was adjusted so "acreage" does not repeat across back-to-back sentences outside the label and its definition
- Review round, October 14, 2026: subdivision answer drops "in the browser or the Perchwell mobile app" (mobile is at parity, and no other answer names it) and adds "then select it from the list of matches", since Subdivision/Condo is a pick list like Street name, confirmed by Tara. The Search for a Condo mirror article still says only "enter the name" and should change when it is migrated
- Review round, October 14, 2026: waterfront list tightened per a reviewer. The Y/N items define Yes only, the Not sentence leads with the action, and Waterfront Footage reads "Enter the minimum and maximum frontage, in feet, in the From and To fields", keeping the unit and matching the acreage answer's minimum and maximum instead of the reviewer's "range of waterfront frontage"
- Review round, October 14, 2026: open house answer tightened per a reviewer, keeping the result in its own sentence. The reviewer's "You can also find upcoming open houses from the Dashboard" became "To find open houses from the Dashboard, ...", the standard's second-way pattern, because "you can" is still banned and the FAQ exception is open (project-status.md, Tara and Kelly). "Upcoming" was left out as unsourced
- Review round, October 14, 2026: MLS ID answer split into one listing and multiple listings, per a reviewer. A click on the result is needed to open a listing from the Universal Search Bar, confirmed by Tara. "status filters" became "under Status & Activity on the Filters tab", the on-screen heading. The Universal Search Bar draft's line "an exact match on either one pulls up that listing directly" reads as if no click is needed and could be clarified on its next review
- Review round, October 14, 2026: Quick Filters answer is now a plain No, the six filters, and a route to the Search filters and values field. The planned-update date and the Baldwin MLS staff reasoning are cut, per a reviewer and approved by Tara, which reverses her earlier "generic 2026 update" answer. Maintenance trigger: rewrite this answer when Quick Filter customization ships
- Review round, October 14, 2026: new filters answer opens with Yes, per a reviewer. Tara confirmed the Board approves new listing fields, not filters, that a new field can then be searched as a filter, and that members request one from Baldwin MLS. Contact line added from the wording CS gives members (email, phone, Monday through Friday hours), with times written 8:00 AM and 4:30 PM per the Date & Time Formatting Guidelines. The same contact details appear in three other live Baldwin articles, so a change to them touches all four. The reviewer's "search fields" was not adopted, since it mixes listing fields and search filters
- Review round, October 14, 2026: map-or-filters-first answer shortened to "No. Draw on the map before or after you set your search filters." The reviewer's "You can draw" became the imperative, since "you can" is still banned pending the FAQ exception. Dropping "works together with your other filters" also removes a hint of And logic that the school-and-map answer contradicts (boundary and Location filters combine as Or)
- Review round, October 14, 2026: radius and commute answer cut from three sentences to two with one "pin icon", per a reviewer. The reviewer's opening ("Click the Address search pin icon ...") gained "To find the Radius and Commute tools," so the first sentence still echoes the question, per the FAQ first-sentence rule and Retrieval signals check 5
- Review round, October 14, 2026: school-and-map answer drops "combine as Or" for the member-facing behavior, per a reviewer, folded into one positive sentence that rules out the expected "only listings in both" reading. Map Tools and Search Page Overview keep "combine as Or", where it ties to the Or dropdown
- Review round, October 14, 2026: waterfront-boundary answer reworded per a reviewer ("limit your results to waterfront listings within the map boundary", "the information entered for each listing"), keeping "the Waterfront option in Lot Description" so "under" keeps one sense. The reviewer asked for the And behavior to be tested before it is locked in, so it carries a confirm marker. The claim rests on Create a Search with Filters (separate filters must each match) and on Map Tools, which documents Or only for Location filters; Lot Description is under Features
- Review round, October 14, 2026: satellite answer drops "the same schedule as Google Maps", per a reviewer. The Search map credits Mapbox and OpenStreetMap (visible in the lower left of the map in Tara's Hidden Listings screenshot), so the Google comparison likely names the wrong provider. The one-to-three-year cadence has no source beyond the live article and old Notion page, which share one sentence, so it carries a confirm marker
- Review round, October 14, 2026: unhide answer reorganized per a reviewer, keeping the opening that answers with "Unhide" and "every hidden listing" for Unhide All. The reviewer's "may not show every listing you have hidden if your current filters exclude some of them" was tested by Tara: with a hidden listing excluded by a new filter, the hidden count still showed it, and unhiding cleared the count without raising the listing count. So the filter limit applies to the results after unhiding, and the answer now says "The listings return to your search results if they still match your current filters." The window's own note ("Some hidden listings may not show depending on your filters") is not quoted, since the test did not check what the window itself lists
- Review round, October 14, 2026: multiple-searches answer opens with "multiple browser tabs", per a reviewer. The reviewer's last sentence ("Your current search stays open with its unsaved changes ...") repeated "current search" and "unsaved changes" from the sentence before it, so it became "A new search opens in another tab, and the original tab keeps your changes."
- Review round, October 14, 2026: Driving Directions answer now tells members to turn on location access for Perchwell in their browser settings, a per-site permission, per a reviewer. "In the Actions menu" is kept to separate it from the Commute tool's driving travel method. The live Chrome image showed the general location setting and no longer matched, so it is replaced by a placeholder for Perchwell's site settings
- Review round, October 14, 2026: sharing answer applied as the reviewer wrote it. The Share item says what the member does rather than that a window opens, and the invited and uninvited cases are now two sentences. Both list items are imperative, so the list is consistent within itself
- Review round, October 14, 2026: CSV answer takes the reviewer's second sentence. The reviewer's "All listing fields are available to export" was not adopted: it is broader than the confirmed scope (fields entered when adding a listing, which may not cover calculated values such as Days on Market), and it dropped the CSV definition required on first use. The first sentence is tightened to "Every field entered when adding a listing is available to export to a CSV (comma-separated values) file."
- Review round, October 14, 2026: CRM answer's link line now says "contact data", per a reviewer, to separate it from listing data. The rest of the reviewer's rewrite ("through a Bridge feed", dropping broker-only and no cost) waits on the Bridge confirmation. The reviewer also proposed dropping the CRM definition; held, since golden question 3 requires it and the Client Collaboration FAQ draft defines CRM
- Review round, October 14, 2026: saved search section applied from a reviewer's batch (no "in Perchwell", "If there is no matching activity, no email is sent", link sentences on their own lines with less repeated detail, "transferred" for the legacy answer), with four adjustments. "There is no limit to the number of saved searches you can have" became "There is no limit on the number of saved searches" ("you can" ban). The second "also" in the client-edit sentences was cut (back-to-back echo). "Have alerts turned off by default" became "arrived with alerts turned off", since alerts were off on transfer, not a default setting. "An email" stayed "one email", from the live source, because it rules out one email per listing. The reviewer's check on client-side hiding syncing to the agent's search was already confirmed by Tara earlier the same day
- Review round, October 14, 2026: opening changed to "Use this article to find quick answers to common questions about the Search page and its features.", per a reviewer, because the article covers sharing, exporting, saved searches, and alerts as well as searching. It now names the feature, which strengthens Retrieval signals check 3, and still states a single job without repeating the description's list
- October 14, 2026: Water Property Type examples are now Bay front, Gulf front, and Lake front, per Tara, as the values Baldwin members most likely search for. Gulf front is confirmed as a value by Tara and replaced River front. Bay front is confirmed on screen; Gulf front and Lake front follow its spelling pattern, so confirm them when the screenshot is shot. The placeholder alt text names Bay front and Bayou front, the values at the top of the open list
- October 14, 2026: sharing answer gains a third option, "Share via Text: Text the listings to a contact directly.", per Tara. The Actions menu lists Share via Text alongside Share and Share via Message (Actions Menu Options on the Search Page and Share Listings with Clients from Search drafts), and it opens the Share window on the Text tab
- October 14, 2026: CRM answer gains the Baldwin MLS team's email, phone, and hours, per Tara, in the same form as the new filters answer. The contact details now appear in two answers of this article; each answer is retrieved on its own, so both carry them. A change to the contact details touches both answers here and three other live Baldwin articles
- October 14, 2026: satellite answer takes a reviewer's structure ("is updated by the map provider", "The frequency varies by location, so ..."), with "periodically" replaced by "with no set schedule". "Periodically" can read as a regular cadence and does not answer "how often"; "no set schedule" is the confirmed answer from Tara's team
- October 14, 2026: satellite answer rewritten per Tara to lead with what members can expect (the imagery may not show recent changes), then "How often the imagery updates varies by location", then a route forward to the listing photos on the Listing Detail Page. The photo tip is advice approved by Tara, not documented product behavior; listing photos are not guaranteed to be recent either

## Open items

- Waterfront Y/N filters: resolved by Tara, October 14, 2026. Named Waterfront Y/N is frontage on a named body of water, such as a lake, river, bay, or creek; Waterfront Feet Y/N is whether the listing records a waterfront frontage measurement in linear feet
- Resolved October 14, 2026: Tara's team confirmed members reach out to the MLS to set up a Bridge feed. The answer now takes the reviewer's direct wording with "Contact the Baldwin MLS team to set up the feed." "Broker-only" and "at no cost" were dropped as unconfirmed; "Brokers can" stays from the live source. The CRM definition stays, per Tara
- Resolved October 14, 2026: Tara's team reported that Perchwell does not control satellite imagery updates. Mapbox supplies the Baldwin Search map, and Google Maps supplies NYC's map and the Listing Detail Page. Neither provider guarantees a refresh schedule, updates vary by location and zoom level, and one to three years is an industry estimate Perchwell cannot guarantee. The number is removed, and the answer says there is no set schedule and timing varies by location. An earlier same-day note that one to three years was confirmed is superseded. The team's suggested wording was adjusted to lead with the answer, keep "Search map" for the heading echo, drop "periodically", and avoid repeating "updated" and "Updates" in back-to-back sentences. The provider is not named, since the Listing Detail Page uses a different one
- Resolved October 14, 2026: Tara tested a map boundary plus Waterfront in Lot Description. The result count dropped and no listing outside the boundary appeared, so the two combine as And and the marker is removed
- Unhide: resolved from Tara's screenshot of the Hidden Listings window (Cancel, Unhide All with a count, Unhide Selected, and the note that some hidden listings may not show depending on filters). The answer carries a three-step numbered list with no `Steps:` heading, because the question is already an H3 and a Steps heading would sit at H4. A reviewer may prefer prose or an H4
- Links: all point at live article titles and URLs, matching the set; six point into the default help center (`/en/`) and get flagged at transfer. Titles change as the siblings port
- Four screenshot placeholders: school filters, Water Property Type values, the Hidden Listings window, and Chrome's site settings for Perchwell with Location set to Allow. The live Driving Directions image is no longer carried
- The live Client Collaboration FAQ answer on legacy alerts carries the same contradiction this article had; its Notion draft already fixes it
- Maintenance trigger: when Quick Filter customization ships, rewrite "Can I customize the Quick Filters on the Search page?" to explain how
