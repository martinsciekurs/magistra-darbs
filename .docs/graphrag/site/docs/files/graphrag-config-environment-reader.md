---
sidebar_position: 19
---

# graphrag/config/environment_reader.py

## Overview

Module to read configuration values by combining a per-context stack of configuration sections with environment variables via an Env instance.

This module defines EnvironmentReader, which uses an Env instance to access environment values and maintains a private _config_stack to support context-based reads. Reads resolve keys against the current top-most section on the stack, and if not found, fall back to environment values via an internal helper.

Public exports:
- EnvironmentReader class: Reads configuration values by combining a per-context stack of configuration sections with environment variables. The EnvironmentReader uses an Env instance to access environment values and maintains a private _config_stack to support context-based reads.
- Type aliases: T, KeyValue, EnvKeySet
- Internal helpers: _read_env (self, env_key: str | list[str], default_value: T, read: Callable[[str, T], T]) -&gt; T | None

Key methods:
- __init__(self, env: Env)
- config_context()
- section()
- use(value: Any | None)
- env()
- envvar_prefix(prefix: KeyValue)
- str(self, key: KeyValue, env_key: EnvKeySet | None = None, default_value: str | None = None) -&gt; str | None
- int(self, key: KeyValue, env_key: EnvKeySet | None = None, default_value: int | None = None) -&gt; int | None
- bool(self, key: KeyValue, env_key: EnvKeySet | None = None, default_value: bool | None = None) -&gt; bool | None
- float(self, key: KeyValue, env_key: EnvKeySet | None = None, default_value: float | None = None) -&gt; float | None
- list(self, key: KeyValue, env_key: EnvKeySet | None = None, default_value: list | None = None) -&gt; list | None

Brief summary:
This module provides a configurable reader that merges context-based sections with environment values to resolve configuration keys in a predictable, layered manner.

## Classes

- [`EnvironmentReader`](../api/classes/graphrag-config-environment-reader-environmentreader)

## Functions

- [`_read_env`](../api/functions/graphrag-config-environment-reader-read-env)
- [`__init__`](../api/functions/graphrag-config-environment-reader-init)
- [`config_context`](../api/functions/graphrag-config-environment-reader-config-context)
- [`read_key`](../api/functions/graphrag-config-environment-reader-read-key)
- [`section`](../api/functions/graphrag-config-environment-reader-section)
- [`use`](../api/functions/graphrag-config-environment-reader-use)
- [`env`](../api/functions/graphrag-config-environment-reader-env)
- [`envvar_prefix`](../api/functions/graphrag-config-environment-reader-envvar-prefix)
- [`str`](../api/functions/graphrag-config-environment-reader-str)
- [`int`](../api/functions/graphrag-config-environment-reader-int)
- [`bool`](../api/functions/graphrag-config-environment-reader-bool)
- [`float`](../api/functions/graphrag-config-environment-reader-float)
- [`list`](../api/functions/graphrag-config-environment-reader-list)

