import json
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self, intend: str = '') -> str:
        """
        >>> tree = TreeNode(1)
        >>> tree.left = TreeNode(2)
        >>> tree.right = TreeNode(3)
        >>> tree.left.left = TreeNode(4)
        >>> tree.left.right = TreeNode(5)
        >>> str(tree)
        '1\\n\\t2\\n\\t\\t4\\n\\t\\t5\\n\\n\\t3\\n'
        """
        left_value = intend
        right_value = intend
        if self.left:
            left_value = self.left.__str__(intend=f'{intend}\t')
        if self.right:
            right_value = self.right.__str__(intend=f'{intend}\t')
        if self.left or self.right:
            return f'{intend}{self.val}\n{left_value}\n{right_value}\n'
        return f'{intend}{self.val}'

    def __repr__(self) -> str:
        """
        >>> tree = TreeNode(1)
        >>> tree.left = TreeNode(2)
        >>> tree.right = TreeNode(3)
        >>> tree.left.left = TreeNode(4)
        >>> tree.left.right = TreeNode(5)
        >>> repr(tree)
        '[1, 2, 3, 4, 5]'
        """
        out = [self.val]
        out.extend(self.get_values())
        return json.dumps(out)

    def get_values(self) -> List:
        values = []
        if self.left or self.right:
            values.append(self.left and self.left.val or None)
            values.append(self.right and self.right.val or None)
            values.extend(self.left.get_values())
            values.extend(self.right.get_values())
        return values


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
    [0]
    >>> tree = make_binary_tree([0, 1, 2])
    >>> str(tree)  # doctest: +NORMALIZE_WHITESPACE
    '0\\n\\t1\\n\\t2\\n'
    >>> tree
    [0, 1, 2]
    >>> tree = make_binary_tree([0, None, 2])
    >>> str(tree)  # doctest: +NORMALIZE_WHITESPACE
    '0\\n\\tNone\\n\\t2\\n'
    >>> tree
    [0, null, 2]
    >>> tree = make_binary_tree([0, 1, 2, 3, 4, 5, 6])
    >>> str(tree) # doctest: +NORMALIZE_WHITESPACE
    '0\\n\\t1\\n\\t\\t3\\n\\t\\t4\\n\\n\\t2\\n\\t\\t5\\n\\t\\t6\\n\\n'
    >>> tree
    [0, 1, 2, 3, 4, 5, 6]
    >>> tree = make_binary_tree([0, 1, 2, 3, 4, None, 6])
    >>> str(tree) # doctest: +NORMALIZE_WHITESPACE
    '0\\n\\t1\\n\\t\\t3\\n\\t\\t4\\n\\n\\t2\\n\\t\\tNone\\n\\t\\t6\\n\\n'
    >>> tree
    [0, 1, 2, 3, 4, null, 6]
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
            if nodes[left_index] is None:
                nodes[left_index] = node
            nodes[i].left = node
        if right_index < len(values):
            node = TreeNode(values[right_index])
            if nodes[right_index] is None:
                nodes[right_index] = node
            nodes[i].right = node
    return nodes[0]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
