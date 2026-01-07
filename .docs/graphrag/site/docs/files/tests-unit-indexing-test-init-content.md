---
sidebar_position: 256
---

# tests/unit/indexing/test_init_content.py

## Overview

Tests for initialization content handling in GraphRag configuration.

Purpose
- Validate loading and validation of initialization content used by GraphRagConfig, including processing of YAML blocks and uncommenting embedded YAML.

Key exports
- uncomment_line(line: str) -&gt; str: Uncomments a line by removing a leading "# " prefix, preserving indentation.
- test_init_yaml(values: dict[str, Any] | None, root_dir: str | None) -&gt; dict[str, Any]: Load configuration parameters into a plain dictionary suitable for subsequent GraphRagConfig validation.
- test_init_yaml_uncommented() -&gt; None: Test that uncommenting the YAML in INIT_YAML produces a valid GraphRagConfig.
- INIT_YAML: YAML snippet used for tests.

Brief summary
- This module provides unit tests that exercise loading and validation of initialization content for GraphRagConfig, including handling of commented and uncommented YAML blocks.

## Functions

- [`uncomment_line`](../api/functions/tests-unit-indexing-test-init-content-uncomment-line)
- [`test_init_yaml`](../api/functions/tests-unit-indexing-test-init-content-test-init-yaml)
- [`test_init_yaml_uncommented`](../api/functions/tests-unit-indexing-test-init-content-test-init-yaml-uncommented)

