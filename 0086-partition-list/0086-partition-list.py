# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l = []
        r = []

        while head:
            if head.val<x:
                l.append(head.val)
            elif head.val >= x:
                r.append(head.val)
            
            head = head.next
        
        res = l+r

        if not res:
            return None
        
        new_head = ListNode(res[0])
        curr = new_head
        for val in res[1:]:
            curr.next = ListNode(val)
            curr = curr.next

        return new_head
        



        