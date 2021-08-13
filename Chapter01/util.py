"""
Utility Functions
-----------------

This module contains miscellaneous utility functions and examples from the textbook.
"""
from collections import Iterable
from typing import Any, TypeVar

NumT = TypeVar("NumT", int, float)


def max_index_value(tab: list[NumT]) -> tuple[NumT, int]:
    """
    Yields the maximum value and the index of the maximum value for an iterable. In the case of a draw between maximal
    values, the one with the highest index is returned.

    :param list[NumT] tab: The iterable you want to find the maximum value and corresponding index of.
    :rtype: tuple[NumT, int]
    :return: A tuple representing the element and its index.
    """
    return max((tab[i], i) for i, tab_i in enumerate(tab))
