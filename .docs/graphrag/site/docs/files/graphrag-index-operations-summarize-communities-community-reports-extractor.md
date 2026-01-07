---
sidebar_position: 84
---

# graphrag/index/operations/summarize_communities/community_reports_extractor.py

## Overview

Module to extract and summarize community reports from input text using a chat model.

Overview:
This module defines the CommunityReportsExtractor, which orchestrates generating a markdown-formatted community report from input text by invoking a chat model with a configurable extraction prompt. It attempts to produce a structured report (if the response can be parsed as a CommunityReportResponse) and a human-readable markdown representation of the report.

Key exports:
- CommunityReportsExtractor: The class that runs the extraction workflow.
- INPUT_TEXT_KEY: The dictionary key used to pass the input text to the workflow (value: 'input_text').
- MAX_LENGTH_KEY: The dictionary key used to cap the maximum length of the generated report (value: 'max_report_length').

Public API and behavior:
- CommunityReportsExtractor(model_invoker: ChatModel, extraction_prompt: str | None = None, on_error: ErrorHandlerFn | None = None, max_report_length: int | None = None) -&gt; None
  Initialize a CommunityReportsExtractor with the provided configuration.
  - model_invoker: ChatModel used to run prompts.
  - extraction_prompt: Optional custom prompt for extraction; if None, defaults to COMMUNITY_REPORT_PROMPT.
  - on_error: Optional error handler. If provided, it is invoked on errors; otherwise errors propagate.
  - max_report_length: Optional maximum length for the generated report.

- __call__(input_text: str) -&gt; CommunityReportsResult
  Generate a community report for the given input text using the configured model and return both structured and text outputs.
  - input_text: The input text to generate the report from.
  - Returns: A CommunityReportsResult containing:
    - structured_output: CommunityReportResponse | None (the parsed structured report if parsing succeeded)
    - output: str (the human-readable markdown-formatted report)

- _get_text_output(report: CommunityReportResponse) -&gt; str
  Convert a CommunityReportResponse into a markdown string for display.
  - report: The report object containing a title, a summary, and a list of findings with summaries and explanations.
  - Returns: A markdown-formatted string (title, summary, and findings).

Error handling and fallbacks:
- If an exception occurs during model invocation or parsing, the on_error callback (if provided) is invoked. If on_error is not provided, the exception propagates to the caller.
- If parsing of the structured output fails, structured_output is set to None, and a best-effort markdown output is produced from the text data available. All encountered errors are logged for debugging.

Notes:
- The module relies on the ChatModel protocol and the COMMUNITY_REPORT_PROMPT by default.
- The constants INPUT_TEXT_KEY and MAX_LENGTH_KEY are intended for use with dictionary-based transport of inputs and options.

Defaults:
- extraction_prompt defaults to COMMUNITY_REPORT_PROMPT.

## Classes

- [`CommunityReportsExtractor`](../api/classes/graphrag-index-operations-summarize-communities-community-reports-extractor-communityreportsextractor)

## Functions

- [`__call__`](../api/functions/graphrag-index-operations-summarize-communities-community-reports-extractor-call)
- [`_get_text_output`](../api/functions/graphrag-index-operations-summarize-communities-community-reports-extractor-get-text-output)
- [`__init__`](../api/functions/graphrag-index-operations-summarize-communities-community-reports-extractor-init)

