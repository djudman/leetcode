from typing import List, Optional

from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/path-sum/
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """
        >>> solution = Solution()
        >>> tree = make_binary_tree([1, 2, 3])
        >>> solution.hasPathSum(tree, 4)
        True
        >>> tree = make_binary_tree([1])
        >>> solution.hasPathSum(tree, 1)
        True
        >>> tree = make_binary_tree([1, 2])
        >>> solution.hasPathSum(tree, 1)
        False
        >>> tree = make_binary_tree([1, 2, 3, 4])
        >>> solution.hasPathSum(tree, 3)
        False
        >>> tree = make_binary_tree([])
        >>> solution.hasPathSum(tree, 0)
        False
        >>> tree = make_binary_tree([1, 2, 3])
        >>> solution.hasPathSum(tree, 6)
        False
        >>> tree = make_binary_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1])
        >>> solution.hasPathSum(tree, 22)
        True
        """
        if not root:
            return False
        sum -= root.val
        if sum == 0 and not root.left and not root.right:
            return True
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
