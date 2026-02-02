# Kiko's AI Learning Diary (LEARNED.md)

## Current Iteration: V3 (Elite Autonomous Engine)

### [2026-02-01] Lesson 1: Research Depth
- **Problem:** Previous versions often just gave links, which Kiko found unhelpful.
- **Root Cause:** Default `web-search` logic prioritizes quick summaries over deep fetching.
- **Correction:** Forced `ddgr` + `curl` combo. I now read the full text of the top 2-3 links before answering. Result: Higher information density, no link-dumping.

### [2026-02-01] Lesson 2: Configuration Stability
- **Problem:** Messed up `openclaw.json` trying to add group whitelists to the wrong section.
- **Root Cause:** Configuration schemas are strict; adding unknown keys at the root level causes gateway failure.
- **Correction:** Use `doctor --fix` to clean up and only use verified sections.

### [2026-02-01] Lesson 3: Reasoning Model Balance
- **Problem:** `o3-mini` is slower for simple greetings.
- **Root Cause:** Reasoning models spend time "thinking" even for "Hi".
- **Correction:** Set `gpt-4o` as primary for conversation and `o3-mini` as the "Heavy Lifting" fallback for complex tasks.
