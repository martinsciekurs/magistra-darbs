"""Resolve function calls to their definitions."""

from dataclasses import dataclass, field
from .builtins import PYTHON_BUILTINS, is_stdlib_module


@dataclass
class ResolvedCall:
    target: str
    type: str  # builtin | stdlib | internal | external | ambiguous | unresolved
    candidates: list[str] = field(default_factory=list)


def build_import_map(imports: list[dict], codebase_files: set[str]) -> dict[str, str]:
    """Convert file's imports into lookup: local_name -> resolved_source."""
    import_map = {}
    
    # Build set of codebase modules (files and packages)
    codebase_modules = set()
    for f in codebase_files:
        # Add file as module: "repo_fetcher.py" -> "repo_fetcher"
        if f.endswith('.py'):
            codebase_modules.add(f[:-3].replace('/', '.'))
        # Add parent directories as packages: "analyzer/core.py" -> "analyzer"
        parts = f.split('/')
        for i in range(len(parts) - 1):
            codebase_modules.add('.'.join(parts[:i+1]))

    for imp in imports:
        module = imp["module"]
        name = imp.get("name")
        alias = imp.get("alias")

        if name:
            # from X import Y [as Z]
            local_name = alias or name
            if module in codebase_modules or module.replace('.', '/') + '.py' in codebase_files:
                # Internal import
                possible_file = f"{module.replace('.', '/')}.py"
                if possible_file in codebase_files:
                    import_map[local_name] = f"{possible_file}::{name}"
                else:
                    # Package import (e.g., from analyzer import CodeParser)
                    import_map[local_name] = f"{module}::{name}"
            else:
                import_map[local_name] = f"{module}::{name}"
        else:
            # import X [as Z]
            local_name = alias or module.split('.')[0]
            import_map[local_name] = module

    return import_map


def is_internal_module(module: str, codebase_files: set[str]) -> bool:
    """Check if a module is part of the codebase."""
    # Build codebase modules
    codebase_modules = set()
    for f in codebase_files:
        if f.endswith('.py'):
            codebase_modules.add(f[:-3].replace('/', '.'))
        parts = f.split('/')
        for i in range(len(parts) - 1):
            codebase_modules.add('.'.join(parts[:i+1]))
    
    return module in codebase_modules or module.split('.')[0] in codebase_modules


def resolve_call(
    call_name: str,
    calling_file: str,
    import_map: dict[str, str],
    symbol_registry: dict[str, list[str]],
    file_local_symbols: set[str],
    codebase_files: set[str],
) -> ResolvedCall:
    """Resolve a function call to its definition."""

    # Handle qualified calls: obj.method or module.func
    if "." in call_name:
        return _resolve_qualified_call(call_name, import_map, codebase_files, calling_file, file_local_symbols)

    # 1. Python builtin?
    if call_name in PYTHON_BUILTINS:
        return ResolvedCall(target=call_name, type="builtin")

    # 2. Explicitly imported?
    if call_name in import_map:
        source = import_map[call_name]
        module_root = source.split("::")[0].split(".")[0]
        
        # Check if internal (file path or internal module)
        if ".py::" in source or is_internal_module(module_root, codebase_files):
            return ResolvedCall(target=source, type="internal")
        # Check if stdlib
        if is_stdlib_module(module_root):
            return ResolvedCall(target=source, type="stdlib")
        return ResolvedCall(target=source, type="external")

    # 3. Defined in same file?
    if call_name in file_local_symbols:
        return ResolvedCall(target=f"{calling_file}::{call_name}", type="internal")

    # 4. Unique match in codebase?
    if call_name in symbol_registry:
        matches = symbol_registry[call_name]
        if len(matches) == 1:
            return ResolvedCall(target=matches[0], type="internal")
        return ResolvedCall(target=call_name, type="ambiguous", candidates=matches)

    # 5. Unresolved
    return ResolvedCall(target=call_name, type="unresolved")


def _resolve_qualified_call(
    call_name: str,
    import_map: dict[str, str],
    codebase_files: set[str],
    calling_file: str = "",
    file_local_symbols: set[str] | None = None,
) -> ResolvedCall:
    """Resolve qualified calls like module.func or obj.method."""
    parts = call_name.split(".")
    receiver = parts[0]
    method = ".".join(parts[1:])

    # self.method -> resolve to same-file method if it exists there
    if receiver == "self":
        # Extract immediate method name (self.foo or self.foo.bar -> foo)
        immediate_method = parts[1] if len(parts) > 1 else ""
        if file_local_symbols and immediate_method in file_local_symbols:
            return ResolvedCall(target=f"{calling_file}::{immediate_method}", type="internal")
        return ResolvedCall(target=call_name, type="instance")

    # Check if receiver is an imported module
    if receiver in import_map:
        module = import_map[receiver]
        target = f"{module}::{method}"
        module_root = module.split(".")[0]

        # Check if internal module
        if is_internal_module(module_root, codebase_files):
            return ResolvedCall(target=target, type="internal")
        # Check if stdlib
        if is_stdlib_module(module_root):
            return ResolvedCall(target=target, type="stdlib")
        return ResolvedCall(target=target, type="external")

    # Unknown receiver (local variable, etc.)
    return ResolvedCall(target=call_name, type="unresolved")
