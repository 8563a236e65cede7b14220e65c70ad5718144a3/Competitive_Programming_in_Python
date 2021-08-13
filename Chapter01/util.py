"""
Utility Functions
-----------------

This module contains miscellaneous utility functions and examples from the textbook.
"""
from collections import Iterable
from collections.abc import Callable
from typing import Any, TypeVar, Optional

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


def max_interval_intersec(S: list[tuple[NumT, NumT]]) -> tuple[int, NumT]:
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
    c: int = 0                  # Keeps track of intervals beginnings that have been seen
    x: NumT                     # Pointer
    d: int
    best: tuple[int, NumT]

    # For interval, side
    for x, d in B:
        c += d
        # Keep track of the best interval
        if best[0] < c:
            best = (c, x)

    return best


def min_scalar_prod(x: list[NumT], y: list[NumT]) -> NumT:
    """
    Produces the minimum scalar product between two lists of numbers. Given two vectors :math:`x` and :math:`y` of
    :math:`n` non-negative integers, this yields the permutation :math:`\pi` of :math:`\{1,...,n\}` such that
    :math:`\sum\limits_{i}^{n} x_{i}y_{\pi(i)}` is minimal.

    :param list[NumT] x: First list.
    :param list[NumT] y: Second list.
    :return: Minimum scalar product
    """
    # Return sorted copies of the inputs.
    x1: list[NumT] = sorted(x)
    y1: list[NumT] = sorted(y)
    return sum(x1[i] * y1[-i - 1] for i in range(len(x1)))


def fibo_naive(n: int) -> int:
    """
    A naive implementation of the Fibonacci sequence to illustrate inefficient programming.

    :param int n: The index of the Fibonacci number to calculate
    :return: The Fibonacci number at index n.
    """
    # Clause to terminate if n is less than 2.
    if n <= 1:
        return n
    return fibo_naive(n - 1) + fibo_naive(n - 2)


def fibo_dp(n: int) -> int:
    r"""
    An efficient dynamic programming approach to generating Fibonacci numbers. Calculates Fibonacci numbers forwards,
    storing the results in an array until reaching the desired number. Thus removes a great many nodes from the
    dependency graph. Computes

    .. math::

        F(0) &= 0                \\
        F(1) &= 1                \\
        F(i) &= F(i-1) + F(i-2)

    :param int n: The index of the Fibonacci number to calculate
    :return: The Fibonacci number at index n.
    """
    # Create a list with F(0) and F(1)
    mem: list[int] = [0, 1]

    # Declare iterator
    i: int

    # Iterate up to n
    for i in range(2, n + 1):
        # Use the formula F(i) = F(i-1) + F(i-2) to calculate the latest element.
        mem.append(mem[-2] + mem[-1])

    # Return the last element which is the nth Fibonacci number.
    return mem[-1]


def three_partition(x: list[int]) -> Optional[tuple[int, int, int]]:
    """
    Given :math:`n` integers :math:`x_{0},...x_{n-1}`, we wish to partition them into three sets with the same sum.

    :param x: A list of :math:`n` integers
    :return:
    """
    # Create a list with n 0 entries.
    f = [0] * (1 << len(x))

    # Declare iterators
    i: int
    v: int
    S: int
    A: int
    B: int

    # For each index, value in x
    for i, v in enumerate(x):
        for S in range(1 << i):
            f[S | (1 << i)] = f[S] + x[i]
    for A in range(1 << len(x)):
        for B in range(1 << len(x)):
            # Check f(A) a f(B) and 3f(A) = f({0,...,n-1})
            if A & B == 0 and f[A] == f[B] and 3 * f[A] == f[-1]:
                return A, B, ((1 << len(x)) - 1) ^ A ^ B
    return None


def discrete_binary_search(tab: list[bool], lo: int, hi: int) -> int:
    """
    Discrete binary search that only operates on a sorted boolean array.

    :param list[bool] tab: A boolean array in which we want to find the first True value.
    :param lo: The lower index to search.
    :param hi: The upper index to search.
    :rtype: int
    :return: The index of the first True value.
    """
    # Bisect the search area at each iteration
    while lo < hi:
        mid = lo + (hi - lo) // 2
        # If the value is True, adjust the upper bound
        if tab[mid]:
            hi = mid
        # Otherwise, the value was false and we adjust the lower bound
        else:
            low = mid + 1

    return lo


def continous_binary_search(f: Callable[[float], bool], lo: float, hi: float, gap:float =1e-4):
    """
    This technique can be applied when the domain of :math:`f` is continuous and we seek the smallest :math:`x_{0}`
    such that :math:`f(x_{0}) = 1` for every :math:`x\geq x_{0}` . :math:`f` should only output non-decreasing boolean
    values along its domain.

    :param Callable[[float], bool] f:
    :param float lo: The lower bound of the continuous range to search.
    :param float hi: The upper bound of the continous range to search.
    :param float gap: The desired level of precision.
    :rtype: float
    :return: The smallest :math:`x_{0}` s.t. :math:`f(x_{0}) = 1`
    """

    # Continue until we reach our desired precision.
    while hi - lo > gap:
        mid = (lo + hi) / 2.0
        if f(mid):
            hi = mid
        else:
            lo = mid

    return lo


def optimized_binary_search(tab: list[bool], logsize: int) -> int:
    """
    An optimized binary search if the search space of size n is a power of 2. Uses the dark arts of bit manipulation to
    get the job done in an obscure way.

    :param list[bool] tab: A sorted boolean array to search.
    :param int logsize: The size of the search space.
    :return: The index of the value.
    """
    hi: int = (1 << logsize) - 1
    intervalsize: int = (1 << logsize) >> 1
    while intervalsize > 0:
        if tab[hi ^ intervalsize]:
            hi ^= intervalsize
        intervalsize >>= 1
    return hi
