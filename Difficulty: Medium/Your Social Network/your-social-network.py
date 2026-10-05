class Solution:
    def socialNetwork(self, arr):
        from bisect import bisect_left, bisect_right

        ans = []
        for i0, e in enumerate(arr):
            user = i0+2
            friend = e
            i = bisect_left(ans, e, key=lambda item: item[0])
            j = bisect_right(ans, e, key=lambda item: item[0])
            if i < len(ans):
                for k in range(i, j):
                    e = (user, ans[k][1], ans[k][2]+1)
                    ans.append(e)
            ans.append((user, friend, 1))
        return ans