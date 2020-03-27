from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/contains-duplicate-ii/
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        >>> solution = Solution()
        >>> solution.containsNearbyDuplicate([1, 2, 3, 1], 3)
        True
        >>> solution.containsNearbyDuplicate([1, 0, 1, 1], 1)
        True
        >>> solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
        False
        """
        seen = {}
        for i, v in enumerate(nums):
            if v in seen:
                if abs(seen[v] - i) <= k:
                    return True
            seen[v] = i
        return False
