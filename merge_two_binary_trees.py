# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        r = TreeNode()
        if t1 and t2:
            r.val += t1.val + t2.val
            r.left = self.mergeTrees(t1.left, t2.left)
            r.right = self.mergeTrees(t1.right, t2.right)
        elif t1:
            r.val += t1.val
            r.left = self.mergeTrees(t1.left, None)
            r.right = self.mergeTrees(t1.right, None)
        elif t2:
            r.val += t2.val
            r.left = self.mergeTrees(None, t2.left)
            r.right = self.mergeTrees(None, t2.right)
        else:
            return
        return r


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
