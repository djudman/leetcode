from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/longest-palindrome/
class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        >>> solution = Solution()
        >>> solution.longestPalindrome('abccccdd')
        7
        >>> solution.longestPalindrome('abc')
        1
        >>> solution.longestPalindrome('abca')
        3
        >>> solution.longestPalindrome('abcA')
        1
        >>> solution.longestPalindrome('abcbbB')
        3
        >>> solution.longestPalindrome('bb')
        2
        """
        cnt_by_char = {}
        result = 0
        for char in s:
            cnt = cnt_by_char.get(char, 0) + 1
            if cnt % 2 == 0:
                result += 2
            cnt_by_char[char] = cnt
        return result if result == len(s) else result + 1
