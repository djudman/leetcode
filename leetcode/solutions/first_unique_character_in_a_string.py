from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        >>> solution = Solution()
        >>> solution.firstUniqChar('a')
        0
        >>> solution.firstUniqChar('aa')
        -1
        >>> solution.firstUniqChar('aababba')
        -1
        >>> solution.firstUniqChar('xzbabbx')
        1
        >>> solution.firstUniqChar('aadadaad')
        -1
        """
        char_map = {}
        for char in s:
            if char not in char_map:
                char_map[char] = 0
            char_map[char] += 1
        for i, char in enumerate(s):
            if char_map[char] == 1:
                return i
        return -1
