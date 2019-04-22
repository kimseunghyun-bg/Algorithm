import pytest

from geeksforgeeks.data_structure.array.school.count_of_smaller_elements import count_of_smaller


@pytest.mark.parametrize("test_input_arr, test_input_number, expected",
                         [([1, 2, 4, 5, 8, 10], 9, 5), ([1, 2, 2, 2, 5, 7, 9], 2, 4), ([1, 2, 2, 3], 5, 4)])
def test_index_of_smaller(test_input_arr, test_input_number, expected):
    # given
    # when
    actual = count_of_smaller(test_input_arr, test_input_number)
    # then
    assert actual == expected
