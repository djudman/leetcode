from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/sort-array-by-parity/
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        """
        >>> solution = Solution()
        >>> solution.sortArrayByParity([1, 2, 3, 4])
        [4, 2, 3, 1]
        >>> solution.sortArrayByParity([2, 4, 6])
        [2, 4, 6]
        """
        start = 0
        end = len(A) - 1
        while start < end:
            while A[start] % 2 != 0:
                A[start], A[end] = A[end], A[start]
                end -= 1
                if start >= end:
                    break
            start += 1
        return A
