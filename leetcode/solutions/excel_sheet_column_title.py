from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/excel-sheet-column-title/
class Solution:
    def convertToTitle(self, n: int) -> str:
        """
        >>> solution = Solution()
        >>> solution.convertToTitle(1)
        'A'
        >>> solution.convertToTitle(28)
        'AB'
        >>> solution.convertToTitle(701)
        'ZY'
        >>> solution.convertToTitle(702)
        'ZZ'
        >>> solution.convertToTitle(703)
        'AAA'
        >>> solution.convertToTitle(704)
        'AAB'
        """
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        cnt = len(alphabet)
        n = n - 1
        if n < cnt:
            return alphabet[n]
        out = []
        while n // cnt > 0:
            out.append(self.convertToTitle(n // cnt))
            n = n - (n // cnt * cnt)
        out.append(alphabet[n])
        return ''.join(out)
