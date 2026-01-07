"""Dependency analysis with resolved call graph."""

from .call_resolver import build_import_map, resolve_call


def build_symbol_registry(extracted_code_elements: list[dict]) -> dict[str, list[str]]:
    """Build registry mapping function names to all their node_ids."""
    registry = {}
    for extracted_element in extracted_code_elements:
        for func in extracted_element["functions"]:
            name = func["name"]
            node_id = func["node_id"]
            if name not in registry:
                registry[name] = []
            registry[name].append(node_id)
    return registry


def add_call_dependencies(extracted_code_elements: list[dict]) -> list[dict]:
    """Resolve all calls and add bidirectional called_by links."""
    codebase_files = {f["file_name"] for f in extracted_code_elements}
    symbol_registry = build_symbol_registry(extracted_code_elements)

    # Resolve calls for each file
    for extracted_element in extracted_code_elements:
        file_name = extracted_element["file_name"]
        import_map = build_import_map(extracted_element.get("imports", []), codebase_files)
        file_local_symbols = {f["name"] for f in extracted_element["functions"]}

        for func in extracted_element["functions"]:
            resolved_calls = []
            for call_name in func.get("calls", []):
                resolved = resolve_call(
                    call_name, file_name, import_map, symbol_registry, file_local_symbols, codebase_files,
                )
                call_dict = {"target": resolved.target, "type": resolved.type}
                if resolved.candidates:
                    call_dict["candidates"] = resolved.candidates
                resolved_calls.append(call_dict)
            func["calls"] = resolved_calls

    # Build called_by (reverse lookup for internal calls)
    called_by_map: dict[str, list[str]] = {}
    for extracted_element in extracted_code_elements:
        for func in extracted_element["functions"]:
            caller_id = func["node_id"]
            for call in func["calls"]:
                if call["type"] == "internal":
                    target = call["target"]
                    if target not in called_by_map:
                        called_by_map[target] = []
                    if caller_id not in called_by_map[target]:
                        called_by_map[target].append(caller_id)

    # Add called_by to each function
    for extracted_element in extracted_code_elements:
        for func in extracted_element["functions"]:
            callers = called_by_map.get(func["node_id"], [])
            func["called_by"] = [{"source": c, "type": "internal"} for c in callers]

    return extracted_code_elements
