---
sidebar_position: 292
---

# unified-search-app/app/ui/questions_list.py

## Overview

UI component for rendering the generated questions list in the Unified Search App and handling user selection via Streamlit.

This module exposes create_questions_list_ui(sv: SessionVariables) -&gt; None, which renders the list of generated questions from sv and updates sv.selected_question when a user selects a row.

Key exports:
- create_questions_list_ui(sv: SessionVariables) -&gt; None

Data structures:
- generated_questions: Sequence containing the generated questions. Each item represents a question and may be a string or a mapping with a 'text' key; the exact shape is implementation dependent. The function uses a textual representation for rendering.
- selected_question: Optional[int] index of the currently selected question in generated_questions, or None if nothing is selected.

Side effects:
- Updates sv.selected_question to reflect the selected index; this observable state change may also affect UI highlighting and downstream logic that consumes the selected_question value.

Notes:
- sv is expected to provide at least generated_questions and selected_question attributes.

## Functions

- [`create_questions_list_ui`](../api/functions/unified-search-app-app-ui-questions-list-create-questions-list-ui)

