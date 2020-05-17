from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/number-of-segments-in-a-string/
class Solution:
    def countSegments(self, s: str) -> int:
        """
        >>> solution = Solution()
        >>> solution.countSegments('')
        0
        >>> solution.countSegments('  ')
        0
        >>> solution.countSegments(' ')
        0
        >>> solution.countSegments('a')
        1
        >>> solution.countSegments('a   ')
        1
        >>> solution.countSegments('abc')
        1
        >>> solution.countSegments('abc a')
        2
        >>> solution.countSegments(' abc a  ')
        2
        >>> solution.countSegments(' abc a wwe ')
        3
        >>> solution.countSegments('Hello, my name is John')
        5
        >>> solution.countSegments(', , , ,        a, eaefa')
        6
        """
        words = 0
        cnt = len(s)
        for i in range(cnt):
            if s[i] != ' ':
                if i == cnt - 1 or s[i + 1] == ' ':
                    words += 1
        return words
