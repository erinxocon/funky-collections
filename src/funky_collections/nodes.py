import abc
from typing import Any, Generator, List, Optional, Sequence, Union


class ListNodeBase:
    __slots__ = ("_data", "_prev", "_next")

    def __init__(self, data: Any, prev: Any, _next: Any) -> None:
        self._data = data
        self._prev = prev
        self._next = _next

        if prev is not None:
            prev._next = self
        if _next is not None:
            _next._prev = self

    @property  # type: ignore
    @abc.abstractproperty
    def data(self) -> Any:
        """retrieve data from the node"""

    @data.setter  # type: ignore
    @abc.abstractproperty
    def data(self, value: Any) -> None:
        """set the node's data attribute"""

    @property
    def previous_node(self) -> Any:
        return self._prev

    @previous_node.setter
    def previous_node(self, value: "ListNodeBase") -> None:
        self._prev = value

    @property
    def next_node(self) -> Any:
        return self._next

    @next_node.setter
    def next_node(self, value: "ListNodeBase") -> None:
        self._next = value

    def __repr__(self) -> str:
        return f"<ListNode(data={self.data!r} _prev={self._prev}, _next={self._next})>"

    def __str__(self) -> str:
        return f"ListNode({self.data})"


class ImmutableListNode(ListNodeBase):
    def __init__(
        self,
        data: Any,
        prev: Optional["ImmutableListNode"],
        _next: Optional["ImmutableListNode"],
    ) -> None:
        super().__init__(data, prev, _next)

    @property
    def data(self) -> Any:
        return self._data


class MutableListNode(ListNodeBase):
    def __init__(
        self,
        data: Any,
        prev: Optional["MutableListNode"],
        _next: Optional["MutableListNode"],
    ) -> None:
        super().__init__(data, prev, _next)

    @property
    def data(self) -> Any:
        return self._data

    @data.setter
    def data(self, value: Any) -> None:
        self._data = value
