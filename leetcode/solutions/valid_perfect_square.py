from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/valid-perfect-square/
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        >>> solution = Solution()
        >>> solution.isPerfectSquare(16)
        True
        >>> solution.isPerfectSquare(81)
        True
        >>> solution.isPerfectSquare(9)
        True
        >>> solution.isPerfectSquare(14)
        False
        >>> solution.isPerfectSquare(101)
        False
        >>> solution.isPerfectSquare(1)
        True
        """
        for i in range(num + 1):
            square = i * i
            if square == num:
                return True
            if square > num:
                return False
