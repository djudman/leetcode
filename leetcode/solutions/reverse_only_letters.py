from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/reverse-only-letters/
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        """
        >>> solution = Solution()
        >>> solution.reverseOnlyLetters('ab-cd')
        'dc-ba'
        >>> solution.reverseOnlyLetters('a-bC-dEf-ghIj')
        'j-Ih-gfE-dCba'
        >>> solution.reverseOnlyLetters('Test1ng-Leet=code-Q!')
        'Qedo1ct-eeLg=ntse-T!'
        """
        stack = []
        for i, char in enumerate(S):
            if char.isalpha():
                stack.append(char)
        out = []
        for char in S:
            if char.isalpha():
                out.append(stack.pop())
            else:
                out.append(char)
        return ''.join(out)


