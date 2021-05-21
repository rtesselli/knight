import sys
from knight import data_model
from typing import Iterable, Text


def parse_coordinate(element: Text) -> data_model.ChessCoordinate:
    if len(element) != 2:
        raise ValueError(f"Element {element} is not 2-char long")
    letter, number = element
    return data_model.ChessCoordinate(letter=letter.upper(), number=number)


def parse_line(line: Text) -> data_model.Statement:
    elements = line.strip().split()
    if len(elements) != 2:
        raise ValueError(f"Line {line} is ill-formed")
    return data_model.Statement(start=parse_coordinate(elements[0]), end=parse_coordinate(elements[1]))


def parse_input() -> Iterable[data_model.Statement]:
    return (parse_line(line) for line in sys.stdin.readlines())
