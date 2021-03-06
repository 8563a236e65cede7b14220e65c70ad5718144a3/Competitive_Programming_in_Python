"""
Matrix Input Output
-------------------

This file contains some utility functions for reading from standard input. These cover single integers,
integer arrays and matrices. Also implemented is *Freivalds test* (1979) to determine, probabilistically
whether the equality :math:`AB = C` holds for :math:`n*n` matrices :math:`A, B, C` .
"""
import os
import sys
import logging
from typing import TypeVar, Any, Union, Type, Optional
from random import randint
from pathlib import Path

# Set up the logger for the module
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s [%(lineno)d] %(message)s "
)

# Get the logger
logger = logging.getLogger("Chapter01.matio")
"""Logger for this module."""

NumArrTypes = TypeVar("NumArrTypes", list[int], list[float])
"""Generic variable for numeric arrays."""

NumMatTypes = TypeVar("NumMatTypes", list[list[int]], list[list[float]])
"""Generic variable for numeric matrices."""

def flush_buffers_and_exit(error: int) -> None:
    """
    A convenience function to flush stdout and stderr buffers and exit the program with a given OS return value.

    :param int error: An OS return value from :mod:`os`.
    """
    # Flush the buffers.
    sys.stdout.flush()
    sys.stderr.flush()

    # Exit
    sys.exit(error)


def convert_anystr(any_str: Union[str, bytes]) -> str:
    """
    Helper function to take an :class:`.Union[str, bytes]` type and return :class:`str` output. Returns :class:`str` input
    unmodified but decodes :class:`bytes` input to :class:`str`.

    :param typing.Union[str, bytes] any_str: The :class:`str` or :class:`bytes` object to coerce.
    :rtype: str
    :return: :class:`str` value of any_str.
    """
    return_value: Union[str, bytes]
    if isinstance(any_str, str):
        return_value = any_str
    elif isinstance(any_str, bytes):
        return_value = any_str.decode()

    return return_value


def readint() -> int:
    """
    Reads an integer from :code:`stdin`. This function expects a single line of input with only an integer present. If
    the input value is not an integer, the program exits.

    :rtype: int
    :return: The integer held in the :code:`stdin` buffer.
    """
    # Initialize storage.
    value: int = 0

    # Read the line first.
    stdin_input_str: Union[str, bytes] = sys.stdin.readline()

    # The function is expecting a single integer input. We must handle the case where the input is a single integer.
    try:
        # The input was a recognizable integer.
        value = int(stdin_input_str)
    except ValueError as err:
        # The input was not a recognizable integer. Log the error and exit the program.
        logger.critical(
            "readint - " + str(err) +
            "\nInput: " + convert_anystr(stdin_input_str)
        )
        flush_buffers_and_exit(os.EX_DATAERR)

    return value


def readarray(typ: str) -> list[Any]:
    """
    Reads in an array of a given type from :code:`stdin`. If the elements within :code:`stdin` are not all of the
    correct type, the program exits.

    :param str typ: The type of the elements of the list.
    :rtype: list[Any]
    :return: A list created from the :code:`stdin` input line.
    """
    # Initialize storage.
    if typ == "int" or typ == "float" or typ == "str":
        array: Union[list[int], list[float], list[str]]
    else:
        logger.critical("readarray - Unsupported Type\nInput " + str(typ))
        flush_buffers_and_exit(os.EX_DATAERR)

    # Read the line.
    stdin_input_str: Union[str, bytes] = sys.stdin.readline()

    # We attempt to map the input to a list of appropriate type.
    try:
        # All the entries in the input line were of the correct type.
        if typ == "int":
            array = list(map(int, stdin_input_str.split()))
        elif typ == "float":
            array = list(map(float, stdin_input_str.split()))
        if typ == "str":
            array = list(map(str, stdin_input_str.split()))

    except ValueError as err:
        # At least one of the entries in the input line was of an incorrect type. We log the error message and exit
        # with an os.EX_DATAERR.
        logger.critical(
            "readarray - " + str(err) +
            "\nInput: " + convert_anystr(stdin_input_str)
        )
        flush_buffers_and_exit(os.EX_DATAERR)

    return array


def readmatrix(n: int) -> list[list[int]]:
    """
    Reads an :math:`n*n` matrix from stdin. The input is expected to consist solely of integers.

    :param int n: The dimension of the square matrix.
    :rtype: list[list[int]]
    :return: A list of lists of integers representing the matrix.
    """
    # Create the list to store the results.
    M: list = []

    # For each line of input from stdin.
    for lines in range(n):
        # Read in the values as an array.
        row: list[int] = readarray("int")

        # Check that the length of the row is equal to n.
        assert len(row) == n

        # Append the row to storage.
        M.append(row)

    return M


def mult(M: NumMatTypes, v: NumArrTypes):
    """
    Performs the calculations :math:`M*v` where :math:`M` is an :math:`n*n` matrix, and :math:`v` is a vector of length
    :math:`n` . The function operates on integers or floating point values. The formula applied is
    :math:`\sum\limits_{j=1}^{n} M_{ij}v_{j}` for each row in :math:`M` and returns a list with these values.

    :param M: :math:`n*n` matrix
    :param v: vector of length :math:`n`
    :return: A vector of length :math:`n` that represents :math:`M*v`
    """
    # Get the number of rows in the matrix.
    n: int = len(M)

    # Return the sum.
    return [sum(M[i][j] * v[j] for j in range(n)) for i in range(n)]


def freivalds(A: NumMatTypes, B: NumMatTypes, C: NumMatTypes) -> bool:
    """
    Performs *Freivalds test* (1979). Checks that the the equality :math:`AB = C` holds for :math:`n*n`
    matrices :math:`A, B, C` .
    For more information see the `Freivalds' Algorithm <https://en.wikipedia.org/wiki/Freivalds%27_algorithm>`_
    wikipedia article. This performs the sums
    :math:`\sum\limits_{k=1}^{n} A_{ik} (\sum\limits_{j=1}^{n} B_{ij}x_{j})` and
    :math:`\sum\limits_{j=1}^{n} C_{ij}x_{j}`
    for each row in the matrices and where :math:`x` is a random vector. The lists of results are then compared for
    equality.

    :param NumMatTypes A: :math:`n*n` input matrix.
    :param NumMatTypes B: :math:`n*n` input matrix.
    :param NumMatTypes C: :math:`n*n` to check the :math:`A*B` product against.
    :rtype: bool
    :return: Whether the product is correct.
    """
    n: int = len(A)
    x: list[int] = [randint(0, 1000000) for j in range(n)]
    return mult(A, mult(B, x)) == mult(C, x)


def main() -> None:
    """
    A simple test harness for *Freivalds' test*.
    """
    n: int = readint()
    A: list[list[int]] = readmatrix(n)
    B: list[list[int]] = readmatrix(n)
    C: list[list[int]] = readmatrix(n)
    print(freivalds(A, B, C))
