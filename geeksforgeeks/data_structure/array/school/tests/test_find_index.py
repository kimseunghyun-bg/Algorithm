import pytest

from geeksforgeeks.data_structure.array.school.find_index import find_index


@pytest.mark.parametrize("test_input_arr, number, expected",
                         [([1, 2, 3, 4, 5, 5], 5, [4, 5]), ([6, 5, 4, 3, 1, 2], 4, [2, 2])])
def test_find_index(test_input_arr, number, expected):
    # given
    # when
    actual = find_index(test_input_arr, number)
    # then
    assert actual == expected
