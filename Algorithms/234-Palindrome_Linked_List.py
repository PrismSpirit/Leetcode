# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l = list()
        
        while head:
            l.append(head.val)
            head = head.next
        
        forward_l = list(l)
        l.reverse()
        
        if (len(l) == 0) or (forward_l == l):
            return True
        else:
            return False