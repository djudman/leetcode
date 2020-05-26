from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/next-greater-element-i/
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        >>> solution = Solution()
        >>> solution.nextGreaterElement([4,1,2], [1,3,4,2])
        [-1, 3, -1]
        >>> solution.nextGreaterElement([2,4], [1,2,3,4])
        [3, -1]
        """
        out = []
        for a1 in nums1:
            for i, a2 in enumerate(nums2):
                if a1 == a2:
                    j = i + 1
                    while j < len(nums2):
                        if nums2[j] > a2:
                            out.append(nums2[j])
                            break
                        j += 1
                    else:
                        out.append(-1)
        return out
