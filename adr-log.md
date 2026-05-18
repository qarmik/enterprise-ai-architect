# adr-log.md — Architectural Decision Records
# Format: Context / Decision / Alternatives / Consequences / Status
# Every significant technical choice gets an ADR

## ADR-001 — 2026-04-30
**Context:** Need a development environment. Options: WSL2 on Windows, GitHub Codespaces.
**Decision:** GitHub Codespaces
**Alternatives:** WSL2 (rejected — local setup can fail unpredictably)
**Consequences:** Works from any machine. Zero local installation. Survives hardware changes.
**Status:** Closed

## ADR-002 — 2026-05-12
**Context:** First real artifact needs to produce output. 
Options: print to stdout only, write to file, write to database.
**Decision:** Write to timestamped file in a reports directory.
**Alternatives:** stdout only (not persistent, cannot be audited),
database (over-engineered for Phase 0).
**Consequences:** Reports are preserved with timestamps. 
Reproducible. Auditable. reports/ excluded from git 
(generated output, not source). 
**Status:** Closed
