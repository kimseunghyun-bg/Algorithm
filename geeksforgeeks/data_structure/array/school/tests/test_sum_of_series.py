import pytest

from geeksforgeeks.data_structure.array.school.sum_of_series import sum_of_series


@pytest.mark.parametrize("test_input,expected", [(1, 1), (5, 15)])
def test_sum_of_series(test_input, expected):
    # given
    # when
    actual = sum_of_series(test_input)
    # then
    assert actual == expected
