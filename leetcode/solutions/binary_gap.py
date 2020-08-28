from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/binary-gap/
class Solution:
    def binaryGap(self, N: int) -> int:
        """
        >>> solution = Solution()
        >>> solution.binaryGap(5)
        2
        >>> solution.binaryGap(6)
        1
        >>> solution.binaryGap(8)
        0
        >>> solution.binaryGap(194)
        5
        """
        bits = bin(N)[2:]
        indexes = [i for i, bit in enumerate(bits) if bit == '1']
        max_distance = 0
        prev = indexes[0]
        for i in indexes[1:]:
            d = i - prev
            if d > max_distance:
                max_distance = d
            prev = i
        return max_distance

