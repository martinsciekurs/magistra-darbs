---
sidebar_position: 295
---

# unified-search-app/app/ui/search.py

## Overview

Unified search UI utilities for the Streamlit-based application.

This module provides UI components and helpers used by the unified search UI. It
facilitates rendering of HTML results, parsing and formatting of responses,
formatting citations and hyperlinks, and displaying search-related results and
graphs within the Streamlit interface.

Key exports:
- init_search_ui(container, search_type, title, caption): Initialize search UI component in the specified container for the given search type.
- render_html_table(df, search_type, key): Render a DataFrame as an HTML table in the UI with per-cell formatting and IDs for rows.
- convert_numbered_list_to_array(numbered_list_str): Convert a numbered-list string into an array of extracted items.
- format_response_hyperlinks_by_key(str_response, key, anchor, search_type=""): Format response to show hyperlinks inside the response UI by key.
- get_ids_per_key(str_response, key): Get IDs associated with a given key from a string response.
- format_suggested_questions(questions): Format suggested questions for display in the UI.
- format_response_hyperlinks(str_response, search_type=""): Format response to show hyperlinks inside the response UI.
- display_citations(container=None, result=None): Display citations into the UI.
- display_graph_citations(entities, relationships, citation_type): Display graph citations in the UI.
- display_search_result(container, result, stats=None): Display search results in the UI and update placeholders.

Constants:
- SHORT_WORDS = 12
- LONG_WORDS = 200

Brief summary: The module focuses on rendering search results, formatting responses, and
displaying citations for both textual and graph-based results in the unified search UI.

## Functions

- [`init_search_ui`](../api/functions/unified-search-app-app-ui-search-init-search-ui)
- [`render_html_table`](../api/functions/unified-search-app-app-ui-search-render-html-table)
- [`convert_numbered_list_to_array`](../api/functions/unified-search-app-app-ui-search-convert-numbered-list-to-array)
- [`format_response_hyperlinks_by_key`](../api/functions/unified-search-app-app-ui-search-format-response-hyperlinks-by-key)
- [`get_ids_per_key`](../api/functions/unified-search-app-app-ui-search-get-ids-per-key)
- [`format_suggested_questions`](../api/functions/unified-search-app-app-ui-search-format-suggested-questions)
- [`format_response_hyperlinks`](../api/functions/unified-search-app-app-ui-search-format-response-hyperlinks)
- [`display_citations`](../api/functions/unified-search-app-app-ui-search-display-citations)
- [`display_graph_citations`](../api/functions/unified-search-app-app-ui-search-display-graph-citations)
- [`display_search_result`](../api/functions/unified-search-app-app-ui-search-display-search-result)

