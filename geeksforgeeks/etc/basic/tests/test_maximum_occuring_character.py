import pytest

from geeksforgeeks.etc.basic.maximum_occuring_character import maximum_occuring_character


@pytest.mark.parametrize("test_input, expected", [("testsample", "e"), ("output", "t"), ("geeksforgeeks", "e")])
def test_maximum_occuring_character(test_input, expected):
    # given
    # when
    actual = maximum_occuring_character(test_input)
    # then
    assert actual == expected
