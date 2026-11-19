class Solution:
     def sortIt(self, arr):
        arr.sort(key=lambda a: -a if a & 1 else a)
    
