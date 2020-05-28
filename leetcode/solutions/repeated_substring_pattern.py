from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/repeated-substring-pattern/
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        >>> solution = Solution()
        >>> solution.repeatedSubstringPattern('aaa')
        True
        >>> solution.repeatedSubstringPattern('aba')
        False
        >>> solution.repeatedSubstringPattern('ababab')
        True
        >>> solution.repeatedSubstringPattern('abababc')
        False
        >>> solution.repeatedSubstringPattern('abababa')
        False
        >>> solution.repeatedSubstringPattern('ababcababc')
        True
        """
        n = len(s)
        for i in range(n // 2):
            x = s[:(i + 1)]
            if x * (n // len(x)) == s:
                return True
        return False
