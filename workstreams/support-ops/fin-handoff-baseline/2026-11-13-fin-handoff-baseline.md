# Fin handoff completeness: baseline, September 1 to November 12, 2026

This document records how often Fin (Perchie) hands a conversation to a live agent with everything the agent needs. It is the "before" number for the work to improve Fin's handoffs.

- **Prepared by:** Kevin Liang, Customer Success, with Claude, on November 13, 2026.
- **Source:** Intercom conversations and contact profiles, read only. Nothing was written to Intercom.
- **Raw data:** `confidential/` in this folder (git-ignored). It holds the scoring rules (`SCORING_SPEC.md`), the conversation list, and one scored row per conversation.

## Result

| Measure | Count |
|---|---|
| Fin handoffs scored | 170 |
| Complete handoffs | 96 |
| **Baseline complete rate** | **56.5%** |
| Fail MLS Name | 0 |
| Fail device information | 0 |
| Fail one-line summary | 74 |

Every incomplete handoff failed on the same criterion: the one-line summary. No scored handoff failed MLS Name or device information.

**By MLS**

| MLS | Handoffs | Complete | Rate |
|---|---|---|---|
| Baldwin | 111 | 83 | 74.8% |
| RLS | 59 | 13 | 22.0% |

No CRMLS conversations reached the scored set.

**By month the conversation started**

| Month | Handoffs | Complete | Rate |
|---|---|---|---|
| September | 89 | 47 | 52.8% |
| October | 64 | 38 | 59.4% |
| November 1 to 12 | 17 | 11 | 64.7% |

## How confident this number is

This is a partial count, not the full population. The run was stopped partway, by choice, to save cost.

- **Coverage.** The window has 323 candidate conversations. 205 of them were read and scored. After exclusions, 170 are Fin handoffs. The other 118 candidates were never read.
- **Not a random sample.** Each batch was read newest first and stopped at a different point, so the 170 lean toward the earlier part of each batch. They still span the whole window, from September 1 to November 12.
- **Sampling margin.** If the 170 behave like the full set, the true rate is likely within about 7.5 points of 56.5%, so between 49% and 64%. Treat that as a rough guide, since the sample is not random.
- **Judgment margin.** The summary test takes judgment. 15 passes were marked borderline, which means the summary was thin. 6 fails were marked borderline. Counting all borderline calls as fails gives 47.6%. Counting them all as passes gives 60.0%.
- **Best reading:** the complete-handoff rate sits around 50 to 60 percent. Almost all of the gap comes from the summary.

## Method

### Which conversations count

1. **Window.** Conversations created from September 1, 2026 through November 12, 2026, in UTC. November 12 is the last day included.
2. **Candidates.** Conversations Fin took part in where Intercom recorded that Fin did not resolve them. That gives 304 marked "Escalated" and 19 marked "Negative feedback," where the member said Fin's answer did not help: 323 in all. Conversations Fin resolved, or where it was assumed resolved, are out.
3. **Fin handoff vs. teammate takeover.** Each conversation's history shows who moved it, and when.
   - **Fin handoff:** the first time Perchie moved the conversation off itself, to a team inbox or to Unassigned, after Fin had replied at least once, and before any teammate had replied or assigned it.
   - **Teammate takeover:** a teammate replied to the member, or assigned the conversation, before any such Perchie move. These are left out.
   - **No handoff:** Fin closed the conversation, or the member left. These are left out.
4. **Staff tests left out.** Conversations started by a Perchwell staff account, meaning an `@perchwell.com` email address, are left out. Several were MLS staff test chats with many unrelated questions in one thread.

**From the 205 read:** 170 Fin handoffs, 14 teammate takeovers, 2 conversations with no handoff, and 19 staff tests. Of the staff tests, 17 were otherwise Fin handoffs. Of the 19 "Negative feedback" conversations, 11 were read, and none of them was a Fin handoff: 7 were teammate takeovers, 2 had no handoff, and 2 were staff tests.

### Criterion 1: MLS Name

**Test:** the conversation's MLS attribute was set before the moment of handoff.

The conversation history records the exact time the MLS attribute was set. This criterion is therefore measured at handoff time, not today. As a cross-check, the MLS Name field on the member's contact profile was filled in for every scored handoff. That field shows only its current value, so the cross-check is an approximation.

### Criterion 2: Device information

**Test:** at least one of these is true.
- Web: Browser and Os are both filled in.
- iPhone or iPad: Ios device or Ios os version is filled in.
- Android: Android device or Android os version is filled in.

**This is an approximation.** Intercom shows only today's value for these contact fields, with no history, so a field filled in after the handoff looks the same as one filled in before it. Three things support the result anyway:
- Every scored member had Browser and Os filled in.
- 114 also had iPhone details, and 21 had Android details.
- The Current Page URL, which is recorded when the conversation starts and so is accurate at handoff time, was present on 165 of the 170.

The connector does not return the Ios sessions or Android sessions counts, so they were not used. With this threshold, the device check does not separate complete handoffs from incomplete ones. A stricter rule, such as requiring the device the member was actually using in this conversation, might.

### Criterion 3: One-line summary

**Test:** before the handoff, a Fin message contains a sentence that restates this member's issue clearly enough for a teammate to act on it without scrolling up. The sentence must name both of these:
1. **The thing involved:** a feature, screen, listing, report, field, integration, or account.
2. **What is wrong, or what the member wants done.**

The wording does not have to start with "I understand," but it usually does. Answers that only explain steps do not count unless they also restate the problem.

- **Model pass:** "I understand you're concerned that the branded video is not appearing on Zillow."
- **Fails:** a line that names no issue ("I understand you'd like to speak to a live agent"), a handoff notice alone, a request for the MLS ID, or a restatement too vague to act on ("trouble with your report").

Messages were read and judged one conversation at a time by a Claude helper, then spot-checked.

## Examples

All examples are anonymized. Member names are removed, and the issue is paraphrased.

### Complete handoffs

- **Sharing listings.** The member wanted one link for 28 selected listings. Fin wrote: "I understand you're trying to send multiple listings as an MLS Link, but the current process only sends the listing you're viewing." MLS set, device known.
- **Client collaboration.** The member's client could not see listings sent to them. Fin wrote: "I understand the issue with your contact not seeing the properties you sent." This passes, though it is close to borderline.
- **Listing entry.** The member got an error editing a cancelled listing on an iPad. Fin wrote: "I'm sorry you're encountering an error while editing a cancelled listing."

### Fail: one-line summary

- **No issue named.** A broker asked whether a private listing's price history stays visible after it goes public. Fin's last line before the handoff was: "I understand you'd like confirmation from a live agent. Please share the MLS ID associated with the listing..." The agent has to read the whole thread.
- **Handoff notice only.** In 21 of the 74 summary failures, Fin's only pre-handoff message was the transfer notice, "We will be connecting you to a live agent in a few moments." This happened mostly in RLS, often when the member asked for a person in their first or second message.
- **Too vague.** A member could not find a comparison report they had built weeks earlier. Fin wrote: "I'm sorry to hear about the trouble you've had with your report." It names the report but not the problem.

### Fail: MLS Name

No scored handoff failed this criterion. In every one, the MLS was set on the conversation before Fin handed off.

### Fail: device information

No scored handoff failed this criterion, under the threshold above.

## What this suggests

These are hypotheses for the improvement work, not findings from this count.

- Members may get a better handoff if Fin always writes a one-sentence restatement of the issue as part of the transfer message. The current transfer notice could carry it.
- The RLS workflow (NYC Perchie) may need this change first. Its rate is about a third of Baldwin's.
- To measure the same way after the change, rerun the scoring rules in `confidential/SCORING_SPEC.md` on a later window. Reading every candidate would give an exact count instead of a partial one.
