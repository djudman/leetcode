from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        >>> solution = Solution()
        >>> solution.findDisappearedNumbers([1,1])
        [2]
        >>> solution.findDisappearedNumbers([2,4,2,1])
        [3]
        >>> solution.findDisappearedNumbers([2,2,2,2])
        [1, 3, 4]
        >>> solution.findDisappearedNumbers([4,2,1,2])
        [3]
        >>> solution.findDisappearedNumbers([4,3,2,7,8,2,3,1])
        [5, 6]
        """
        for i, v in enumerate(nums):
            while nums[i] != (i + 1):
                j = nums[i] - 1
                if nums[i] == nums[j]:
                    break
                nums[i], nums[j] = nums[j], nums[i]
        return [i + 1 for i, v in enumerate(nums) if v != (i + 1)]


