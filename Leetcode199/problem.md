199. Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Solution:
Each level we only need one node on the right most
so we could check the level.

how to check the each level

for the first queue, we store the root with level is 1

we need to track each level, each level only add one node, then move the next level

what node we will add for the queue, add node for the right one
