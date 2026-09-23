# Dashboard collection: review packet

Everything a reviewer needs to move the five Dashboard drafts from `Draft` to `Ready to Transfer`, in one pass instead of five Notion pages. Written September 23, 2026.

Reviewer on all five: Kelly Miragliotta, Baldwin content audit owner, [kelly.miragliotta@perchwell.com](mailto:kelly.miragliotta@perchwell.com). Project lead: Tara, [tara.bars@perchwell.com](mailto:tara.bars@perchwell.com). Fin answer quality: Rafe Petkovic, [rafe.petkovic@perchwell.com](mailto:rafe.petkovic@perchwell.com).

## The one thing blocking all of it

Every one of these is rewritten, scored, and sitting at `Article Status: Draft` with `Article Review Status: Not Started`. `/port-to-intercom` refuses to push anything that is not `Ready to Transfer`, so nothing reaches members until a person reviews each page and moves the row.

Two of the five need a decision from Tara before review can finish. Three need only screenshots dropped in.

The Dashboard collection currently shows members seven articles, two of which are the rewritten versions. The other five are pre-migration text.

## Status at a glance

| Article | Score, before to after | Blocked on | Notion comments open |
|---|---|---|---|
| [Find Listings in the Listings Widget](https://app.notion.com/p/3dd8b9e01438813ea9f6cdadffa18871) | 41.2 to 100.0 | 2 screenshots | 2 |
| [Customize Your Dashboard](https://app.notion.com/p/3db8b9e01438819b95c4f80b6b719fae) | 61.8 to 100.0 | **CRMLS duplicate article**, 1 screenshot, video call | 0 |
| [Add a Hot Sheet to the Dashboard](https://app.notion.com/p/3dc8b9e01438815891e6ccd033eccf97) | 60.0 to 96.4 | video call | 1 |
| [Open Your MLS Integrations from the Dashboard](https://app.notion.com/p/3e38b9e0143881619bdbca3f04117a1e) | 39.0 to 100.0 | 3 screenshots | 1 |
| [Dashboard FAQ](https://app.notion.com/p/3e48b9e014388136ba05ee2adf6955ed) | 66.3 to 95.7 | 1 screenshot | 0 |

All five pass the 14 golden questions and the plain language gate. Scores are against the September 10, 2026 revision 2 check set.

Two scores carry an asterisk, both for the same reason. Find Listings and Dashboard FAQ are scored with Retrieval check 1 failing on their title patterns, which is the open question in `docs/project-status.md` about whether `<Page> Overview` and `<Area> FAQ` satisfy a check that wants a task-led title. If the team rules the patterns pass, Find Listings is unchanged at 100.0 and Dashboard FAQ rises to 100.0. Neither changes band.

## One decision Tara owes, and one item now closed

### 1. Customize Your Dashboard is marked for two MLSs and written for one

`MLS/AOR` reads Baldwin and CRLMS All. The body is Baldwin's, and the mobile constraint in Things to Know traces to Baldwin sources only.

**The widget list is no longer a reason to worry.** Tara confirmed on September 23, 2026 that CRMLS no longer has the Days on Market widget, so both MLSs run the same five: Hot Sheets, Contacts, Saved Searches, Tags, and Listings. The draft's list is correct for both.

What still needs deciding is that CRMLS already has its own article on this subject, `Customizing your Dashboard`, ID 10159813. Publishing this one to both help centers means deciding what happens to that row.

### 2. SentriLock: no action, it is coming back

Open Your MLS Integrations carries `[confirm: SentriLock does not currently appear in the Baldwin Integrations panel and the team is looking into why]`. Tara confirmed on September 23, 2026 that SentriLock returns within 24 to 48 hours, so the absence is a temporary outage rather than a documentation error.

The article stays as written, SentriLock included. The live Dashboard Overview, which names ShowingTime, SentriLock, and RPR as commonly connected integrations, needs no correction either. The marker can come off once the panel is back; leave it until then, since it is the reminder to check.

## What changed in each article

### Find Listings in the Listings Widget

Retitled from "Listings Widget Overview". Scored lowest of the set before the rewrite and is the closest to ready now.

The live article documents a Tag quick action that no longer exists in the product, and its filter row is out of date: it lists a Recently Added filter the product dropped and omits Active Under Contract, which it has. A screenshot settled both. The rewrite covers the four Scope by options, the search field, the eight listing type filters, and the pencil and ShowingTime quick actions.

**For review:** the live article is wrong on the Tag action and Fin answers from it today. Correcting the published version is outside this migration and should be logged separately.

### Customize Your Dashboard

The live version bolds every UI element, capitalizes Manage Widgets wrongly, and describes four checkbox widgets. The rewrite has Hot Sheets as an Add hot sheet action rather than a checkbox, names the green Widget added and Widget removed confirmations, and states that the Listings widget is absent from Manage widgets because it cannot be added or removed.

**For review:** the green confirmation's exact wording is from Tara's description rather than a screenshot, so it is worth a glance at the screen. Two older screenshots on the old Notion page were never transferred and may be superseded.

### Add a Hot Sheet to the Dashboard

The live version says "Monitor activity for up to 2+ years"; the rewrite says up to 998 days per timeframe, in both Steps blocks. It renames the two types to quick hot sheet and saved search hot sheet, matching the widget's own labels, and corrects the Edit hot sheet modal to five Days boxes where the draft had described one field.

**Changed September 22, 2026, after its score.** A Things to Know bullet restating the five-timeframe cap was cut, because Dashboard FAQ answers that question and two articles were answering it; and one sentence was added naming brokerage and office filtering, which no version of this article had. Neither change is reflected in the 96.4 above. Neither moves it.

**For review:** the one open Notion comment is on "or custom market segment:" in the opening paragraph.

### Open Your MLS Integrations from the Dashboard

Retitled from "Integration Tools on the Dashboard". The largest factual correction in the set: a screenshot showed SentriLock absent from the Baldwin panel and CRS Login present, and both the old Notion page and the live article had it the other way round. The two documents agreed with each other and were both wrong.

**For review:** the open Notion comment is on the "Where to find integrations on a listing" heading. CRMLS has a twin article, 13921493, with the old title, so the pair diverges by name until CRMLS is migrated.

### Dashboard FAQ

Created September 22, 2026. Grew from five questions to six: a Market Monitor question was added, because the legacy term appeared only in the article's description where Fin cannot retrieve it. The live version answers the brokerage question with the wrong filter, has no opening paragraph, and describes a four-step procedure in prose.

**For review:** this one has been through a full wording pass with Tara already.

## Cross-cutting, and worth fixing once rather than five times

**Default help center links.** Every article in the set links to at least one article at `support.perchwell.com/en/...` rather than `/baldwin/en/...`, because that is how the mirror records them. Seven of nine in Customize Your Dashboard, seven of eight in Add a Hot Sheet. The linking standard prefers the MLS path, and `/port-to-intercom` flags them at transfer, but somebody should confirm they resolve for Baldwin members.

**Two Arcade recordings, twice.** Customize Your Dashboard and Add a Hot Sheet each have a live embed and a different Notion embed, and the drafts carry the Notion ones per the migration rule. Nobody has confirmed which recording ships. Add a Hot Sheet's row reads `Video: Update Required`, which suggests both may be stale.

**Screenshots exist but are not in Notion.** Tara has captures for the Manage widgets panel, the Listings widget, the filter row, and the Hot Sheet widget. They cannot be pasted from a chat; the files have to be dropped into the Notion pages. The Manage widgets capture fits both Customize Your Dashboard and the live Dashboard Overview.

**Alt text is sitting in Notion captions.** Notion has no alt text field, so each placeholder carries its alt text prefixed `Alt text:` in the caption. `/port-to-intercom` moves it into Intercom's alt attribute at transfer. A draft with alt text in the caption looks finished and is not, which is why this is written down.

**CRMLS questions on three of five.** Customize Your Dashboard, Add a Hot Sheet, and Find Listings all carry `CRMLS?: 100% Applicable` on their old rows while CRMLS has its own separate articles on two of the three subjects. Per Tara on September 14, no CRMLS articles are being edited yet.

## After a row moves to Ready to Transfer

1. `/port-to-intercom` converts the body, shows a before-and-after diff, takes one confirmation per article, writes the changelog, sets the row to `Live in Intercom`, and re-syncs the mirror
2. Fin labels per `docs/standards/fin-labeling.md`, by a person. The connector cannot write tags
3. MLS audience, by a person
4. Publishing stays a human action in Intercom. A port to an already-live article keeps its published state
