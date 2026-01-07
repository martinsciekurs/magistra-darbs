---
sidebar_position: 168
---

# graphrag/logger/progress.py

## Overview

Progress reporting utilities for tracking and emitting progress updates during processing.

This module provides a lightweight, generic progress reporting framework used to monitor how many items have been completed out of a known total and to notify a callback with Progress objects. A Progress object exposes total_items, completed_items, and an optional description. The public API includes a ProgressTicker class, a progress_ticker factory, and a progress_iterable helper, along with a ProgressHandler type alias and the type variable T for typing iterable items.

Key exports:
- ProgressTicker: class that tracks progress toward a known total and can notify a callback with progress updates
- progress_ticker(callback, num_total, description=""): factory to create a configured ProgressTicker
- progress_iterable(iterable, progress, num_total=None, description=""): wraps an iterable to emit progress updates after each item
- ProgressHandler: type alias for a callback that receives a Progress object
- T: TypeVar for generic item type

## Classes

- [`ProgressTicker`](../api/classes/graphrag-logger-progress-progressticker)

## Functions

- [`__call__`](../api/functions/graphrag-logger-progress-call)
- [`progress_ticker`](../api/functions/graphrag-logger-progress-progress-ticker)
- [`__init__`](../api/functions/graphrag-logger-progress-init)
- [`done`](../api/functions/graphrag-logger-progress-done)
- [`progress_iterable`](../api/functions/graphrag-logger-progress-progress-iterable)

