from typing import List, Optional

from leetcode.utils.tree import TreeNode, make_binary_tree


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        >>> solution = Solution()
        >>> solution.sortedArrayToBST([-10, -3, 0, 5, 9])
        [0, -3, 9, -10, None, 5]
        """
        if not nums:
            return
        return self.makeTree(nums, 0, len(nums) - 1)

    def makeTree(self, nums: List[int], left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return
        middle = left + (right - left) // 2
        tree = TreeNode(nums[middle])
        tree.left = self.makeTree(nums, left, middle - 1)
        tree.right = self.makeTree(nums, middle + 1, right)
        return tree
