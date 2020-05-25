from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/number-of-boomerangs/
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        """
        >>> solution = Solution()
        >>> solution.numberOfBoomerangs([[0,0], [1,0], [2,0]])
        2
        >>> solution.numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]])
        20
        """
        out = 0
        for i in range(0, len(points)):
            cnt_by_sum = {}
            p0 = points[i]
            for j in range(0, len(points)):
                p1 = points[j]
                d = (p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2
                if d not in cnt_by_sum:
                    cnt_by_sum[d] = 0
                cnt_by_sum[d] += 1
            for s, cnt in cnt_by_sum.items():
                if cnt > 1:
                    out += cnt * (cnt - 1)
        return out
