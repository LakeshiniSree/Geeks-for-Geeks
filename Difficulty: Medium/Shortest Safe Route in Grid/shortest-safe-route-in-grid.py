from collections import deque

class Solution:
    def shortestPath(self, mat: list[list[int]]) -> int:
        # code here
        n, m = len(mat), len(mat[0])

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        vis = [[False for _ in range(m)] for _ in range(n)]
        q = deque()

        def canWalk(r: int, c: int) -> bool:
            if r < 0 or r >= n or c < 0 or c >= m or mat[r][c] == 0 or vis[r][c]:
                return False

            if r > 0 and mat[r - 1][c] == 0: return False
            if r < n - 1 and mat[r + 1][c] == 0: return False
            if c > 0 and mat[r][c - 1] == 0: return False
            if c < m - 1 and mat[r][c + 1] == 0: return False

            return True

        for i in range(n):
            if canWalk(i, 0):
                q.append([1, i, 0])
                vis[i][0] = True

        while q:
            (cost, x, y) = q.popleft()
            if y == m - 1:
                return cost

            for d in dirs:
                nx = x + d[0]
                ny = y + d[1]
                if canWalk(nx, ny):
                    vis[nx][ny] = True
                    q.append([cost + 1, nx, ny])

        return -1