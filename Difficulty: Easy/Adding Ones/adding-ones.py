class Solution:
    def update(self, n: int, updates: list[int]) -> list[int]:
           arr = [0] * n
           for i in updates:
               arr[i - 1] += 1
           for i in range(1, n):
               arr[i] += arr[i - 1]
           return arr