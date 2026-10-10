# Definition for a binary tree node.
# Time: O(nlogk), where n is the number of nodes in the tree. We traverse all nodes in the tree and maintain a heap of size k to keep track of the k largest level sums.
# Space: O(n), where n is the number of nodes in the tree. We store the level sums in a list, which can have at most n elements in the worst case (when the tree is a complete binary tree).
import heapq
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestLevelSum(self, root: TreeNode | None, k: int) -> int:
        if not root:
            return -1
        queue = deque([root])
        levelSum = []
        while queue:
            curSum = 0
            curLevel = len(queue)
            for _ in range(curLevel):
                node = queue.popleft()
                curSum = curSum + node.val
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            levelSum.append(curSum)
        if not 1 <= k <= len(levelSum):
            return -1
        return heapq.nlargest(k, levelSum)[-1]

