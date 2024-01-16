#!/usr/bin/env python3
"""Module with a function that replicates each element in an array a specified no.of times."""
from typing import List, Tuple

def zoom_array(lst: List, factor: int = 2) -> List:
    """Returns a list of replicated list by a certain factor.
    Args:
        lst (List): A list of elements.
        factor (int): Number to multiply each element.
    Return:
        List: Returns a list where each element is replicated by a certain factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

if __name__ == "__main__":
    array = [12, 72, 91]

    zoom_2x = zoom_array(array)
    zoom_3x = zoom_array(array, 3)

    print("Original Array:", array)
    print("Zoom 2x:", zoom_2x)
    print("Zoom 3x:", zoom_3x)

