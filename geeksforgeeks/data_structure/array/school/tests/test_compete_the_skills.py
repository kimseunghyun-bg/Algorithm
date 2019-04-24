import pytest

from geeksforgeeks.data_structure.array.school.compete_the_skills import compete_the_skills


@pytest.mark.parametrize("test_input_A, test_input_B, expected",
                         [([4, 2, 7], [5, 6, 3], [1, 2]), ([4, 2, 7], [5, 2, 8], [0, 2])])
def test_compete_the_skills(test_input_A, test_input_B, expected):
    # given
    # when
    actual = compete_the_skills(test_input_A, test_input_B)
    # then
    assert actual == expected
