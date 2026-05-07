# adr-log.md — Architectural Decision Records
# Format: Context / Decision / Alternatives / Consequences / Status
# Every significant technical choice gets an ADR

## ADR-001 — 2026-04-30
**Context:** Need a development environment. Options: WSL2 on Windows, GitHub Codespaces.
**Decision:** GitHub Codespaces
**Alternatives:** WSL2 (rejected — local setup can fail unpredictably)
**Consequences:** Works from any machine. Zero local installation. Survives hardware changes.
**Status:** Closed