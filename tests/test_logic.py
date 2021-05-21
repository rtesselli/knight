from knight.logic import KNIGHT_MOVES, solve_statement
from knight.data_model import Statement, ChessCoordinate


def test_knight_moves():
    assert type(KNIGHT_MOVES) == tuple
    assert len(KNIGHT_MOVES) == 8
    assert len(set(KNIGHT_MOVES)) == 8  # all distinct
    assert all(abs(x) in {1, 2} and abs(y) in {1, 2} for x, y in KNIGHT_MOVES)


def test_solve_statement():
    result = list(
        solve_statement(
            Statement(
                start=ChessCoordinate(letter='D', number=4),
                end=ChessCoordinate(letter='G', number=7),
            )
        )
    )
    expected = [
        ChessCoordinate(letter='D', number=4),
        ChessCoordinate(letter='F', number=5),
        ChessCoordinate(letter='G', number=7),
    ]
    assert result == expected
