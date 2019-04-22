import pytest

from geeksforgeeks.data_structure.array.school.palin_array import is_palindromic_array
from geeksforgeeks.data_structure.array.school.palin_array import is_palindromic_number


@pytest.mark.parametrize("test_input,expected",
                         [([111, 222, 333, 444, 555], True), ([121, 131, 20], False)])
def test_is_palindromic_array(test_input, expected):
    # given
    # when
    actual = is_palindromic_array(test_input)
    # given
    assert actual == expected


@pytest.mark.parametrize("test_input,expected", [(111, True), (121, True), (20, False), (24642, True)])
def test_is_palindromic_number(test_input, expected):
    # given
    # when
    actual = is_palindromic_number(test_input)
    # then
    assert actual == expected
