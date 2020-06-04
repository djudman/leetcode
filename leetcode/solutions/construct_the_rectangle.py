import math
from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/construct-the-rectangle/
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        """
        >>> solution = Solution()
        >>> solution.constructRectangle(4)
        [2, 2]
        >>> solution.constructRectangle(16)
        [4, 4]
        >>> solution.constructRectangle(17)
        [17, 1]
        >>> solution.constructRectangle(12)
        [4, 3]
        >>> solution.constructRectangle(18)
        [6, 3]
        >>> solution.constructRectangle(24)
        [6, 4]
        >>> solution.constructRectangle(2)
        [2, 1]
        """
        W = int(math.sqrt(area))
        while area % W != 0:
            W -= 1
        L = area // W
        return [L, W]
