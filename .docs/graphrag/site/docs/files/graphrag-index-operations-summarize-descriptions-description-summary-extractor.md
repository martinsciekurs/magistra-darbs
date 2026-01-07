---
sidebar_position: 95
---

# graphrag/index/operations/summarize_descriptions/description_summary_extractor.py

## Overview

Summarize descriptions for entities using a chat-based language model.

This module defines SummarizeExtractor, which orchestrates the summarization of a list of description strings into a single concise description for a target entity (or a pair of entities) by invoking a language model with a dedicated summarization prompt. It is configurable via a model invoker, a prompt template, and token constraints, and can optionally delegate error handling to a provided callback.

Public API
- SummarizeExtractor: Class that encapsulates the model invocation and configuration for performing the summarization.
- ENTITY_NAME_KEY, DESCRIPTION_LIST_KEY, MAX_LENGTH_KEY: Module-level constants used to structure input data for summarization (e.g., &#123;ENTITY_NAME_KEY: ..., DESCRIPTION_LIST_KEY: ..., MAX_LENGTH_KEY: ...&#125;).

Class: SummarizeExtractor
Initializes a summarizer tied to a ChatModel-backed prompt and exposes a callable interface to produce a summarized description for a given id.

__init__(
    model_invoker: ChatModel,
    max_summary_length: int,
    max_input_tokens: int,
    summarization_prompt: str | None = None,
    on_error: ErrorHandlerFn | None = None,
)
Args:
- model_invoker: The model invoker used to execute prompts.
- max_summary_length: Maximum length of the resulting summary.
- max_input_tokens: Maximum number of input tokens to consider for summarization.
- summarization_prompt: Optional custom prompt; if None, SUMMARIZE_PROMPT is used.
- on_error: Optional callback to handle errors.
Returns: None
Raises: Propagates exceptions from initialization or dependencies unless on_error handles them.

__call__(
    id: str | tuple[str, str],
    descriptions: list[str],
) -&gt; SummarizationResult
Args:
- id: The identifier for the summarization target. It can be a string or a pair of strings.
- descriptions: The list of description strings to summarize. If empty, the result is an empty description.
Returns:
- SummarizationResult: The result object encapsulating the summarized description and any related metadata.
Raises: Exception if the underlying LLM call or input processing fails.

_summarize_descriptions_with_llm(
    self, id: str | tuple[str, str] | list[str], descriptions: list[str]
) -&gt; str
Args:
- id: Identifier(s) for the entity or entities.
- descriptions: Descriptions to be summarized.
Returns:
- str: The summarized description produced by the LLM.
Raises: Exception if the LLM call or processing encounters an error.

_summarize_descriptions(
    self, id: str | tuple[str, str], descriptions: list[str]
) -&gt; str
Args:
- id: Identifier(s) for the entity or entities.
- descriptions: Descriptions to be summarized.
Returns:
- str: The summarized description string.
Raises: Exception if the underlying call fails.

Dependencies and behavior
- External dependencies: ChatModel (language model interface), SUMMARIZE_PROMPT (default prompt template), and get_tokenizer (tokenization utility).
- The module uses these components to construct and execute a summarization prompt that respects token constraints and the configured maximum summary length.
- Error handling: An optional on_error callback can be supplied to intercept and handle exceptions; if not handled, exceptions propagate to the caller. The public API documents the intended return types and potential exceptions.

## Classes

- [`SummarizeExtractor`](../api/classes/graphrag-index-operations-summarize-descriptions-description-summary-extractor-summarizeextractor)

## Functions

- [`_summarize_descriptions_with_llm`](../api/functions/graphrag-index-operations-summarize-descriptions-description-summary-extractor-summarize-descriptions-with-llm)
- [`_summarize_descriptions`](../api/functions/graphrag-index-operations-summarize-descriptions-description-summary-extractor-summarize-descriptions)
- [`__call__`](../api/functions/graphrag-index-operations-summarize-descriptions-description-summary-extractor-call)
- [`__init__`](../api/functions/graphrag-index-operations-summarize-descriptions-description-summary-extractor-init)

