class Solution:
    def findPairs(self, arr: list[int]) -> list[int]:
           n = len(arr)
           pairs = {}
           ans = [n, n, n, n]
           for c in range(n - 1):
               for d in range(c + 1, n):
                   sumi = arr[c] + arr[d]
                   if sumi in pairs:
                       a, b = pairs[sumi]
                       if a != c and a != d and b != c and b != d:
                           ans = min(ans, [a, b, c, d])
                   else:
                       pairs[sumi] = (c, d)
           return ans if ans[0] != n else [-1, -1, -1, -1]