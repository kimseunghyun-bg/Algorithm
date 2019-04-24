import pytest

from geeksforgeeks.data_structure.array.school.print_the_left_element import print_the_left_element


@pytest.mark.parametrize("test_input, expected", [([7, 8, 3, 4, 2, 9, 5], 5), ([8, 1, 2, 9, 4, 3, 7, 5], 4)])
def test_print_the_left_element(test_input, expected):
    # given
    # when
    actual = print_the_left_element(test_input)
    # then
    assert actual == expected
