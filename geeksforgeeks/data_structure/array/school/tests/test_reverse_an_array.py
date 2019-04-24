import pytest

from geeksforgeeks.data_structure.array.school.reverse_an_array import reverse_an_array


@pytest.mark.parametrize("test_input,expected",
                         [([1, 2, 3, 4], [4, 3, 2, 1]), ([6, 5, 4, 3, 1, 2], [2, 1, 3, 4, 5, 6])])
def test_reverse_an_array(test_input, expected):
    # given
    # when
    actual = reverse_an_array(test_input)
    # then
    assert actual == expected
