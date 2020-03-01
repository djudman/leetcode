from leetcode.utils.tree import TreeNode, make_binary_tree
from typing import List


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """
        >>> solution = Solution()
        >>> tree = make_binary_tree([3, 9, 20, None, None, 15, 7])
        >>> solution.levelOrderBottom(tree)
        [[15, 7], [9, 20], [3]]
        >>> tree = make_binary_tree(([0,2,4,1,None,3,-1,5,1,None,6,None,8]))
        >>> solution.levelOrderBottom(tree)
        [[5, 1, 6, 8], [1, 3, -1], [2, 4], [0]]
        """
        values_by_level = []
        self.getValuesByLevel(root, 0, values_by_level)
        values_by_level.reverse()
        return values_by_level

    def getValuesByLevel(self, tree: TreeNode, level: int, out: List):
        if not tree:
            return
        if level >= len(out):
            out.append([])
        self.getValuesByLevel(tree.left, level + 1, out)
        self.getValuesByLevel(tree.right, level + 1, out)
        if tree.val is not None:
            out[level].append(tree.val)
