---
sidebar_position: 280
---

# unified-search-app/app/app_logic.py

## Overview

Unified search app logic for the unified search experience.

This module provides the core orchestration for the unified search application: loading datasets and the knowledge model, and running multiple search strategies (global, local, drift, and basic) as well as question generation. It coordinates with the UI layer and data sources to manage session state and produce SearchResult objects for display.

Exports:
- load_knowledge_model(sv: SessionVariables) -&gt; None
  Load the knowledge model from the data source and populate the session state with the loaded model data. This includes entities, relationships, covariates, community reports, communities, and text units. It also resets generated_questions and related UI state. May raise exceptions if loading fails.

- dataset_name(key: str, sv: SessionVariables) -&gt; str
  Return the dataset name corresponding to the provided key. Raises AttributeError if the key is not found in sv.datasets.value.

- run_global_search_question_generation(query: str, sv: SessionVariables) -&gt; SearchResult
  Run global search question generation and return a SearchResult describing the generated questions.

- run_global_search(query: str, sv: SessionVariables) -&gt; SearchResult
  Execute the global search and return its result.

- run_drift_search(query: str, sv: SessionVariables) -&gt; SearchResult
  Execute the drift-based search and return its result.

- run_local_search(query: str, sv: SessionVariables) -&gt; SearchResult
  Execute the local search and return its result.

- run_basic_search(query: str, sv: SessionVariables) -&gt; SearchResult
  Execute the basic search and return its result.

- run_generate_questions(query: str, sv: SessionVariables) -&gt; tuple[SearchResult, ...]
  Run the global search to generate questions for the dataset; returns a tuple containing the results of the individual generation tasks in the order they were added.

- load_dataset(dataset: str, sv: SessionVariables) -&gt; None
  Load the selected dataset into session state, initializing related fields and data sources; may load the corresponding knowledge model if available. May raise exceptions on failure.

- run_all_searches(query: str, sv: SessionVariables) -&gt; list[SearchResult]
  Run all enabled search engines and return their results as a list.

Notes:
- Function naming in code uses load_knowledge_model; if a future refactor renames this to load_model, align the docstring to avoid confusion.
- Exceptions: callers should handle generic Exceptions raised by I/O, API calls, or data loading.
- Side effects: this module mutates session state (sv) and may perform network calls as part of search execution.

## Functions

- [`load_knowledge_model`](../api/functions/unified-search-app-app-app-logic-load-knowledge-model)
- [`dataset_name`](../api/functions/unified-search-app-app-app-logic-dataset-name)
- [`run_global_search_question_generation`](../api/functions/unified-search-app-app-app-logic-run-global-search-question-generation)
- [`run_global_search`](../api/functions/unified-search-app-app-app-logic-run-global-search)
- [`run_drift_search`](../api/functions/unified-search-app-app-app-logic-run-drift-search)
- [`run_local_search`](../api/functions/unified-search-app-app-app-logic-run-local-search)
- [`run_basic_search`](../api/functions/unified-search-app-app-app-logic-run-basic-search)
- [`run_generate_questions`](../api/functions/unified-search-app-app-app-logic-run-generate-questions)
- [`load_dataset`](../api/functions/unified-search-app-app-app-logic-load-dataset)
- [`run_all_searches`](../api/functions/unified-search-app-app-app-logic-run-all-searches)

