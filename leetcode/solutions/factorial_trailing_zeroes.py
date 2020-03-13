from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/factorial-trailing-zeroes/
class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        >>> solution = Solution()
        >>> solution.trailingZeroes(3)
        0
        >>> solution.trailingZeroes(5)
        1
        """
        if n < 5:
            return 0
        res = 0
        while n > 0:
            n //= 5
            res += n
        return res
