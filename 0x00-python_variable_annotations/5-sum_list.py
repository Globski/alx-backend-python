#!/usr/bin/env python3
"""
Module for summing operations on lists.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sum a list of floats and return the total.

    Args:
        input_list (List[float]): The list of floats to sum.

    Returns:
        float: The sum of the floats in input_list.
    """
    return sum(input_list)
