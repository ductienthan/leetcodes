# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            curLen = len(queue)
            curLevel = []
            for _ in range(curLen):
                curNode = queue.popleft()
                curLevel.append(curNode.val)
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
            result.append(curLevel.copy())
        return result

