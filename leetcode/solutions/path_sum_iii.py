from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/path-sum-iii/
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        """
        >>> solution = Solution()
        >>> tree = make_binary_tree([10, 5,-3, 3,2, None,11, 3,-2, None,1])
        >>> solution.pathSum(tree, 8)
        3
        >>> tree = make_binary_tree([1, 2, 3, 4, 5, 2, 6])
        >>> solution.pathSum(tree, 6)
        3
        >>> tree = make_binary_tree([0, 1, 1])
        >>> solution.pathSum(tree, 1)
        0
        """
        if not root:
            return 0
        self.cnt = 0
        self.countSums(root, [], search_sum=sum)
        return self.cnt

    def countSums(self, node: TreeNode, current_sums: List[int], search_sum: int):
        current_sums.append(0)
        for i in range(len(current_sums)):
            current_sums[i] += node.val
            if current_sums[i] == search_sum:
                self.cnt += 1
        if node.left:
            self.countSums(node.left, current_sums, search_sum)
        if node.right:
            self.countSums(node.right, current_sums, search_sum)
        for i in range(len(current_sums)):
            current_sums[i] -= node.val
        current_sums.remove(0)
