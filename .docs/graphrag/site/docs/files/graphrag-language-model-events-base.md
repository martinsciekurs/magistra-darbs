---
sidebar_position: 141
---

# graphrag/language_model/events/base.py

## Overview

Base definitions for language model event error handling.

This module provides a minimal contract for handling errors raised by language model operations. It defines a small Protocol (ModelEventHandler) that concrete event handlers can implement to process and respond to model-related errors, and a conventional on_error signature intended to be used by such handlers.

Public API
- on_error(self, error: BaseException | None, traceback: str | None = None, arguments: dict[str, Any] | None = None) -&gt; None
  Handle a model error. error is the exception that occurred, or None if no error is provided. traceback is an optional textual traceback, or None if not available. arguments is an optional dict with additional contextual data related to the error. Returns None.

- ModelEventHandler
  Protocol that defines the on_error method. Implementations of this protocol must provide an on_error method with the above signature to process model-related errors.

Notes
- This module is designed to be importable and easily mockable for testing. It does not perform I/O by itself beyond the contract it defines.

## Classes

- [`ModelEventHandler`](../api/classes/graphrag-language-model-events-base-modeleventhandler)

## Functions

- [`on_error`](../api/functions/graphrag-language-model-events-base-on-error)

