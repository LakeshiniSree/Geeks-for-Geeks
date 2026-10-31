
class Solution:
    def maxPackages(self, arr: list[int], totalTime: int) -> int:
        max_sum = curr_sum = sum(arr[:totalTime])
        for i in range(totalTime, len(arr)):
            curr_sum += arr[i] - arr[i - totalTime]
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum
        