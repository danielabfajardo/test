"""Simple single-function priority queue exercise."""

from heapq import heappop, heappush
from typing import Iterable, List, Tuple


def process_priority_queue(operations: Iterable[Tuple[str, int]]) -> List[int]:
    """
    Execute push/pop operations on a min-priority queue and return popped values.

    Supported operations:
    - ("push", value): push value into the priority queue
    - ("pop", _): pop and record the smallest value if the queue is not empty
    """

    heap: List[int] = []
    popped_values: List[int] = []

    for operation, value in operations:
        if operation == "push":
            heappush(heap, value)
        elif operation == "pop" and heap:
            popped_values.append(heappop(heap))

    return popped_values
