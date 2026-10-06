class Solution:
    def longIncPath(self, matrix, n, m):

           def neighbors(x: int, y: int):
               if x > 0:
                   yield x - 1, y
               if x < n - 1:
                   yield x + 1, y
               if y > 0:
                   yield x, y - 1
               if y < m - 1:
                   yield x, y + 1

           dists = [[-1] * m for _ in range(n)]

           def dfs(x: int, y: int) -> int:
               if dists[x][y] == -1:
                   dists[x][y] = 1 + max(
                       (dfs(x1, y1) for x1, y1 in neighbors(x, y) if matrix[x1][y1] > matrix[x][y]),
                       default = 0
                   )
               return dists[x][y]

           return max(dfs(x, y) for x in range(n) for y in range(m))