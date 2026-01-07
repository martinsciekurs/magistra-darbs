---
sidebar_position: 205
---

# graphrag/query/structured_search/drift_search/action.py

## Overview

DriftAction module for representing a single action in a structured drift search workflow.

Overview:
This module provides the DriftAction class used as a node in the drift search graph. Each action stores a query, an optional answer, an optional list of follow-up actions, and an optional score that may be computed by a scorer. It supports serialization/deserialization for persistence or inter-process communication, construction from DRIFTPrimer responses, and integration with search engines to populate results and drive the drift search.

Exports:
- DriftAction

API contract (high level):
- DriftAction.__init__(query, answer=None, follow_ups=None) -&gt; None
  Args: query (str): the drift action query. answer (Optional[str]): answer if available. follow_ups (Optional[list[DriftAction]]): follow-up actions.
  Returns: None
  Raises: TypeError if argument types are invalid.

- DriftAction.compute_score(self, scorer) -&gt; None
  Args: scorer (Any): scorer used to compute the score.
  Returns: None

- DriftAction.serialize(self, include_follow_ups=True) -&gt; dict[str, Any]
  Args: include_follow_ups (bool): whether to serialize follow-up actions.
  Returns: A dictionary representation of the action.

- DriftAction.is_complete(self) -&gt; bool
  Returns: True if an answer is present, False otherwise.

- DriftAction.from_primer_response(cls, query, response) -&gt; DriftAction
  Args: query (str), response (str|dict|list). Returns: DriftAction.

- DriftAction.deserialize(cls, data) -&gt; DriftAction
  Args: data (dict[str, Any]). Returns: DriftAction. Raises: ValueError if required fields missing such as 'query'.

- DriftAction.__eq__(self, other) -&gt; bool
  Returns: True if other is a DriftAction with the same query.

- DriftAction.__hash__(self) -&gt; int
  Returns: int used for hashing in graphs.

- DriftAction.search(self, search_engine, global_query, scorer=None) -&gt; DriftAction
  Args: search_engine (Any), global_query (str), scorer (Any, optional)
  Returns: DriftAction (self) with updated results and optional score.

Notes:
- The from_primer_response path uses try_parse_json_object to interpret JSON-like primer payloads.
- The class is designed for graph-based drift search workflows; its __hash__ and __eq__ implementations enable inclusion in graph structures such as networkx.MultiDiGraph.

Usage example:
- action = DriftAction('What is the price?')
- action.is_complete()  # False
- serialized = action.serialize()
- restored = DriftAction.deserialize(serialized)
- primer_action = DriftAction.from_primer_response('What is the price?', &#123;'intermediate_answer': 'About &#36;10', 'score': 0.8, 'follow_up_queries': [&#123;'query': 'Distance?'&#125;]&#125;)
- updated = action.search(search_engine, 'What is the price?', scorer)

## Classes

- [`DriftAction`](../api/classes/graphrag-query-structured-search-drift-search-action-driftaction)

## Functions

- [`compute_score`](../api/functions/graphrag-query-structured-search-drift-search-action-compute-score)
- [`__hash__`](../api/functions/graphrag-query-structured-search-drift-search-action-hash)
- [`__init__`](../api/functions/graphrag-query-structured-search-drift-search-action-init)
- [`serialize`](../api/functions/graphrag-query-structured-search-drift-search-action-serialize)
- [`is_complete`](../api/functions/graphrag-query-structured-search-drift-search-action-is-complete)
- [`from_primer_response`](../api/functions/graphrag-query-structured-search-drift-search-action-from-primer-response)
- [`deserialize`](../api/functions/graphrag-query-structured-search-drift-search-action-deserialize)
- [`__eq__`](../api/functions/graphrag-query-structured-search-drift-search-action-eq)
- [`search`](../api/functions/graphrag-query-structured-search-drift-search-action-search)

