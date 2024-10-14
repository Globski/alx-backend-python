#!/usr/bin/env python3
"""
Module for safely retrieving values from dictionaries.
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely retrieve a value from a dictionary.

    Args:
        dct (Mapping): The dictionary to retrieve from.
        key (Any): The key to look for.
        default (Union[T, None]): The value to return if the key is not found.

    Returns:
        Union[Any, T]: The value from the dictionary or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
