# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        self.inOrderSearch(root)
        return root
    def inOrderSearch(self, node: TreeNode | None) -> None:
        if not node:
            return None
        self.inOrderSearch(node.left)
        node.right, node.left = node.left, node.right
        self.inOrderSearch(node.left)
