import math
from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/relative-ranks/
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        """
        >>> solution = Solution()
        >>> solution.findRelativeRanks([5, 4, 3, 2, 1])
        ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5']
        >>> solution.findRelativeRanks([4, 2, 5, 1, 3])
        ['Silver Medal', '4', 'Gold Medal', '5', 'Bronze Medal']
        """
        scores = sorted(nums, reverse=True)
        rewards = {}
        for i, score in enumerate(scores):
            if i == 0:
                reward = 'Gold Medal'
            elif i == 1:
                reward = 'Silver Medal'
            elif i == 2:
                reward = 'Bronze Medal'
            else:
                reward = str(i + 1)
            rewards[score] = reward
        return [rewards[score] for score in nums]
