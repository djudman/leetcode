from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/buddy-strings/
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        """
        >>> solution = Solution()
        >>> solution.buddyStrings('ab', 'ba')
        True
        >>> solution.buddyStrings('ab', 'ab')
        False
        >>> solution.buddyStrings('axz', 'abc')
        False
        >>> solution.buddyStrings('aa', 'aa')
        True
        >>> solution.buddyStrings('abc', 'abc')
        False
        >>> solution.buddyStrings('aaaaaaabc', 'aaaaaaacb')
        True
        >>> solution.buddyStrings('aabc', 'aabc')
        True
        >>> solution.buddyStrings('', 'aa')
        False
        >>> solution.buddyStrings('abcd', 'acdb')
        False
        """
        cnt = len(A)
        if cnt != len(B):
            return False
        chars = {}
        has_repeated_char = False
        diff = 0
        for i, char in enumerate(A):
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1
            has_repeated_char = has_repeated_char or chars[char] > 1
            diff += 1 if char != B[i] else 0
        for char in B:
            if char not in chars:
                return False
            chars[char] -= 1
            if chars[char] == 0:
                del chars[char]
        if chars or diff > 2:
            return False
        return A != B or has_repeated_char
