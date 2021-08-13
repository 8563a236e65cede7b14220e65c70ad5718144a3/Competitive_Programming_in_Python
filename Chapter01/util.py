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


def closest_values(L: list[NumT]) -> tuple[NumT, NumT]:
    """
    Find the two values in a list with the closest values.

    :param list[NumT] L:
    :rtype: tuple[NumT, NumT]
    :return: The two values with the minimal difference.
    """
    # If there are less than two items we cannot do the comparison.
    assert len(L) >= 2

    # Sort the list.
    L.sort()

    # Get the smallest difference and the index of the minimum difference.
    valmin, argmin = min((L[i] - L[i-1], i) for i in range(1, len(L)))

    # Returns the two numbers that produced the minimum difference.
    return L[argmin-1], L[argmin]


def max_interval_intersec(S: list[tuple[NumT, NumT]]):
    """
    Given :math:`n` intervals :math:`[l_{i}, r_{i})` for :math:`i = 0,...,n-1` we wish to find a value :math:`x`
    included in a maximum number of intervals. This implementation is in time :math:`O(n\log n)` .

    :param list[tuple[NumT, NumT]] S: n sets of intervals.
    :rtype: tuple[NumT, NumT]
    :return: The maximum interval intersection.
    """
    # Construct left and right intervals.
    B: list[tuple[NumT, int]] = ([(left, +1) for left, right in S] +
         [(right, -1) for left, right in S])

    # Sort intervals.
    B.sort()

    # Declare a counter, two iterators and storage for the result.
    c: int = 0
    x: NumT
    d: int
    best: tuple[int, NumT]

    # For interval, side
    for x, d in B:
        c += d
        # Keep track of the best interval
        if best[0] < c:
            best = (c, x)

    return best
