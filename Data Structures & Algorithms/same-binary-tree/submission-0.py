# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #base case:
        # If empty: Return True
        if q is None and p is None:
            return True
        # If pValue != qValue return False, If p and Not q or Not p and q return False
        if p is None or q is None or p.val != q.val:
            return False
        #return True (isSametree(q.left,p.left) and isSameTree(q.right,p.right))
        return (self.isSameTree(q.left,p.left) and self.isSameTree(q.right,p.right))
        #O(n)
        