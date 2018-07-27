import collections

from typing import Any, Generator, List, Optional, Sequence, Union

from .abc import DoublyLinkedList
from .nodes import MutableListNode


class MutableFixedList(DoublyLinkedList, collections.abc.MutableSequence):
    __slots__ = "_max_len"

    def __init__(self, max_len: int = 0, seq: Sequence = ()) -> None:
        if max_len <= 0:
            raise ValueError("Max lenth  must be more than 0")

        self._max_len = max_len
        self._head: Optional[MutableListNode] = None
        self._tail: Optional[MutableListNode] = None
        super().__init__()

        try:
            for val in seq[0 : self._max_len]:
                node = MutableListNode(val, self._tail, None)
                if self._head is None:
                    self._head = node

                self._tail = node

                self._size += 1
        except TypeError:
            raise TypeError("seq must be a sequence object")

    @property
    def max_len(self) -> int:
        return self._max_len

    def append_left(self, value: Any) -> None:
        if self._size < self._max_len:
            node = MutableListNode(value, None, self._head)

            if self._tail is None:
                self._tail = node

            self._head = node

            self._size += 1

        else:
            raise ValueError("List full!")

    def append_right(self, value: Any) -> None:
        if self._size < self._max_len:
            node = MutableListNode(value, self._tail, None)
            if self._head is None:
                self._head = node

            self._tail = node

            self._size += 1

        else:
            raise ValueError("List full!")

    def pop_left(self) -> Any:
        if self._head is None:
            raise ValueError("List Empty!")

        node = self._head
        data = node.data

        self._head = node.next_node

        if self._tail is node:
            self._tail = None

        self._size -= 1

        if node.previous_node is not None:
            node.previous_node.next_node = node.next_node
        if node.next_node is not None:
            node.next_node.previous_node = node.previous_node

        return data

    def pop_right(self) -> Any:
        if self._tail is None:
            raise ValueError("List Empty!")

        node = self._tail
        data = node.data

        self._tail = node.previous_node

        if self._head is node:
            self._head = None

        self._size -= 1

        if node.previous_node is not None:
            node.previous_node.next_node = node.next_node
        if node.next_node is not None:
            node.next_node.previous_node = node.previous_node

        return data

    def __getitem__(self, index: Union[slice, int]) -> Any:
        if isinstance(index, slice):
            if index.start == index.stop == index.step:
                return self

            else:
                _slice = index.indices(len(self))
                sliced = [self[i] for i in range(*_slice)]
                return self._from_sequence(max_len=self._max_len, seq=sliced)

        elif isinstance(index, int):
            return self.get_node(index).data

        else:
            raise TypeError("List index must be int or slice")


class MutableList(DoublyLinkedList, collections.abc.MutableSequence):
    def __init__(self, seq: Sequence = ()) -> None:
        self._head: Optional[MutableListNode] = None
        self._tail: Optional[MutableListNode] = None
        super().__init__()
        try:
            for val in seq:
                node = MutableListNode(val, self._tail, None)
                if self._head is None:
                    self._head = node

                self._tail = node

                self._size += 1
        except TypeError:
            raise TypeError("seq must be a sequence object")

    def append_left(self, value: Any) -> None:
        node = MutableListNode(value, None, self._head)

        if self._tail is None:
            self._tail = node

        self._head = node

        self._size += 1

    def append_right(self, value: Any) -> None:

        node = MutableListNode(value, self._tail, None)
        if self._head is None:
            self._head = node

        self._tail = node

        self._size += 1

    def pop_left(self) -> Any:
        if self._head is None:
            raise ValueError("List Empty!")

        node = self._head
        data = node.data

        self._head = node.next_node

        if self._tail is node:
            self._tail = None

        self._size -= 1

        if node.previous_node is not None:
            node.previous_node.next_node = node.next_node
        if node.next_node is not None:
            node.next_node.previous_node = node.previous_node

        return data

    def pop_right(self) -> Any:
        if self._tail is None:
            raise ValueError("List Empty!")

        node = self._tail
        data = node.data

        self._tail = node.previous_node

        if self._head is node:
            self._head = None

        self._size -= 1

        if node.previous_node is not None:
            node.previous_node.next_node = node.next_node
        if node.next_node is not None:
            node.next_node.previous_node = node.previous_node

        return data

    def __getitem__(self, index: Union[slice, int]) -> Any:
        if isinstance(index, slice):
            if index.start == index.stop == index.step:
                return self

            else:
                _slice = index.indices(len(self))
                sliced = [self[i] for i in range(*_slice)]
                return self._from_sequence(seq=sliced)

        elif isinstance(index, int):
            return self.get_node(index).data

        else:
            raise TypeError("List index must be int or slice")
