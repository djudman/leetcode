from typing import List, Optional

from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        >>> solution = Solution()
        >>> solution.maxProfit([7, 1, 5, 3, 6, 4])
        7
        >>> solution.maxProfit([1, 2, 3, 4, 5])
        4
        >>> solution.maxProfit([7, 6, 4, 3, 1])
        0
        >>> solution.maxProfit([1, 2, 9, 1, 2])
        9
        >>> solution.maxProfit([11, 2, 9, 1, 2])
        8
        """
        s = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                s += prices[i] - prices[i - 1]
        return s
