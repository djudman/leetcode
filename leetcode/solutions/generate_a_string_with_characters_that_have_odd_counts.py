from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/
class Solution:
    def generateTheString(self, n: int) -> str:
        """
        >>> solution = Solution()
        >>> solution.generateTheString(4)
        'aaab'
        >>> solution.generateTheString(5)
        'aaaaa'
        """
        if n % 2 == 0:
            s = 'a' * (n - 1) + 'b'
        else:
            s = 'a' * n
        return s
