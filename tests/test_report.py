"""Automated checks for Activity 2: The Calculation Report."""

import re
from pathlib import Path
from unittest.mock import patch

from main import main

# Chosen so every quotient is short to write out, and so one pair divides
# exactly (7 and 7), which is where % producing 0 is easiest to get wrong.
PAIRS = [(17, 5), (100, 8), (45, 6), (7, 7)]

BANNER = "=" * 34

# Students pick their own separator, so the input string has to match
# whatever they actually wrote. A quoted literal inside .split(...) is that
# separator; a bare .split() splits on whitespace, which a single space
# satisfies too.
_SOURCE = (Path(__file__).parent.parent / "src" / "main.py").read_text()
_SPLIT_CALL = re.search(r"\.split\(\s*(?:([\"'])(.*?)\1\s*)?\)", _SOURCE)
SEPARATOR = _SPLIT_CALL.group(2) if _SPLIT_CALL and _SPLIT_CALL.group(2) is not None else " "


def run_with(first, second, capsys):
    """Run main() once with a single line of input and return what it printed."""
    with patch("builtins.input", side_effect=[f"{first}{SEPARATOR}{second}"]):
        main()
    out, err = capsys.readouterr()
    assert err == ""
    return out


def test_program_runs_and_prints(capsys):
    out = run_with(17, 5, capsys)
    # An untouched starter runs cleanly but prints nothing at all, so a check
    # on stderr alone would pass against a file still full of TODO markers.
    assert out.strip() != ""


def test_report_lines_are_correct(capsys):
    for first, second in PAIRS:
        out = run_with(first, second, capsys)
        # Expected text is built with the same arithmetic the student writes,
        # so float formatting matches whatever Python itself produces rather
        # than a number spelled out here by hand.
        for line in [
            f"{first} + {second} = {first + second}",
            f"{first} - {second} = {first - second}",
            f"{first} * {second} = {first * second}",
            f"{first} / {second} = {first / second}",
            f"{first} % {second} = {first % second}",
        ]:
            assert line in out


def test_title_and_repeated_lines(capsys):
    out = run_with(17, 5, capsys)
    assert "CALCULATION REPORT: 17 and 5" in out
    assert BANNER in out
