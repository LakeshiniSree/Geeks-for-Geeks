class Solution:
    def minimumEdgeReversal(self, edges: list[list[int]], n: int, src: int, dst: int) -> int:
          from heapq import heappush, heappop
          if src == dst:
              return 0
          adj = [[] for _ in range(n + 1)]
          for u, v in edges:
              adj[u].append((v, 0))
              adj[v].append((u, 1))
          costs = [n] * (n + 1)
          costs[src] = 0
          h = [(0, src)]
          while h:
              cost, u = heappop(h)
              if costs[u] < cost:
                  continue
              if u == dst:
                  return cost
              for v, weight in adj[u]:
                  if (c := cost + weight) < costs[v]:
                      costs[v] = c
                      heappush(h, (c, v))
          return -1