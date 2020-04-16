from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/intersection-of-two-arrays/
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        >>> solution = Solution()
        >>> solution.intersection([1,2,2,1], [2,2])
        [2]
        >>> solution.intersection([4,9,5], [9,4,9,8,4])
        [9, 4]
        """
        nums_map = {x: False for x in nums2}
        nums_map.update({x: True for x in nums1 if x in nums_map})
        return [x for x, v in nums_map.items() if v]
