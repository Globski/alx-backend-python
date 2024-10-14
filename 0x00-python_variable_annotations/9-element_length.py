#!/usr/bin/env python3
"""
Module for getting lengths of elements in an iterable.
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Get the lengths of elements in an iterable.

    Args:
        lst (Iterable[Sequence]): The iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples with elements and their lengths.
    """
    return [(i, len(i)) for i in lst]
