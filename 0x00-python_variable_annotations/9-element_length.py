#!/usr/bin/env python3
"""Module with a function that reps input list and elements of list respectively."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains an element from the input list
    and its corresponding length.

    Args:
        lst (Iterable[Sequence]): An Iterable object containing sequences.
    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains an element
        from the input list and its length.
    """
    return [(i, len(i)) for i in lst]

