# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None


        self.counter = 0

        self.preorder = preorder

        self.inorder_map = {}

        for x in range(len(inorder)):
            self.inorder_map[inorder[x]] = x

        return self.mod_dfs(0,len(inorder) - 1)


    
    def mod_dfs(self, left, right):
        if left > right:
            return None

        val = self.preorder[self.counter]
        self.counter += 1
        root = TreeNode(val)

        ind = self.inorder_map[val]

        root.left = self.mod_dfs(left, ind-1)
        root.right = self.mod_dfs(ind+1, right)

        return root

