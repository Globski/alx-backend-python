#!/usr/bin/env python3
"""
Module for creating tuples from string and number.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple from a string and the square of a number.

    Args:
        k (str): The string key.
        v (Union[int, float]): The number to square.

    Returns:
        Tuple[str, float]: A tuple with the string and the square of the number.
    """
    return (k, v ** 2)
