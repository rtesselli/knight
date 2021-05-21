import string
from pydantic import BaseModel, validator
from typing import Text, Union


class ChessCoordinate(BaseModel):
    letter: Text
    number: int

    @validator("letter")
    def valid_letter(cls, letter: Text) -> Text:
        if letter.upper() not in string.ascii_uppercase[:8]:
            raise ValueError(f"Letter {letter} is not valid")
        return letter

    @validator("number")
    def valid_number(cls, number: Union[Text, int]) -> int:
        number = int(number)
        if number <= 0:
            raise ValueError(f"Number {number} is not valid")
        return number


class Statement(BaseModel):
    start: ChessCoordinate
    end: ChessCoordinate
