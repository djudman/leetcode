from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/string-compression/
class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        >>> solution = Solution()
        >>> solution.compress(['a'])
        1
        >>> solution.compress(['a', 'a'])
        2
        >>> solution.compress(['a', 'a', 'a'])
        2
        >>> solution.compress(['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c'])
        6
        >>> solution.compress(['a', 'b', 'c', 'd', 'd', 'd', 'd', 'd'])
        5
        >>> solution.compress(['a', 'b', 'c', 'd'])
        4
        >>> solution.compress(['a', 'b', 'd', 'd'])
        4
        >>> solution.compress(['a', 'd', 'd', 'd'])
        3
        >>> a = ['a','b','b','b','b','b','b','b','b','b','b', 'c', 'c']
        >>> solution.compress(a)
        6
        >>> a
        ['a', 'b', '1', '0', 'c', '2']
        """
        n = len(chars)
        i = 0
        index = 0
        while i < n:
            j = i
            while j < n and chars[i] == chars[j]:
                j += 1
            chars[index] = chars[i]
            index += 1
            if j - i > 1:
                for x in str(j - i):
                    chars[index] = x
                    index += 1
            i = j
        for k in range(index, n):
            chars.pop()
        return index
