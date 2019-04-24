import pytest

from geeksforgeeks.data_structure.array.school.swap_kth_elements import swap_kth_elements


@pytest.mark.parametrize("test_input_arr, test_input_index,expected",
                         [([1, 2, 3, 4, 5, 6, 7, 8], 3, [1, 2, 6, 4, 5, 3, 7, 8])])
def test_swap_kth_elements(test_input_arr, test_input_index, expected):
    # given
    # when
    actual = swap_kth_elements(test_input_arr, test_input_index)
    # then
    assert actual == expected
