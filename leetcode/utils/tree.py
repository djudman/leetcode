from typing import List, Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self, intend: str = '') -> str:
        """
        >>> tree = TreeNode(1)
        >>> tree.left = TreeNode(2)
        >>> tree.right = TreeNode(3)
        >>> tree.left.left = TreeNode(4)
        >>> tree.left.right = TreeNode(5)
        >>> repr(tree)
        '1\\n\\t2\\n\\t\\t4\\n\\t\\t5\\n\\n\\t3\\n'
        >>> str(tree)
        '1\\n\\t2\\n\\t\\t4\\n\\t\\t5\\n\\n\\t3\\n'
        """
        left_value = intend
        right_value = intend
        if self.left:
            left_value = self.left.__repr__(intend=f'{intend}\t')
        if self.right:
            right_value = self.right.__repr__(intend=f'{intend}\t')
        if self.left or self.right:
            return f'{intend}{self.val}\n{left_value}\n{right_value}\n'
        return f'{intend}{self.val}'


def make_binary_tree(values: List) -> Optional[TreeNode]:
    """
    # Here an agreement:
    #   0 element is value of root
    #   1st is value of left child of root (L)
    #   2nd element is value of right child of root (R)
    #   3rd is value of left child of L
    #   4th is value of right child of L
    #   5th is value of left child of R
    #   etc.

    >>> make_binary_tree([0])
    0
    >>> make_binary_tree([0, 1, 2]) # doctest: +NORMALIZE_WHITESPACE
    0\n\t1\n\t2\n\n
    >>> make_binary_tree([0, None, 2]) # doctest: +NORMALIZE_WHITESPACE
    0\n\tNone\n\t2\n\n
    >>> make_binary_tree([0, 1, 2, 3, 4, 5, 6]) # doctest: +NORMALIZE_WHITESPACE
    0\n\t1\n\t\t3\n\t\t4\n\t2\n\t\t5\n\t\t6\n\n
    >>> make_binary_tree([0, 1, 2, 3, 4, None, 6]) # doctest: +NORMALIZE_WHITESPACE
    0\n\t1\n\t\t3\n\t\t4\n\t2\n\t\tNone\n\t\t6\n\n
    """
    if not values:
        return
    nodes = [None] * len(values)
    for i, v in enumerate(values):
        if not nodes[i]:
            nodes[i] = TreeNode(values[i])
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(values):
            node = TreeNode(values[left_index])
            nodes[left_index] = node
            nodes[i].left = node
        if right_index < len(values):
            node = TreeNode(values[right_index])
            nodes[right_index] = node
            nodes[i].right = node
    return nodes[0]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
