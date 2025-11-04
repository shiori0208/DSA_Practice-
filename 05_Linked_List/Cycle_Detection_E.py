#Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

#Input: head = [1,2,3,4], index = 1
#Output: true
#makes more sense in diagram form
#using Flyod's fast and slow concept 



from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            if slow == fast:
                return True 
                
        return False 