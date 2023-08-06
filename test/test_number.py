# File: tests/test_find_largest_element.py


import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main import find_largest_element, calculate_average


def test_find_largest_element_empty_list():
    result = find_largest_element([])
    assert result is None


def test_find_largest_element_single_element():
    result = find_largest_element([5])
    assert result == 5


def test_find_largest_element_multiple_elements():
    result = find_largest_element([2, 4, 6, 8, 10])
    assert result == 10


def test_find_largest_element_negative_elements():
    result = find_largest_element([-1, -2, -3, -4, -5])
    assert result == -1


def test_calculate_average_empty_list():
    result = calculate_average([])
    assert result == 0


def test_calculate_average_single_element():
    result = calculate_average([5])
    assert result == 5


def test_calculate_average_multiple_elements():
    result = calculate_average([2, 4, 6, 8, 10])
    assert result == 6.0


def test_calculate_average_negative_elements():
    result = calculate_average([-1, -2, -3, -4, -5])
    assert result == -3.0
