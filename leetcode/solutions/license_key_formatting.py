from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/license-key-formatting/
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        """
        >>> solution = Solution()
        >>> solution.licenseKeyFormatting("5F3Z-2e-9-w", 4)
        '5F3Z-2E9W'
        >>> solution.licenseKeyFormatting("2-5g-3-J", 2)
        '2-5G-3J'
        """
        groups = []
        group = []
        j = 0
        for s in S[::-1]:
            if s == '-':
                continue
            j += 1
            group.insert(0, s.upper())
            if j % K == 0:
                groups.insert(0, ''.join(group))
                group = []
        if group:
            groups.insert(0, ''.join(group))
        return '-'.join(groups)
