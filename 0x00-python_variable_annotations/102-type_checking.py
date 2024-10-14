#!/usr/bin/env python3
"""
Module for zooming an array.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zoom in on an array.

    Args:
        lst (Tuple): The tuple to zoom in on.
        factor (int): The zoom factor.

    Returns:
        List: A list with elements from lst zoomed in by factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
