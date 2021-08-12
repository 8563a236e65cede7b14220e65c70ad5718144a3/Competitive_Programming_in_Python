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
from typing import Type, Any, AnyStr
from random import randint
from pathlib import Path

# Set up the logger for the module
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s [%(lineno)d] %(message)s "
)

# Get the logger
logger = logging.getLogger("Chapter01.matrix_input_output")


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


def convert_anystr(any_str: AnyStr) -> str:
    """
    Helper function to take an :class:`.AnyStr` type and return :class:`str` output. Returns :class:`str` input
    unmodified but decodes :class:`bytes` input to :class:`str`.

    :param typing.AnyStr any_str: The :class:`str` or :class:`bytes` object to coerce.
    :rtype: str
    :return: :class:`str` value of any_str.
    """
    return any_str if isinstance(any_str, str) else any_str.decode()


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
    stdin_input_str: AnyStr = sys.stdin.readline()

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


def readarray(typ: Type) -> list[Any]:
    """
    Reads in an array of a given type from :code:`stdin`. If the elements within :code:`stdin` are not all of the
    correct type, the program exits.

    :param typing.Type typ: The type of the elements of the list.
    :rtype: list[Any]
    :return: A list created from the :code:`stdin` input line.
    """
    # Initialize storage.
    array: list[typ]

    # Read the line.
    stdin_input_str: AnyStr = sys.stdin.readline()

    # We attempt to map the input to a list of appropriate type.
    try:
        # All the entries in the input line were of the correct type.
        array = list(map(typ, stdin_input_str.split()))
    except ValueError as err:
        # At least one of the entries in the input line was of an incorrect type. We log the error message and exit
        # with an os.EX_DATAERR
        logger.critical(
            "readarray - " + str(err) +
            "\nInput: " + convert_anystr(stdin_input_str)
        )
        flush_buffers_and_exit(os.EX_DATAERR)

    return array


if __name__ == "__main__":
    #return_value = readint()
    #print("Returned: " + str(return_value))

    arr = readarray(int)
    print(arr)


