class Solution:
    """
    Problem:
        Diameter of Binary Tree — return the length (in edges) of the longest
        path between any two nodes in the tree. This path may or may not pass
        through the main root.

    Pattern:
        Postorder Depth-First Search (Bottom-Up Height Accumulation + Global Tracker).

    Intuition:
        - Every node can act as the highest "bend" (bridge) connecting its left
          subtree to its right subtree. The longest path bending through a given
          node has length `left_height + right_height`.
        - Because a recursive call can only return one branch height upward to
          its parent, we maintain `self.res` as a shared scoreboard to record
          the maximum `left + right` bend seen across all nodes.
        - Meanwhile, `maxDepth` returns `1 + max(left, right)` upward so the
          parent node knows the single longest branch extending below it.

    Complexity:
        - Time Complexity: O(N), where N is the number of nodes in the tree.
          Each node is visited once when reusing the stored `left` and `right`
          variables (re-calling `self.maxDepth` in the return line would degrade
          time complexity to O(N^2)).
        - Space Complexity: O(H), where H is the height of the tree, due to the
          recursion call stack (O(log N) on a balanced tree, O(N) worst-case
          on a skewed tree).
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Shared scoreboard tracking the largest (left + right) bend seen anywhere
        self.res = 0
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
        self.res = max(self.res, left + right)

        # Reuse `left` and `right` (avoiding duplicate recursive calls) to pass
        # the single deepest branch height upward to the parent
        return 1 + max(left, right)