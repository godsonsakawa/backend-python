#!/usr/bin/env python3
"""Module with a function..."""
from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """Returns the first element of a sequence or None if the sequence is empty.

    Args:
        lst (Sequence): A sequence of elements.
    Returns:
        Union[Any, None]: First element of the sequence or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
