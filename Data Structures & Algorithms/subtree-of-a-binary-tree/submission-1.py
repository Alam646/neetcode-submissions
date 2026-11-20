class Solution:
    """
    Problem:
        Subtree of Another Tree — return True if there is a subtree of `root`
        that has the exact same structure and node values as `subRoot`
        (including all descendants down to the leaves), and False otherwise.

    Pattern:
        Nested Preorder Depth-First Search (Outer Search DFS + Inner Lockstep Match Helper).

    Intuition:
        - Outer DFS (`isSubtree`): Walks through every node in `root` as a
          candidate starting point. If `subRoot` is empty, it is trivially a
          subtree (`True`); if `root` runs out of nodes while `subRoot` still
          has nodes left, this path cannot match (`False`).
        - Inner DFS (`isSameTree`): At each candidate node in `root`, compares
          the subtree rooted there against `subRoot` in lockstep. If it matches
          completely, return `True` immediately.
        - Fallback Search: If the current node is not a match, recursively search
          `root.left` OR `root.right` so `True` bubbles up if the subtree exists
          anywhere deeper in either branch.

    Complexity:
        - Time Complexity: O(N * M), where N is the number of nodes in `root`
          and M is the number of nodes in `subRoot`. In the worst case, `isSubtree`
          visits all N nodes of `root` and runs an O(M) `isSameTree` check at each.
        - Space Complexity: O(H_root + H_sub), where H_root and H_sub are the
          heights of `root` and `subRoot`, due to the nested recursion call stacks
          (O(N + M) worst-case on skewed trees, O(log N + log M) balanced).
    """
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base case 1: an empty `subRoot` is always a valid subtree of any tree
        if not subRoot:
            return True

        # Base case 2: `root` ran out of nodes while `subRoot` still has nodes to match
        elif not root and subRoot:
            return False

        # Check if an exact structural and value match starts at the current `root` node
        if self.isSameTree(root, subRoot) == True:
            return True
        else:
            # Otherwise, keep searching both branches; finding a match on either side wins
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