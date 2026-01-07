---
sidebar_position: 12
---

# graphrag/cli/initialize.py

## Overview

GraphRag CLI initialization utilities.

Purpose:
Module that provides the CLI entry point functionality to initialize a GraphRag project at a given filesystem path by creating initial configuration files and preparing prompt templates.

Key exports:
- initialize_project_at(path: Path, force: bool) -&gt; None: Initialize the project at the given path.

Summary:
The module uses INIT_DOTENV and INIT_YAML to set up initial configuration and references a suite of prompt templates to bootstrap components such as community reports, claims extraction, graph extraction, summarization, and various search system prompts.

Args:
- path: The path at which to initialize the project.
- force: Whether to force initialization even if the project already exists.

Returns:
None

Raises:
- ValueError: If the project already exists and force is False.

## Functions

- [`initialize_project_at`](../api/functions/graphrag-cli-initialize-initialize-project-at)

