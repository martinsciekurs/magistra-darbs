"""Tests for the analyzer module - topological sort."""

import pytest
from docgen.analyzer.topological_sort import topological_sort, get_documentation_order


class TestTopologicalSort:
    """Test the topological sort algorithm with the real API."""

    def test_empty_input(self):
        """Empty input returns empty output."""
        result = topological_sort([])
        assert result == []

    def test_single_function_no_calls(self):
        """Single function with no calls."""
        extracted = [{
            "file_name": "test.py",
            "imports": [],
            "functions": [
                {"node_id": "test.py::func_a", "name": "func_a", "calls": []}
            ]
        }]
        result = topological_sort(extracted)
        assert len(result) == 1
        assert result[0]["node_id"] == "test.py::func_a"

    def test_two_independent_functions(self):
        """Two independent functions (no dependencies)."""
        extracted = [{
            "file_name": "test.py",
            "imports": [],
            "functions": [
                {"node_id": "test.py::func_a", "name": "func_a", "calls": []},
                {"node_id": "test.py::func_b", "name": "func_b", "calls": []},
            ]
        }]
        result = topological_sort(extracted)
        assert len(result) == 2
        node_ids = {r["node_id"] for r in result}
        assert node_ids == {"test.py::func_a", "test.py::func_b"}

    def test_dependency_order(self):
        """A calls B (internal) -> B should come before A."""
        extracted = [{
            "file_name": "test.py",
            "imports": [],
            "functions": [
                {
                    "node_id": "test.py::caller",
                    "name": "caller",
                    "calls": [{"type": "internal", "target": "test.py::helper"}]
                },
                {
                    "node_id": "test.py::helper",
                    "name": "helper",
                    "calls": []
                },
            ]
        }]
        result = topological_sort(extracted)
        node_ids = [r["node_id"] for r in result]
        
        # helper should come before caller
        assert node_ids.index("test.py::helper") < node_ids.index("test.py::caller")

    def test_chain_dependency(self):
        """A -> B -> C: C should come first, then B, then A."""
        extracted = [{
            "file_name": "test.py",
            "imports": [],
            "functions": [
                {
                    "node_id": "test.py::a",
                    "name": "a",
                    "calls": [{"type": "internal", "target": "test.py::b"}]
                },
                {
                    "node_id": "test.py::b",
                    "name": "b",
                    "calls": [{"type": "internal", "target": "test.py::c"}]
                },
                {
                    "node_id": "test.py::c",
                    "name": "c",
                    "calls": []
                },
            ]
        }]
        result = topological_sort(extracted)
        node_ids = [r["node_id"] for r in result]
        
        assert node_ids.index("test.py::c") < node_ids.index("test.py::b")
        assert node_ids.index("test.py::b") < node_ids.index("test.py::a")

    def test_external_calls_ignored(self):
        """External and stdlib calls don't affect ordering."""
        extracted = [{
            "file_name": "test.py",
            "imports": [],
            "functions": [
                {
                    "node_id": "test.py::func",
                    "name": "func",
                    "calls": [
                        {"type": "external", "target": "requests.get"},
                        {"type": "stdlib", "target": "os.path.join"},
                    ]
                },
            ]
        }]
        result = topological_sort(extracted)
        assert len(result) == 1
        assert result[0]["dependencies"] == []

    def test_cycle_handling(self):
        """Cycles should be handled (nodes still included)."""
        extracted = [{
            "file_name": "test.py",
            "imports": [],
            "functions": [
                {
                    "node_id": "test.py::a",
                    "name": "a",
                    "calls": [{"type": "internal", "target": "test.py::b"}]
                },
                {
                    "node_id": "test.py::b",
                    "name": "b",
                    "calls": [{"type": "internal", "target": "test.py::a"}]
                },
            ]
        }]
        result = topological_sort(extracted)
        node_ids = {r["node_id"] for r in result}
        
        # Both should be in result despite cycle
        assert node_ids == {"test.py::a", "test.py::b"}


class TestGetDocumentationOrder:
    """Test get_documentation_order (wraps topological_sort)."""

    def test_empty_extraction(self):
        """Empty extraction returns empty order."""
        result = get_documentation_order([])
        assert result == []

    def test_returns_same_as_topological_sort(self):
        """Should return same result as topological_sort."""
        extracted = [{
            "file_name": "test.py",
            "imports": [],
            "functions": [
                {"node_id": "test.py::func_a", "name": "func_a", "calls": []},
            ]
        }]
        assert get_documentation_order(extracted) == topological_sort(extracted)
