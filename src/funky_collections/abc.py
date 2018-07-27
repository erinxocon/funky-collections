import abc
import collections

from typing import Any, Generator, List, Optional, Sequence, Union

from .nodes import ImmutableListNode


class ImmutableDoublyLinkedList(collections.abc.Sequence):
    __slots__ = ("_size", "_head", "_tail")

    @abc.abstractmethod
    def __init__(self) -> None:
        """Initialize a list with optional max length"""
        self._size = 0
        self._head: Optional[ImmutableListNode] = None
        self._tail: Optional[ImmutableListNode] = None

    @abc.abstractmethod
    def append_left(self, value: Any) -> None:
        """Add an element to the left side of the list"""

    @abc.abstractmethod
    def append_right(self, value: Any) -> None:
        """Add an element to the right side of the list"""

    @abc.abstractmethod
    def pop_left(self) -> Any:
        """Pop an element from the left side of the list"""

    @abc.abstractmethod
    def pop_right(self) -> Any:
        """Pop an element from the right side of the list"""

    def get_node(self, index: int) -> ImmutableListNode:
        try:
            if index < 0:
                index = self._size + index
        except TypeError:
            raise TypeError("List indices must be integers")

        if index < 0 or self._size <= index:
            raise IndexError("List index is out of range")

        middle_index = self._size // 2

        if index <= middle_index:
            node = self._head
            start_index = 0
            transverse_reversed = False

        else:
            node = self._tail
            start_index = self._size - 1
            transverse_reversed = True

        if not transverse_reversed:
            while start_index < index:
                node = node.next_node  # type: ignore
                start_index += 1
        else:
            while start_index > index:
                node = node.previous_node  # type: ignore
                start_index -= 1

        return node  # type: ignore

    def __repr__(self) -> str:
        data = ",".join(repr(x) for x in self)
        name = self.__class__.__name__
        return f"<{name} data=[{data}]>"

    def __str__(self) -> str:
        data = ",".join(str(x) for x in self)
        name = self.__class__.__name__
        return f"{name}([{data}])"

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Generator:
        current = self._head
        while current is not None:
            yield current.data
            current = current.next_node

    def __reversed__(self) -> Generator:
        current = self._tail
        while current is not None:
            yield current.data
            current = current.previous_node

    @classmethod
    def _from_sequence(cls, **kwargs):
        return cls(**kwargs)
