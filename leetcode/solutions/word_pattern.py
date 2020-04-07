from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/word-pattern/
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        """
        >>> solution = Solution()
        >>> solution.wordPattern('abba', 'dog cat cat dog')
        True
        >>> solution.wordPattern('abba', 'dog cat cat fish')
        False
        >>> solution.wordPattern('aaaa', 'dog cat cat dog')
        False
        >>> solution.wordPattern('abba', 'dog dog dog dog')
        False
        >>> solution.wordPattern('aaa', 'aa aa aa aa')
        False
        """
        word_by_letter = {}
        letter_by_word = {}
        words = str.split(' ')
        if len(words) != len(pattern):
            return False
        for i, letter in enumerate(pattern):
            w = words[i]
            if w in letter_by_word and letter_by_word[w] != letter:
                return False
            if letter in word_by_letter and word_by_letter[letter] != w:
                return False
            if w not in letter_by_word:
                word_by_letter[letter] = w
                letter_by_word[w] = letter
        return True
