from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/intersection-of-two-arrays-ii/
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        >>> solution = Solution()
        >>> solution.intersect([1,2,2,1], [2,2])
        [2, 2]
        >>> solution.intersect([4,9,5], [9,4,9,8,4])
        [4, 9]
        """
        result = []
        cnt_by_value = {}
        for v in nums2:
            if v not in cnt_by_value:
                cnt_by_value[v] = 0
            cnt_by_value[v] += 1
        for v in nums1:
            if cnt_by_value.get(v, 0) > 0:
                result.append(v)
                cnt_by_value[v] -= 1
        return result
