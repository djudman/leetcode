from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/is-subsequence/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        >>> solution = Solution()
        >>> solution.isSubsequence('a', 'a')
        True
        >>> solution.isSubsequence('a', 'ba')
        True
        >>> solution.isSubsequence('ax', 'ba')
        False
        >>> solution.isSubsequence('abc', 'ahbgdc')
        True
        >>> solution.isSubsequence('axc', 'ahbgdc')
        False
        >>> solution.isSubsequence('axc', 'ahbgdcxdbg')
        False
        >>> solution.isSubsequence('', 'a')
        True
        """
        j = 0
        cnt = len(s)
        if not s:
            return True
        for char in t:
            if char == s[j]:
                j += 1
            if j == cnt:
                return True
        return False
