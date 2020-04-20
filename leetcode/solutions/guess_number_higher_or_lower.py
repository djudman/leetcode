from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/guess-number-higher-or-lower/
def guess(num: int) -> int:
    target = 6
    if num == target:
        return 0
    return -1 if num > target else 1


class Solution:
    def guessNumber(self, n: int) -> int:
        """
        >>> solution = Solution()
        >>> solution.guessNumber(20)
        6
        >>> solution.guessNumber(6)
        6
        >>> solution.guessNumber(100)
        6
        >>> solution.guessNumber(203)
        6
        >>> solution.guessNumber(20)
        6
        >>> solution.guessNumber(10)
        6
        """
        return self.findNumber(0, n + 1)

    def findNumber(self, begin: int, end: int) -> int:
        v = begin + (end - begin) // 2
        found = guess(v)
        if found == 0:
            return v
        if found < 0:
            end = v
        else:
            begin = v
        return self.findNumber(begin, end)
