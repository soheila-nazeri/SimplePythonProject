# File: test/test_main.py
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import hello_world


def test_hello_world():
    result = hello_world()
    assert result == "Hello, World!"
