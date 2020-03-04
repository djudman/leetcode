from typing import List, Optional

from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/pascals-triangle-ii/
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        >>> solution = Solution()
        >>> solution.getRow(0)
        [1]
        >>> solution.getRow(1)
        [1, 1]
        >>> solution.getRow(2)
        [1, 2, 1]
        >>> solution.getRow(3)
        [1, 3, 3, 1]
        >>> solution.getRow(4)
        [1, 4, 6, 4, 1]
        >>> solution.getRow(5)
        [1, 5, 10, 10, 5, 1]
        """
        if rowIndex < 0:
            return []
        row = [1]
        if rowIndex == 0:
            return row
        for i in range(1, rowIndex + 1):
            prev_row = row.copy()
            row.append(1)
            for j in range(1, i):
                row[j] = prev_row[j - 1] + prev_row[j]
        return row


