'''
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = self.left = None
        
'''

class Solution:
    def minDiff(self, root: 'Node', k: int) -> int:
           node = root
           min_diff = abs(root.data - k)
           while node:
               if node.data == k:
                   return 0
               if k < node.data:
                   min_diff = min(min_diff, node.data - k)
                   node = node.left
               else:
                   min_diff = min(min_diff, k - node.data)
                   node = node.right
           return min_diff