"""
Data Structures
---------------

This module contains data structures built from first principles. It is merely illustrative as the standard library data
structures are preferred for general use.
"""
from typing import Any
from collections.abc import Iterable


class OurQueue:
    """
    This is a concrete class for the Queue abstract data type. It implements the push, pop and len methods required for
    this data structure.

    .. automethod:: __init__
    .. automethod:: __len__
    """
    def __init__(self) -> None:
        """
        The initialization function comprises of initializing two stacks. The first stack is the in_stack which stores
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


class OurHeap:
    """
    This is a concrete class for the Heap abstract data type. The structure stores the heap in a list and keeps a rank
    dictionary to keep track of the elements' indexes.

    It represents a quasi-perfect binary tree and allows the extraction of the smallest element and insertion of a new
    element at logarithmic cost.

    .. automethod:: __init__
    .. automethod:: __len__
    """
    def __init__(self, items: Iterable[Any]) -> None:
        """
        Initialized the heap with given items.

        :param Iterable[Any] items: Items to be added to the heap upon initialization.
        """
        # Declare the iterator for later use.
        x: Any

        # Initialize the heap and the dictionary to keep track of rank.
        self.heap: list[Any] = [None]
        self.rank: dict[Any, int] = {}

        # Add the items to the heap.
        for x in items:
            self.push(x)

    def __len__(self) -> int:
        """
        Retrieves the length of the heap. Since the position 0 element is not used, this function returns the length of
        the heap less 1 element.

        :rtype: int
        :return: The heap length.
        """
        return len(self.heap) - 1

    def push(self, x: Any) -> None:
        """
        Push an element onto the heap. The element can be of any type.

        :param Any x: The desired element to push.
        """
        # Check that the item has not already been added to the heap.
        assert x not in self.rank

        # Get the index that the new element will be inserted at.
        i: int = len(self.heap)

        # Append the element.
        self.heap.append(x)

        # Add the location of the element to the dictionary.
        self.rank[x] = i

        # Reorganise the heap.
        self.up(i)

    def pop(self) -> Any:
        """
        Pop the root node from the heap. The latest leaf then becomes the new root.

        :rtype: Any
        :return: The root node.
        """
        # Get the root node.
        root: Any = self.heap[1]

        # Remove its location from the rank dictionary.
        del self.rank[root]

        # Pop the latest leaf.
        x: Any = self.heap.pop()

        # If the heap is not empty
        if self:
            # Move the last leaf to the root to maintain heap order.
            self.heap[1] = x
            self.rank[x] = 1
            self.down(1)

        return root

    def up(self, i: int) -> None:
        """
        Move the element up in the heap.

        :param int i: The index of the element in the heap.
        """
        # Get the element from the heap.
        x: Any = self.heap[i]

        # We bisect the heap using integer division, swapping the current element with those at half its index until its
        # correct position is found..
        while i > 1 and x < self.heap[i // 2]:
            self.heap[i] = self.heap[i // 2]
            self.rank[self.heap[i // 2]] = i
            i //= 2

        # Do a final swap.
        self.heap[i] = x
        self.rank[x] = i

    def down(self, i: int) -> None:
        """
        Move the element down in the heap.

        :param int i: The index of the element in the heap.
        """
        # Get the element from the heap.
        x: Any = self.heap[i]

        # Get the total length of the heap.
        n = len(self.heap)

        # Climb down the tree iteratively.
        while True:
            left: int = 2 * i
            right: int = left + 1

            if (right < n and self.heap[right] < x and
                    self.heap[right] < self.heap[left]):
                # Move the right child up.
                self.heap[i] = self.heap[right]
                self.rank[self.heap[right]] = i
                i = right
            elif left < n and self.heap[left] < x:
                # Move the left child up.
                self.heap[i] = self.heap[left]
                self.rank[self.heap[left]] = i
                i = left
            else:
                # Put the child in its correct insertion point.
                self.heap[i] = x
                self.rank[x] = i
                return

    def update(self, old: Any, new: Any) -> None:
        """
        Update the heap by removing the old element and replacing it with a new element. The elements of the  heap are
        then reordered to maintain heap order.

        :param Any old: The element to replace.
        :param Any new: The new element to insert.
        """
        # Get the index of the old element
        i: int = self.rank[old]

        # Delete the index entry.
        del self.rank[old]

        # Insert the new entry at the old entry's location.
        self.heap[i] = new

        # Update the rank dictionary with the new entry's location.
        self.rank[new] = i

        # If the old value is less than the new value
        if old < new:
            # Move the element down.
            self.down(i)
        # Otherwise the old value is greater
        else:
            # Move the element up.
            self.up(i)
