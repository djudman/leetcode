from typing import List, Optional

from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        >>> solution = Solution()
        >>> solution.maxProfit([8, 2, 7, 4, 3, 2, 9])
        7
        >>> solution.maxProfit([7, 1, 5, 3, 6, 4])
        5
        >>> solution.maxProfit([1, 9, 8, 7, 6, 5])
        8
        >>> solution.maxProfit([9, 3, 2, 7, 1, 2])
        5
        >>> solution.maxProfit([7, 6, 4, 3, 1])
        0
        >>> solution.maxProfit([])
        0
        >>> solution.maxProfit([1])
        0
        >>> solution.maxProfit([1, 2])
        1
        >>> solution.maxProfit([2, 1])
        0
        >>> solution.maxProfit([1, 2, 3, 4])
        3
        """
        j = 0
        s = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[j]:
                j = i
            s = max(s, prices[i] - prices[j])
        return s
