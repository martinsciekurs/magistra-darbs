---
sidebar_position: 225
---

# graphrag/utils/cli.py

## Overview

Graphrag CLI utilities for path validation and configuration redaction.

This module provides helper functions for validating CLI inputs and redacting sensitive values in configuration objects. It exports the following main utilities: dir_exist, file_exist, redact, and redact_dict.

Functions:
- dir_exist(path)
  Check for directory existence.
  Args:
    path (str): Path to the directory.
  Returns:
    str: The input path if the directory exists.
  Raises:
    argparse.ArgumentTypeError: If the directory does not exist.

- file_exist(path)
  Check that the given path points to an existing file.
  Args:
    path (str): Path to the file to validate. May be a string or Path object.
  Returns:
    str: The input path if the file exists.
  Raises:
    argparse.ArgumentTypeError: If the file does not exist.
  Notes:
    This check uses Path.is_file() to verify that the path refers to a regular file.

- redact(config: dict) -&gt; str
  Sanitize secrets in a configuration object by redacting sensitive fields.
  Args:
    config (dict): The configuration dictionary to redact.
  Returns:
    str: A JSON string representation with sensitive values redacted.
  Notes:
    Redacts keys: api_key, connection_string, container_name, organization. If a sensitive key's value is None, that key is omitted from the resulting JSON.

- redact_dict(config: dict) -&gt; dict
  Redact sensitive values in a dictionary.
  Args:
    config (dict): The configuration dictionary to redact.
  Returns:
    dict: A new dictionary with sensitive keys redacted. Keys in &#123;"api_key", "connection_string", "container_name", "organization"&#125; will have their values replaced with "==== REDACTED ====" when not None. Nested dictionaries and lists are processed recursively.

## Functions

- [`dir_exist`](../api/functions/graphrag-utils-cli-dir-exist)
- [`file_exist`](../api/functions/graphrag-utils-cli-file-exist)
- [`redact`](../api/functions/graphrag-utils-cli-redact)
- [`redact_dict`](../api/functions/graphrag-utils-cli-redact-dict)

