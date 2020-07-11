# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = 0
        l3 = None
        
        w = 1
        while(1):
            sum += l1.val * w
            w *= 10
            if(l1.next == None):
                break
            l1 = l1.next
        
        w = 1 
        while(1):
            sum += l2.val * w
            w *= 10
            if(l2.next == None):
                break
            l2 = l2.next
            
        t = list(str(sum))
        
        for _ in t:
            l3 = ListNode(_, l3)
        
        return l3