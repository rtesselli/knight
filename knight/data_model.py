import string
from pydantic import BaseModel, validator
from typing import Text, Union, TypeVar, NamedTuple


class HashableModel(BaseModel):
    """
    This custom class is needed to make pydantic.BaseModel hashable
    """
    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))


class ChessCoordinate(HashableModel):
    """
    A chess coordinate, e.g. C2.
    Pydantic BaseClass is not hashable, we need hashing to use this class with sets
    """
    letter: Text
    number: int

    @validator("letter")
    def valid_letter(cls, letter: Text) -> Text:
        if letter.upper() not in string.ascii_uppercase:
            raise ValueError(f"Letter {letter} is not valid")
        return letter.upper()

    @validator("number")
    def valid_number(cls, number: Union[Text, int]) -> int:
        number = int(number)
        if number <= 0:
            raise ValueError(f"Number {number} is not valid")
        return number

    def __str__(self):
        return f"{self.letter}{self.number}"


class Statement(BaseModel):
    """
    Problem statement, e.g. D4 G7
    """
    start: ChessCoordinate
    end: ChessCoordinate


# Generic type, needed to define generic functions/classes
T = TypeVar('T')


class Pair(NamedTuple):
    """
    A generic pair of values of same type
    """
    a: T
    b: T
