# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.mod_dfs(root, float('-inf'), float('inf'))
        
    def mod_dfs(self, node, lower, upper):
        if not node:
            return True

        if not lower < node.val < upper:
            return False
        
        return self.mod_dfs(node.left, lower, node.val) and self.mod_dfs(node.right, node.val, upper)
        
        
