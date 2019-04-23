import pytest

from geeksforgeeks.data_structure.array.school.display_longest_name import display_longest_name


@pytest.mark.parametrize("test_input, expected",
                         [(["Geek", "Geeks", "Geeksfor", "GeeksforGeek", "GeeksforGeeks"], "GeeksforGeeks"),(
                          ["Harsh", "Gaurav", "GauravMiglani", "HarshAgarwal", "GeeksforGeeksGeeks"],
                          "GeeksforGeeksGeeks")])
def test_display_longest_name(test_input, expected):
    # given
    # when
    actual = display_longest_name(test_input)
    # then
    assert actual == expected
