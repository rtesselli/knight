from knight import data_model
from typing import Iterable, Text


def parse_coordinate(element: Text) -> data_model.ChessCoordinate:
    """
    Try to convert a string into a ChessCoordinate
    :param element: token element to parse, e.g. 'A2'
    :return: Typed ChessCoordinate
    """
    if len(element) != 2:
        raise ValueError(f"Element {element} is not 2-char long")
    letter, number = element
    return data_model.ChessCoordinate(letter=letter.upper(), number=number)


def parse_line(line: Text) -> data_model.Statement:
    """
    Try to convert a string representing a text line into a problem statement, e.g. 'A1 C5'
    :param line: String representing a full text line
    :return: Typed Statement
    """
    elements = line.strip().split()
    if len(elements) != 2:
        raise ValueError(f"Line {line} is ill-formed")
    return data_model.Statement(start=parse_coordinate(elements[0]), end=parse_coordinate(elements[1]))


def parse_input(reader: Iterable[Text]) -> Iterable[data_model.Statement]:
    """
    Reads from stdin and parse each line
    :return: Iterable of problem statements
    """
    return (parse_line(line) for line in reader)
