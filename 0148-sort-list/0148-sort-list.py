# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        curr = head
        while curr:
            res.append(curr.val)
            curr = curr.next
        
        res.sort()
        print(res)
        if res:
            start = ListNode(res[0])
            curr = start
            for i in res[1:]:
                nn = ListNode(i)
                curr.next = nn
                curr = nn
            return start

        return head
        