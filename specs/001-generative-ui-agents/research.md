# Research: Generative UI Course Workspace

## Decision 1: Use a dedicated course slug under `POCs/`

- **Decision**: Create one folder named
  `POCs/build-interactive-agents-with-generative-ui/`.
- **Rationale**: A slug derived from the course title is readable, stable, and
  avoids ambiguity when more courses are added later.
- **Alternatives considered**:
  - `POCs/generative-ui-course/`: shorter, but loses the exact course title.
  - `POCs/interactive-agents/`: too broad and more likely to collide with other
    learning material.

## Decision 2: Separate code and notes into top-level subdirectories

- **Decision**: Use `code/` and `notes/` as first-level subdirectories under the
  course workspace.
- **Rationale**: The user explicitly requested storage for code and lecture
  notes. First-level folders minimize cognitive load and make the workspace easy
  to scan.
- **Alternatives considered**:
  - Store everything at the root: simpler at first, but becomes cluttered as
    lessons accumulate.
  - Organize by lecture first: useful later, but adds unnecessary hierarchy to
    the initial version.

## Decision 3: Make the README the entry point for the workspace

- **Decision**: Add a top-level README describing the course, workspace purpose,
  and where to place code and notes.
- **Rationale**: The README satisfies the feature requirement for a self-
  explanatory workspace and supports fast orientation when returning later.
- **Alternatives considered**:
  - Rely only on folder names: insufficient context for future maintenance.
  - Maintain notes only: does not provide a durable summary of intent and layout.

## Decision 4: Use repository-managed files only

- **Decision**: Implement the feature with plain files and folders already
  tracked in the repository.
- **Rationale**: The feature is organizational, not application behavior. File
  operations are sufficient and keep complexity low.
- **Alternatives considered**:
  - Add automation scripts: unnecessary for one course workspace.
  - Add database or metadata storage: unjustified for this scope.
