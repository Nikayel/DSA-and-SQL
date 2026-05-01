# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #if empty -0> retunr null
        if not root:
            return None
        #rootLeft,rootRigth = right,left
        root.left,root.right = root.right,root.left
        #recrusion invertTree(rootLeft)
        self.invertTree(root.left)
        #recrusion invertTree(rootRight)
        self.invertTree(root.right)
        return root