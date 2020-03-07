from typing import List, Optional

from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/min-stack/
class MinStack:
    """
    >>> s = MinStack()
    >>> s.push(-2)
    >>> s.push(0)
    >>> s.push(-3)
    >>> s.getMin()
    -3
    >>> s.pop()
    >>> s.top()
    0
    >>> s.getMin()
    -2
    """

    def __init__(self):
        self._data = []
        self._min = []

    def push(self, x: int) -> None:
        self._data.append(x)
        min_value = min(self._min[-1], x) if self._min else x
        self._min.append(min_value)

    def pop(self) -> None:
        self._data.pop()
        self._min.pop()

    def top(self) -> int:
        return self._data[-1]

    def getMin(self) -> int:
        return self._min[-1]
