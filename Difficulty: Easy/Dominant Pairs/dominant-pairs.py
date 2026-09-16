class Solution:
    def dominantPairs(self, arr):
        n = len(arr)
        half = n // 2

        left = arr[:half]
        right = arr[half:]

        left.sort()
        right.sort()

        j = 0
        count = 0

        for x in left:
            while j < half and x >= 5 * right[j]:
                j += 1

            count += j

        return count