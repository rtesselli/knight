from pydantic import BaseModel
from typing import Text


class ChessCoordinate(BaseModel):
    letter: Text
    number: int


class Statement(BaseModel):
    start: ChessCoordinate
    end: ChessCoordinate
