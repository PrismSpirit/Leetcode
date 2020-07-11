# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = None
        list1 = []
        list2 = []
        print(l1)
        
        while(1):
            if(l1 == None):
                break
            list1.append(l1.val)
            if(l1.next == None):
                break
            l1 = l1.next
        while(1):
            if(l2 == None):
                break
            list2.append(l2.val)
            if(l2.next == None):
                break
            l2 = l2.next
        
        list3 = list1 + list2
        list3.sort()
        list3.reverse()
        
        for element in list3:
            l3 = ListNode(element, l3)
        
        print(l3)
        
        return l3