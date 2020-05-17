import math
from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/third-maximum-number/
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
        >>> solution = Solution()
        >>> solution.thirdMax([3, 2, 1])
        1
        >>> solution.thirdMax([3, 1])
        3
        >>> solution.thirdMax([2, 2, 3, 1])
        1
        >>> solution.thirdMax([2, 2, 1, 1])
        2
        >>> solution.thirdMax([3, 3, 3, 1])
        3
        >>> solution.thirdMax([3, 34, 5, 1])
        3
        >>> solution.thirdMax([1,2,3,4,5,6,7,8,9])
        7
        >>> solution.thirdMax([9,8,7,6,5,4,3,2,1])
        7
        """
        a = b = c = -math.inf
        for i in range(0, len(nums)):
            if nums[i] > a:
                c = b
                b = a
                a = nums[i]
            elif a > nums[i] > b:
                c = b
                b = nums[i]
            elif b > nums[i] > c:
                c = nums[i]
        if c > -math.inf:
            return c
        return a
