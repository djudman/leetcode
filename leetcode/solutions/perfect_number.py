import math
from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/perfect-number/
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        """
        >>> solution = Solution()
        >>> solution.checkPerfectNumber(28)
        True
        >>> solution.checkPerfectNumber(1)
        False
        >>> solution.checkPerfectNumber(-6)
        False
        >>> solution.checkPerfectNumber(0)
        False
        """
        if num <= 0:
            return False
        s = 0
        for i in range(1, int(math.sqrt(num) + 1)):
            if i != num:
                res = num % i
                if res == 0:
                    s += i
                    divisor = num // i
                    if divisor != num:
                        s += divisor
                if s > num:
                    return False
        return s == num
