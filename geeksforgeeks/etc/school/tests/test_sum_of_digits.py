import pytest

from geeksforgeeks.etc.school.sum_of_digits import sum_of_digits


@pytest.mark.parametrize("test_input, expected", [(123, 6), ("45", 9)])
def test_sum_of_digits(test_input, expected):
    # given
    # when
    actual = sum_of_digits(test_input)
    # then
    assert actual == expected
