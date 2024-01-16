#!/usr/bin/env python3
""" Module with a function that filters values frm a dict."""
from typing import TypeVar, Mapping, Any, Union, Optional


T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Optional[T] = None) -> Union[Any, T]:
    """
    Safely gets the value from a dictionary by key, with an optional default value.
    Args:
        dct (Mapping): A mapping (e.g., dictionary)
        key (Any): The key to look up in the dictionary.
        default (Optional[T]): An optional default value to return the key if not found.
                               Default is None.
    Returns:
        Union[Any, T]: The value corresponfing to the key in the dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default

