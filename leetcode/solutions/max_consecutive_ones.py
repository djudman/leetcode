from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/max-consecutive-ones/
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        >>> solution = Solution()
        >>> solution.findMaxConsecutiveOnes([1,1,0,1,1,1])
        3
        """
        out = []
        cnt = 0
        for n in nums:
            if n == 0:
                out.append(cnt)
                cnt = 0
            else:
                cnt += 1
        out.append(cnt)
        return max(out)
