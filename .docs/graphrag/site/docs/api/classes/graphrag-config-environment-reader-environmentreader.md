---
sidebar_position: 40
---

# EnvironmentReader

**File:** `graphrag/config/environment_reader.py`

## Overview

Reads configuration values by combining a per-context stack of configuration sections with environment variables. The EnvironmentReader uses an Env instance to access environment values and maintains a private _config_stack to support context-based reads. Reads resolve keys against the current top-most section on the stack, and if not found, fall back to environment values via an internal helper. Context managers can push a new section onto the stack for the duration of a with-block to scope reads.

Args:
    env (Env): Environment instance used to read configuration values.

Attributes:
    env (Env): The environment instance used to read configuration values.
    _config_stack (list): Internal stack that stores configuration sections for the duration of a read context.

Notes:
    - The private helper _read_env is used to fetch values from the environment.
    - Keys are normalized to strings via internal mechanisms before lookup.
    - Context management affects subsequent reads within the with-block by extending the active configuration.
    - Typical return values are strings, integers, booleans, floats, lists, or None when a value cannot be found.

Raises:
    - TypeError, ValueError: if arguments have invalid types or the read context is misused.
    - Exceptions from the underlying Env reads may be raised as encountered.

Public API overview:
    _read_env(env_key, default_value, read) -&gt; T | None
    __init__(self, env) -&gt; None
    config_context() -&gt; contextmanager
    section() -&gt; dict
    use(value) -&gt; contextmanager
    env() -&gt; Env
    envvar_prefix(prefix) -&gt; None
    str(key, env_key=None, default_value=None) -&gt; str | None
    int(key, env_key=None, default_value=None) -&gt; int | None
    bool(key, env_key=None, default_value=None) -&gt; bool | None
    float(key, env_key=None, default_value=None) -&gt; float | None
    list(key, env_key=None, default_value=None) -&gt; list | None

## Methods

### `_read_env`

```python
def _read_env(
        self, env_key: str | list[str], default_value: T, read: Callable[[str, T], T]
    ) -> T | None
```

### `__init__`

```python
def __init__(self, env: Env)
```

### `config_context`

```python
def config_context()
```

### `section`

```python
def section(self) -> dict
```

### `use`

```python
def use(self, value: Any | None)
```

### `env`

```python
def env(self)
```

### `envvar_prefix`

```python
def envvar_prefix(self, prefix: KeyValue)
```

### `str`

```python
def str(
        self,
        key: KeyValue,
        env_key: EnvKeySet | None = None,
        default_value: str | None = None,
    ) -> str | None
```

### `int`

```python
def int(
        self,
        key: KeyValue,
        env_key: EnvKeySet | None = None,
        default_value: int | None = None,
    ) -> int | None
```

### `bool`

```python
def bool(
        self,
        key: KeyValue,
        env_key: EnvKeySet | None = None,
        default_value: bool | None = None,
    ) -> bool | None
```

### `float`

```python
def float(
        self,
        key: KeyValue,
        env_key: EnvKeySet | None = None,
        default_value: float | None = None,
    ) -> float | None
```

### `list`

```python
def list(
        self,
        key: KeyValue,
        env_key: EnvKeySet | None = None,
        default_value: list | None = None,
    ) -> list | None
```

