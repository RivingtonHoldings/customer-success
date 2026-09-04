# Humanizer

Removes signs of AI-generated writing from text. Lives in this repo at `.claude/skills/humanizer/`; nothing to install.

Run it with `/humanizer` followed by the text or a file path. The article-draft, article-rewrite, and intercom-macros skills suggest it as a follow-up when a draft reads stilted. After humanizing help center copy, re-run the article quality checklist, because the humanizer may reintroduce "you can."

Based on Wikipedia's "Signs of AI writing" guide (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). The pattern list and examples are in `SKILL.md`, which is the source of truth. Pattern 25 (over-claimed certainty about human behavior) was added by the Perchwell marketing team and matches the "hedge predictions" rule in the root `CLAUDE.md`.
