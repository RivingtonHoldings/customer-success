# Transformation Patterns Reference

Detailed examples for each of the 12 help center article transformation patterns. Use these as a guide when rewriting articles.

## 1. Jobs-to-be-Done Opening

Every article opens with one paragraph stating what the reader will accomplish. Intercom's Fin guidance is explicit that the opening must state the job, not the topic.

**Before:**
> Use the Dashboard to monitor real-time market activity and manage client needs in one view.

**Also before (the older house style, now retired):**
> In this article: You will learn how the Perchwell Dashboard allows you to monitor real-time market activity and manage all your client needs in one view.

**After:**
> Use this article to set up your Perchwell Dashboard, add and rearrange widgets, and track market activity and client needs from one view.

One paragraph, no heading above it. Name the feature. Say who it is for when the workflow needs a role. The description field carries a shorter version of the same idea in 120 to 140 characters.

## 2. Specific Over Vague

Replace generic "allows you to" descriptions with concrete actions and named UI elements.

**Before:**
> The Contacts widget allows you to stay connected to your clients by storing their information in one place.

**After:**
> Stay connected to your clients with a structured view of your Contacts.
> - Filter by Recently Created or New.
> - Use the search bar to quickly locate a contact.

Name the filters, buttons, and options the reader will actually see on screen.

## 3. Grouped Structure

Consolidate related items under meaningful parent headings. Remove sections that state the obvious.

**Before:**
```
## Navigate to the Dashboard
## Customize Dashboard Widgets
### Hot Sheets
### Contacts Widget
### Saved Searches Widget
```

**After:**
```
## Customizing Your Dashboard with Widgets
### Hot Sheets Widget
### Contacts Widget
### Saved Searches Widget
```

"Navigate to the Dashboard" (click an icon) doesn't need its own section. The widgets are grouped under one parent heading.

## 4. Bullet-Point Capabilities

Expand one-sentence descriptions into a lead sentence plus action bullets.

**Before:**
> The Listings widget allows you to view and manage your listings.

**After:**
> Monitor listing activity across your selected scope.
> - View listings at a glance.
> - Filter by address or quick options such as Price Drop and Open Houses.
> - Scope can be adjusted by MLS Listings, Brokerage Listings, or your own listings.

Each bullet describes one concrete action or option the reader can take.

**Expand into actions, not into an inventory of the screen.** The failure mode of this pattern is a bullet list of every field a display renders, which is longer than the sentence it replaced and answers nothing the member cannot already see:

**Not this:**
> Each listing card shows the address, property type, city, MLS ID, price, bedrooms, bathrooms, and a status badge with its date, such as **Active Sale** or **Closed**.

**This:**
> Listings in every status appear, including Active, Pending, Closed, and Expired.

The first describes the picture. The second answers a question a member actually asks. Image alt text is the exception to the rule, because it is written for people who cannot see the image.

## 5. Imperative Voice

Remove "You can" and "allows you to." Use direct instructions.

**Before:**
> You can use the Manage widgets button in the top right corner of your screen to customize your layout.

**After:**
> Click Manage widgets in the top right corner to customize your layout.

**More examples:**
- "You can filter by..." → "Filter by..."
- "This allows you to track..." → "Track..."
- "You can sort by Name" → "Sort by Name or Recently Updated."

**Open the section with the verb, not with the thing.** Deleting "you can" is half the pattern. The other half is that a section lead starts with what the member does, and the control follows it. A lead that starts with the control describes the screen; a lead that starts with the verb hands the member the next move, and it still echoes the heading.

| Starts with the thing | Starts with the verb |
|---|---|
| "The Save button sits in the upper left of the Search page." | "Click Save in the upper left of the Search page to save your current search." |
| "The Columns control names the template currently applied." | "Open the Columns control to add or remove columns with the checkboxes." |
| "The View control above them sets how those listings display." | "Click the View control above the search results to choose how the listings display." |

Added September 24, 2026. On Search Page Overview the reviewer made this swap in three sections that had passed every grep in step 7, because nothing in "The Columns control names the template currently applied" is a banned construction. It is just the wrong end of the sentence.

## 6. Descriptive Section Titles

Make titles specific enough for scanning.

**Before:** Access Integrated Tools
**After:** Access Third-Party Integration Tools

**Before:** Manage Your Account
**After:** Manage Your Account Settings and Notifications

The reader should know what's in the section before reading it.

## 7. Callout Labels and Varied Link Phrasing

Two rules that used to be one.

**Callouts lead with a bold label.** Intercom's guidance is that a bold "Note" or "Important" label is what flags a passage for Fin to include in an answer; the colored block is for the human reader, and emoji do nothing for retrieval.

**Before:**
> 💡 **Tip**: Use fewer columns to keep the printout easy to read.

**After:**
> **Tip:** Use fewer columns to keep the printout easy to read.

Labels are **Note:** for system behavior, **Important:** for a hard cap with an exact number, a deadline, or something irreversible, and **Tip:** for a recommendation. Do not stack two callouts, and do not use one where a plain sentence in the flow would carry the point just as well. An **Important:** callout is not the place for a soft constraint; write that as the route forward in the section where the member meets it.

**Link phrasing varies.** Links to related articles are ordinary sentences or bullets, not callouts.

**Variations to use:**
- "Learn how the [Listings Widget] works in [Dashboard Widgets Overview]."
- "[Customize Your Search View] covers column templates in detail."
- "For step-by-step guidance on adding hot sheets, see [Add a Hot Sheet to Your Dashboard]."

Never "click here" or "view our article here." Each reference should feel fresh, not copy-pasted.

## 8. Coverage Gaps

Look for features that exist in the product but aren't mentioned in the article.

**Example:** The original Dashboard Overview article didn't mention:
- The Add/Edit management tools accessible from the Listings Widget
- The pencil icon for opening the Add/Edit form on eligible listings

When updating, ask: "What can the member actually do with this feature that isn't documented here?"

The question is about missing capabilities and missing steps. It is not a hunt for shortcomings. Add a constraint only when a member will hit it, and write it as the route forward, in the section where they meet it. See `docs/standards/content-standards.md`, Constraints, and where to go instead.

## 9. Name UI Elements Exactly, and Do Not Bold Them

Name every interactive element by its exact on-screen label. Do not bold it. The house style bolded every UI element until September 10, 2026; migrating an older article means stripping that bold out.

**Before:**
> Click **Manage widgets**, then filter by **Price Drop** or **Open Houses**. Listings marked **Coming Soon** appear in the **Dashboard** widget.

**After:**
> Click Manage widgets, then filter by Price Drop or Open Houses. Listings marked Coming Soon appear in the Dashboard widget.

The exact label is what the member matches against the screen, and it does that whether or not it is bold. A page where every other phrase is bold puts emphasis on nothing.

**The two survivors,** both labels that introduce a block rather than emphasis inside a sentence:

- Callout labels: `> **Note:** ...`, `> **Important:** ...`, `> **Tip:** ...`. Intercom names the bold label as the signal Fin reads, so this one earns its keep.
- The `**Description:**` line at the top of the article.

**Bullet lead-in labels are not a third survivor.** `- **Listings.** Matched on address or MLS ID` looks like the callout pattern, a label introducing its own block, and it is not: Fin-parsable formatting check 3 reads "No other bold in the body", and Intercom names the callout label specifically. Write them plain and with a colon, as `- Listings: Matched on address or MLS ID`. The Universal Search Bar draft carried three bolded labels and unbolding them is what returned Fin-parsable formatting to 8 of 8 and the article to 95.7. Corrected September 16, 2026; this file said to keep them and was the last place in the repo still teaching the retired bold style. The colon settled September 24, 2026, and the examples under pattern 10 were corrected at the same time, having kept the bold for eight days after this paragraph banned it.

## 10. Say It Once

Fin retrieves sections alone, so the feature name repeats in every section. The facts attached to it do not. Repeat the name; give each fact one home.

The first migration test is the worked example. The Universal Search Bar draft stated the same three record types six times in 84 lines, across three consecutive sections that each enumerated them again.

**Before:**

> ## When to use the Universal Search Bar
> Open the Universal Search Bar when you already know which listing, agent, or contact you want.
> - Open one listing by its address or MLS ID
> - Open an agent's profile by name
> - Open a contact's record by name or email
>
> ### Steps:
> 2. Type one of the following:
>    - An address
>    - An MLS ID
>    - An agent name
>    - A contact name or email
>
> ## What the Universal Search Bar returns
> The Universal Search Bar returns matching records of three types: listings, agents, and contacts.
> - Listings: ...
> - Agents: ...
> - Contacts: ...

**After:** one canonical enumeration, in the section whose job it is.

> ## When to use the Universal Search Bar
> Open the Universal Search Bar when you already know which record you want and need to reach it without building a search.
>
> ### Steps:
> 2. Type an address, an MLS ID, or a name
>
> ## What the Universal Search Bar returns
> The Universal Search Bar returns matching records of three types: listings, agents, and contacts.
> - Listings: Match on address or MLS ID. ...
> - Agents: Match on name. ...
> - Contacts: Match on name or email. ...

Each section still names the feature, still stands alone, and still answers the question a member would ask it. Nothing is said twice.

**The test:** list every distinct fact in the draft. Each should appear in exactly one section. When a later section needs one that lives elsewhere, name that section or link the article rather than restating it.

---

## 11. Say It in the Member's Words

Name the real things, not the category that contains them, and use the word an agent would say out loud.

The reason is retrieval as much as readability. Kelly Miragliotta's note on the first migrated article: "they will search and type into Perchie those words they know and we want to make sure we show the right answer." A word an agent would not say is a word Fin cannot match them on, which is why the headings change too.

**Before:**
> ## Look up a record with the Universal Search Bar
>
> Look up a record from the Universal Search Bar, the Search field in the upper right of the top navigation. It is a lookup tool: type what identifies the record, click the match, and the record opens.
>
> ## What the Universal Search Bar returns
>
> The Universal Search Bar returns matching records of three types: listings, agents, and contacts.
>
> Partial entries return close matches, which means an address that matches the street name but not the street number still appears.

**After:**
> ## Find a listing, agent, or contact with the Universal Search Bar
>
> Find a listing, agent, or contact from the Universal Search Bar, the Search field in the upper right of the top navigation.
>
> ## What you find with the Universal Search Bar
>
> The Universal Search Bar finds listings, agents, and contacts.
>
> You do not have to type the whole thing, which means an address that matches the street name but not the street number still appears.

Five words carried the whole defect: **lookup**, **record**, **returns**, **partial entries**, and one sentence the reviewer could not parse at all ("what does this mean?"). The sentence was cut rather than reworded, because the mechanics it described already sat in the `Steps:` block twelve lines below it. A section lead says what the feature is for; the steps say how it works.

Two more from the same week:

- "Each Dashboard widget **is a tile that** displays a specific type of information" → "Each Dashboard widget displays a specific type of information." The reviewer proposed "section", which was rejected because a Dashboard section is a grouping of widgets; dropping the noun was better than replacing it. A definition that says what a thing does beats one that says what shape it is on screen.
- "Launch **third-party** integrations from the Dashboard" → "Launch integrations from the Dashboard." An MLS's own announcement page is the MLS's own site, not a third party, so the word was wrong as well as stiff.

**Where the pattern stops.** The same pass changed "modal" to "search window" and it was reverted the same day. `docs/product-context.md` already required "modal", one word, used consistently, "so a member and Fin both track the same thing", which is the same argument the pattern rests on. The pass was right to go beyond the reviewer's literal list; what it skipped was checking each candidate against the terminology rules first, and "modal" was the one candidate with a rule already written against it.

**The test:** read the description, the opening, and every H2 aloud as if to an agent on the phone. Any word you would not say is a candidate. Then check each candidate against the terminology rules in `docs/product-context.md` and against the on-screen label before you change it. The do-not list, with replacements and its three known false positives, is in `docs/standards/content-standards.md`.

## 12. Two or More Named Things Get a Labeled List

When a section introduces two or more named controls, tabs, views, options, or states, name them in a bullet list: the label first, a colon, one sentence on what each does. Prose is for one thing; a list is for a set.

This is a retrieval rule as much as a scanning one. A member asking Fin "what is the Results tab" wants the line that defines it, and a labeled bullet is that line. The same fact buried mid-paragraph next to three other facts is a worse chunk.

**Before:**
> The Search page has two tabs in the upper right, Filters and Results. Filters is where you set your criteria, and Results is where the matching listings appear. Click either one to switch between them. Each tab carries its own count. Filters shows how many criteria are active, Results shows how many listings match them.

**After:**
> The Perchwell Search page has two tabs in the upper right:
> - Filters: Set and adjust your search criteria. The number next to Filters shows how many filters are applied to the search.
> - Results: View the listings that match your search criteria. The number next to Results shows how many listings match the search.
>
> Click the Filters or Results tab to move between them.

**Where the pattern stops.** The trigger is a *set* of named things. A section that names one control and links out stays as prose, and so does a section with no named controls at all. On Search Page Overview the reviewer converted four sections of nine and left the other five alone, which is what makes this a rule rather than a preference: the five she left had nothing to list.

Do not confuse this with pattern 4. Pattern 4 expands a thin description into actions and warns against inventorying the screen. This one is about form: when a set exists, it is a list. Both can apply to the same section, and neither licenses a bullet per field on a listing card.

Added September 24, 2026, after the Search Page Overview migration, where this single transformation accounts for four of the nine sections the reviewer rewrote. The standard carries it under Lists and tables, along with the colon convention.
