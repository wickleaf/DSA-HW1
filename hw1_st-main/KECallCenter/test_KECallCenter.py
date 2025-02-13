import pytest

from KECallCenter import simulate_call_center


KECallCenter_testcases = [
    (
        "inputs/KEComplaints01.txt",
        [
            ("John", "Billing", "A1", 0, 5, 0),
            ("Eve", "Billing", "A2", 1, 5, 0),
            ("Alice", "Technical", "B1", 2, 5, 0),
            ("Charlie", "Technical", "B2", 3, 5, 0),
            ("Bob", "General", "C1", 4, 10, 0),
        ],
    ),
    (
        "inputs/KEComplaints02.txt",
        [
            ("Ahsan", "Billing", "Ali", 0, 3, 0),
            ("Bilal", "Technical", "Usman", 0, 2, 0),
            ("Sara", "General", "Ahmed", 1, 5, 0),
            ("Fahad", "Billing", "Ayesha", 2, 7, 0),
            ("Zain", "Technical", "Sarah", 3, 6, 0),
            ("Zara", "Technical", "John", 3, 9, 0),
            ("Imran", "Billing", "Ali", 4, 6, 0),
            ("Asma", "Technical", "Usman", 5, 6, 0),
            ("Saba", "General", "Ahmed", 5, 9, 3),
            ("Amna", "General", "Ahmed", 9, 12, 3),
        ],
    ),
    (
        "inputs/KEComplaints03.txt",
        [
            ("John", "Technical", "B1", 0, 5, 0),
            ("Alice", "Technical", "B2", 0, 3, 0),
            ("Bob", "Technical", "B2", 3, 7, 0),
            ("Eve", "Technical", "B1", 5, 9, 1),
            ("Charlie", "Technical", "B2", 7, 9, 2),
        ],
    ),
    (
        "inputs/KEComplaints04.txt",
        [
            ("Ahsan", "Billing", "A1", 0, 4, 0),
            ("Bilal", "Technical", "B1", 0, 4, 0),
            ("Sara", "General", "C1", 0, 4, 0),
            ("Farah", "Billing", "A2", 1, 6, 0),
            ("Fahad", "Technical", "B2", 1, 6, 0),
            ("Zara", "Billing", "A3", 4, 7, 0),
            ("Imran", "Technical", "B1", 4, 7, 0),
            ("Zain", "General", "C1", 4, 9, 3),
            ("Asma", "General", "C1", 9, 12, 5),
        ],
    ),
]


@pytest.mark.parametrize("filename, output", KECallCenter_testcases)
def test_alien(filename, output):
    assert simulate_call_center(filename) == output
