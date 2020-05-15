from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/convert-a-number-to-hexadecimal/
class Solution:
    def toHex(self, num: int) -> str:
        """
        >>> solution = Solution()
        >>> solution.toHex(0)
        '0'
        >>> solution.toHex(1)
        '1'
        >>> solution.toHex(16)
        '10'
        >>> solution.toHex(11)
        'b'
        >>> solution.toHex(-1)
        'ffffffff'
        >>> solution.toHex(-2)
        'fffffffe'
        """
        if num == 0:
            return '0'
        if num < 0:
            for i in range(32):
                num = (num ^ (1 << i))
            num += 1
        return self.bits2hex(self.toBits(num))

    def bits2hex(self, bits):
        char_map = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        out = []
        for i in range(0, 32, 4):
            n = self.bin2dec(bits[i:i+4])
            out.append(str(char_map.get(n, n)))
        i = 0
        while out[i] == '0':
            i += 1
        return ''.join(out[i:])

    def toBits(self, num: int):
        offset = 3 if num < 0 else 2
        bits = [int(b) for b in bin(num)[offset:]]
        while len(bits) < 32:
            bits.insert(0, 0)
        return tuple(bits)

    def bin2dec(self, bits):
        out = 0
        n = len(bits)
        for i in range(n - 1, -1, -1):
            out += bits[i] * (2 ** (n - i - 1))
        return out
