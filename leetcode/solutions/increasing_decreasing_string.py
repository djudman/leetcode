from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/increasing-decreasing-string/
class Solution:
    def sortString(self, s: str) -> str:
        """
        >>> solution = Solution()
        >>> solution.sortString('aaaabbbbcccc')
        'abccbaabccba'
        >>> solution.sortString('rat')
        'art'
        >>> solution.sortString('leetcode')
        'cdelotee'
        >>> solution.sortString('ggggggg')
        'ggggggg'
        >>> solution.sortString('spo')
        'ops'
        """
        chars = [0] * 26
        for i, char in enumerate(s):
            index = ord(char) - ord('a')
            chars[index] += 1
        out = []
        while sum(chars) > 0:
            for i in range(len(chars)):
                cnt = chars[i]
                if cnt > 0:
                    out.append(chr(ord('a') + i))
                    chars[i] -= 1
            for j in range(len(chars) - 1, -1, -1):
                cnt = chars[j]
                if cnt > 0:
                    out.append(chr(ord('a') + j))
                    chars[j] -= 1
        return ''.join(out)
