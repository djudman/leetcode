from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/nim-game/
class Solution:
    def solve(self, n: int) -> bool:
        """
        >>> solution = Solution()
        >>> solution.solve(4)
        False
        >>> solution.solve(5)
        True
        """
        return n % 4 != 0
