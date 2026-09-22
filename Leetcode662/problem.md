662. Maximum Width of Binary Tree

Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.

thinking:
Do the BFS, checking each level with total number of nodes

Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

Key idea: Think about how you'd index nodes in a complete binary tree using array-style indexing — where the root is at index i, its left child is at 2*i, and its right child is at 2*i + 1.

The problem: If you don't normalize, indices double at every level (2*i, 2*i+1), so by level 30 you could have numbers like 2^30, which can overflow or just get unwieldy.

The fix: At the start of processing each level, grab the index of the first node in the queue for that level — call it first. Then, for every node in that level, before computing its children's indices, subtract first from its own index.

Step-by-step:

Start BFS with queue = [(root, 0)].
For each level:
Let first = queue[0]'s index (the index of the leftmost node in this level, before normalization).
For each (node, idx) in the current level (processing in order):
Compute the normalized index: norm = idx - first
This norm is what you use to:
Compute width contribution (for the last node in the level, norm gives you last - first directly since first's own norm is 0)
Compute children indices: left child gets 2 _ norm, right child gets 2 _ norm + 1
Track width = norm_of_last_node + 1 for this level.

The core idea

In BFS, all nodes in the queue at the start of an iteration belong to the same level. So instead of popping one node at a time forever, you snapshot len(queue) before processing, and pop exactly that many nodes — those are guaranteed to be one full level.

General BFS level-tracking pattern
python
from collections import deque

queue = deque([root])
while queue:
level*size = len(queue) # snapshot: how many nodes are in THIS level
for * in range(level_size):
node = queue.popleft() # process node
if node.left:
queue.append(node.left)
if node.right:
queue.append(node.right) # end of level — everything appended during the for-loop is the NEXT level
