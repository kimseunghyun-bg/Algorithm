import pytest

from geeksforgeeks.data_structure.array.school.print_elements_of_array import print_elements_of_array


@pytest.mark.parametrize("test_input, expected", [([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])])
def test_print_elements_of_array(test_input, expected):
    # given
    # when
    actual = print_elements_of_array(test_input)
    # then
    assert actual == expected
