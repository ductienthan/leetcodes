# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        result = None
        counter = 0
        def dfs(node):
            nonlocal result, counter
            if not node or result is not None:
                return
            dfs(node.left)
            counter += 1
            if counter == k:
                result = node.val
                return
            dfs(node.right)
        dfs(root)
        return result