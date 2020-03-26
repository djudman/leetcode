from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        >>> solution = Solution()
        >>> solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6
        >>> solution.maxSubArray([-2, -1, -3])
        -1
        >>> solution.maxSubArray([])
        0
        >>> solution.maxSubArray([3])
        3
        >>> solution.maxSubArray([-2, 1])
        1
        """
        if not nums:
            return 0
        max_sum = 0
        current_sum = 0
        start = current_start = end = 0
        local_max = nums[0]
        for i in range(len(nums)):
            if nums[i] > local_max:
                local_max = nums[i]
            current_sum += nums[i]
            if current_sum < 0:
                current_sum = 0
                current_start = i + 1
            if current_sum > max_sum:
                max_sum = current_sum
                start = current_start
                end = i
        if start == end == 0:
            return local_max
        return sum([nums[i] for i in range(start, end + 1)])
