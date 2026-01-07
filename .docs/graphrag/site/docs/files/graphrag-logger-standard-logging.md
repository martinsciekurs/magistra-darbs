---
sidebar_position: 169
---

# graphrag/logger/standard_logging.py

## Overview

Graphrag standard logging initialization.

This module provides a simple utility to configure the top-level graphrag logger based on a GraphRagConfig, including a default log filename and handling of existing file/stream handlers to avoid resource leaks and duplicate logs.

Exports:
- init_loggers(config: GraphRagConfig, verbose: bool = False, filename: str = DEFAULT_LOG_FILENAME) -&gt; None: Initialize logging for graphrag based on configuration.
- DEFAULT_LOG_FILENAME: str: The default log filename used by init_loggers.

Summary:
A lightweight helper to ensure consistent logging setup across the graphrag project.

## Functions

- [`init_loggers`](../api/functions/graphrag-logger-standard-logging-init-loggers)

