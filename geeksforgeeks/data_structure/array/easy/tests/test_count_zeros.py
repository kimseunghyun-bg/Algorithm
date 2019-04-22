import pytest

from geeksforgeeks.data_structure.array.easy.count_zeros import count_zeros


@pytest.mark.parametrize("test_input, expected",
                         [([1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], 3), ([0, 0, 0, 0, 0], 5), ([1, 1, 1, 1, 1, 1], 0)])
def test_count_zeros(test_input, expected):
    # given
    # when
    actual = count_zeros(test_input)
    # then
    assert actual == expected
