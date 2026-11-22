class Solution:
	def longestSubarrayDivK(self, arr, k):
       n = len(arr)
   	first, last = [n] * k, [-1] * k
   	reminder = 0
   	first[reminder] = -1
   	for i in range(n):
           reminder = (reminder + arr[i]) % k
           if first[reminder] == n:
               first[reminder] = i
           else:
               last[reminder] = i
       return max(l - f for l, f in zip(last, first))