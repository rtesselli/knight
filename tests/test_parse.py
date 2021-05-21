import pytest
import string
from knight.parse import parse_coordinate, parse_line, parse_input
from knight.data_model import ChessCoordinate, Statement


def test_parse_coordinate():
    for letter in string.ascii_lowercase[:8] + string.ascii_uppercase[:8]:
        for number in range(1, 9):
            assert parse_coordinate(f"{letter}{number}") == ChessCoordinate(letter=letter.upper(), number=number)
    with pytest.raises(ValueError):
        parse_coordinate("I1")
    with pytest.raises(ValueError):
        parse_coordinate("A0")
    with pytest.raises(ValueError):
        parse_coordinate("ABC")
    with pytest.raises(ValueError):
        parse_coordinate("A")


def test_parse_line():
    assert parse_line("A1 B2") == Statement(
        start=ChessCoordinate(letter='A', number=1),
        end=ChessCoordinate(letter='B', number=2)
    )
    with pytest.raises(ValueError):
        parse_line("A1")

    with pytest.raises(ValueError):
        parse_line("A1 A1 A1")


def test_parse_input(monkeypatch):
    monkeypatch.setattr('sys.stdin.readlines', lambda: ["A1 B1", "C2  D4"])
    assert list(parse_input()) == [
        Statement(
            start=ChessCoordinate(letter='A', number=1),
            end=ChessCoordinate(letter='B', number=1)
        ),
        Statement(
            start=ChessCoordinate(letter='C', number=2),
            end=ChessCoordinate(letter='D', number=4)
        )
    ]
