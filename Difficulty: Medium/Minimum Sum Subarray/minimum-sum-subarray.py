class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        curr_min = global_min = arr[0]
        for i in range(1, len(arr)):
            curr_min = min(curr_min + arr[i], arr[i])
            global_min = min(global_min, curr_min)
        return global_min