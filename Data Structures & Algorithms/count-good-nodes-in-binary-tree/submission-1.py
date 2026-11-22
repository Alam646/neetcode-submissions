# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)
    
    def dfs(self, node, maxval):
        if not node:
            return 0
        
        count = 0

        if node.val >= maxval:
            count += 1
            maxval = node.val

        count += self.dfs(node.left, maxval)
        count += self.dfs(node.right, maxval)

        return count

