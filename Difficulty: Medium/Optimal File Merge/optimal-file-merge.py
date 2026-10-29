class Solution:
    def minComputation(self, files):

            import heapq
            pq = files
            heapq.heapify(pq)

            ans = 0
            while len(pq) > 1:
                x, y = heapq.heappop(pq), heapq.heappop(pq)
                ans += x + y
                heapq.heappush(pq, x+y)

            return ans