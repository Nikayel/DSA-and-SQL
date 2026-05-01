# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # return True if both are empty or None
        if p is None and q is None:
            return True
        #return False > if either p or q == None
        if p is None or q is None:
            return False
        #value of P.right != q.Roght or p.left!=q.left
        if p.val != q.val:
            return False
        
        #return isSameTree(pLeft,qLeft) and isSameTree(pright,qright)
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)