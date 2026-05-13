# AI_POCs Constitution

A living governance document for the AI_POCs repository — a collection of AI
Proof of Concepts built on courses, lectures, and experimental research.

## Core Principles

### I. Modular AI Components
Every AI capability — agent, tool, pipeline, or utility — lives in its own
module with a single, well-defined responsibility. Modules must be
independently runnable, importable, and testable without pulling in unrelated
code. If removing a module breaks nothing outside its own boundary, the
boundary is correct.

### II. Schema-First Design
Define data contracts (Pydantic models, TypedDicts, or JSON Schema) **before**
writing implementation code. Schemas are the single source of truth for data
shape. All agent inputs, outputs, and inter-module messages MUST conform to a
schema; unstructured dicts do not leave a module boundary.

### III. Test-First (NON-NEGOTIABLE)
Write tests before implementation code. The cycle is strict:

1. Write the test (it must fail).
2. Get peer or spec approval on what the test asserts.
3. Implement the feature until the test passes.
4. Refactor with the safety net of passing tests.

No code lands in `main` without at least one failing test that it was written
to satisfy.

### IV. Integration Testing for Multi-Agent Workflows
Any workflow that crosses module or agent boundaries requires an integration
test. Focus areas:

- Multi-agent orchestration (root agent → sub-agent → tool chain)
- Schema handoff between pipeline stages
- External API resilience (mocked and live-gated)
- End-to-end runs from user prompt to final output artifact

### V. Observability & Reproducibility
Every AI call (LLM invocation, tool use, callback) MUST be logged with:

- Input prompt / tool arguments
- Model name and provider
- Token usage (prompt + completion) where available
- Timestamp and latency
- Final output or error

Logs enable replay, cost tracking, and debugging. Structured logging (JSON) is
preferred; human-readable format is acceptable for local dev only.

## AI-Specific Constraints

### Model Selection
- Default model for agents: the most capable **cost-appropriate** model
  available (currently `gemini-2.5-flash` for speed, `gemini-3.1-flash-live-preview`
  for complex reasoning).
- Model choice MUST be documented in the feature spec and justified by
  cost, latency, or capability requirements.

### Token Budgets
- Every agent pipeline MUST define a max token budget for both input and
  output. Default: 8 k input / 2 k output per call unless the spec justifies
  otherwise.

### Data Privacy
- No real user data, API keys, or secrets in committed code.
- `.env` files are gitignored. Environment variables are the only mechanism
  for secrets at runtime.

## Development Workflow

### Branch Strategy
- `main` is always deployable.
- Features branch from `main` using the pattern `###-feature-name`.
- Merge to `main` only after constitution check (plan-template gate) and
  peer review.

### Prompt Versioning
- Prompt text is treated as code. Changes to agent instructions, system
  prompts, or tool descriptions follow the same review process as code changes.
- Breaking prompt changes are flagged in the PR title: `[PROMPT-BREAK]`.

### Code Review Requirements
- Every PR requires at least one approving review.
- Reviewers verify: schema compliance, test coverage, observability logging,
  and constitution principle adherence.

### Quality Gates
- Tests pass in CI before merge.
- No new warnings from linters or type checkers.
- Complexity violations (see plan-template "Complexity Tracking") require
  written justification merged into the PR.

## Governance

This constitution supersedes ad-hoc practices. Any project process, tool
choice, or architectural decision that contradicts a principle here MUST be
justified in writing and approved by peer review.

### Amendment Procedure
1. Proposed change is raised as a PR against `.specify/memory/constitution.md`.
2. PR description states what changed and why, including impact on existing
   features or principles.
3. Requires approval from at least two contributors.
4. Version bump follows semantic versioning (see below).

### Versioning Policy
- **MAJOR**: Backward-incompatible governance or principle removals / redefinitions.
- **MINOR**: New principle, section, or materially expanded guidance added.
- **PATCH**: Clarifications, wording fixes, typo corrections, non-semantic refinements.

### Compliance Review
- PRs are spot-checked for constitution compliance at review time.
- Quarterly audit of open PRs and recent merges against all active principles.
- Violations discovered post-merge are logged as issues and remediated in the
  next sprint.

**Version**: 1.0.0 | **Ratified**: 2026-05-13 | **Last Amended**: 2026-05-13