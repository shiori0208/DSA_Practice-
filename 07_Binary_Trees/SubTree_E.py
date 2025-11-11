#Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

#Input: root = [1,2,3,4,5], subRoot = [2,4,5]
#Output: true

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        t = subRoot
        s = root
        if not t: return True
        if not s: return False 

        if self.sameTree(s, t):
            return True 

        return (self.isSubtree(s.left, t) or 
        self.isSubtree(s.right, t))

    def sameTree(self, s, t):
        if not s and not t:
            return True 

        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and 
            self.sameTree(s.right, t.right))

        return False      