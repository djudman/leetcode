from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/range-sum-query-immutable/
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = []
        s = 0
        [self.sums.append(s := s + v) for v in nums]

    def sumRange(self, i: int, j: int) -> int:
        """
        >>> obj = NumArray([1,2,3,4,5,6,7,8,9])
        >>> obj.sumRange(0, 1)
        3
        >>> obj.sumRange(0, 5)
        21
        """
        return self.sums[j] - self.sums[i] + self.nums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
