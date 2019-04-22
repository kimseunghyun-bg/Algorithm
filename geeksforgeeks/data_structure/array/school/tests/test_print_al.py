import pytest

from geeksforgeeks.data_structure.array.school.print_al import get_alternate_order


@pytest.mark.parametrize("test_input,expected", [([1, 2, 3, 4], [1, 3]), ([1, 2, 3, 4, 5], [1, 3, 5])])
def test_get_alternate_order(test_input, expected):
    # given
    # when
    actual = get_alternate_order(test_input)
    # then
    assert actual == expected

