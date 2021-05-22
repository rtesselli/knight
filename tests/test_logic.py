from knight.logic import Solver, ChessBoard
from knight.data_model import Statement, ChessCoordinate


class TestChessBoard:
    def test_knight_moves(self):
        assert type(ChessBoard.KNIGHT_MOVES) == tuple
        assert len(ChessBoard.KNIGHT_MOVES) == 8
        assert len(set(ChessBoard.KNIGHT_MOVES)) == 8  # all distinct
        assert all(abs(x) in {1, 2} and abs(y) in {1, 2} for x, y in ChessBoard.KNIGHT_MOVES)


class TestSolver:
    def __init__(self):
        self.solver = Solver(ChessBoard(size=8))

    def test_solve_statement(self):
        result = list(
            self.solver.solve_statement(
                Statement(
                    start=ChessCoordinate(letter='D', number=4),
                    end=ChessCoordinate(letter='G', number=7),
                )
            )
        )
        expected1 = [
            ChessCoordinate(letter='D', number=4),
            ChessCoordinate(letter='F', number=5),
            ChessCoordinate(letter='G', number=7),
        ]
        expected2 = [
            ChessCoordinate(letter='D', number=4),
            ChessCoordinate(letter='E', number=6),
            ChessCoordinate(letter='G', number=7),
        ]
        assert result == expected1 or result == expected2
