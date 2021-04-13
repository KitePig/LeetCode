# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        self.prev = None
        self.minDiff = 10e6
        self.inOrder(root)
        return self.minDiff

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        if self.prev:
            self.minDiff = min(root.val - self.prev.val, self.minDiff)
        self.prev = root
        self.inOrder(root.right)
