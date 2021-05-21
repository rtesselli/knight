import string
from pydantic import BaseModel, validator
from typing import Text, Union, TypeVar


class ChessCoordinate(BaseModel):
    """
    A chess coordinate, e.g. C2.
    """
    letter: Text
    number: int

    @validator("letter")
    def valid_letter(cls, letter: Text) -> Text:
        if letter.upper() not in string.ascii_uppercase:
            raise ValueError(f"Letter {letter} is not valid")
        return letter

    @validator("number")
    def valid_number(cls, number: Union[Text, int]) -> int:
        number = int(number)
        if number <= 0:
            raise ValueError(f"Number {number} is not valid")
        return number


class Statement(BaseModel):
    """
    Problem statement, e.g. D4 G7
    """
    start: ChessCoordinate
    end: ChessCoordinate


# Generic type, needed to define generic functions/classes
T = TypeVar('T')
