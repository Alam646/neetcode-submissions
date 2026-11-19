# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        elif not root and subRoot:
            return False
        
        if self.isSameTree(root, subRoot) == True:
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        

    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both trees ran out of nodes at the exact same spot -> matching branch
        if not p and not q:
            return True

        # Only one pointer is None (since both-None was caught above) -> shape mismatch
        elif not p or not q:
            return False

        # Both nodes exist, but hold different values -> value mismatch
        elif p.val != q.val:
            return False

        # Current nodes match; both left subtrees AND right subtrees must also match
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)