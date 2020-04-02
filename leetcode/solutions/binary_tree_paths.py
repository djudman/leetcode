from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/binary-tree-paths/
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        """
        >>> solution = Solution()
        >>> tree = make_binary_tree([1, 2, 3, None, 5])
        >>> solution.binaryTreePaths(tree)
        ['1->2->5', '1->3']
        >>> tree = make_binary_tree([1, 2, 3, 4, 5, None, 6])
        >>> solution.binaryTreePaths(tree)
        ['1->2->4', '1->2->5', '1->3->6']
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]

        left_path = self.binaryTreePaths(root.left)
        right_path = self.binaryTreePaths(root.right)

        result = []
        for path in left_path + right_path:
            result.append(f'{root.val}->{path}')
        return result
