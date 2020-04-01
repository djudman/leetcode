from collections import deque
from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/implement-stack-using-queues/
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._queue = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self._queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        for i in range(len(self._queue) - 1):
            self.push(self._queue.popleft())
        return self._queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        size = len(self._queue)
        value = None
        for i in range(size):
            value = self._queue.popleft()
            self.push(value)
        return value

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self._queue) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


class Solution:
    def solve(self) -> None:
        """
        >>> stack = MyStack()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.top()
        2
        >>> stack.pop()
        2
        >>> stack.empty()
        False
        """
        pass
