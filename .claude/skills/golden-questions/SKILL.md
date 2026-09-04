---
name: golden-questions
description: Mine real member questions from Baldwin Fin conversations in Intercom and cluster them into a golden question set for testing Fin and steering the help center audit. Use whenever a teammate types /golden-questions, asks "what are members actually asking," "build the test questions for Fin," "pull questions from the cutover conversations," or wants the golden question set refreshed. Supports --sample N, --since, and --until. Read-only toward Intercom; raw excerpts stay in confidential/.
---

# Golden questions

A golden question is one real thing members ask, in their own words, paired with the right answer and the article that should carry it. The set is how the team tests Fin (does it answer these correctly?) and prioritizes the audit (which articles do the most-asked questions land on?). This skill builds and refreshes it from Baldwin conversations where Fin took part.

Privacy first: search results and conversation threads contain member names, emails, and sometimes phone numbers and addresses. Everything raw goes under `workstreams/help-center-overhaul/confidential/golden-questions/<run>/`, which git ignores. The only committed output is `workstreams/help-center-overhaul/golden-questions/golden-question-set.md`, and it is scrubbed and checked before it is saved.

## Flags

`/golden-questions [--sample N] [--since YYYY-MM-DD] [--until YYYY-MM-DD]`

- `--sample N`: how many conversations to read in full (default 25). The pool can be hundreds; reading every thread is slow and unnecessary for clustering.
- `--since`, `--until`: the window, inclusive, in UTC. Default: the two weeks after the Baldwin cutover, 2026-08-03 to 2026-08-17.

## How Baldwin conversations are identified

Every conversation that starts in the Baldwin chat workflow carries the custom attribute `MLS: Baldwin` and `ai_agent.source_title` = `(Members) Baldwin | Support Bot Workflow NEW`. The connector can filter on the workflow title server-side (`ai_agent_source_title`) but not on the custom attribute, so the pool step checks both on the client from the returned records.

## Steps

`SCRIPT` is `.claude/skills/golden-questions/scripts/golden_questions.py`. `RUN` is a run name like `2026-08-03-to-2026-08-17`. Work from the repo root.

1. **Pull the search results.** Call `mcp__eff8e27b-83eb-43ee-befe-90e26bf3b57b__search_conversations` with `ai_agent_source_title: "(Members) Baldwin | Support Bot Workflow NEW"`, `created_at: {operator: ">", value: <since as unix seconds, midnight UTC>}`, `per_page: 150`. Results sort by last update, not by creation, so keep paging with `starting_after` until a page contains no conversation created after `until` and the previous page did not either, or until `pages.next` is gone. Large results are saved to files automatically; note each path. Small pages arrive inline; save them to a file under the scratchpad yourself.
2. **Build the pool.**
   `python3 SCRIPT pool --run RUN --since <since> --until <until> --search-results <files>`
   Prints the pool size and its spread by day, Intercom resolution state, and part of the platform. If the pool is empty or tiny, say so and stop; do not pad it with other MLSs.
3. **Sample.**
   `python3 SCRIPT sample --run RUN --n <N>`
   Picks N conversations round-robin across days so the sample spans the window. Prints the IDs.
4. **Read each sampled thread.** For each ID call `mcp__eff8e27b-83eb-43ee-befe-90e26bf3b57b__get_conversation`. Save the full JSON result to a scratch file (large results are saved for you; for inline results write the JSON to a file verbatim), then
   `python3 SCRIPT ingest --run RUN <file>`
   Ingest keeps every part that has a body plus assignment, close, tag, and Fin guidance events, with timestamps and author type. The stored copy includes Intercom's `ai_agent.resolution_state` and the parts, so the weekly Fin report can apply Perchwell's own resolution definition later.
5. **Extract.**
   `python3 SCRIPT extract --run RUN`
   For each conversation this records the member's question(s) in their own words (quick-reply button clicks and the "Let's get started" opener are excluded), the topic from Intercom's AI title and Part of the Platform attributes, whether Fin answered, whether a teammate stepped in, the articles Fin cited (matched to the mirror by content ID), Intercom's resolution state, and the Perchwell resolution: Fin answered, no teammate message afterward, no member follow-up within 48 hours. It writes `extracted.json` (raw) and `extract-scrubbed.md` (identifiers replaced) in the run folder. Read only the scrubbed file for the next step.
6. **Cluster and write the set.** Read `extract-scrubbed.md`. Group questions that ask the same thing into one golden question each. For every cluster record:
   - canonical phrasing (one clear sentence, the way a member would ask it),
   - three real paraphrases, quoted from the scrubbed extract, lightly trimmed for typos only,
   - volume (how many sampled conversations, and the share of the sample),
   - the correct answer in two or three sentences, drawn from the mirrored article, not invented,
   - the target Baldwin article (title and mirror path from `docs/help-center/baldwin/`), or "gap" if none fits,
   - the CRMLS equivalent from `docs/help-center/crmls/` if one exists, else "none",
   - how Fin handled it: answered and resolved, answered but the member pushed back, escalated, or no answer, with the article it cited if any.
   Write `workstreams/help-center-overhaul/golden-question-set.md` in the format below. Order clusters by volume. Every member is "the member"; every Perchwell person is "a teammate". No names, emails, phone numbers, addresses, or MLS IDs anywhere in the committed file.
7. **Check before saving.**
   `python3 SCRIPT check --run RUN workstreams/help-center-overhaul/golden-questions/golden-question-set.md`
   Fix anything it flags and run it again until it reports clean. Then grep the file yourself for `@` and for any capitalized name-like pair you recognize from the threads.
8. **Report** the pool size, sample size, number of clusters, the three highest-volume questions, the Perchwell-resolved share of the sample next to Intercom's own count, and any filter problems worth noting in `docs/decisions.md` for the next session.

## Committed file format

```markdown
# Golden questions: Baldwin

Run: <RUN> | Window: <since> to <until> | Pool: <n> conversations | Sampled: <N> | Built: <date>

Fin resolution in the sample, Perchwell definition: <x> of <N> resolved. Intercom's own states: <counts>. The two are reported side by side, never blended.

## 1. <Canonical question>

- Volume: <k> of <N> sampled (<pct>)
- Paraphrases:
  - "<paraphrase 1>"
  - "<paraphrase 2>"
  - "<paraphrase 3>"
- Correct answer: <two or three sentences>
- Target Baldwin article: [<title>](../../../docs/help-center/baldwin/<file>) or gap: <what is missing>
- CRMLS equivalent: [<title>](../../../docs/help-center/crmls/<file>) or none
- How Fin handled it: <summary>, cited <article or none>

## 2. ...
```

## Rules

- Read-only toward Intercom. Never add notes, never write to conversations.
- Nothing from the run folder is ever committed. If a teammate pastes raw text into chat, keep it in the run folder.
- Do not invent answers. If the mirror has no article that answers the question, record a gap; a gap is a finding.
- Teammate names never appear in committed output, including in "how Fin handled it."
