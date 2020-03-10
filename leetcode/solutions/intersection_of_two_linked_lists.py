from typing import List, Optional

from leetcode.utils.tree import TreeNode, make_binary_tree
from leetcode.utils.list import ListNode, make_linked_list


# https://leetcode.com/problems/intersection-of-two-linked-lists/
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        >>> solution = Solution()
        >>> headA = make_linked_list([4, 1, 8, 4, 5])
        >>> headB = make_linked_list([5, 0, 1, 8, 4, 5])
        >>> solution.getIntersectionNode(headA, headB)
        [1, 8, 4, 5]
        >>> headA = make_linked_list([0, 9, 1, 2, 4])
        >>> headB = make_linked_list([3, 2, 4])
        >>> solution.getIntersectionNode(headA, headB)
        [2, 4]
        """
        if not headA or not headB:
            return
        curA = headA
        curB = headB
        while curA and curB:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next
            if curA == curB:
                return curA
            if not curA:
                curA = headB
            if not curB:
                curB = headA
        return curA
