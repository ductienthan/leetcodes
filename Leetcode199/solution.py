# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        queue = deque([(root, 0)])
        ans = []
        while queue:
            node, level = queue.popleft()
            if level == len(ans):
                ans.append(node.val)
                currlevel +=1
            if node.right is not None:
                queue.append((node.right, level+1))
            if node.left is not None:
                queue.append((node.left, level+1))
        return ans
class Solution2:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        ans = []
        def dfs(node, level):
            if not node:
                return
            if level == len(ans):
                ans.append(node.val)
            dfs(node.right, level+1)
            dfs(node.left, level+1)
        dfs(root, 0)
        return ans
        