from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/peak-index-in-a-mountain-array/
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        """
        >>> solution = Solution()
        >>> solution.peakIndexInMountainArray([0, 1, 0])
        1
        >>> solution.peakIndexInMountainArray([0, 1, 2, 0])
        2
        >>> solution.peakIndexInMountainArray([0, 1, 2, 3, 5, 2, 0])
        4
        >>> solution.peakIndexInMountainArray([0, 5, 4, 3, 2, 1, 0])
        1
        """
        cnt = len(A)
        for i in range(1, cnt - 1):
            if A[i - 1] < A[i] > A[i + 1]:
                return i
