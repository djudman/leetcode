from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/add-strings/
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        >>> solution = Solution()
        >>> solution.addStrings('2', '3')
        '5'
        >>> solution.addStrings('9', '1')
        '10'
        >>> solution.addStrings('99', '3')
        '102'
        >>> solution.addStrings('99', '00003')
        '102'
        >>> solution.addStrings('99', '90')
        '189'
        >>> solution.addStrings('99', '99')
        '198'
        >>> solution.addStrings('99', '0')
        '99'
        >>> solution.addStrings('0', '0')
        '0'
        """
        out = []
        inc = 0
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        j = len(num2) - 1
        for i in range(len(num1) - 1, -1, -1):
            d1 = int(num1[i])
            if j >= 0:
                d2 = int(num2[j])
                j -= 1
            else:
                d2 = 0
            s = d1 + d2 + inc
            if s > 9:
                s = s % 10
                inc = 1
            else:
                inc = 0
            out.insert(0, str(s))
        if inc > 0:
            out.insert(0, str(inc))
        while len(out) > 1 and out[0] == '0':
            out.pop(0)
        return ''.join(out)
