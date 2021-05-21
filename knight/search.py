from collections import deque
from typing import Generic, Iterable, Callable
from knight.data_model import T


def breadth_first_search(start: Generic[T], key: Generic[T],
                         neighbors: Callable[[T], Iterable[T]]) -> Iterable[T]:
    def backtrace(node: Generic[T]) -> Iterable[T]:
        parent = parents.get(node, None)
        trace = []
        while parent:
            trace.append(parent)
            parent = parents.get(parent, None)
        return list(reversed(trace)) + [node]

    to_do = deque([start])
    visited = {start}
    parents = {}
    while to_do:
        node = to_do.popleft()
        if node == key:
            return backtrace(node)
        for neighbor in neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                to_do.append(neighbor)
                parents[neighbor] = node
    return []