# Data Model: Generative UI Course Workspace

## Entity: Course Workspace

- **Description**: The top-level directory representing one course inside
  `POCs/`.
- **Fields**:
  - `course_title`: Human-readable course name
  - `course_slug`: Filesystem-safe directory name
  - `readme_path`: Relative path to the workspace README
  - `code_directory`: Relative path to the code container folder
  - `notes_directory`: Relative path to the lecture notes folder
- **Validation Rules**:
  - `course_slug` must be unique within `POCs/`
  - `readme_path`, `code_directory`, and `notes_directory` must exist after
    setup
  - `course_title` must match the course referenced in the README

## Entity: Lecture Note

- **Description**: A written artifact capturing lesson content, ideas, or
  follow-up work for the course.
- **Fields**:
  - `title`: Short note title
  - `lesson_reference`: Optional lecture or module reference
  - `summary`: Main takeaway or topic captured in the note
  - `file_path`: Relative path under `notes/`
- **Validation Rules**:
  - `file_path` must remain inside the workspace `notes/` directory
  - `title` should be meaningful enough to distinguish one note from another

## Entity: Course README

- **Description**: The overview document that explains the workspace.
- **Fields**:
  - `course_name`: Full course title
  - `purpose`: Why the workspace exists
  - `structure_summary`: Explanation of where code and notes live
  - `usage_guidance`: How the learner should use the workspace over time
- **Validation Rules**:
  - Must mention the course title
  - Must explain both `code/` and `notes/`
  - Must be understandable without opening any other file

## Relationships

- One **Course Workspace** contains one **Course README**.
- One **Course Workspace** contains zero or more **Lecture Notes**.
- One **Course Workspace** contains a dedicated directory for code artifacts.
