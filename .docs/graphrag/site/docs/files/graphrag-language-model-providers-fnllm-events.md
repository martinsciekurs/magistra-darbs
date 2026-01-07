---
sidebar_position: 146
---

# graphrag/language_model/providers/fnllm/events.py

## Overview

FNLLM event integration for Graphrag language model provider.

This module defines FNLLMEvents, which handles FNLLM-specific events and delegates error processing to a provided error handler.

Key exports:
- FNLLMEvents: FNLLMEvents handles FNLLM-specific events and delegates error processing to a provided error handler.
  Args:
    on_error: ErrorHandlerFn to be invoked on errors.
  Returns:
    None
  Raises:
    Exception: If the configured error handler raises an exception.

  __init__(self, on_error: ErrorHandlerFn)
  Args:
    on_error: ErrorHandlerFn to be invoked on errors.
  Returns:
    None

  on_error(self, error: BaseException | None, traceback: str | None = None, arguments: dict[str, Any] | None = None) -&gt; None
  Args:
    error: The error to handle, or None if no error is available.
    traceback: The traceback string, or None if not provided.
    arguments: Additional arguments related to the error, or None.
  Returns:
    None
  Raises:
    Exception: If the configured error handler raises an exception.

Brief summary:
- The FNLLMEvents class is initialized with an on_error handler and provides on_error to process errors, potentially raising an exception if the error handler fails.

## Classes

- [`FNLLMEvents`](../api/classes/graphrag-language-model-providers-fnllm-events-fnllmevents)

## Functions

- [`__init__`](../api/functions/graphrag-language-model-providers-fnllm-events-init)
- [`on_error`](../api/functions/graphrag-language-model-providers-fnllm-events-on-error)

