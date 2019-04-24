import pytest

from geeksforgeeks.data_structure.array.school.average import average


@pytest.mark.parametrize("test_input, expected", [([10, 20, 30, 40, 50], [10, 15, 20, 25, 30]), ([12, 2], [12, 7])])
def test_average(test_input, expected):
    # given
    # when
    actual = average(test_input)
    # then
    assert actual == expected
