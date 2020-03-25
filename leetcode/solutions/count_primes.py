from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/count-primes/
class Solution:
    def countPrimes(self, n: int) -> int:
        """
        >>> solution = Solution()
        >>> solution.countPrimes(10)
        4
        >>> solution.countPrimes(2)
        0
        >>> solution.countPrimes(3)
        1
        >>> solution.countPrimes(4)
        2
        """
        if n <= 1:
            return 0
        ans = [1] * n
        ans[0] = 0
        ans[1] = 0
        for i in range(2, n):
            if ans[i]:
                j = 2
                while i * j < n:
                    ans[i * j] = 0
                    j += 1
        return sum(ans)
