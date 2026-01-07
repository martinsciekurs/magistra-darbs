---
sidebar_position: 281
---

# unified-search-app/app/home_page.py

## Overview

Home page UI for the Unified Search App rendered via Streamlit.

Purpose:
This module defines the main Streamlit-based home page renderer for the Unified Search App. It wires together the app logic and UI components to render the GraphRAG UI, among other UI pieces (questions, reports, and side bar).

Key exports:
- main(): asynchronous coroutine that renders the main UI.
  Args: None: This function takes no parameters.
  Returns: None: This coroutine does not return a value.
- on_click_reset(sv: SessionVariables): Reset the relevant session variables on reset action.
  Args: sv (SessionVariables): The session variables container; resets sv.generated_questions.value to [], sv.selected_question.value to '', and sv.show_text_input.value to True.
  Returns: None: This function does not return a value.
- on_change(sv: SessionVariables): Updates the current question in the session variables from the Streamlit session state.
  Args: sv (SessionVariables): The session variables container; updates sv.question.value from the input.
  Returns: None: This function does not return a value.
  Raises: KeyError: If the key 'question_input' is not present in st.session_state.

Brief summary:
The module coordinates app logic with UI components to present the primary user interface, including graph visualization, question generation/listing, and reports, through Streamlit calls.

## Functions

- [`main`](../api/functions/unified-search-app-app-home-page-main)
- [`on_click_reset`](../api/functions/unified-search-app-app-home-page-on-click-reset)
- [`on_change`](../api/functions/unified-search-app-app-home-page-on-change)

