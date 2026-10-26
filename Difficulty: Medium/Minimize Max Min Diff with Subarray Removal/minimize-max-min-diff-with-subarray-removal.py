class Solution:
    def minDiff(self, k: int, arr: list[int]) -> int:
        n = len(arr)

        # If the whole array or more is removed, the remaining difference is 0
        if n <= k:
            return 0

        # Initialize prefix and suffix max/min arrays
        pref_max = [0] * n
        pref_min = [0] * n
        suff_max = [0] * n
        suff_min = [0] * n

        # Fill prefix arrays
        pref_max[0] = arr[0]
        pref_min[0] = arr[0]
        for i in range(1, n):
            pref_max[i] = max(pref_max[i-1], arr[i])
            pref_min[i] = min(pref_min[i-1], arr[i])

        # Fill suffix arrays
        suff_max[n-1] = arr[n-1]
        suff_min[n-1] = arr[n-1]
        for i in range(n-2, -1, -1):
            suff_max[i] = max(suff_max[i+1], arr[i])
            suff_min[i] = min(suff_min[i+1], arr[i])

        min_difference = float('inf')

        # Slide the window of size k to remove
        for i in range(n - k + 1):
            cur_max = -float('inf')
            cur_min = float('inf')

            # Check the remaining prefix portion
            if i > 0:
                cur_max = max(cur_max, pref_max[i-1])
                cur_min = min(cur_min, pref_min[i-1])

            # Check the remaining suffix portion
            if i + k < n:
                cur_max = max(cur_max, suff_max[i+k])
                cur_min = min(cur_min, suff_min[i+k])

            # Update the global minimum difference
            min_difference = min(min_difference, cur_max - cur_min)

        return min_difference
