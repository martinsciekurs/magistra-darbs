---
sidebar_position: 232
---

# tests/conftest.py

## Overview

Test configuration for pytest used by the test suite.

This module defines pytest hooks and fixtures required by the test suite. It currently exposes pytest_addoption to register a custom command-line option that controls whether slow tests are executed.

Key exports:
- pytest_addoption(parser): Registers the --run_slow option with the pytest CLI parser.

Brief summary:
Enables selective execution of tests by introducing a --run_slow flag which tests can consult to decide if slow tests should be run.

## Functions

- [`pytest_addoption`](../api/functions/tests-conftest-pytest-addoption)

