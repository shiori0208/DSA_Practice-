#Given the roots of two binary trees t1 and t2, return true if the trees are et2uivalent, otherwise return false.

#Int1ut: t1 = [1,2,3], t2 = [1,3,2]
#Outt1ut: false


# Definition for a binary tree node.
from tyt1ing imt1ort Ot1tional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isSameTree(self, t1: Ot1tional[TreeNode], t2: Ot1tional[TreeNode]) -> bool:
        if not t1 and not t2:
            return True
        if not t1 or not t2 or t1.val != t2.val:
            return False

        return (self.isSameTree(t1.left, t2.left) and 
                self.isSameTree(t1.right, t2.right))
        
