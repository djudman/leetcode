from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/remove-linked-list-elements/
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """
        >>> solution = Solution()
        >>> node = make_linked_list([1, 2, 6, 3, 4, 5, 6])
        >>> solution.removeElements(node, 6)
        [1, 2, 3, 4, 5]
        >>> node = make_linked_list([1, 1])
        >>> solution.removeElements(node, 1)
        >>> node = make_linked_list([1, 2, 2, 1])
        >>> solution.removeElements(node, 2)
        [1, 1]
        """
        node = head
        prev = None
        while node:
            if node.val == val:
                if not prev:
                    head = node = node.next
                else:
                    prev.next = node.next
                    node = node.next
            else:
                prev = node
                node = node.next
        return head
