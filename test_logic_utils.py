import pytest
from logic_utils import parse_guess

@pytest.mark.parametrize(
    "raw,expected",
    [
        ("", (False, None, "Enter a guess.")),
        ("5", (True, 5, None)),
        ("-3", (True, -3, None)),
        ("3.0", (True, 3, None)),
        ("4.9", (True, 4, None)),
        ("-2.7", (True, -2, None)),
        (" 7 ", (True, 7, None)),
        ("abc", (False, None, "That is not a number.")),
        ("3.5.2", (False, None, "That is not a number.")),
        ("five", (False, None, "That is not a number.")),
    ],
)
def test_parse_guess_various(raw, expected):
    assert parse_guess(raw) == expected