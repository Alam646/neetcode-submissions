# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Kick off top-down DFS at the root with wide-open bounds (-inf, +inf)
        # so the root itself passes regardless of how large or negative its value is.
        return self.mod_dfs(root, float('-inf'), float('inf'))
        
    def mod_dfs(self, node: Optional[TreeNode], lower: float, upper: float) -> bool:
        # Base case: Reached a dead end past a leaf; an empty subtree breaks no BST rules.
        if not node:
            return True

        # Boundary check: Every node must stay strictly inside its inherited (lower, upper) window.
        # Using strict inequality catches both ancestor violations and duplicate values.
        if not (lower < node.val < upper):
            return False
        
        # Recurse on both subtrees, narrowing the allowed range for each direction:
        # - Left child must be strictly less than current node -> tighten upper ceiling to node.val
        # - Right child must be strictly greater than current node -> tighten lower floor to node.val
        # Both branches must return True for the entire tree to be valid.
        return self.mod_dfs(node.left, lower, node.val) and self.mod_dfs(node.right, node.val, upper)