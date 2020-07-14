# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return None
        
        rll = None
        l = list()
        
        while head:
            if head.val != val:
                l.append(head.val)
            head = head.next

        l.reverse()
        
        for x in l:
            rll = ListNode(x, rll)
            
        return rll