# decisions.md — Technical and Curriculum Decisions
# Rule: 30–60 min timebox per decision. Once logged, the decision is closed.

## D001 — 2026-04-30
**Decision:** Use GitHub Codespaces as primary environment
**Options:** WSL2 local install vs GitHub Codespaces
**Reasoning:** Zero installation friction. Works from any browser. Survives hardware failure.
**Status:** Closed

## D002 — 2026-04-30
**Decision:** Start date is April 30 2026
**Reasoning:** Personal anchor date. 42-month timeline targets early 2030.
**Status:** Closed
## D006&D007 - 2026-05-15 & 2026-05-16
**Decision:** build Artifact P0-A1 in phase-0/ as a real Python program that reads a CSV and prints transaction statistics
**Reasoning:** You wanted the first artifact to be a real working program, not a placeholder, so you used a CSV analyzer that actually computes meaningful banking-style statistics.
**Status:** Session 7 is now complete: the analyzer runs successfully, the sample CSV exists with the correct name, the tests pass locally, and the pytest import issue has been fixed and pushed.

## D008 — 2026-05-18
**Decision:** Extend Artifact P0-A1 so the analyser writes a timestamped text report to `phase-0/reports/`
**Reasoning:** Session 8 required the first real artifact to produce a persistent output, not just print to stdout. A timestamped text report is simple, auditable, and appropriate for Phase 0.
**Status:** Closed
## D009 — 2026-05-19
**Decision:** Build Artifact P0-A2 as a latency statistics calculator with simulated latency percentiles and a simple GPU cost model
**Reasoning:** Session 9 should extend Phase 0 with a second real Python artifact that demonstrates both statistical analysis and basic infrastructure cost planning.
**Status:** Closed
