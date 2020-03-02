from typing import List, Optional

from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/minimum-depth-of-binary-tree/
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """
        >>> solution = Solution()
        >>> tree = make_binary_tree([1, 21, 22, None, None, 31, 32])
        >>> solution.minDepth(tree)
        2
        >>> tree = make_binary_tree([1, 2, 3, 4, 5, 6, 7])
        >>> solution.minDepth(tree)
        3
        >>> tree = make_binary_tree([1, 2, 3, 4, 5, None, 7])
        >>> solution.minDepth(tree)
        3
        >>> tree = make_binary_tree([])
        >>> solution.minDepth(tree)
        0
        >>> tree = make_binary_tree([1])
        >>> solution.minDepth(tree)
        1
        >>> tree = make_binary_tree([1, 2])
        >>> solution.minDepth(tree)
        2
        >>> tree = make_binary_tree([1, 2, 3])
        >>> solution.minDepth(tree)
        2
        >>> tree = make_binary_tree([1, 2, None])
        >>> solution.minDepth(tree)
        2
        >>> tree = make_binary_tree([1, 2, None, 3, 4])
        >>> solution.minDepth(tree)
        3
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left = 1 + self.minDepth(root.left)
        right = 1 + self.minDepth(root.right)
        if left == 1:
            return right
        if right == 1:
            return left
        return min(left, right)
