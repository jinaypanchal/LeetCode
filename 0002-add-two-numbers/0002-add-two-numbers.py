# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        li1 = []
        while l1:
            li1.append(str(l1.val))
            l1 = l1.next 
        
        li2 = []
        while l2:
            li2.append(str(l2.val))
            l2 = l2.next
        
        li1 = li1[::-1]
        li2 = li2[::-1]

        li3 = list(str(int("".join(li1)) + int("".join(li2))))
        li3 = li3[::-1]

        dummy = head = ListNode()
        for i in li3:
            dummy.next = ListNode(int(i))
            dummy = dummy.next
        
        return head.next

        