class Solution:
    def absDiff(self, root):
        self.res = self.prev = float('inf')

        def dfs(node):
            if node:
                dfs(node.left)
                self.res = min(self.res, abs(node.data - self.prev))
                self.prev = node.data
                dfs(node.right)

        dfs(root)
        return self.res