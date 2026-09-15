class Solution:
    def getCount(self, root, k):

        leaves = []

        def dfs(node, depth):
            if node:
                if not node.left and not node.right:
                    leaves.append(depth)
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)

        dfs(root, 1)

        total = ans = 0

        for d in sorted(leaves):
            total += d
            if total > k:
                break
            ans += 1

        return ans