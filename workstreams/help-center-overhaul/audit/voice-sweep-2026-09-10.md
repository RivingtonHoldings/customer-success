# Voice sweep: exposure to scorecard check 5

A count of how many live articles fail the Fin-readiness check added on September 10, 2026, so the audit backlog can be ranked knowing what the new check costs. Run against the mirror in `docs/help-center/` at its September 4, 2026 sync. Swept by Claude for Tara, September 10, 2026.

This is a triage input, not an audit verdict. Nothing here carries a recommendation or a priority yet.

## What the check is

Accuracy and confidence check 5, added in revision 2 of the September 10, 2026 check set: "Verbs name what the member does rather than what the screen does back, and no 'you can', 'allows you to', or verb 'use' outside the accepted exceptions."

The important part for planning: **"you can" was already banned** by `docs/standards/content-standards.md`, under Voice and terminology and in the quality checklist, before September 10. It was never scored, because revision 1's Accuracy and confidence dimension had four checks and none of them looked at voice. Revision 2 does not create this exposure, it makes a long-standing rule scoreable for the first time.

## Totals

| Pattern | Baldwin (123 articles) | CRMLS (85 articles) |
|---|---|---|
| "you can" | 74 | 55 |
| "able to" | 20 | 7 |
| "allows you to" or "allow you to" | 4 | 14 |
| **Any of the three** | **79 (64%)** | **57 (67%)** |

**136 of 208 articles** fail check 5.

"Allows you to" is not the driver, despite reading like the old house style. Baldwin has it in four articles, and Dashboard Overview accounted for six of Baldwin's ten occurrences before its rewrite. The driver is "you can".

## How much of the backlog actually re-ranks

Less than the 64 percent headline suggests. Accuracy and confidence carries 10 points across 5 checks, so one failed check costs exactly **2.0 points**. Band boundaries sit at 50, 75, and 90, which means only an article currently scoring 90.0 to 91.9, 75.0 to 76.9, or 50.0 to 51.9 changes band. Everything else drops two points and stays in the band it was in.

How many articles sit in those windows is unknown, because only two articles in the repo have a scorecard. The re-ranking risk is real and bounded; it is not two thirds of the backlog.

## Depth of the problem, by article

Most flagged articles have a stray phrase, not a voice problem.

| Hits in one article | Articles |
|---|---|
| 1 | 70 |
| 2 | 33 |
| 3 to 4 | 14 |
| 5 or more | 11 |
| 12 or more | 1 |

### Articles with 5 or more hits

These are the ones where the voice, not a phrase, is the issue.

| Hits | Article |
|---|---|
| 18 | `baldwin/search-faq.md` |
| 9 | `baldwin/dashboard-overview.md` (rewritten September 10, 2026; the live article still carries them) |
| 7 | `crmls/what-s-new-in-perchwell-crmls.md` |
| 7 | `crmls/the-search-page-overview.md` |
| 7 | `crmls/customize-your-search-view.md` |
| 7 | `baldwin/search-page-overview.md` |
| 7 | `baldwin/quick-guide-getting-clients-started-in-perchwell.md` |
| 7 | `baldwin/customize-your-search-view.md` |
| 6 | `crmls/export-to-excel.md` |
| 6 | `crmls/creating-a-search-with-filters-in-perchwell.md` |
| 6 | `baldwin/listing-detail-page-overview.md` |
| 6 | `baldwin/contacts-page-overview.md` |
| 5 | `crmls/using-the-map-on-the-search-page.md` |
| 5 | `crmls/sharing-listings-with-clients.md` |
| 5 | `crmls/adding-a-hot-sheet-to-the-dashboard.md` |
| 5 | `baldwin/share-multiple-listings-in-perchwell.md` |
| 5 | `baldwin/listing-maintenance-faq.md` |
| 5 | `baldwin/common-perchwell-faqs.md` |

### Articles flagged only in the description field

Eight articles have clean bodies and the phrase only in their Intercom description. That is a different fix in a different place, a field edit rather than a rewrite, and it can be done without reopening the article.

- `baldwin/create-communication-templates.md`
- `baldwin/export-listings-in-perchwell.md`
- `baldwin/how-to-tag-individual-listings.md`
- `baldwin/new-terminology.md`
- `baldwin/set-up-saved-searches-for-hot-sheets.md`
- `crmls/export-listings-in-perchwell.md`
- `crmls/reporting-listings.md`
- `crmls/saving-listings-with-tags.md`

A further 13 articles are flagged in both the body and the description, so a body rewrite alone will not clear them.

## The FAQ problem

FAQ articles are where check 5 is hardest to satisfy, because "you can" is the natural answer to a question-form heading. Twelve of the sixteen FAQ-style articles are flagged, and the worst article in either help center is an FAQ.

| Hits | Question headings | Article |
|---|---|---|
| 18 | 24 | `baldwin/search-faq.md` |
| 5 | 17 | `baldwin/common-perchwell-faqs.md` |
| 5 | 12 | `baldwin/listing-maintenance-faq.md` |
| 4 | 5 | `baldwin/dashboard-faq.md` |
| 4 | 6 | `baldwin/login-access-troubleshooting-guide-and-faq.md` |
| 4 | 4 | `baldwin/reports-faq.md` |
| 3 | 11 | `baldwin/client-collaboration-faq.md` |
| 3 | 21 | `baldwin/most-common-questions-asked-to-mls-staff.md` |
| 3 | 4 | `baldwin/user-settings-faqs.md` |
| 1 | 3 | `baldwin/analytics-faq.md` |
| 1 | 32 | `baldwin/top-compliance-questions.md` |
| 1 | 0 | `baldwin/manage-people-faq.md` |
| 1 | 0 | `crmls/frequently-asked-questions.md` |
| 0 | 5 | `baldwin/listings-faq.md` |
| 0 | 3 | `baldwin/mobile-faq.md` |
| 0 | 3 | `baldwin/tags-faq.md` |

`baldwin/dashboard-faq.md` is the clean example of the problem. Under the heading "How many Hot Sheets can I add?" the answer reads "There is no limit. You can add as many as you'd like." Rewriting that to "Add as many as you'd like" reads oddly against the question above it, and the question heading is required by golden question 5 and by the standard's FAQ rules.

The standard already grants explicit exceptions to the verb-"use" ban for "When to use" headings and the "Use this article to" opening. **FAQ answers have no equivalent exception for "you can" and may need one.** That question is on the project status page, owned by Tara and Kelly.

Until it is settled, do not schedule FAQ rewrites on the strength of check 5 alone; three of the eleven worst-offender articles are FAQs, and an exception would remove them from the list entirely.

## Method, so this can be re-run

From the repo root:

```bash
grep -ric "allows\? you to\|you can\|able to" docs/help-center/baldwin/*.md docs/help-center/crmls/*.md | grep -v ':0$'
```

Counts are per matching line, so an article with two hits on one line reads as one. The frontmatter split was taken by counting matches inside the `---` block separately from the whole file. The sweep does not check the verb-nuance half of check 5 ("what the screen does back"), which is not greppable; those cases surface in the skill's verb pass during a rewrite.
