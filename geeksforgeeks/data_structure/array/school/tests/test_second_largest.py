import pytest

from geeksforgeeks.data_structure.array.school.second_largest import second_largest


@pytest.mark.parametrize("test_input,expected", [([89, 24, 75, 11, 23], 75), ([56, 42, 21, 23, 65, 20], 56)])
def test_second_largest(test_input, expected):
    # given
    # when
    actual = second_largest(test_input)
    # then
    assert actual == expected
