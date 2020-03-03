from typing import List, Optional

from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        >>> solution = Solution()
        >>> solution.generate(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        >>> solution.generate(6)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
        >>> solution.generate(3)
        [[1], [1, 1], [1, 2, 1]]
        >>> solution.generate(0)
        []
        >>> solution.generate(1)
        [[1]]
        """
        result = []
        for i in range(numRows):
            row = [1]
            if i - 1 >= 0:
                for j in range(i - 1):
                    prev_row = result[i - 1]
                    s = prev_row[j] + prev_row[j + 1]
                    row.append(s)
                row.append(1)
            result.append(row)
        return result
