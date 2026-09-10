# Transformation Patterns Reference

Detailed examples for each of the 10 help center article transformation patterns. Use these as a guide when rewriting articles.

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
- "You can sort by Name" → "Sort by **Name** or **Recently Updated**."

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

Bullet lead-in labels, as in `- **Listings.** Matched on address or MLS ID`, follow the callout pattern: a label introducing its own block, not emphasis in running prose. Keep them.

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
> - **Listings.** ...
> - **Agents.** ...
> - **Contacts.** ...

**After:** one canonical enumeration, in the section whose job it is.

> ## When to use the Universal Search Bar
> Open the Universal Search Bar when you already know which record you want and need to reach it without building a search.
>
> ### Steps:
> 2. Type an address, an MLS ID, or a name
>
> ## What the Universal Search Bar returns
> The Universal Search Bar returns matching records of three types: listings, agents, and contacts.
> - **Listings.** Match on address or MLS ID. ...
> - **Agents.** Match on name. ...
> - **Contacts.** Match on name or email. ...

Each section still names the feature, still stands alone, and still answers the question a member would ask it. Nothing is said twice.

**The test:** list every distinct fact in the draft. Each should appear in exactly one section. When a later section needs one that lives elsewhere, name that section or link the article rather than restating it.
