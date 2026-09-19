class Solution:
    def findMinCost(self, s1: str, s2: str, costS1: int, costS2: int) -> int:
            m, n = len(s1), len(s2)
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(m + 1):
                dp[i][0] = i * costS1
            for j in range(n + 1):
                dp[0][j] = j * costS2
            for i in range(m):
                for j in range(n):
                    if s1[i] == s2[j]:
                        dp[i + 1][j + 1] = dp[i][j]
                    else:
                        dp[i + 1][j + 1] = min(
                            costS2 + dp[i + 1][j],
                            costS1 + dp[i][j + 1]
                        )
            return dp[m][n]