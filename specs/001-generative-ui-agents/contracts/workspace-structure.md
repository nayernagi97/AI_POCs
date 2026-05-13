# Contract: Course Workspace Structure

## Purpose

Define the required public structure for the course workspace created by this
feature.

## Required Layout

```text
POCs/
└── build-interactive-agents-with-generative-ui/
    ├── README.md
    ├── code/
    └── notes/
```

## Contract Rules

1. The workspace directory name is
   `build-interactive-agents-with-generative-ui`.
2. `README.md` is required at the workspace root.
3. `code/` is the only root-level location for course code artifacts created by
   this feature.
4. `notes/` is the only root-level location for lecture notes created by this
   feature.
5. The workspace must live directly under `POCs/`.
6. A second root-level workspace for the same course title must not be created.

## Acceptance Surface

- A reviewer can verify compliance by inspecting the repository tree.
- A learner can identify the correct destination for new code and notes without
  opening source files.
