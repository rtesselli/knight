from typing import Iterable
from knight import data_model


def output_solutions(results: Iterable[Iterable[data_model.ChessCoordinate]]) -> None:
    """
    Prints to stdout the results
    :param results: Iterable of knight paths
    :return: None
    """
    for result in results:
        print(" ".join(str(coordinate) for coordinate in result))
