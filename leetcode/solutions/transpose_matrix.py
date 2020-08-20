from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/transpose-matrix/
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        """
        >>> solution = Solution()
        >>> solution.transpose([[1,2,3],[4,5,6],[7,8,9]])
        [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        >>> solution.transpose([[1,2,3,0],[4,5,6,0],[7,8,9,0]])
        [[1, 4, 7], [2, 5, 8], [3, 6, 9], [0, 0, 0]]
        """
        T = []
        cnt = len(A[0])
        [T.append([None] * len(A)) for _ in range(cnt)]
        for i in range(len(A)):
            for j in range(len(A[0])):
                T[j][i] = A[i][j]
        return T

