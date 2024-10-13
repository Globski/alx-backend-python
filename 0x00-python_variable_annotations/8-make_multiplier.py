#!/usr/bin/env python3
"""
Module for creating multiplier functions.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that multiplies its input by multiplier.
    """
    return lambda x: x * multiplier
