import math
from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/find-mode-in-binary-search-tree/
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        """
        >>> solution = Solution()
        >>> tree = make_binary_tree([1, None, 2, None, None, 2, None])
        >>> solution.findMode(tree)
        [2]
        """
        self.out = []
        self.cnt = 0
        self.maxCnt = 0
        self.prevVal = None
        self.find(root)
        return self.out

    def find(self, root: TreeNode):
        if not root:
            return
        self.find(root.left)
        if root.val == self.prevVal:
            self.cnt += 1
        else:
            self.cnt = 1
            self.prevVal = root.val
        if self.cnt == self.maxCnt:
            self.out.append(root.val)
        elif self.cnt > self.maxCnt:
            self.out.clear()
            self.out.append(root.val)
            self.maxCnt = self.cnt
        self.find(root.right)
