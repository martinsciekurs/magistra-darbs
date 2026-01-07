---
sidebar_position: 124
---

# CommunityReportsExtractor

**File:** `graphrag/index/operations/summarize_communities/community_reports_extractor.py`

## Overview

CommunityReportsExtractor orchestrates generation of a markdown-formatted community report from input text by invoking a chat model with a configurable extraction prompt, producing both a structured report and a human-readable markdown output.

Args:
    model_invoker: ChatModel - The model invoker used to run prompts.
    extraction_prompt: str | None - Custom prompt to use for extraction. If None, defaults to COMMUNITY_REPORT_PROMPT.
    on_error: ErrorHandlerFn | None - Function to handle errors. If None, a no-op is used.
    max_report_length: int | None - Maximum length for the generated report.

Returns:
    CommunityReportsResult - The result containing:
      structured_output: CommunityReportResponse | None - The parsed structured report from the model.
      output: str - The human-readable markdown text report.

Raises:
    Exceptions raised by the underlying model invocation or error handler may propagate.

Attributes:
    model_invoker: The model invoker used to run prompts (ChatModel).
    extraction_prompt: str | None - Custom prompt to use for extraction. If None, defaults to COMMUNITY_REPORT_PROMPT.
    on_error: ErrorHandlerFn | None - Function to handle errors. If None, a no-op is used.
    max_report_length: int | None - Maximum report length.

## Methods

### `__call__`

```python
def __call__(self, input_text: str)
```

### `_get_text_output`

```python
def _get_text_output(self, report: CommunityReportResponse) -> str
```

### `__init__`

```python
def __init__(
        self,
        model_invoker: ChatModel,
        extraction_prompt: str | None = None,
        on_error: ErrorHandlerFn | None = None,
        max_report_length: int | None = None,
    )
```

