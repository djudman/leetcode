import math
from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        """
        >>> solution = Solution()
        >>> solution.minMoves([1,2,3])
        3
        >>> solution.minMoves([2, 3, 2])
        1
        >>> solution.minMoves([2, 3, 5])
        4
        >>> solution.minMoves([1])
        0
        >>> solution.minMoves([1, 1, 1])
        0
        >>> solution.minMoves([1, 1, 1])
        0
        """
        min_value = math.inf
        for v in nums:
            if v < min_value:
                min_value = v
        s = 0
        for v in nums:
            s += v - min_value
        return s
