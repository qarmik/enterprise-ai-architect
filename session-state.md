# session-state.md — End-of-Session Context
# Write 3 lines at the end of every session from Phase 1 Output 2 onward

## Template
---
**Date:** YYYY-MM-DD
**Working on:** [artifact or task]
**Next step:** [one specific next action]
**Confused by:** [sate all points of friction]
---

## Session 1 — 2026-05-07
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