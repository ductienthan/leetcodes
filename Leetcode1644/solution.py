# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#Time Compplexity: O(N) where N is the number of nodes in the tree. We visit each node once.
#Space Complexity: O(H) where H is the height of the tree. The recursion stack can go as deep as the height of the tree.
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        found = 0
        def dfs(node):
            nonlocal found
            if node is None:
                return None
            left = dfs(node.left)
            right = dfs(node.right)

            if node is p or node is q:
                found+=1
                return node
            if left and right:
                return node #common ancestor
            return left or right

        result = dfs(root)
        return result if found == 2 else None
        