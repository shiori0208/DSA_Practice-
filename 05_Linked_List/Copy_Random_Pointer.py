#You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.

#Input: head = [[3,null],[7,3],[4,0],[5,1]]
#Output: [[3,null],[7,3],[4,0],[5,1]]


# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}
        
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy 
            cur = cur.next

        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]

        
