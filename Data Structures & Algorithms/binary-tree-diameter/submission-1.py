# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.res = 0
        self.maxDepth(root)

        return self.res 


        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: an empty child pointer past a leaf has a depth of 0
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        self.res = max(self.res, left+right)

        # Take the deeper subtree's depth and add 1 for the current node's level
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))