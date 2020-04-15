from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/reverse-vowels-of-a-string/
class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        >>> solution = Solution()
        >>> solution.reverseVowels('leetcode')
        'leotcede'
        >>> solution.reverseVowels('hello')
        'holle'
        >>> solution.reverseVowels('doh')
        'doh'
        >>> solution.reverseVowels('Ae')
        'eA'
        >>> solution.reverseVowels('xxx')
        'xxx'
        """
        # The vowels does not include the letter "y".
        vowels = 'aeiou'
        vowels = vowels + vowels.upper()
        s = [char for char in s]
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and s[i] not in vowels:
                i += 1
            while i < j and s[j] not in vowels:
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return ''.join(s)
