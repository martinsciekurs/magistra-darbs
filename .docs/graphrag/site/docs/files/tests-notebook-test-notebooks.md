---
sidebar_position: 245
---

# tests/notebook/test_notebooks.py

## Overview

Module for testing notebook execution using nbconvert.

Purpose and overview
This module runs Jupyter notebooks located under NOTEBOOKS_PATH while excluding EXCLUDED_PATH, by invoking nbconvert and collecting error outputs from executed cells. It provides two main interfaces for testing notebook execution: _notebook_run and test_notebook.

Key exports
- _notebook_run(filepath: Path)
- test_notebook(notebook_path: Path)

Functions
_notebook_run(filepath: Path)
  Args: filepath: Path to the notebook file to execute.
  Returns: list: A list of error outputs collected from the executed notebook cells.
  Raises: subprocess.CalledProcessError: If the nbconvert command fails to execute.

test_notebook(notebook_path: Path)
  Args: notebook_path: Path to the notebook file to test.
  Returns: None
  Raises: subprocess.CalledProcessError: If the nbconvert command fails to execute.

## Functions

- [`_notebook_run`](../api/functions/tests-notebook-test-notebooks-notebook-run)
- [`test_notebook`](../api/functions/tests-notebook-test-notebooks-test-notebook)

