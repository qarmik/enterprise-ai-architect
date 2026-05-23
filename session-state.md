# session-state.md — End-of-Session Context
# Write 3 lines at the end of every session from Phase 1 Output 2 onward

## Template
---
**Date:** YYYY-MM-DD
**Working on:** [artifact or task]
**Next step:** [one specific next action]
**Confused by:** [sate all points of friction]
---

#### Phase 0 Session 1 — 2026-05-07
---
**Date:** 2026-05-07
**Working on:** Phase 0 — creating repository and system files
**Next step:** Complete Phase 0 folder structure and commit all files - Done
**Confused by:** # Phase 0 — Confusion & Resolution Log - stating all points of friction :
## 1. `git config user.name` — Username vs. Full Name
**Confusion:** I wasn't sure whether to put my GitHub username (`qarmik`) or my real name (`Rohit Kumar`).
**Resolution:** It should be my real full name. I also accidentally set `user.name` to my email address — I had to re-run the command correctly.

---

## 2. Changes Not Reflecting on GitHub
**Confusion:** I wasn't sure why edits I made in VS Code weren't showing up on the GitHub repo page.
**Resolution:** Saving in VS Code is not enough. I must always run all three commands — `git add .` → `git commit -m "..."` → `git push origin main` — to send changes to GitHub.

---

## 3. GitHub Pages 404 Error
**Confusion:** I wasn't sure why my live URLs (`qarmik.github.io/enterprise-ai-architect/...`) were giving a 404 error.
**Resolution:** Two issues — GitHub Pages hadn't been enabled yet (Settings → Pages), and the HTML files hadn't been pushed to the repo yet.

---

## 4. File Name Mismatch
**Confusion:** I wasn't sure why the live URL wasn't working even after uploading the file. The uploaded file was named `enterpriseAI_systems_architect_curriculum.html` but the live URL expected `curriculum.html`.
**Resolution:** The filename in the repo must exactly match the URL path. I renamed the file to `curriculum.html`.

---

## 5. `rejected — fetch first` Push Error
**Confusion:** I wasn't sure why I got the error *"failed to push some refs"* when trying to push.
**Resolution:** I had uploaded files directly via GitHub's website, creating a commit my Codespace didn't have locally. Fix was `git pull origin main --rebase` followed by `git push origin main`.

---

## 6. Live URLs Not Clickable from Repo Page
**Confusion:** I wasn't sure why the live URLs worked when pasted in a browser but didn't open when clicked on the GitHub repo page.
**Resolution:** Completely normal — the repo page shows raw code, not a live website. I must copy/paste or bookmark the `github.io` URLs directly.

---

## 7. "Opulent Xylophone" Name on Codespaces
**Confusion:** I wasn't sure why my Codespace showed a random name instead of something related to my project.
**Resolution:** GitHub auto-generates a random two-word nickname for every Codespace. It has no meaning — my repo name (`enterprise-ai-architect`) is what matters.

---

## 8. Codespaces Free Quota
**Confusion:** I wasn't sure if leaving Codespaces open would waste my free monthly hours.
**Resolution:** Yes — compute quota is consumed while the Codespace is actively running. I should always stop it when not coding via the three-dot menu → Stop codespace.

---

## 9. `touch` vs `code` Commands
**Confusion:** I wasn't sure when to use `touch filename` vs `code filename`.
**Resolution:** `touch` creates a new empty file. `code` opens a file for editing. For existing files, just use `code filename.md`. For new files, use `touch filename.md && code filename.md`
---

## Session 2 — 2026-05-08

**Date:** 2026-05-08
**Working on:** Phase 0 — updated python and git version numbers. 
06e7b39 (HEAD -> main, origin/main, origin/HEAD) phase0 - complete system files with real version numbers
89a3364 Changed the template of session-sate.md and the date of first commit
4bcf728 Clarify purpose of session-state.md in README
**Next step:** Complete Phase 0 folder structure and commit all files - Done
**Confused by:** # Phase 0 — Confusion & Resolution Log - stating all points of friction : None on 2026-05-08

## Session 3- 2026-05-10
---
**Date:** 2026-05-10
**Working on:** [phase-0/hello.py]
**Next step:** [updated hello.py to reflect 42 months long curriculum]
**Confused by:** [None encountered on Day 4/Session 3- 2026-05-10]

## Session 4- 2026-05-10
---
**Date:** 2026-05-10
**Working on:** [phase-0/test-hello.py]
**Next step:** " Session 5 done definition --Done = versions.md has pytest 9.0.3 added, a requirements.txt file exists in the root with pytest listed, and both are committed and pushed."
**Confused by:** 1. Meaning of #!/usr/bin/env python
Confusion: I wasn't sure what the line at the very beginning of a Python script means.
Resolution: It is called a shebang — it tells the operating system which interpreter to use to run the file. /usr/bin/env searches for Python wherever it is installed on the system, making the script portable. The correct form is #!/usr/bin/env python3 — with no slash before python, otherwise it causes an error.

2. Meaning of Triple Quotes """
Confusion: I wasn't sure why a program starts with three apostrophes/quotes """.
Resolution: Triple quotes in Python serve two purposes:

As a docstring — when placed at the start of a file, function, or class, they act as a built-in description explaining what the code does

As a multi-line string — they allow text to span multiple lines, unlike regular single quotes which only hold one line

Triple quotes are not comments (comments use #) — they are technically strings that Python treats as documentation when not assigned to a variable.

I thought Python was "doing the work itself," but discovered Python is just talking to the OS through pre-built tools.

Key friction busted: 

| Fiction You Had                       | Reality                             |
| ------------------------------------- | ----------------------------------- |
| Python "runs" other programs          | Python asks OS via subprocess       |
| sys.executable is optional            | Required for correct Python version |
| Code "does work itself"               | Code = instructions to OS butler    |

## Session 5:
Date: 2026-05-10
Working on: Dependency Management: update versions.md, add requirements.txt --        Reproducibility is the primary concern while building artifacts. Dependency management complete
Next Step: Session 6: Day 4 - 2026-05-11
Confused by: --break-system-packages safety (✅ resolved: use venv)

Virtual environment activation frequency (✅ resolved: create once, activate per session)

.gitignore for existing files (✅ resolved: just append venv/ line)

Status: ✅ Production-ready environment complete!

Today's Wins
text
✅ requirements.txt → pytest==9.0.3 installed
✅ venv created + activated + gitignored  
✅ pip upgraded to 26.1.1
✅ Reproducible setup locked in

## Session 6 - Date: 2026-05-11 & 2026-05-13
Working on: Dependency and deployment debugging for the enterprise-ai-architect repository, including CI workflow fixes, requirements.txt cleanup, and GitHub Pages workflow troubleshooting.
Next step: Update the GitHub Pages workflow so it uploads the required github-pages artifact before the deploy job runs.
Confused by:

Why the first CI run failed even though the workflow syntax looked correct.

Why requirements.txt caused a pip error from a line that was not a package.

Why GitHub Pages deployment reached the deploy step but still failed.

Whether warning messages in workflow logs were actual failure causes or just noise.

Corrective Actions
Keep requirements.txt limited to package lines only.

Verify file contents before committing with a quick terminal check.

Use a two-stage Pages workflow: build/upload first, deploy second.

Read workflow logs from the first real error upward instead of getting distracted by warnings.

Session Outcome
CI dependency error identified and understood.

requirements.txt corruption bug identified and fixed.

GitHub Pages deployment root cause identified.

Next clear action established: repair the Pages workflow artifact upload path.

## Session 7: Day 6 & Day 7
**Date** : 2026-05-15 & 2026-05-16
**Working On**: build Artifact P0-A1 in phase-0/ as a real Python program that reads a CSV and prints transaction statistics.
**Next Step** : create sample_transactions.csv and type in data manually. after that, create a transaction_log_analyser.py and write Tests for transaction_log_analyser.py by creating a test_transaction_log_analyser.py
**Confused by** : # Session 7 Confusion Summary

## File name confusion
- The CSV file name changed between `sample.transactions.csv` and `sample_transactions.csv`.
- This created repeated `FileNotFoundError` problems even though the file contents were correct.
- The confusion was about using the exact same filename in both the filesystem and the command.

## Python script confusion
- The analyzer script had several typos, including `basicCongig`, `init(...)`, wrong field names, and mismatched variable names.
- Some functions and variables were named inconsistently, which made the script fail in different ways.
- This made it hard to tell whether the main issue was syntax, logic, or just spelling mistakes.

## Indentation confusion
- The script produced `IndentationError` around the `if __name__ == "__main__":` block.
- Mixed indentation and incorrectly nested functions made the file harder to debug.
- This created the impression that the whole script was broken, even when only the structure was wrong.

## Execution confusion
- At one point the script ran but printed nothing.
- That made it unclear whether the file was executing at all.
- The root issue was around the entry-point structure and whether `main()` was being called correctly.

## Test file confusion
- The failing test used `pytest.raises(...)` but `pytest` was not imported in the needed scope.
- Local progress and CI results did not seem aligned at first, which made the error feel inconsistent.
- The actual fix was small, but it took time to isolate because the symptom appeared only in the test run.

## CI workflow confusion
- The CI workflow failed after the code had already started working locally.
- It was unclear whether the failure came from the workflow YAML, Python version, installed packages, or the test file itself.
- The confusion reduced once the missing `pytest` import was identified as the direct cause.

## Terminal and Git confusion
- A broken `git commit -m` command left the shell at the `>` prompt waiting for more input.
- There was also a typo like `git coomit`, which interrupted the flow.
- These issues were not related to Python, but they added friction and made the session feel more chaotic.

## Overall pattern
- Most confusion in Session 7 came from small mismatches: filename mismatch, import mismatch, indentation mismatch, and command syntax mismatch.
- The work itself was valid, but tiny inconsistencies created repeated blockers.
- Once each mismatch was corrected, the analyzer ran successfully and all 6 tests passed.
---
**Date:** 2026-05-18
**Working on:** Session 8 — add timestamped file output to `phase-0/transaction_log_analyser.py`, write ADR-002, and confirm CI is green
**Next step:** Begin Session 9 by reading `versions.md`, `decisions.md`, `session-state.md`, and `error-log.md`, then define the next Phase 0 artifact change
**Confused by:** None at session close

---
**Date:** 2026-05-19
**Working on:** Session 9 — Artifact P0-A2: `phase-0/latency_calculator.py` with latency percentiles, GPU cost model, and tests
**Next step:** Run the latency calculator and tests, then commit and push the Session 9 changes
**Confused by:** None at session close

---
**Date:** 2026-05-20
**Working on:** Session 10 — Artifact P0-A3: REST API client in `phase-0/api_client.py` that fetches exchange rates, validates schema, saves timestamped CSV, with tests and CI
**Next step:** Begin Session 11 by reading `versions.md`, `decisions.md`, `session-state.md`, and `error-log.md`, then define the next Phase 0 artifact change
**Confused by:** None at session close

**Date:** 2026-05-21
**Working on:** Phase 0 gate review - all artifacts complete
Next Step: Phae 1 begins - read the PagedAttention blog post
before writing any vLLM code
Confused by: I am not really great at Python and I am only typing the code which Claude gave me. Then I asked Claude and it said we were building the bridge through scaffolding where we will learn to code in Python at a later stage. So, today, we are learning to read code and get accustomed to various coding, jargons and syntax.

## Phase 1 - Session 1 - 2026-05-23
**Working on:** Phase I — Session 01: reading the vLLM blog (https://vllm.ai/blog/2023-06-20-vllm)  and understanding PagedAttention, autoregressive decoding, EOS, and long-context behavior
**Next step:** Begin the next Phase I session by rereading the vLLM blog notes and turning the key concepts into one-page plain-English summaries with analogies
**Confused by:** The difference between model behavior, application behavior, context windows, and how stopping/decoding interact