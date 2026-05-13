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

## Session 5: No debugging done

## Session 6: 

1. CI failure from malformed requirements.txt
The first CI run failed because requirements.txt had an accidental terminal command pasted into it instead of containing only dependency lines. The broken line looked like pytest==9.0.3git commit -m ..., so pip treated the whole string as an invalid requirement and stopped installation.

Root cause: A git commit command was accidentally pasted into requirements.txt while editing files and using the terminal.

Fix applied: Cleaned requirements.txt so it contained only valid dependency entries such as:

text
pytest==9.0.3
2. CI workflow understanding
The CI workflow itself was structurally fine: checkout code, set up Python 3.12, install dependencies, and run pytest. The failure was not caused by the workflow design, but by bad project input data inside requirements.txt and earlier syntax issues in the test file.

3. GitHub Pages deployment failure
The GitHub Pages workflow failed during actions/deploy-pages@v5 because no artifact named github-pages existed in that workflow run. The deploy step searched for the artifact and found zero artifacts, so deployment could not continue.

Root cause: The workflow tried to deploy without first uploading the special Pages artifact required by actions/deploy-pages.

Evidence from logs:

Found 0 artifact(s)

No artifacts named "github-pages" were found for this workflow run

Fix needed: Add a build/upload step using actions/upload-pages-artifact@v4 and make the deploy job depend on that upload job.
---