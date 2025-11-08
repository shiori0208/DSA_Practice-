#Given the root of a binary tree, return its depth.
#The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

#Input: root = [1,2,3,null,null,4]
#Output: 3

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [[root, 1]]
        res = 1

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return res 