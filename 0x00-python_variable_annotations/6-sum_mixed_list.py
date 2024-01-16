#!/usr/bin/env python3
""" Module contains a function that sums up a list of mixed integers and floats."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Takes a list of integers and floats and returns their sum as a float.
    Args:
        mxd_list (list): A list of integers and floats.
    Return:
        Returns sum as float.
    """
    result: float = sum(mxd_lst)

    return result
