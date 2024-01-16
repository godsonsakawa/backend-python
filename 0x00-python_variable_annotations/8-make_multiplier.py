#!/usr/bin/env python3
""" Module with a function that Multiplies a float by the given multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that mult a float by the given multiplier.
    Args:
        multiplier (float): The value to multiply by.
    Returns:
        Callable[[float], float]: A function that takes a float argument 
        and returns the product.
     """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
