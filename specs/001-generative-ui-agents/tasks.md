# Tasks: Generative UI Course Workspace

**Input**: Design documents from `/specs/001-generative-ui-agents/`

**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/, quickstart.md

**Tests**: Tests are not explicitly requested in the feature specification. Validation is performed through repository structure and documentation checks.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g. US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Prepare the repository paths and documentation files needed for the course workspace.

- [X] T001 Create the course workspace directory at `POCs/build-interactive-agents-with-generative-ui/`
- [X] T002 [P] Create the code container directory at `POCs/build-interactive-agents-with-generative-ui/code/`
- [X] T003 [P] Create the notes container directory at `POCs/build-interactive-agents-with-generative-ui/notes/`
- [X] T004 [P] Add placeholder file in `POCs/build-interactive-agents-with-generative-ui/code/.gitkeep`
- [X] T005 [P] Add placeholder file in `POCs/build-interactive-agents-with-generative-ui/notes/.gitkeep`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Establish the shared documentation contract and base content that all user stories depend on.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T006 Review the required workspace layout against `specs/001-generative-ui-agents/contracts/workspace-structure.md`
- [X] T007 Draft the base course overview in `POCs/build-interactive-agents-with-generative-ui/README.md`
- [X] T008 Ensure the README in `POCs/build-interactive-agents-with-generative-ui/README.md` includes the exact course title and workspace purpose
- [X] T009 Verify the root workspace paths in `POCs/build-interactive-agents-with-generative-ui/README.md` match `POCs/build-interactive-agents-with-generative-ui/code/` and `POCs/build-interactive-agents-with-generative-ui/notes/`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Create Course Workspace (Priority: P1) 🎯 MVP

**Goal**: Deliver a dedicated, correctly named course workspace under `POCs/` with a clear place for code and notes.

**Independent Test**: Open `POCs/` and confirm `POCs/build-interactive-agents-with-generative-ui/` exists with `code/`, `notes/`, and `README.md` visible.

### Implementation for User Story 1

- [X] T010 [US1] Create the root course workspace in `POCs/build-interactive-agents-with-generative-ui/` if it does not already exist
- [X] T011 [P] [US1] Create the code subdirectory in `POCs/build-interactive-agents-with-generative-ui/code/`
- [X] T012 [P] [US1] Create the notes subdirectory in `POCs/build-interactive-agents-with-generative-ui/notes/`
- [X] T013 [US1] Add a placeholder file to `POCs/build-interactive-agents-with-generative-ui/code/.gitkeep`
- [X] T014 [US1] Add a placeholder file to `POCs/build-interactive-agents-with-generative-ui/notes/.gitkeep`
- [X] T015 [US1] Validate that the created structure matches `specs/001-generative-ui-agents/contracts/workspace-structure.md`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Capture Lecture Notes (Priority: P2)

**Goal**: Make lecture notes easy to add, find, and maintain within the course workspace.

**Independent Test**: Add one sample note file under `POCs/build-interactive-agents-with-generative-ui/notes/` and confirm it is separate from code files and discoverable by inspection.

### Implementation for User Story 2

- [X] T016 [US2] Create an initial lecture note file in `POCs/build-interactive-agents-with-generative-ui/notes/lecture-01.md`
- [X] T017 [US2] Add a title, lesson reference, and summary to `POCs/build-interactive-agents-with-generative-ui/notes/lecture-01.md`
- [X] T018 [US2] Update `POCs/build-interactive-agents-with-generative-ui/README.md` to explain where lecture notes belong
- [X] T019 [US2] Verify the notes guidance in `POCs/build-interactive-agents-with-generative-ui/README.md` matches the note model described in `specs/001-generative-ui-agents/data-model.md`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Read Course Overview (Priority: P3)

**Goal**: Make the workspace self-explanatory through a README that describes the course and folder organization.

**Independent Test**: Open `POCs/build-interactive-agents-with-generative-ui/README.md` and confirm it explains the course, the workspace purpose, and where code and notes should be stored.

### Implementation for User Story 3

- [X] T020 [US3] Expand the overview content in `POCs/build-interactive-agents-with-generative-ui/README.md` with the course description and learning purpose
- [X] T021 [US3] Add a workspace structure section to `POCs/build-interactive-agents-with-generative-ui/README.md` covering `code/` and `notes/`
- [X] T022 [US3] Add usage guidance to `POCs/build-interactive-agents-with-generative-ui/README.md` for returning to the workspace over time
- [X] T023 [US3] Review `POCs/build-interactive-agents-with-generative-ui/README.md` against `specs/001-generative-ui-agents/quickstart.md` and align any mismatched instructions

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final consistency checks across the full workspace.

- [X] T024 [P] Re-check `POCs/build-interactive-agents-with-generative-ui/` against `specs/001-generative-ui-agents/contracts/workspace-structure.md`
- [X] T025 Validate the learner workflow in `specs/001-generative-ui-agents/quickstart.md` against the final files in `POCs/build-interactive-agents-with-generative-ui/`
- [X] T026 [P] Proofread `POCs/build-interactive-agents-with-generative-ui/README.md` and `POCs/build-interactive-agents-with-generative-ui/notes/lecture-01.md` for clarity and consistency

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Depends on User Story 1 because notes live inside the created course workspace
- **User Story 3 (P3)**: Depends on User Story 1 and benefits from User Story 2 content to document the final workspace state

### Within Each User Story

- Workspace structure before content
- Notes content before README references to specific notes
- README overview before final quickstart validation
- Story complete before moving to the next dependent story

### Parallel Opportunities

- `T002` and `T003` can run in parallel after `T001`
- `T004` and `T005` can run in parallel after `T002` and `T003`
- `T011` and `T012` can run in parallel after `T010`
- `T024` and `T026` can run in parallel during polish

---

## Parallel Example: User Story 1

```bash
Task: "Create the code subdirectory in POCs/build-interactive-agents-with-generative-ui/code/"
Task: "Create the notes subdirectory in POCs/build-interactive-agents-with-generative-ui/notes/"
```

## Parallel Example: User Story 2

```bash
Task: "Update README.md to explain where lecture notes belong"
Task: "Create an initial lecture note file in POCs/build-interactive-agents-with-generative-ui/notes/lecture-01.md"
```

## Parallel Example: Polish

```bash
Task: "Re-check workspace against contracts/workspace-structure.md"
Task: "Proofread README.md and notes/lecture-01.md for clarity and consistency"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Confirm the workspace exists and matches the documented structure

### Incremental Delivery

1. Complete Setup + Foundational to establish the workspace contract
2. Add User Story 1 to create the actual course workspace
3. Add User Story 2 to seed the notes workflow
4. Add User Story 3 to finalize the README and orientation guidance
5. Finish with polish validation against quickstart and contract docs

### Parallel Team Strategy

1. One contributor completes Setup + Foundational
2. After the workspace exists:
   - Contributor A: complete notes seed content for User Story 2
   - Contributor B: refine README content for User Story 3
3. Rejoin for final polish and validation

---

## Notes

- All tasks follow the required checklist format: checkbox, task ID, optional `[P]`, optional story label, and exact file path
- The suggested MVP scope is **User Story 1** only
- This feature uses manual validation rather than automated tests because the scope is repository structure and documentation
