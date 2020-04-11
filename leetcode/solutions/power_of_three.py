from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/power-of-three/
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        >>> solution = Solution()
        >>> solution.isPowerOfThree(0)
        False
        >>> solution.isPowerOfThree(27)
        True
        >>> solution.isPowerOfThree(27)
        True
        >>> solution.isPowerOfThree(45)
        False
        >>> solution.isPowerOfThree(1)
        True
        """
        if n == 1:
            return True
        while n > 3:
            if n % 3 != 0:
                return False
            n = n // 3
        return n == 3
