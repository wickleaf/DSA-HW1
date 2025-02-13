import pytest
from alien_student import main


alien_testcases = [
    ("inputs/alien01.txt", "Hello World"),
    ("inputs/alien02.txt", "Hi, Hello"),
    ("inputs/alien03.txt", "EnD!Ng"),
]


@pytest.mark.parametrize("filename, output", alien_testcases)
def test_alien(filename, output):
    assert main(filename) == output
