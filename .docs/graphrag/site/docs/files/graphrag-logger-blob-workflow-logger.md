---
sidebar_position: 166
---

# graphrag/logger/blob_workflow_logger.py

## Overview

Blob-based workflow logger that persists log records to Azure Blob storage as JSON lines.

Purpose
Provide a logging.Handler implementation that formats LogRecord instances as compact JSON payloads and appends each as a separate line to a blob in an Azure Storage container. The blob stores a JSON Lines (JSONL) stream suitable for append-only ingestion and later processing.

Public exports
- BlobWorkflowLogger: Logging.Handler subclass that writes logs to Azure Blob storage.

Brief summary
The BlobWorkflowLogger formats each record into a JSON object containing a type, a message, and optional details (from exc_info) and stack traces if present. The payload is persisted to a blob via internal helper methods. An internal BlobServiceClient is reinitialized when the accumulated block count reaches a configured maximum to manage blob growth. I/O errors during blob operations raise OSError to propagate failures to callers.

__init__ parameters
- connection_string (str | None): Connection string for the blob storage, or None if using other authentication methods.
- container_name (str | None): Name of the blob container.
- blob_name (str): Name of the blob to create; if empty, a timestamped default will be used.
- base_dir (str | None): Optional base directory to prepend to the blob name, or None.
- storage_account_blob_url (str | None): URL of the storage account blob service, or None.
- level (int): Logging level; default NOTSET.

Methods
- emit(record) -&gt; None: Formats a LogRecord as JSON and writes it to blob storage. May raise OSError on I/O errors.
- _write_log(log: dict[str, Any]) -&gt; None: Appends the provided JSON line to the blob; may reinitialize the internal client when the maximum block count is reached. May raise OSError on I/O errors.
- _get_log_type(level: int) -&gt; str: Returns "log" for non-critical levels, "warning" for WARNING, or "error" for ERROR and above.

Returns
- None for all public methods (emit, _write_log); the handler performs side effects rather than returning data.

Raises
- OSError: If an I/O error occurs during blob operations.

## Classes

- [`BlobWorkflowLogger`](../api/classes/graphrag-logger-blob-workflow-logger-blobworkflowlogger)

## Functions

- [`_write_log`](../api/functions/graphrag-logger-blob-workflow-logger-write-log)
- [`_get_log_type`](../api/functions/graphrag-logger-blob-workflow-logger-get-log-type)
- [`__init__`](../api/functions/graphrag-logger-blob-workflow-logger-init)
- [`emit`](../api/functions/graphrag-logger-blob-workflow-logger-emit)

