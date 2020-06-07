from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/base-7/
class Solution:
    def convertToBase7(self, num: int) -> str:
        """
        >>> solution = Solution()
        >>> solution.convertToBase7(100)
        '202'
        >>> solution.convertToBase7(-7)
        '-10'
        """
        base = 7
        out = []
        sign = 1
        if num < 0:
            sign = -1
            num *= sign
        while num >= base:
            x = num // base
            rest = num % (x * base)
            out.insert(0, str(rest))
            num = x
        out.insert(0, str(num))
        if sign < 0:
            out.insert(0, '-')
        return ''.join(out)
