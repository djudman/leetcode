from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/sum-of-two-integers/
class Solution:
    def getSum(self, x: int, y: int) -> int:
        """
        >>> solution = Solution()
        >>> solution.getSum(1, 2)
        3
        """

        # while (y != 0):
        #     z = x & y
        #     x = x ^ y
        #     y = z << 1
        # return x
        return sum([x, y])
