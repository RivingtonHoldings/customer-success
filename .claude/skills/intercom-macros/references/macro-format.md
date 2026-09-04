# Macro Format

The file template, the per-macro template, and two worked examples modeled on the CS team's own best macros. Apply everything silently; a macro never mentions these rules.

## File template

```markdown
# Macros: <Feature name>

<!-- Status: Draft | MLS: <scope> | Source: <release notes ref> | Date: YYYY-MM-DD -->

Related article: <public URL, or [link: <article title>], or "none">

Open items: <every [confirm: ...] marker collected in one list, or "none">

## <Macro 1 title>

**Intercom settings:** Available for Everyone. Available when Starting conversations, Replying, Adding notes.

<paste-ready macro body>

## <Macro 2 title>

...
```

Everything above the first `##` is for CS eyes only. Everything under a macro title, except the settings line, must be paste-ready: no markers, no notes to CS other than screenshot placeholders, which CS replaces with real images before saving the macro.

## Per-macro shape

1. **Opening line.** Answer the question directly in one or two sentences before any steps, so a member who reads nothing else still gets the answer. If the question is "where did X go," the opening line says where it is now.
2. **Numbered steps.** One action each, from an entry point the member can always find. Bold the exact UI label. Say where on the screen the element sits. A direct URL beats navigation instructions when one exists.
3. **Screenshot placeholders.** After each step that points at the screen: `[Screenshot: <screen or menu state>. Highlight: <element to box or arrow>.]` One per line, own line.
4. **What happens next.** After the last step, one sentence confirming the result the member should see.
5. **Extras, only if they earn their place.** A default, a limit, an irreversible action, or a link to the related help center article ("<Article title> covers this in more detail: <URL>").
6. **Closing line.** One short, warm invitation to follow up. Vary it across macros in the same file; reps may also personalize it.

## Worked example 1: navigation question

Title: `BALDWIN- AGENT ROSTER / MYMLS`

```
You can find the agent roster in the Contacts tab:

1. Head over to the Contacts page: https://www.perchwell.com/contacts

[Screenshot: Top navigation bar. Highlight: the Contacts tab.]

2. Click on the My MLS section:

[Screenshot: Contacts page with the My Contacts / My MLS tabs visible. Highlight: the My MLS tab.]

Now you will be able to see the agent roster!

I hope this helps, and please let me know if you have any other questions. Thank you so much!
```

Why it works: the opening line answers immediately; each step is one click with a placeholder telling CS exactly what to box; the closing is warm without being long.

## Worked example 2: workflow question

Title: `CSV- How can I create a CSV template?`

```
You can create and modify a CSV template by going to Actions on Search, then clicking Export CSV.

1. Choose your listings, then go to **Actions** on the upper right-hand side. Click on **Export CSV**.

[Screenshot: Search results with the Actions menu open. Highlight: the Export CSV option.]

2. This opens the CSV template page, where you can add, remove, and re-order columns. Re-order by dragging the six-dot icon.

[Screenshot: CSV template page. Highlight: the six-dot drag icon next to a column.]

3. To add a column that is not pre-selected, search for it in the **Search columns** bar. You can find fields like HOA, Lot Size, and more.

[Screenshot: CSV template page. Highlight: the Search columns bar.]

4. To save this configuration, click **Save as template** on the top right and give it a name.

[Screenshot: Template naming view. Highlight: the Save as template button.]

5. (Optional) To make this your default, click the **Set as default list** toggle.

[Screenshot: Template naming view. Highlight: the Set as default list toggle.]

Your saved templates will now appear on the left-hand side the next time you export.

Hope that does the trick! If anything looks different on your screen, just reply here and we will sort it out together.
```

Why it works: it walks a brand-new user through the whole flow without skipping a click, marks the optional step, and confirms what the member sees at the end.

## Checklist

Confirm every macro before saving the file:

- Title reads the way a member asks, with an ALL-CAPS topic or MLS prefix
- Settings line present and exact
- Opening line answers the question before any steps
- Steps are numbered, one action each, from a findable entry point, with screen locations
- Every clickable element the member sees is named exactly and bolded (or given as a direct URL)
- A screenshot placeholder follows every step that points at the screen, naming what to capture and what to highlight
- Result sentence after the last step
- Defaults, limits, and irreversible actions stated when the release notes mention them
- Related article linked when one exists
- Closing line is short, warm, and varies across the file
- No em dashes, no horizontal rules, no marketing adjectives, no internal jargon
- Every fact traces to the release notes or a live article; unknowns are `[confirm: ...]` and collected under Open items
