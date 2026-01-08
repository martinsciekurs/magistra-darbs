"""Tests for the code parser module."""

import pytest
from docgen.analyzer.code_parser import CodeParser


class TestCodeParser:
    """Test code parsing for Python."""

    @pytest.fixture
    def parser(self):
        """Create a Python parser."""
        return CodeParser("python")

    def test_parse_simple_function(self, parser):
        """Parse a simple function with no arguments."""
        code = '''
def hello():
    """Say hello."""
    print("hello")
'''
        result = parser.parse_file(code, "test.py")
        
        assert "functions" in result
        assert len(result["functions"]) == 1
        
        func = result["functions"][0]
        assert func["name"] == "hello"
        assert "test.py::hello" == func["node_id"]

    def test_parse_function_with_args(self, parser):
        """Parse function with typed arguments."""
        code = '''
def greet(name: str, count: int = 1) -> str:
    """Greet someone."""
    return f"Hello {name}" * count
'''
        result = parser.parse_file(code, "test.py")
        
        func = result["functions"][0]
        assert func["name"] == "greet"
        assert "name" in func["signature"]
        assert "str" in func["signature"]

    def test_parse_class_method_node_id(self, parser):
        """Methods should have ClassName.method in node_id."""
        code = '''
class Calculator:
    def add(self, a: int, b: int) -> int:
        return a + b
'''
        result = parser.parse_file(code, "calc.py")
        
        assert len(result["functions"]) == 1
        func = result["functions"][0]
        assert func["name"] == "add"
        # Node ID should include class name
        assert "Calculator.add" in func["node_id"]

    def test_parse_imports(self, parser):
        """Parse import statements."""
        code = '''
import os
from pathlib import Path
from typing import List, Dict

def func():
    pass
'''
        result = parser.parse_file(code, "test.py")
        
        assert "imports" in result
        imports = result["imports"]
        assert len(imports) >= 1
        
        # Check os import
        os_imports = [i for i in imports if i.get("module") == "os"]
        assert len(os_imports) == 1

    def test_parse_function_calls_are_strings(self, parser):
        """Function calls should be a list of strings."""
        code = '''
def caller():
    helper()
    another_func(1, 2)
'''
        result = parser.parse_file(code, "test.py")
        
        func = result["functions"][0]
        calls = func.get("calls", [])
        
        # Calls are stored as strings
        assert isinstance(calls, list)
        if calls:
            assert isinstance(calls[0], str)
        assert "helper" in calls
        assert "another_func" in calls

    def test_empty_file(self, parser):
        """Parse an empty file."""
        result = parser.parse_file("", "empty.py")
        
        assert result["functions"] == []
        assert result["imports"] == []

    def test_function_visibility(self, parser):
        """Test visibility detection based on naming."""
        code = '''
def public_func():
    pass

def _protected_func():
    pass

def __private_func():
    pass
'''
        result = parser.parse_file(code, "test.py")
        
        funcs = {f["name"]: f for f in result["functions"]}
        
        assert funcs["public_func"]["visibility"] == "public"
        assert funcs["_protected_func"]["visibility"] == "protected"
        assert funcs["__private_func"]["visibility"] == "private"

    def test_decorators_extracted(self, parser):
        """Decorators should be captured."""
        code = '''
@property
def name(self):
    return self._name

@staticmethod
def helper():
    pass
'''
        result = parser.parse_file(code, "test.py")
        
        funcs = {f["name"]: f for f in result["functions"]}
        
        assert "@property" in funcs["name"]["decorators"]
        assert "@staticmethod" in funcs["helper"]["decorators"]

    def test_raises_extracted(self, parser):
        """Exception types from raise statements should be captured."""
        code = '''
def risky():
    if bad:
        raise ValueError("oops")
    raise RuntimeError("fail")
'''
        result = parser.parse_file(code, "test.py")
        
        func = result["functions"][0]
        raises = func.get("raises", [])
        
        assert "ValueError" in raises
        assert "RuntimeError" in raises
