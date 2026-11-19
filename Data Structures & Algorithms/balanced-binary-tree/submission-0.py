# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        self.res = True
        self.maxDepth(root)

        return self.res



    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: an empty child pointer past a leaf contributes 0 edges
        if not root:
            return 0

        # Measure the height of the left and right subtrees once
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        # Update the global diameter if the path bending at `root` is the longest so far
        if abs(left - right) > 1:
            self.res = False

        # Reuse `left` and `right` (avoiding duplicate recursive calls) to pass
        # the single deepest branch height upward to the parent
        return 1 + max(left, right)