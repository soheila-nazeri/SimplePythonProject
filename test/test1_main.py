from ..main import calculate_average


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
