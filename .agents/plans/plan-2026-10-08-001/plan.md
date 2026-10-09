# Plan — project setup (tooling, hooks, CI, agents)

Status: done (see result.md). Prompts: initial-prompt.md, follow-up-prompts.md.

1. [x] Extract the course PDFs to `docs/spec/*.md` so agents can read them; gitignore `docs/spec/`.
   The extraction script is kept out of the repo (user's choice); the md files are shared within the group.
2. [x] Cargo workspace (`crates/*`) with `[workspace.lints]`: unsafe, pedantic, missing_docs, unwrap/expect/panic outside tests.
   Empty skeletons for the group crates chart, admiralty, ship, harness (an empty workspace does not build).
   Island and Cartographer crates are individual work: each member creates their own.
3. [x] `clippy.toml`: disallow `HashMap`/`HashSet`, `thread_rng`/`rng`, `SystemTime::now` (main §10.1).
   `Instant::now` is not banned workspace-wide because the Admiralty needs it for deadlines.
4. [x] `.githooks/pre-commit` (fmt check + clippy; a commit-msg hook was dropped as unnecessary), enabled with `git config core.hooksPath .githooks`.
5. [x] GitHub Actions: fmt, crate-root attribute check, clippy pedantic, docs, tests ×3 (flakiness); `actions/checkout@v7`.
6. [x] Claude Code hooks (Python, cross-platform, no dependencies): save prompts, rustfmt, plan reminder. (A git-blame ownership guard was removed at the user's request.)
   No commit gate in Claude: the git pre-commit hook already covers commits made by Claude.
7. [x] `.claude/agents/` (read-only): spec-checker (with API surface), protocol-defect-hunter, view-leak-auditor,
   determinism-auditor, hostile-input-auditor, test-gap-finder, ai-declaration-checker; `oral-prep` as a skill,
   because it must converse with the user.
8. [x] `explainer` agent: detailed Italian study notes in `study/` (gitignored, personal); first note: the CI workflow.
9. [x] Cross-platform: hooks run through `.claude/hooks/run.sh` (python3, falling back to `python` on Windows;
    `PYTHONUTF8=1`), `.gitattributes` forces LF everywhere, `.DS_Store` ignored.
10. [x] README: group name, members (contributions to be defined), components.

Open: channel library (crossbeam vs async) is a WG decision, not fixed here.
