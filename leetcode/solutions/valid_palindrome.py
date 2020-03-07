import string
from typing import List, Optional

from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        >>> solution = Solution()
        >>> solution.isPalindrome('A man, a plan, a canal: Panama')
        True
        >>> solution.isPalindrome('race a car')
        False
        >>> solution.isPalindrome('')
        True
        >>> solution.isPalindrome('0P')
        False
        """
        if not s:
            return True
        arr = []
        for char in s:
            char = char.lower()
            if 'a' <= char <= 'z' or '0' <= char <= '9':
                arr.append(char)
        i = 0
        j = len(arr) - 1
        while i < j:
            if arr[i] != arr[j]:
                return False
            i += 1
            j -= 1
        return True


