class Solution:
    def formPyramid(self, arr):
           n = len(arr)
           peaks = [0] * n
           peaks[0] = min(1, arr[0])
           for i in range(1, n):
               peaks[i] = min(peaks[i - 1] + 1, arr[i])
           peaks[-1] = min(1, peaks[-1])
           for i in range(n - 2, -1, -1):
               peaks[i] = min(peaks[i + 1] + 1, peaks[i])
           return sum(arr) - max(peaks)**2