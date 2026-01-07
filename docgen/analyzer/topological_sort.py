"""Topological sorting of functions for documentation order."""

from collections import deque


def topological_sort(extracted_code_elements: list[dict]) -> list[dict]:
    """
    Sort functions topologically based on call graph.
    Dependencies come first.
    
    Args:
        extracted_code_elements: List of file dicts with 'functions' containing 'node_id' and 'calls'
        
    Returns:
        List of function dicts in documentation order
    """
    # Build adjancency list: target -> [callers] (reverse graph for Kahn's algo?)
    # For documentation order: we want dependencies documented BEFORE the function that uses them.
    # So if A calls B, B should come before A.
    # This means B must be processed first.
    # This is a standard topological sort where edges are dependency -> dependent.
    # Edge: B -> A (because A depends on B)
    
    graph = {}
    in_degree = {}
    all_nodes = set()
    node_data = {}
    
    # Initialize graph
    for extracted_element in extracted_code_elements:
        for func in extracted_element["functions"]:
            node_id = func["node_id"]
            all_nodes.add(node_id)
            if node_id not in graph:
                graph[node_id] = []
                in_degree[node_id] = 0
            node_data[node_id] = func
    
    # Build edges
    for extracted_element in extracted_code_elements:
        for func in extracted_element["functions"]:
            dependent_id = func["node_id"]  # This function depends on others
            
            for call in func.get("calls", []):
                if call["type"] == "internal":
                    dependency_id = call["target"]
                    
                    # If dependency is in our graph (might be filtered out or in another module)
                    if dependency_id in all_nodes:
                        # Edge: dependency -> dependent
                        graph[dependency_id].append(dependent_id)
                        in_degree[dependent_id] += 1

    # Kahn's Algorithm
    queue = deque([node for node in all_nodes if in_degree[node] == 0])
    sorted_nodes = []
    
    while queue:
        u = queue.popleft()
        sorted_nodes.append(u)
        
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    # Check for cycles (remaining nodes with in_degree > 0)
    cycle_nodes = [node for node in all_nodes if in_degree[node] > 0]
    
    # Append cycle nodes at the end (breaking cycles arbitrarily for docs)
    # We sort them to have deterministic output
    sorted_nodes.extend(sorted(cycle_nodes))
    
    # Format output
    result = []
    for node_id in sorted_nodes:
        func = node_data[node_id]
        deps = []
        for call in func.get("calls", []):
            if call["type"] == "internal":
                deps.append(call["target"])
                
        result.append({
            "node_id": node_id,
            "dependencies": sorted(list(set(deps)))
        })
        
    return result


def get_documentation_order(extracted_code_elements: list[dict]) -> list[dict]:
    """
    Get the order in which functions should be documented.
    
    Args:
        extracted_code_elements: Output from node extraction with resolved dependencies
        
    Returns:
        List of dicts with 'node_id' and 'dependencies'
    """
    return topological_sort(extracted_code_elements)
