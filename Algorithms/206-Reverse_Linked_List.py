# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        rev_ll = None
        l = list()
        
        while(True):
            l.append(head.val)
            if(head.next != None):
                head = head.next
            else:
                break
        
        for element in l:
            rev_ll = ListNode(element, rev_ll)
            
        return rev_ll