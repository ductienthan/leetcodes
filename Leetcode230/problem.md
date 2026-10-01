230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Doing the dfs

left, root, right

dfs(node, ith, k)
if node is none:
return 0
IthSmall = self.dfs(node.left, ith, k)
need to find out how to add the ith here
if ith == k:
result = node.val
ithSmall = self.dfs(node.right, ith+1)
