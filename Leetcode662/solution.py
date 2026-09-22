# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        queue = deque([(root, 0)])
        maxWidth = 0
        while queue:
            firstIndex = queue[0][1]
            lenSize = len(queue)
            lastIndex = 0
            for _ in range(lenSize):
                currentNode, currentIndex = queue.popleft()
                if currentNode.left:
                    queue.append((currentNode.left, 2*(currentIndex-firstIndex)))
                if currentNode.right:
                    queue.append((currentNode.right, 2*(currentIndex-firstIndex)+1))
                lastIndex = currentIndex
            maxWidth = max(maxWidth, lastIndex-firstIndex+1)
        return maxWidth

        