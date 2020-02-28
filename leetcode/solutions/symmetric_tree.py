from leetcode.utils.tree import TreeNode, make_binary_tree


class Solution:
    """
    >>> solution = Solution()
    >>> solution.isSymmetric(make_binary_tree([1]))
    True
    >>> solution.isSymmetric(make_binary_tree([1, 2, 3]))
    False
    >>> solution.isSymmetric(make_binary_tree([1, 2, 2, 3, 4, 4, 3]))
    True
    >>> solution.isSymmetric(make_binary_tree([1, 2, 2, 3, 4, 3, 4]))
    False
    >>> solution.isSymmetric(make_binary_tree([1, 2, 2, None, 3, None, 3]))
    False
    """

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return t1.val == t2.val and \
            self.isMirror(t1.left, t2.right) and \
            self.isMirror(t1.right, t2.left)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
