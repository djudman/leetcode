from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


def isBadVersion(version: int) -> bool:
    return version > 5

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


# https://leetcode.com/problems/first-bad-version/
class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        >>> solution = Solution()
        >>> solution.firstBadVersion(16)
        6
        >>> solution.firstBadVersion(2506)
        6
        """
        left = 1
        right = n
        if isBadVersion(left):
            return left
        if not isBadVersion(n):
            return -1
        while abs(left - right) > 1:
            x = left + (right - left) // 2
            if isBadVersion(x):
                right = x
            else:
                left = x
        return right
