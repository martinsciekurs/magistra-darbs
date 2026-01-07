---
sidebar_position: 167
---

# graphrag/logger/factory.py

## Overview

Registry-based factory for creating logging.Handler instances for various Graphrag reporting types.

Overview
This module maintains an internal registry mapping reporting_type identifiers to creator callables and exposes a class-based API to register new loggers, query supported types, and instantiate logger handlers for a requested type. It also provides concrete helpers for common logger implementations such as file-based and blob storage-based loggers.

Constants
LOG_FORMAT: The log format string used for logs.
DATE_FORMAT: The date/time format for logs.

Public API
- LoggerFactory
  A registry-based factory class for creating logging.Handler instances for various reporting types.
- create_logger(cls, reporting_type: str, kwargs: dict) -&gt; logging.Handler
  Create a logger handler for the requested type using the built-in registry. This method looks up the given reporting_type in the internal registry and invokes the registered creator with the provided kwargs to create and return a logging.Handler instance.
- is_supported_type(cls, reporting_type: str) -&gt; bool
  Check if the given logger type is supported.
- register(cls, reporting_type: str, creator: Callable[..., logging.Handler]) -&gt; None
  Register a custom logger implementation. This is a classmethod on LoggerFactory. It updates the internal registry (cls._registry) by storing a mapping from the provided reporting_type to the given creator callable. The registry is consulted by create_logger to instantiate loggers for the requested type.
- create_file_logger(**kwargs) -&gt; logging.Handler
  Create a file-based logger handler.
  Args: root_dir: The root directory under which logs are stored. base_dir: The base directory under root_dir where logs are written. filename: The log filename to use for the log file.
  Returns: logging.Handler
  Raises: KeyError: If required keys (root_dir, base_dir, filename) are missing.
- get_logger_types(cls) -&gt; list[str]
  Get the registered logger implementations.
  Args: cls: The class on which this classmethod is invoked.
  Returns: list[str]: The list of registered logger implementation names.
- create_blob_logger(**kwargs) -&gt; logging.Handler
  Create a blob storage-based logger.
  Args: kwargs: The keyword arguments for configuring the blob logger. Typically includes: connection_string, container_name, base_dir, storage_account_blob_url.
  Returns: logging.Handler

Notes
This module relies on the Graphrag configuration and the BlobWorkflowLogger for blob-based logging.

## Classes

- [`LoggerFactory`](../api/classes/graphrag-logger-factory-loggerfactory)

## Functions

- [`create_logger`](../api/functions/graphrag-logger-factory-create-logger)
- [`is_supported_type`](../api/functions/graphrag-logger-factory-is-supported-type)
- [`register`](../api/functions/graphrag-logger-factory-register)
- [`create_file_logger`](../api/functions/graphrag-logger-factory-create-file-logger)
- [`get_logger_types`](../api/functions/graphrag-logger-factory-get-logger-types)
- [`create_blob_logger`](../api/functions/graphrag-logger-factory-create-blob-logger)

