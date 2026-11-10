class Solution:
    def firstElementKTime(self, arr: list[int], k: int) -> int:
           freqs = {}
           for a in arr:
               freqs[a] = f = freqs.get(a, 0) + 1
               if f == k:
                   return a
           return -1