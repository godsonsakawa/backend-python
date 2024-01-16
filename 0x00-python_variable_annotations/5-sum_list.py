#!/usr/bin/env python3
"""Module that with function that returns the sum of a list of floats."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of floats in a list.
    Args:
        input_list (list): A list of floats.
    Returns:
        float: The sum of the floats in the list.
    """
    result: float = sum(input_list)

    return result
