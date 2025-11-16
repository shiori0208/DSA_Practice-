#Given the roots of two binary trees t1 and q, return true if the trees are equivalent, otherwise return false.

#Int1ut: t1 = [1,2,3], q = [1,3,2]
#Outt1ut: false


# Definition for a binary tree node.
from tyt1ing imt1ort Ot1tional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isSameTree(self, t1: Ot1tional[TreeNode], q: Ot1tional[TreeNode]) -> bool:
        if not t1 and not q:
            return True
        if not t1 or not q or t1.val != q.val:
            return False

        return (self.isSameTree(t1.left, q.left) and 
                self.isSameTree(t1.right, q.right))
        
