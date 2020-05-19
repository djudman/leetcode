from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/island-perimeter/
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        >>> solution = Solution()
        >>> solution.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
        16
        >>> solution.islandPerimeter([[0,1]])
        4
        """
        out = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    out += self.count(grid, i, j, len(grid), len(grid[i]))
        return out

    def count(self, grid, row, col, n, m):
        out = 0
        if row - 1 < 0 or grid[row - 1][col] == 0:
            out += 1
        if row + 1 >= n or grid[row + 1][col] == 0:
            out += 1
        if col - 1 < 0 or grid[row][col - 1] == 0:
            out += 1
        if col + 1 >= m or grid[row][col + 1] == 0:
            out += 1
        return out
