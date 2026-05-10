# error-log.md — Debugging History
# Rule: write the error BEFORE searching. Name it precisely.
# Rule: write the solution AFTER fixing. Future-you will be grateful.

## Template
---
**Date:** YYYY-MM-DD
**Error:** [exact error message — copy from terminal]
**Tried:** [list attempts in order]
**Fixed by:** [exact command or change that worked]
**Why it happened:** [one sentence]
---

## Session 3
---
**Date:** 2026-05-10
**Error:** [NameError: name 'months' is not defined]
**Tried:** [corrected the error in 'months']
**Fixed by:** [cause was a typo 'motnhs' - fixed it]
**Why it happened:** [cause was a typo 'motnhs']
---

## Session 4
---
**Tried:** 
1. Ran `pytest phase-0/test-hello.py` → collected 0 items / 1 error
2. Identified no quotes around filename on line number 23
**Fixed by:** Added quotes around filename: `[sys.executable, "phase-0/hello.py"]`
**Why it happened:** `phase-0/hello.py` without quotes was treated as Python code (variable subtraction) instead of a string filename for the OS.
---