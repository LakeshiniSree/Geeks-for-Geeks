class Solution:
    def checkWithinK(self, arr: list[int], k: int) -> bool:
           k1 = k + 1
           kset = set(arr[:k1])
           if len(kset) < k1:
               return True
           for i in range(k1, len(arr)):
               kset.remove(arr[i - k1])
               if (a := arr[i]) in kset:
                   return True
               kset.add(a)
           return False