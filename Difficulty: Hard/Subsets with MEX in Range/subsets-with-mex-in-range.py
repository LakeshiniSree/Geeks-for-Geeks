from typing import List

class Solution:
    def cntSubsets(self, arr: List[int], l: int, r: int) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        maxv = n  # since 0 ≤ arr[i] ≤ n
        cnt = [0] * (maxv + 1)
        for x in arr:
            cnt[x] += 1

        # prefix sums of counts
        pref = [0] * (maxv + 1)
        pref[0] = cnt[0]
        for i in range(1, maxv + 1):
            pref[i] = pref[i - 1] + cnt[i]

        # powers of 2 up to n
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        # productBelow[x] = Π (2^cnt[i] − 1) for i = 0..x−1
        # valid[x] = True iff all cnt[0..x−1] > 0
        productBelow = [1] * (maxv + 2)
        valid = [False] * (maxv + 2)
        valid[0] = True

        prod = 1
        for i in range(maxv + 1):
            if cnt[i] == 0:
                break
            prod = (prod * (pow2[cnt[i]] - 1)) % MOD
            productBelow[i + 1] = prod
            valid[i + 1] = True

        def ways(x: int) -> int:
            # number of subsets with MEX exactly x
            if x == 0:
                # MEX 0 ⇒ no 0 in subset; all non-zero elements are free
                nonzero = n - cnt[0]
                return pow2[nonzero]

            if x > maxv or not valid[x]:
                return 0

            # elements with value > x
            greater = n - pref[x]
            return (productBelow[x] * pow2[greater]) % MOD

        ans = 0
        for x in range(l, r + 1):
            ans = (ans + ways(x)) % MOD

        return ans % MOD