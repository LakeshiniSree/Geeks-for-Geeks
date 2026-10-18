class Solution:
    def minimumStep (self, n):
           count = -2
           while n:
               n, r = divmod(n, 3)
               count += r + 1
           return count