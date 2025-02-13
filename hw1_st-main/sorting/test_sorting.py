import pytest

from sorting_student import main


sorting_testcases = [
    ("Inputs/sorting01.txt", [99, 55, 48, 46, 39, 22, 13, 10]),
    ("Inputs/sorting02.txt", [875, 777, 534, 96, 13, None, None, None, None, None]),
    ("Inputs/sorting03.txt", [None, None, None, None, None]),
]


@pytest.mark.parametrize("filename, output", sorting_testcases)
def test_sorting(filename, output):
    assert main(filename) == output
