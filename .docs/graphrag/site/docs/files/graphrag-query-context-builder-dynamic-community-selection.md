---
sidebar_position: 185
---

# graphrag/query/context_builder/dynamic_community_selection.py

## Overview

Dynamic selection of relevant communities for a query using a language model and relevancy scoring.

This module exposes the DynamicCommunitySelection class, which orchestrates the dynamic filtering and ranking of communities to address a given query. It relies on a language model to evaluate relevance and a dedicated relevancy scoring function to guide the selection across a hierarchical set of communities, using precomputed community reports and Community objects as inputs. The process can operate asynchronously, supports optional summarization, and is configurable for depth, concurrency, and model parameters. The outcome is a list of CommunityReport objects representing the selected communities and a metrics dictionary containing language-model usage data and intermediate scoring information.

Public API
- DynamicCommunitySelection
  - __init__(community_reports, communities, model, tokenizer, rate_query=RATE_QUERY, use_summary=False, threshold=1, keep_parent=False, num_repeats=1, max_level=2, concurrent_coroutines=8, model_params=None)
      Initialize the selector with the data sources, language model, tokenizer, and configuration.
      Args:
        community_reports (list[CommunityReport]): Reports for communities to consider, typically mapped by community_id.
        communities (list[Community]): Community objects used to build the hierarchy and starting points.
        model (ChatModel): Language model instance used to rate relevance of communities with respect to the query.
        tokenizer (Tokenizer): Tokenizer used for prompt construction and token counting.
        rate_query (str): Prompt/template used to solicit relevance judgments from the language model (default RATE_QUERY).
        use_summary (bool): If True, incorporate summaries of communities when computing relevance.
        threshold (int): Minimum relevance level or score required for a community to be selected.
        keep_parent (bool): If True, retain parent communities in the final results.
        num_repeats (int): Number of times to repeat the prompting/ranking process per candidate.
        max_level (int): Maximum hierarchical depth to traverse during selection.
        concurrent_coroutines (int): Maximum number of concurrent asynchronous tasks.
        model_params (dict[str, Any] | None): Optional additional parameters passed to the language model.
      Returns: None

  - select(query)
      Asynchronously select relevant communities for the given query.
      Args:
        query (str): The user query to rate against.
      Returns:
        tuple[list[CommunityReport], dict[str, Any]]: A list of CommunityReport objects representing the relevant communities and a dictionary with additional information including llm usage metrics (llm_calls, prompt_tokens, output_tokens) and other relevancy data produced during the process.
      Raises:
        ValueError: If the input query is not a string or is empty, or if required initialization data is missing.
        RuntimeError: If interactions with the language model or rate_relevancy computations fail unexpectedly.
        TypeError: If input types do not match the expected annotations.

Notes
- Relevance is determined by combining language-model judgments with the rate_relevancy scoring function, potentially leveraging summaries and hierarchical relationships among communities. The term relevant communities refers to those that exceed the configured threshold and contribute meaningful context to answer the query.
- The module is designed to integrate with the DynamicCommunitySelection class and its methods, providing a cohesive API for building context-aware communities for downstream tasks.

## Classes

- [`DynamicCommunitySelection`](../api/classes/graphrag-query-context-builder-dynamic-community-selection-dynamiccommunityselection)

## Functions

- [`__init__`](../api/functions/graphrag-query-context-builder-dynamic-community-selection-init)
- [`select`](../api/functions/graphrag-query-context-builder-dynamic-community-selection-select)

