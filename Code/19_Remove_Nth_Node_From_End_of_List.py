# 2019-06-09  Runtime: 36 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        l, r = dummy, dummy
        
        for i in range(1, n + 2):
            l = l.next
        
        while (l):
            l = l.next
            r = r.next
        r.next = r.next.next
        return dummy.next
