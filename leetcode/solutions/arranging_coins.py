import math
from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/arranging-coins/
class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        >>> solution = Solution()
        >>> solution.arrangeCoins(0)
        0
        >>> solution.arrangeCoins(1)
        1
        >>> solution.arrangeCoins(2)
        1
        >>> solution.arrangeCoins(3)
        2
        >>> solution.arrangeCoins(5)
        2
        >>> solution.arrangeCoins(6)
        3
        >>> solution.arrangeCoins(8)
        3
        """
        # D = 1 + 8n
        # x = (-1 + math.sqrt(1 + 8n)) / 2
        return int((-1 + math.sqrt(1 + 8 * n)) / 2)
        # cnt = 0
        # current_row = 0
        # while n > 0:
        #     current_row += 1
        #     n -= current_row
        #     if n >= 0:
        #         cnt += 1
        # return cnt
