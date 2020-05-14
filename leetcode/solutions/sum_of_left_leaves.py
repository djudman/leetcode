from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/sum-of-left-leaves/
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        """
        >>> solution = Solution()
        >>> tree = make_binary_tree([3, 9, 20, None, None, 15, 7])
        >>> solution.sumOfLeftLeaves(tree)
        24
        >>> tree = make_binary_tree([1, 2, 3, 4, 5])
        >>> solution.sumOfLeftLeaves(tree)
        4
        """
        if not root:
            return 0
        s = 0
        s += self.sumOfLeftLeaves(root.left)
        s += self.sumOfLeftLeaves(root.right)
        if root.left and not root.left.left and not root.left.right:
            s += root.left.val
        return s
