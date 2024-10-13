#!/usr/bin/env python3
"""
Module for summing operations on mixed lists.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum a mixed list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The mixed list to sum.

    Returns:
        float: The sum of the integers and floats in mxd_lst.
    """
    return sum(mxd_lst)
