# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Store a shared countdown and result slot on `self` so every recursive
        # call across the tree updates the exact same state ("shared whiteboard").
        self.count = k
        self.res = 0

        # Run the Inorder traversal (visits BST nodes in sorted ascending order).
        self.mod_dfs(root)

        # Return the k-th smallest value recorded during the walk.
        return self.res
    
    def mod_dfs(self, node: Optional[TreeNode]) -> None:
        # Base case: Reached an empty spot past a leaf; unwind back to the parent.
        if not node:
            return
        
        # Step 1 (Left): Visit all smaller values in the left subtree first.
        self.mod_dfs(node.left)

        # Step 2 (Current Node): Process the current node in sorted order
        # by ticking down the shared counter.
        self.count = self.count - 1
        
        # Once the counter hits 0, we have landed on the exact k-th smallest node.
        # Save its value and return early to skip its right subtree.
        if self.count == 0:
            self.res = node.val
            return 
        
        # Step 3 (Right): Continue into larger values in the right subtree.
        self.mod_dfs(node.right)