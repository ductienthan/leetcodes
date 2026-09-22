class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not q and not p:
            return True
        if not q or not p or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(q.right, p.right)