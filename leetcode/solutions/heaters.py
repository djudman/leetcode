from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/heaters/
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        """
        >>> solution = Solution()
        >>> solution.findRadius([1,2,3], [2])
        1
        >>> solution.findRadius([1,2,3,4], [1,4])
        1
        >>> solution.findRadius([1,2,3,4], [1])
        3
        >>> solution.findRadius([1,2,3,4], [2])
        2
        >>> solution.findRadius([1,4], [2])
        2
        >>> solution.findRadius([0,2,3,4], [5])
        5
        >>> solution.findRadius([0,2,3,4], [1, 5])
        2
        >>> solution.findRadius([0,100], [1,50,80,100])
        1
        """
        houses.sort()
        heaters.sort()

        j = 0
        out = []
        for house in houses:
            while j < len(heaters) and house > heaters[j]:
                j += 1
            min_distance = abs(heaters[j - 1] - house)
            if j < len(heaters):
                min_distance = min(min_distance, abs(house - heaters[j]))
            out.append(min_distance)
        return max(out)
