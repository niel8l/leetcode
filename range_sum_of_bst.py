# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.n = 0
        self.sum(root, L, R)
        return self.n

    def sum(self, root, L, R):
        if not root:
            return
        if L <= root.val <= R:
            self.n += root.val
        if L < root.val:
            self.sum(root.left, L, R)
        if root.val < R:
            self.sum(root.right, L, R)
