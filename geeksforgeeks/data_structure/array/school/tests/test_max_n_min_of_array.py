import pytest

from geeksforgeeks.data_structure.array.school.max_n_min_of_array import max_n_min_of_array


@pytest.mark.parametrize("test_input,expected", [([5, 4, 2, 1], [5, 1]), ([8], [8, 8])])
def test_max_n_min_of_array(test_input, expected):
    # given
    # when
    actual = max_n_min_of_array(test_input)
    # then
    assert actual == expected
