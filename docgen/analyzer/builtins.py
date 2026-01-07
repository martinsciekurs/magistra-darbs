"""Python builtin and stdlib detection."""

import builtins
import sys

# All Python builtin names (functions, types, exceptions)
PYTHON_BUILTINS: set[str] = {
    name for name in dir(builtins) if not name.startswith('_')
}

# Standard library modules (Python 3.10+, with fallback)
STDLIB_MODULES: set[str] = getattr(sys, 'stdlib_module_names', {
    'abc', 'argparse', 'ast', 'asyncio', 'base64', 'collections', 'contextlib',
    'copy', 'dataclasses', 'datetime', 'enum', 'functools', 'hashlib', 'http',
    'importlib', 'io', 'itertools', 'json', 'logging', 'math', 'os', 'pathlib',
    'pickle', 're', 'shutil', 'socket', 'sqlite3', 'subprocess', 'sys',
    'tempfile', 'threading', 'time', 'typing', 'unittest', 'urllib', 'uuid',
    'warnings', 'xml', 'zipfile', 'fnmatch', 'glob', 'csv', 'random', 'secrets',
    'string', 'textwrap', 'struct', 'codecs', 'unicodedata', 'difflib',
    'contextlib', 'decimal', 'fractions', 'numbers', 'cmath', 'statistics',
    'operator', 'weakref', 'types', 'copy', 'pprint', 'reprlib', 'graphlib',
    'heapq', 'bisect', 'array', 'queue', 'shelve', 'dbm', 'platform',
    'errno', 'ctypes', 'select', 'selectors', 'signal', 'mmap', 'email',
    'html', 'ftplib', 'poplib', 'imaplib', 'smtplib', 'telnetlib', 'socketserver',
    'xmlrpc', 'ipaddress', 'cgi', 'cgitb', 'wsgiref', 'webbrowser', 'getpass',
    'netrc', 'uu', 'quopri', 'binascii', 'binhex', 'configparser', 'tomllib',
    'fileinput', 'stat', 'filecmp', 'linecache', 'tokenize', 'tabnanny',
    'pyclbr', 'compileall', 'dis', 'pickletools', 'inspect', 'site',
})


def is_builtin(name: str) -> bool:
    return name in PYTHON_BUILTINS


def is_stdlib_module(module: str) -> bool:
    return module.split('.')[0] in STDLIB_MODULES





