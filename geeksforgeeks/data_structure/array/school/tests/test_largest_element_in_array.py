import pytest

from geeksforgeeks.data_structure.array.school.largest_element_in_array import largest_element_in_array


@pytest.mark.parametrize("test_input,expected", [([10, 324, 45, 90, 9808], 9808), ([1, 2, 0, 3, 2, 4, 5], 5)])
def test_largest_element_in_array(test_input, expected):
    # given
    # when
    actual = largest_element_in_array(test_input)
    # then
    assert actual == expected
