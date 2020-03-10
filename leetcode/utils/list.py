from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    """
    >>> node = ListNode(1)
    >>> node.next = ListNode(2)
    >>> repr(node)
    '[1, 2]'
    """
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr(self):
        out = [self.val]
        current_node = self
        while current_node.next:
            current_node = current_node.next
            out.append(current_node.val)
        return out

    def __repr__(self):
        return str(self.__repr())

    def __eq__(self, other):
        return repr(self) == repr(other)


def make_linked_list(values: List) -> Optional[ListNode]:
    if not values:
        return
    node = ListNode(values[0])
    node.next = make_linked_list(values[1:])
    return node
