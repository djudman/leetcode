from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/rotate-array/
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        >>> solution = Solution()
        >>> nums = [1,2,3,4,5,6,7]
        >>> solution.rotate(nums, 3)
        >>> nums
        [5, 6, 7, 1, 2, 3, 4]
        >>> nums = [-1,-100,3,99]
        >>> solution.rotate(nums, 2)
        >>> nums
        [3, 99, -1, -100]
        >>> nums = [-1]
        >>> solution.rotate(nums, 2)
        >>> nums
        [-1]
        >>> nums = [1,2,3]
        >>> solution.rotate(nums, 4)
        >>> nums
        [3, 1, 2]
        """
        if not nums:
            return
        n = len(nums)
        if k > n:
            k = k % n
        nums = self.reverse(nums, 0, n - 1)
        nums = self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    def reverse(self, nums: List[int], i, j) -> List:
        while i >= 0 and j < len(nums) and i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return nums
