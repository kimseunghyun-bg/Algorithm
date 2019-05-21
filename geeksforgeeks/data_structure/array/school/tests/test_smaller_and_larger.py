import pytest

from geeksforgeeks.data_structure.array.school.smaller_and_larger import smaller_and_larger


@pytest.mark.parametrize("test_arr, test_num, expected", [([1, 2, 8, 10, 11, 12, 19], 0, [0, 7]), 
                                                          ([1, 2, 8, 10, 11, 12, 19], 5, [2, 5]),
                                                          ([1, 2, 8, 10, 11, 12, 19], 10, [4, 4])])
def test_smaller_and_larger(test_arr, test_num, expected):
    # given
    # when
    actual = smaller_and_larger(test_arr, test_num)
    # then
    assert actual == expected
