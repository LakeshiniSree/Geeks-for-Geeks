class Solution:
    def maxEqualSum(self, s1: list[int], s2: list[int], s3: list[int]) -> int:
        a, b, c = sum(s1), sum(s2), sum(s3)
        i = j = k = 0

        while True:
            if a == b == c:
                return a
            if a == 0 and b == 0 and c == 0:
                return 0

            if a >= b and a >= c:
                if i >= len(s1):
                    return 0
                a -= s1[i]
                i += 1
            elif b >= a and b >= c:
                if j >= len(s2):
                    return 0
                b -= s2[j]
                j += 1
            else:
                if k >= len(s3):
                    return 0
                c -= s3[k]
                k += 1