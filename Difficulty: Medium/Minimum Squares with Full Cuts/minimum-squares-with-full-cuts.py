class Solution:
    def minSquares(self, n, m):
            squares = 0
            while n:
                (c, n), m = divmod(m, n), n
                squares += c
            return squares