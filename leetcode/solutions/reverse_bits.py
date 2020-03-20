from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/reverse-bits/
class Solution:
    def reverseBits(self, n: int) -> int:
        """
        >>> solution = Solution()
        >>> solution.reverseBits(43261596) # 10100101000001111010011100
        964176192
        >>> solution.reverseBits(4294967293) # 11111111111111111111111111111101
        3221225471
        """
        bits = []
        for i in range(32):
            bits.append(n % 2)
            n = n // 2
        out = 0
        for i, bit in enumerate(bits):
            out += bit * (2 ** (31 - i))
        return out
