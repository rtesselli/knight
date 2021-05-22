from knight import data_model
from typing import Iterable, Optional
from knight.search import breadth_first_search
from itertools import product


class ChessBoard:
    KNIGHT_MOVES = tuple(product((1, -1), (2, -2))) + tuple(product((2, -2), (1, -1)))

    def __init__(self, size=8):
        self.size = size

    def move_from(self, cell: data_model.ChessCoordinate,
                  move: data_model.Pair) -> Optional[data_model.ChessCoordinate]:
        x = ord(cell.letter) - 64  # 'A' -> 1, 'B' -> 2 ...
        y = cell.number
        new_x = x + move[0]
        new_y = y + move[1]
        if 1 <= new_x <= self.size and 1 <= new_y <= self.size:
            return data_model.ChessCoordinate(letter=chr(new_x + 64), number=new_y)
        return None

    def knight_neighbors(self, cell: data_model.ChessCoordinate) -> Iterable[data_model.ChessCoordinate]:
        return (
            new_coordinate
            for move in ChessBoard.KNIGHT_MOVES
            if (new_coordinate := self.move_from(cell, move))
        )


class Solver:
    def __init__(self, board: ChessBoard):
        self.board = board

    def solve_statement(self, statement: data_model.Statement) -> Iterable[data_model.ChessCoordinate]:
        start = statement.start
        end = statement.end
        return breadth_first_search(start, end, self.board.knight_neighbors)

    def solve(self, statements: Iterable[data_model.Statement]) -> Iterable[Iterable[data_model.ChessCoordinate]]:
        return (
            self.solve_statement(statement)
            for statement in statements
        )
