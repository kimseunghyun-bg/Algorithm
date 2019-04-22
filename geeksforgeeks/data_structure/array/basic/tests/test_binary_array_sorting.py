import pytest

from geeksforgeeks.data_structure.array.basic.binary_array_sorting import binary_array_sorting


@pytest.mark.parametrize("test_input, expected", [([1, 0, 1, 1, 0], [0, 0, 1, 1, 1]),
                                                  ([1, 0, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1, 1, 1])])
def test_binary_array_sorting(test_input, expected):
    # given
    # when
    actual = binary_array_sorting(test_input)
    # then
    assert actual == expected
