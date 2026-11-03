class Solution:
    def maximumWeight(self, n, edges, queries):
            from operator import itemgetter
            parent = list(range(n + 1))
            size = [1] * (n + 1)
            size[0] = 0

            def find(u: int) -> int:
                if parent[u] != u:
                    parent[u] = find(parent[u])
                return parent[u]

            edges.sort(key=itemgetter(2))
            q_order = sorted(range(len(queries)), key=queries.__getitem__)
            answers = [0] * len(queries)
            e_i = count = 0
            for q_i in q_order:
                w = queries[q_i]
                while e_i < n - 1 and edges[e_i][2] <= w:
                    u, v, _ = edges[e_i]
                    u, v = find(u), find(v)
                    if u != v:
                        count += size[u] * size[v]
                        size[u] += size[v]
                        parent[v] = u
                    e_i += 1
                answers[q_i] = count
            return answers