from typing import List, Optional

from leetcode.utils.list import ListNode, make_linked_list
from leetcode.utils.tree import TreeNode, make_binary_tree


# https://leetcode.com/problems/binary-watch/
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        """
        >>> solution = Solution()
        >>> solution.readBinaryWatch(1)
        ['0:01', '0:02', '0:04', '0:08', '0:16', '0:32', '1:00', '2:00', '4:00', '8:00']
        """
        out = []
        for h in range(12):
            s = self.get_amount_set_bits(h)
            for m in range(60):
                if (s + self.get_amount_set_bits(m)) == num:
                    out.append(f'{h}:{m:02d}')
        return out

    def get_amount_set_bits(self, num: int) -> int:
        cnt = 0
        while num > 0:
            cnt += num & 1
            num = num >> 1
        return cnt
