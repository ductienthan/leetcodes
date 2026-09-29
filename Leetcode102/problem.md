102. Binary Tree Level Order Traversal
     Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

could insert all of left and right for the next queue

1. For each level, we only append the node of that level
2. For each node, we will append for the next level
3. Append the current data to the result

Time: O(n) - n is the number of node of tree
Space: O(n) - n is number of the node
