# Spec-Driven Development Template Kit

This kit keeps intent, design, implementation, and verification separate so an AI assistant has a clear, reviewable source of truth.

This repository uses the kit for **Team 2**: a World Cup 2022 API dashboard, pytest coverage, and GitHub Actions that run tests on pull requests to `main` (`.github/workflows/tests.yml`).

How to run the app, call the API, and open the dashboard is in [README.md](../README.md).

## Files

```text
.
├── README.md                         # Project documentation
├── 00-constitution.md
├── 01-requirements.md
├── 02-design.md
├── 03-tasks.md
├── 04-verification.md
├── assets/
├── docs/sdd-kit.md                   # This file
└── .github/workflows/tests.yml       # CI: pytest on PRs and pushes to main
```

Store mocks, screenshots, prototype exports, and sample data in `assets/`. In the requirements file, label every asset as **Binding** or **Inspiration**.

## How to use the kit

1. Set the stable rules in `00-constitution.md`.
2. Write and approve `01-requirements.md`. Do not design or code yet.
3. Create and approve `02-design.md`.
4. Generate and review `03-tasks.md`.
5. Implement only approved tasks and record evidence in `04-verification.md`.
6. Run a final traceability review. Any gap becomes a new task; do not change requirements merely to hide it.
7. Pull requests to `main` must keep the GitHub Actions `pytest` check green.

## Working rules for the AI

- Work on one phase at a time and update only its file.
- Ask questions before making high-impact assumptions. Use `[QUESTION]` and `[ASSUMPTION]`.
- Do not start implementation until requirements, design, and tasks are approved.
- Link decisions, tasks, and tests to requirement IDs.
- Stop and request approval when a binding mock conflicts with a requirement or design.
- Do not merge to `main` while the CI `pytest` job is red.

## Copy-and-paste instruction

```text
Read README.md, 00-constitution.md, and the current phase file.
Update only the current phase file. Keep requirement IDs traceable.
Use [QUESTION] for unresolved information and [ASSUMPTION] for explicit inferences.
Do not move to the next phase or write code without approval.
```

## Method references

This kit follows the common flow of requirements → design → tasks → implementation → verification:

- [GitHub Spec Kit](https://github.github.io/spec-kit/) — Specify → Plan → Tasks → Implement → Converge, with optional quality gates.
- [Kiro Feature Specs](https://kiro.dev/docs/specs/feature-specs/) — requirements, design, and tasks; EARS requirements and acceptance criteria.
- [OpenSpec overview](https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/overview.md) — proposal, specification deltas, design, tasks, and an archive step for existing systems.

Primary sources: [Spec Kit](https://github.github.io/spec-kit/), [Agentic SDD reference](https://github.github.io/spec-kit/reference/agentic-sdd.html), [Kiro Feature Specs](https://kiro.dev/docs/specs/feature-specs/), [OpenSpec overview](https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/overview.md).
