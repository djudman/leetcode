from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/palindrome-linked-list/
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        >>> solution = Solution()
        >>> solution.isPalindrome(make_linked_list([1, 2]))
        False
        >>> solution.isPalindrome(make_linked_list([1, 2, 2, 1]))
        True
        >>> solution.isPalindrome(make_linked_list([1]))
        True
        >>> solution.isPalindrome(make_linked_list([1, 1]))
        True
        >>> solution.isPalindrome(make_linked_list([1, 1, 2]))
        False
        """
        stack = []
        current_node = head
        while current_node:
            stack.append(current_node.val)
            current_node = current_node.next
        current_node = head
        while current_node:
            if stack.pop() != current_node.val:
                return False
            current_node = current_node.next
        return True
