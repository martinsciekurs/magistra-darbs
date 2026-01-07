---
sidebar_position: 4
---

# graphrag/callbacks/console_workflow_callbacks.py

## Overview

Console-based callback implementation for graph workflow events.

This module exposes ConsoleWorkflowCallbacks, a concrete console-oriented implementation of the workflow callback interface. It inherits NoopWorkflowCallbacks, prints status messages for pipeline and workflow lifecycle events, and renders a live progress bar to stdout as progress updates are received. When verbose mode is enabled, additional information may be emitted to aid debugging.

Key exports:
- ConsoleWorkflowCallbacks: Concrete callback implementation that logs console output for pipeline and workflow events with optional verbose logging.

Brief summary:
Used to observe and debug graph runs in a terminal by emitting human-readable messages and a live progress indicator.

## Classes

- [`ConsoleWorkflowCallbacks`](../api/classes/graphrag-callbacks-console-workflow-callbacks-consoleworkflowcallbacks)

## Functions

- [`__init__`](../api/functions/graphrag-callbacks-console-workflow-callbacks-init)
- [`pipeline_end`](../api/functions/graphrag-callbacks-console-workflow-callbacks-pipeline-end)
- [`pipeline_start`](../api/functions/graphrag-callbacks-console-workflow-callbacks-pipeline-start)
- [`workflow_start`](../api/functions/graphrag-callbacks-console-workflow-callbacks-workflow-start)
- [`progress`](../api/functions/graphrag-callbacks-console-workflow-callbacks-progress)
- [`workflow_end`](../api/functions/graphrag-callbacks-console-workflow-callbacks-workflow-end)

