import math

class Solution:
    def sameMod(self, arr):
        # If all elements are identical, there are infinitely many solutions
        unique_elements = list(set(arr))
        if len(unique_elements) <= 1:
            return -1

        # Sort the unique elements to find consecutive differences
        unique_elements.sort()

        # Compute the GCD of all consecutive differences
        g = 0
        for i in range(1, len(unique_elements)):
            diff = unique_elements[i] - unique_elements[i-1]
            g = math.gcd(g, diff)

        # Count the number of positive divisors of the final GCD
        divisor_count = 0
        for i in range(1, int(math.isqrt(g)) + 1):
            if g % i == 0:
                divisor_count += 1       # i is a divisor
                if i * i != g:
                    divisor_count += 1   # g // i is also a distinct divisor

        return divisor_count
