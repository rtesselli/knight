from typing import Iterable
from knight import data_model


def output_solutions(results: Iterable[Iterable[data_model.ChessCoordinate]]) -> None:
    for result in results:
        print(" ".join(str(coordinate) for coordinate in result))
