#!/usr/bin/env python3
""" A module a function that returns a tuple."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Create a tuple where 1st element is a string and 2nd element 
    a square of the int/float 'v', annotated as a float.
    Args:
        k (str): The string key.
        v (Union[int, float]): The value value can either be an int or float.
    Returns:
        Tuple[str, float]: A tuple with 'k' as the fist element and the square of 'v'
    """
    squared_value: float = v ** 2

    return k, squared_value
