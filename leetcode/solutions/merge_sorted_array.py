from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        >>> solution = Solution()
        >>> a = [2, 0]
        >>> b = [1]
        >>> solution.merge(a, 1, b, 1)
        >>> a
        [1, 2]
        >>> a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        >>> b = [-50, -50, -48, -47, -44, -44, -37, -35, -35, -32, -32, -31,\
        -29, -29, -28, -26, -24, -23, -23, -21, -20, -19, -17, -15, -14, -12,\
        -12, -11, -10, -9, -8, -5, -2, -2, 1, 1, 3, 4, 4, 7, 7, 7, 9, 10, 11,\
        12, 14, 16, 17, 18, 21, 21, 24, 31, 33, 34, 35, 36, 41, 41, 46, 48, 48]
        >>> solution.merge(a, 0, b, 63)
        >>> a
        [-50, -50, -48, -47, -44, -44, -37, -35, -35, -32, -32, -31, -29, -29, \
-28, -26, -24, -23, -23, -21, -20, -19, -17, -15, -14, -12, -12, -11, \
-10, -9, -8, -5, -2, -2, 1, 1, 3, 4, 4, 7, 7, 7, 9, 10, 11, 12, 14, 16, \
17, 18, 21, 21, 24, 31, 33, 34, 35, 36, 41, 41, 46, 48, 48]
        """
        if m > 0:
            for j in range(n - 1, -1, -1):
                i = m - 1
                if nums1[i] > nums2[j]:
                    nums1[i], nums2[j] = nums2[j], nums1[i]
                while i > 0 and nums1[i] < nums1[i - 1]:
                    nums1[i], nums1[i - 1] = nums1[i - 1], nums1[i]
                    i -= 1
        j = 0
        for i in range(m, m + n):
            nums1[i] = nums2[j]
            j += 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
