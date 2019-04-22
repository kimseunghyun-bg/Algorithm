import pytest

from geeksforgeeks.data_structure.array.school.at_least_two_greater_elements import remove_two_greater


@pytest.mark.parametrize("test_input,expected", [([2, 8, 7, 1, 5], [1, 2, 5]), ([7, -2, 3, 4, 9, -1], [-2, -1, 3, 4])])
def test_remove_two_greater(test_input, expected):
    # given
    # when
    actual = remove_two_greater(test_input)
    # then
    assert actual == expected
