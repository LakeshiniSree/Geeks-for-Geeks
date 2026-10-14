class Solution:
    def findRollOut(self, s, roll):
           n = len(s)
           changes = [0] * (n + 1)
           for i in roll:
               changes[i] -= 1
           arr = []
           r = len(roll)
           for c, d in zip(s, changes):
               r += d
               arr.append(chr(ord("a") + (ord(c) - ord("a") + r) % 26))
           return "".join(arr)