#!/usr/bin/env python3
"""
Module for safely retrieving the first element of a sequence.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Get the first element of a sequence safely.

    Args:
        lst (Sequence[Any]): The sequence to retrieve the first element from.

    Returns:
        Union[Any, None]: The first element of the sequence, or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
