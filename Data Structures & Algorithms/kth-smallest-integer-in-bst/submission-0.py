# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        self.res = 0
        self.mod_dfs(root)
        return self.res
    
    def mod_dfs(self, node):
        if not node:
            return
        
        self.mod_dfs(node.left)

        self.count = self.count - 1
        
        if self.count == 0:
            self.res = node.val
            return 
        
        self.mod_dfs(node.right)

