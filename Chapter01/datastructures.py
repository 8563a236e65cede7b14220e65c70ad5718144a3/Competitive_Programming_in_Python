"""
Data Structures
---------------

This module contains data structures built from first principles. It is merely illustrative as the standard library data
structures are preferred for general use.
"""
from typing import Any


class OurQueue:
    def __init__(self) -> None:
        """
        The initialization function comprises of intializing two stacks. The first stack is the in_stack which stores
        incoming objects. The out_stack are where items are retrieved, from newest to oldest.
        """
        self.in_stack: list[Any] = []
        self.out_stack: list[Any] = []

    def __len__(self) -> int:
        """
        The length of the queue is comprised of the lengths of the in_queue and out_queue.

        :rtype: int
        :return: The length of the queue
        """
        return len(self.in_stack) + len(self.out_stack)

    def push(self, obj: Any) -> None:
        """
        Push an object onto the in_stack.

        :param Any obj: An object to add to the stack
        """
        self.in_stack.append(obj)

    def pop(self) -> Any:
        """
        Pop an object from the out_stack. If the out_stack is empty, swap it with the in_stack and empty the in_stack.
        """
        # If the head of the queue is empty
        if not self.out_stack:
            # We copy the in_stack in reverse order and set it as the out_stack. The in_stack stores data from oldest to
            # newest whereas the out_stack needs to pop elements from newest to oldest.
            self.out_stack = self.in_stack[::-1]

            # Reinitialize the in_stack.
            self.in_stack = list()

        return self.out_stack.pop()
