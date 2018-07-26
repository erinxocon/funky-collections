from typing import Any, Callable, Generator, List, Optional, Sequence, Union

from .nodes import ImmutableListNode


class ImmutableFixedList:
    __slots__ = ("_max_len", "_size", "_head", "_tail")

    def __init__(self, max_len: int, *, seq: Sequence = None) -> None:
        if max_len <= 0:
            raise ValueError("Max lenth  must be more than 0")

        self._max_len = max_len
        self._size = 0
        self._head: Optional[ImmutableListNode] = None
        self._tail: Optional[ImmutableListNode] = None

        try:
            if seq is not None:
                for val in seq[0 : self._max_len]:
                    node = ImmutableListNode(val, self._tail, None)
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
            node = ImmutableListNode(value, None, self._head)

            if self._tail is None:
                self._tail = node

            self._head = node

            self._size += 1

        else:
            raise ValueError("Queue full!")

    def append_right(self, value: Any) -> None:
        if self._size < self._max_len:
            node = ImmutableListNode(value, self._tail, None)
            if self._head is None:
                self._head = node

            self._tail = node

            self._size += 1

        else:
            raise ValueError("Queue full!")

    def pop_left(self) -> Any:
        if self._head is None:
            raise ValueError("Queue Empty!")

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
            raise ValueError("Queue Empty!")

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
        data = f"{','.join(repr(x) for x in self)}"
        return f"<ImmutableFixedList size={self._size} max_size={self.max_len} data=[{data}]>"

    def __str__(self) -> str:
        data = f"{','.join(str(x) for x in self)}"
        return f"ImmutableFixedList({data})"

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

    def __getitem__(self, index: Union[slice, int]) -> Any:
        if isinstance(index, slice):
            if index.start == index.stop == index.step:
                return self

            else:
                _slice = index.indices(len(self))
                sliced = [self[i] for i in range(*_slice)]
                return ImmutableFixedList(self._max_len, seq=sliced)

        elif isinstance(index, int):
            return self.get_node(index).data

        else:
            raise TypeError("List index must be int or slice")
