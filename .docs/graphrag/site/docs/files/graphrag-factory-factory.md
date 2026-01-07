---
sidebar_position: 41
---

# graphrag/factory/factory.py

## Overview

Generic per-subclass singleton Factory for registering and creating services by strategy name.

This module defines a generic Factory class that maintains a registry of strategy names to callables returning instances of T. Each subclass uses its own singleton instance, accessible via __new__. The Factory supports registering service initializers, checking registration, listing registered strategies, and creating instances.

Exports:
- Factory: A per-subclass singleton factory that maps strategy names to initializers.
- T: TypeVar representing the produced service type.

Public API
- create(self, *, strategy: str, **kwargs: Any) -&gt; T
  Create a service instance based on the strategy. strategy is the name of the registered strategy; kwargs are passed to the service initializer.
  Returns: T: An instance of T.
  Raises: ValueError: If the strategy is not registered.

- __contains__(self, strategy: str) -&gt; bool
  Returns: bool: True if a strategy is registered, False otherwise.

- __new__(cls, *args: Any, **kwargs: Any) -&gt; "Factory"
  Returns: The per-subclass singleton instance for the class that invokes __new__.

- register(self, *, strategy: str, service_initializer: Callable[..., T]) -&gt; None
  Register a new service factory for a strategy. Stores a factory (callable) under the given strategy name. The factory is not invoked at registration time; it will be called later by create(**kwargs) to produce an instance of T.
  Args:
    strategy (str): The name of the strategy.
    service_initializer (Callable[..., T]): A callable that returns an instance of T.
  Returns: None. If a factory is already registered under the same strategy name, it will be overwritten with the new factory.

- __init__(self)
  Initializes internal state for the Factory singleton instance on first initialization.
  Returns: None
  Raises: None
  Attributes: _services: dict[str, Callable[..., T]] — registry mapping strategy names to callables that return T.

- keys(self) -&gt; list[str]
  Returns: list[str]: A list of the registered strategy names.

## Classes

- [`Factory`](../api/classes/graphrag-factory-factory-factory)

## Functions

- [`create`](../api/functions/graphrag-factory-factory-create)
- [`__contains__`](../api/functions/graphrag-factory-factory-contains)
- [`__new__`](../api/functions/graphrag-factory-factory-new)
- [`register`](../api/functions/graphrag-factory-factory-register)
- [`__init__`](../api/functions/graphrag-factory-factory-init)
- [`keys`](../api/functions/graphrag-factory-factory-keys)

