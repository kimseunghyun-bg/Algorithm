import pytest

from geeksforgeeks.data_structure.array.school.sum_of_array import sum_of_array


@pytest.mark.parametrize("test_input,expected", [([1, 2, 3, 4], 10), ([1, 2, 3, 4, 5], 15)])
def test_sum_of_array(test_input, expected):
    # given
    # when
    actual = sum_of_array(test_input)
    # then
    assert actual == expected
