class Solution:
    """
    Problem:
        Maximum Depth of Binary Tree — return the number of nodes along the
        longest path from the root node down to the farthest leaf node.

    Pattern:
        Postorder Depth-First Search (Bottom-Up Recursive Depth Accumulation).

    Intuition:
        - Base Case: Stepping past a leaf hits an empty `None` pointer, which
          contributes 0 levels to the depth, so return `0`.
        - Recursive Step (Children First): Query both the right and left
          subtrees to get the maximum depth beneath each branch as integers.
        - Combine at Current Node: Take the deeper of the two child subtrees
          with `max(...)` and add `1` to count the floor `root` occupies,
          passing that total upward to its parent.

    Complexity:
        - Time Complexity: O(N), where N is the total number of nodes in the
          tree. Every node is visited once with O(1) work per node.
        - Space Complexity: O(H), where H is the height of the tree, due to
          the recursion call stack (O(log N) on a balanced tree, O(N) worst-case
          on a completely skewed tree).
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: an empty child pointer past a leaf has a depth of 0
        if not root:
            return 0

        # Take the deeper subtree's depth and add 1 for the current node's level
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))