from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/lemonade-change/
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        >>> solution = Solution()
        >>> solution.lemonadeChange([5, 5, 5, 10, 20])
        True
        >>> solution.lemonadeChange([5, 5, 10])
        True
        >>> solution.lemonadeChange([10, 10])
        False
        >>> solution.lemonadeChange([5, 10, 5, 20])
        True
        >>> solution.lemonadeChange([5, 5, 10, 10, 20])
        False
        >>> solution.lemonadeChange([5, 5, 10, 5, 20, 10, 5, 10])
        True
        """
        change = []
        cost = 5
        for bill in bills:
            need_change = bill - cost
            i = len(change) - 1
            while need_change > 0:
                if not change or i < 0:
                    return False
                val = change[i]
                if val <= need_change:
                    need_change -= val
                    change.remove(val)
                i -= 1
            change.append(bill)
            change.sort()
        return True