# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, l, r):
        if l != None and r != None:
            if self.helper(l.left, r.right) == False:
                return False
            
            if l.val != r.val:
                return False
            
            if self.helper(l.right, r.left) == False:
                return False
        
        if l == None and r != None:
            return False
        if l != None and r == None:
            return False
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if self.helper(root.left, root.right) == False:
            return False
        return True
