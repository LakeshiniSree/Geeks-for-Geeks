class Solution:        
    def maxPathSum(self, root):
        self.res = float("-inf")

        def fun(node):

            if not node:
                return float("-inf")

            if not node.left and not node.right:
                return node.data

            left = fun(node.left)
            right = fun(node.right)

            if node.left and node.right:
                self.res = max(self.res, left + node.data + right )

            return node.data + max(left, right)

        fun(root)
        return -1 if self.res == float("-inf") else self.res