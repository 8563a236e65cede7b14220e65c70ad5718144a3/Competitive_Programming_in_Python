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
from typing import Type, Any
from random import randint
from pathlib import Path

# Set up the logger for the module
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s [%(lineno)d] %(message)s "
)

# Get the logger
logger = logging.getLogger("Chapter01.matrix_input_output")


def flush_buffers() -> None:
    """
    A convenience function to flush stdout and stderr buffers. Useful for when exiting with sys.exit.
    """
    sys.stdout.flush()
    sys.stderr.flush()


def readint() -> int:
    """
    Reads an integer from :code:`stdin`. This function expects a single line of input with only an integer present.

    :rtype: int
    :return: The integer held in the :code:`stdin` buffer.
    """
    # Initialize storage.
    value: int = 0

    # The function is expecting a single integer input. We must handle the case where the input is a single integer.
    try:
        # The input was a recognizable integer.
        value = int(sys.stdin.readline())
    except ValueError as err:
        # The input was not a recognizable integer. Log the error and exit the program.
        logger.critical("readint " + str(err))
        flush_buffers()
        sys.exit(os.EX_DATAERR)

    return value


def readarray(typ: Type):
    array: list[typ]
    array = list(map(typ, sys.stdin.readline().split()))
    return array


if __name__ == "__main__":
    #return_value = readint()
    #print("Returned: " + str(return_value))


