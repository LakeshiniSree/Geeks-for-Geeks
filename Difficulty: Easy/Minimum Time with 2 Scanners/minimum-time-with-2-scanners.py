class Solution:
    def minTime(self, n: int, s1: int, s2: int) -> int:
            from math import ceil, floor
            # t = max(n1 * s1, n2 * s2)
            # n1 * s1 = n2 * s2  | and n2 = n - n1
            # n1 * s1 = (n - n1) * s2
            # n1 * s1 = n * s2 - n1 * s2  | + n1 * s2
            # n1 * (s1 + s2) = n * s2  | / (s1 + s2)
            n1 = n * s2 / (s1 + s2)
            n1_lo, n1_hi = floor(n1), ceil(n1)
            return min(
                max(n1_lo * s1, (n - n1_lo) * s2),
                max(n1_hi * s1, (n - n1_hi) * s2)
            )