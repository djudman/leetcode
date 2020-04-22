from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/ransom-note/
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        >>> solution = Solution()
        >>> solution.canConstruct('aa', 'bb')
        False
        >>> solution.canConstruct('aa', 'ab')
        False
        >>> solution.canConstruct('aa', 'aab')
        True
        """
        ransom_note_chars = {}
        for char in ransomNote:
            if char not in ransom_note_chars:
                ransom_note_chars[char] = 0
            ransom_note_chars[char] += 1
        for char in magazine:
            if char in ransom_note_chars:
                ransom_note_chars[char] -= 1
                if ransom_note_chars[char] == 0:
                    del ransom_note_chars[char]
        return len(ransom_note_chars) == 0
