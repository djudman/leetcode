from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/isomorphic-strings/
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        >>> solution = Solution()
        >>> solution.isIsomorphic('egg', 'add')
        True
        >>> solution.isIsomorphic('foo', 'bar')
        False
        >>> solution.isIsomorphic('paper', 'title')
        True
        >>> solution.isIsomorphic('aa', 'aa')
        True
        >>> solution.isIsomorphic('aa', 'bb')
        True
        >>> solution.isIsomorphic('abc', 'cab')
        True
        >>> solution.isIsomorphic('abc', 'cbb')
        False
        >>> solution.isIsomorphic('ab', 'aa')
        False
        """
        if len(s) != len(t):
            return False
        alphabet = {}
        used = {}
        for i in range(len(s)):
            char = alphabet.get(s[i])
            if char and char != t[i]:
                return False
            if not char and t[i] in used:
                return False
            alphabet[s[i]] = t[i]
            used[t[i]] = True
        return True
