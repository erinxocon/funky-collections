from typing import Any, Generator, List, Optional, Sequence, Union


class ListNode:
    __slots__ = ("_data", "_prev", "_next")

    def __init__(
        self, data: Any, prev: Optional["ListNode"], _next: Optional["ListNode"]
    ) -> None:
        self._data = data
        self._prev = prev
        self._next = _next

        if prev is not None:
            prev._next = self
        if _next is not None:
            _next._prev = self

    def __repr__(self) -> str:
        return f"<ListNode(data={self.data!r} _prev={self._prev}, _next={self._next})>"

    def __str__(self) -> str:
        return f"ListNode({self.data})"

    @property
    def data(self) -> Any:
        return self._data

    @property
    def previous_node(self) -> Optional["ListNode"]:
        return self._prev

    @previous_node.setter
    def previous_node(self, value: "ListNode") -> None:
        self._prev = value

    @property
    def next_node(self) -> Optional["ListNode"]:
        return self._next

    @next_node.setter
    def next_node(self, value: "ListNode") -> None:
        self._next = value
