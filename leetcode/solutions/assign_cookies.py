from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/assign-cookies/
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        >>> solution = Solution()
        >>> solution.findContentChildren([1,2,3], [1,1])
        1
        >>> solution.findContentChildren([1,2], [1,2,3])
        2
        >>> solution.findContentChildren([3,4,2,3,1,4], [3,2,2])
        3
        >>> solution.findContentChildren([3,4,2,3,1,4], [])
        0
        >>> solution.findContentChildren([], [1,2])
        0
        >>> solution.findContentChildren([4, 3, 3, 2, 2, 2], [3, 2, 3])
        3
        """
        children = sorted(g, reverse=True)
        cookie = sorted(s, reverse=True)
        out = 0
        i, j = 0, 0
        while i < len(children) and j < len(cookie):
            if children[i] <= cookie[j]:
                j += 1
            i += 1
        return j
