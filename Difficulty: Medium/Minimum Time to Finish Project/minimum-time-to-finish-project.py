from collections import deque
class Solution:
    def minTime(self, duration, dependencies):
        # code here
        n = len(duration)

        g = [[] for _ in range(n)]
        indegree = [0]*n
        for u,v in dependencies:
            g[u].append(v)
            indegree[v] +=1

        dp = [0]*n
        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
                dp[i] = duration[i]
        final = 0

        while q:
            u = q.popleft()
            final+=1

            for v in g[u]:
                dp[v] = max(dp[v],dp[u]+duration[v])
                indegree[v]-=1

                if indegree[v] ==0:
                    q.append(v)
        if final!=n:
            return -1

        return max(dp)