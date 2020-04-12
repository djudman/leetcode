from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/power-of-four/
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        """
        >>> solution = Solution()
        >>> solution.isPowerOfFour(4)
        True
        >>> solution.isPowerOfFour(1)
        True
        >>> solution.isPowerOfFour(16)
        True
        >>> solution.isPowerOfFour(17)
        False
        >>> solution.isPowerOfFour(5)
        False
        """
        if num == 0:
            return False
        if num == 1:
            return True
        # 1) check that only one bit is set.
        # 2) Why 0xAAAAAAAA ? This is because the bit representation is of \
        # powers of 2 that are not of 4. Like 2, 8, 32 so on..
        return num & (num - 1) == 0 and \
               num & int('0xAAAAAAAA', 16) == 0
