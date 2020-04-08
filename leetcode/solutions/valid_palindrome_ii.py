from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/valid-palindrome-ii/
class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        >>> solution = Solution()
        >>> solution.validPalindrome('aba')
        True
        >>> solution.validPalindrome('abca')
        True
        >>> solution.validPalindrome('abcb')
        True
        >>> solution.validPalindrome('abc')
        False
        >>> solution.validPalindrome('abcbax')
        True
        >>> solution.validPalindrome('axbcba')
        True
        >>> solution.validPalindrome('abxcba')
        True
        """
        def isPalindrome(i, j, cutted=False):
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                elif not cutted:
                    return isPalindrome(i + 1, j, True) or isPalindrome(i, j - 1, True)
                else:
                    return False
            return True

        return isPalindrome(0, len(s) - 1)
