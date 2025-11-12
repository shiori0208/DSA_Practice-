#Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

#Input: root = [1,2,3,4,5,6,7]
#Output: [[1],[2,3],[4,5,6,7]]


#Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node: 
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                 res.append(level)
           
        return res    