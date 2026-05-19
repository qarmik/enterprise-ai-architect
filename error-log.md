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

## Session 7:

**Date** : 2026-05-15 & 2026-05-16
# Session 7 Error Log

**Error:** `FileNotFoundError: File not found: phase-0/sample_transactions.csv`  
**Tried:**  
- Ran `python3 phase-0/transaction_log_analyser.py phase-0/sample_transactions.csv`.  
- Ran `python3 phase-0/transaction_log_analyser.py phase-0/sample.transactions.csv`.  
- Renamed `sample.transactions.csv` to `sample_transactions.csv` with `mv`.  
**Fixed by:** `mv phase-0/sample.transactions.csv phase-0/sample_transactions.csv`  
**Why it happened:** The command used a filename that did not match the actual file path.

**Error:** `SyntaxError: invalid syntax` at `processing_times.sort():`  
**Tried:**  
- Ran the analyzer script several times after editing.  
- Kept correcting earlier typos and reran the file.  
**Fixed by:** Removing the extra colon from `processing_times.sort()`  
**Why it happened:** A stray `:` made a valid Python statement invalid.

**Error:** `AttributeError: module 'logging' has no attribute 'basicCongig'. Did you mean: 'basicConfig'?`  
**Tried:**  
- Ran the script again after fixing the sort syntax.  
- Reopened the file and corrected other typos.  
**Fixed by:** Changing `logging.basicCongig` to `logging.basicConfig`  
**Why it happened:** The function name was misspelled.

**Error:** `IndentationError: unindent does not match any outer indentation level`  
**Tried:**  
- Re-ran the script after editing the bottom of the file.  
- Checked the `if __name__ == "__main__":` block and surrounding code.  
**Fixed by:** Rewriting the file with consistent 4-space indentation  
**Why it happened:** Tabs/spaces or misaligned blocks broke Python’s indentation rules.

**Error:** Script ran with no visible output  
**Tried:**  
- Ran `python3 phase-0/transaction_log_analyser.py phase-0/sample.transactions.csv`.  
- Checked whether `main()` existed and whether the entry point was called.  
**Fixed by:** Adding a correct `if __name__ == "__main__": main()` block  
**Why it happened:** The program structure was not reaching the analyzer entry point.

**Error:** `NameError: name 'pytest' is not defined`  
**Tried:**  
- Ran `pytest phase-0/ -v`.  
- Added and removed `import pytest` in different places.  
- Committed and pushed the test file, then reran CI.  
**Fixed by:** Adding `import pytest` to `phase-0/test_transaction_log_analyser.py`  
**Why it happened:** The test used `pytest.raises()` without importing `pytest`.

**Error:** Git shell got stuck at `>` after a broken commit command  
**Tried:**  
- Typed a long `git commit -m` message with mismatched quotes.  
- Entered `exit`.  
- Pressed `Ctrl + C`.  
**Fixed by:** `Ctrl + C`, then rerunning the commit with one properly quoted message  
**Why it happened:** The shell was waiting for a closing quote in the unfinished command.

**Error:** `git: 'coomit' is not a git command`  
**Tried:**  
- Typed `git coomit -m ...` instead of `git commit -m ...`.  
**Fixed by:** Re-running the correct command: `git commit -m ...`  
**Why it happened:** The command name was misspelled.

**Error:** CI failed with `NameError: name 'pytest' is not defined`  
**Tried:**  
- Edited the workflow.  
- Changed Python version to `3.12.1`.  
- Switched test execution to `python -m pytest phase-0/ -v`.  
- Re-ran the GitHub Actions workflow.  
**Fixed by:** Importing `pytest` in the test file and using `python -m pytest` in CI  
**Why it happened:** The test file was missing the import, and CI needed a reliable test command.

**Error:** `bash: -: command not found` and `bash: run:: command not found`  
**Tried:**  
- Pasted YAML workflow lines directly into the terminal.  
- Tried to change `.github/workflows/ci.yml` from the shell prompt instead of the editor.  
**Fixed by:** Opening and editing `.github/workflows/ci.yml` in the editor  
**Why it happened:** YAML was entered into Bash instead of into the workflow file.

---
**Date:** 2026-05-18
**Error:** None in Session 8
**Tried:** Added `write_report()`, updated CLI with `--output`, added `phase-0/reports/` to `.gitignore`, ran the analyser, checked generated report, updated ADR-002
**Fixed by:** No fix required
**Why it happened:** Session completed without a debugging event

---
**Date:** 2026-05-19
**Error:** None in Session 9
**Tried:** Created `phase-0/latency_calculator.py`, created `phase-0/test_latency_calculator.py`, ran the program, prepared commit
**Fixed by:** No fix required
**Why it happened:** Session completed without a debugging event
