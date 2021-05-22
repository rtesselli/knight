from knight.logic import Solver, ChessBoard
from knight.data_model import Statement, ChessCoordinate, Pair


class TestChessBoard:
    def __init__(self):
        self.board = ChessBoard(size=8)

    def test_knight_moves(self):
        assert type(ChessBoard.KNIGHT_MOVES) == tuple
        assert len(ChessBoard.KNIGHT_MOVES) == 8
        assert len(set(ChessBoard.KNIGHT_MOVES)) == 8  # all distinct
        assert all(abs(x) in {1, 2} and abs(y) in {1, 2} for x, y in ChessBoard.KNIGHT_MOVES)

    def test_move_from(self):
        assert self.board.move_from(ChessCoordinate(letter='A', number=1), Pair(-1, 0)) is None
        assert self.board.move_from(ChessCoordinate(letter='A', number=1), Pair(0, -1)) is None
        assert self.board.move_from(ChessCoordinate(letter='A', number=1), Pair(-1, -1)) is None

        assert self.board.move_from(ChessCoordinate(letter='A', number=8), Pair(-1, 0)) is None
        assert self.board.move_from(ChessCoordinate(letter='A', number=8), Pair(0, 1)) is None
        assert self.board.move_from(ChessCoordinate(letter='A', number=8), Pair(-1, 1)) is None

        assert self.board.move_from(ChessCoordinate(letter='H', number=8), Pair(1, 0)) is None
        assert self.board.move_from(ChessCoordinate(letter='H', number=8), Pair(0, 1)) is None
        assert self.board.move_from(ChessCoordinate(letter='H', number=8), Pair(1, 1)) is None

        assert self.board.move_from(ChessCoordinate(letter='H', number=1), Pair(1, 0)) is None
        assert self.board.move_from(ChessCoordinate(letter='H', number=1), Pair(0, -1)) is None
        assert self.board.move_from(ChessCoordinate(letter='H', number=1), Pair(1, -1)) is None

        assert self.board.move_from(
            ChessCoordinate(letter='B', number=1), Pair(1, 1)) == ChessCoordinate(letter='C', number=2)

    def test_knight_neighbors(self):
        result = set(self.board.knight_neighbors(ChessCoordinate(letter='C', number=3)))
        expected = {
            ChessCoordinate(letter='B', number=5),
            ChessCoordinate(letter='D', number=5),
            ChessCoordinate(letter='B', number=1),
            ChessCoordinate(letter='D', number=1),
            ChessCoordinate(letter='A', number=4),
            ChessCoordinate(letter='E', number=4),
            ChessCoordinate(letter='A', number=2),
            ChessCoordinate(letter='E', number=2)
        }
        assert result == expected

        result = set(self.board.knight_neighbors(ChessCoordinate(letter='A', number=1)))
        expected = {
            ChessCoordinate(letter='B', number=3),
            ChessCoordinate(letter='C', number=2),
        }
        assert result == expected


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
        assert result in {expected1, expected2}

        result = list(
            self.solver.solve_statement(
                Statement(
                    start=ChessCoordinate(letter='D', number=4),
                    end=ChessCoordinate(letter='D', number=5),
                )
            )
        )
        expected1 = [
            ChessCoordinate(letter='D', number=4),
            ChessCoordinate(letter='E', number=2),
            ChessCoordinate(letter='F', number=4),
            ChessCoordinate(letter='D', number=5)
        ]
        expected2 = [
            ChessCoordinate(letter='D', number=4),
            ChessCoordinate(letter='C', number=2),
            ChessCoordinate(letter='B', number=4),
            ChessCoordinate(letter='D', number=5)
        ]
        expected3 = [
            ChessCoordinate(letter='D', number=4),
            ChessCoordinate(letter='C', number=6),
            ChessCoordinate(letter='B', number=4),
            ChessCoordinate(letter='D', number=5)
        ]
        expected4 = [
            ChessCoordinate(letter='D', number=4),
            ChessCoordinate(letter='E', number=6),
            ChessCoordinate(letter='F', number=4),
            ChessCoordinate(letter='D', number=5)
        ]
        assert result in {expected1, expected2, expected3, expected4}
