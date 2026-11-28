class Solution:
    def checkPath(self, adj: list[list[int]], u: int, v: int) -> bool:
            n = len(adj)
            visited = [False] * n
            s = [u]
            visited[u] = True
            while s:
                a = s.pop()
                for b in adj[a]:
                    if visited[b]:
                        continue
                    if b == v:
                        return True
                    visited[b] = True
                    s.append(b)
            return False