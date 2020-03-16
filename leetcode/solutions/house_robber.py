from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/house-robber/
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        >>> solution = Solution()
        >>> solution.rob([1,2,3,1])
        4
        >>> solution.rob([2,7,9,3,1])
        12
        >>> solution.rob([2,1,1,2])
        4
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        out = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            out.append(max(out[i - 1], out[i - 2] + nums[i]))
        return out[-1]
