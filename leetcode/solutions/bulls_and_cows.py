from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/bulls-and-cows/
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        """
        >>> solution = Solution()
        >>> solution.getHint('1807', '7810')
        '1A3B'
        >>> solution.getHint('null', 'news')
        '1A0B'
        >>> solution.getHint('null', 'lols')
        '1A1B'
        >>> solution.getHint('1123', '0111')
        '1A1B'
        >>> solution.getHint('1123', '1111')
        '2A0B'
        >>> solution.getHint('1123', '1211')
        '1A2B'
        >>> solution.getHint('1123', '1231')
        '1A3B'
        >>> solution.getHint('1234', '4321')
        '0A4B'
        >>> solution.getHint('11', '10')
        '1A0B'
        >>> solution.getHint('12111', '21111')
        '3A2B'
        """
        bulls = 0
        cows = 0
        char_map = {}
        for i, char in enumerate(secret):
            if guess[i] == char:
                bulls += 1
            else:
                self.inc(char_map, char)
        for i, char in enumerate(guess):
            if char != secret[i] and char_map.get(char, 0) - 1 >= 0:
                self.inc(char_map, char, -1)
                cows += 1
        return f'{bulls}A{cows}B'

    def inc(self, data: dict, key: int, value=1) -> None:
        if key not in data:
            data[key] = 0
        data[key] += value
