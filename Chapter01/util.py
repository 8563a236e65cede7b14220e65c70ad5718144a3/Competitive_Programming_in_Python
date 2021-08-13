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


def majority(L: list[str]) -> str:
    """
    Find the most common element of an array. This implementation has average complexity :math:`O(nk)` and a worst case
    complexity of :math:`O(n^{2}k)` . The algorithm yields the first word encountered with the highest number of
    occurrences.

    :param list[str] L: The words to count the frequency of, given as a list.
    :return: The word with the highest number of occurrences.
    """
    # Initialize storage for counter and iterator.
    count: dict[str, int] = {}
    word: str

    # Count the number of occurrences for each word in the list.
    for word in L:
        # If the word has already been encountered
        if word in count:
            # Increment the counter by 1.
            count[word] += 1
        # Otherwise this is the first time we are seeing the word
        else:
            # Initialize the counter to 1.
            count[word] = 1

    # Yield the first word with maximal count.
    val_1st_max, arg_1st_max = min((-count[word], word) for word in count)

    return arg_1st_max
