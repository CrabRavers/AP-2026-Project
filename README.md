# CrabRavers — AP 2026/2027 Project

Group and individual contributions of **CrabRavers** for the Advanced Programming course project, A.Y. 2026/2027.

## Group

| Member | Contributions |
|---|---|
| Luca Civera | to be defined |
| Alessandro Ceresa | to be defined |
| Lorenzo Caraffini | to be defined |
| Andrea Soranzo Mendez | to be defined |

## Components

- Group work: Chart (`crates/chart`), Admiralty (`crates/admiralty`), Ship (`crates/ship`), and the harness that starts a
  game (`crates/harness`).
- Individual work, one crate each, to be added: Islands (at least two) and Cartographers.

## Getting Started

This repository **must be forked**.
Do not create a new repository from scratch.
You can rename the fork afterward if desired.

When initializing a library or binary crate, you must add the following crate-level attributes to the crate root:

- For a library crate, add them to `src/lib.rs`.
- For a binary crate, add them to `src/main.rs`.

```
#![deny(unsafe_code)]
#![deny(clippy::pedantic)]
```

These rules are part of the project's coding standards and must be present from the beginning of development.

## README Requirements

You may modify this `README.md` to document your project.
At a minimum, clearly specify:

* The **group name**.
* Which **component(s)** your repository implements.
* Who **contributed to which component(s)**.

Feel free to add any additional information that helps explain the project, its structure, or how to use it.

## AGENTS.md

You can modify `AGENTS.md`, but the current content must be kept as is.

## CLAUDE.md

`CLAUDE.md` must import `@AGENTS.md` at the top.
Do not remove it.

## Rules for code in this repository

These are the project's coding principles, and here they are enforced rather than encouraged.

- **No `unsafe`.**
- **No undocumented panics.** If a function can panic, say so in its doc comment and say when. Most things in here should not panic at all.
- **rustfmt.** Configure your editor.
- Before committing, `cargo fmt --all` must pass. If it does not pass, and the latest commit is not authored by the current user, make a single commit: `style: format code`.

## Development setup

Run once after cloning:

```bash
git config core.hooksPath .githooks        # pre-commit: fmt + clippy
```

The agents read the course specs as text from `docs/spec/` (`main.md`, `protocol.md`, `org.md`, `ai-statement.md`).
The folder is gitignored because the specs are course material: ask a group member for a copy.

What enforces what:

| Check | Local (git hooks) | CI (GitHub Actions) |
|---|---|---|
| `cargo fmt --all --check` | pre-commit | yes |
| `cargo clippy --workspace --all-targets -- -D warnings -W clippy::pedantic` | pre-commit | yes |
| `#![deny(unsafe_code)]` / `#![deny(clippy::pedantic)]` in every crate root | — | yes |
| docs build without warnings, tests (run 3× to catch flakiness) | — | yes |

The CI is the one that counts; enable branch protection on `main` requiring it. Every crate goes in `crates/` and must
have `[lints] workspace = true` in its `Cargo.toml`. `clippy.toml` bans `HashMap`/`HashSet`, `thread_rng` and
`SystemTime::now` for determinism (main §10.1).

### Claude Code (optional, nothing above depends on it)

Open the Claude Code session in this folder, or the project settings are not loaded. The hooks need Python 3 and a
POSIX shell: built in on macOS/Linux; on Windows, Git for Windows (Git Bash) provides the shell.

- `.claude/settings.json` hooks (run through `.claude/hooks/run.sh`): save every prompt verbatim into `.agents/plans/`
  (one session = one task), rustfmt every edited `.rs` file, warn when `plan.md`/`result.md` are missing.
- `.claude/agents/`, all read-only: `spec-checker`, `protocol-defect-hunter`, `view-leak-auditor`,
  `determinism-auditor`, `hostile-input-auditor`, `test-gap-finder`, `ai-declaration-checker`.
- `explainer`: writes a detailed study note on a change into `study/` (gitignored, personal).
- `/oral-prep <module>`: mock oral exam on code you wrote.
