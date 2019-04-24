import pytest

from geeksforgeeks.data_structure.array.school.multiply_array import multiply_array


@pytest.mark.parametrize("test_input, expected", [([1, 2, 3, 4, 5], 120), ([5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 9765625)])
def test_multiply_array(test_input, expected):
    # given
    # when
    actual = multiply_array(test_input)
    # then
    assert actual == expected
