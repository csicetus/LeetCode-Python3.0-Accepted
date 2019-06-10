# 2019-06-10  Runtime: 52 - 60 - 48 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        ################
        # other sol 1
        
        # if l1 and l2:
        #     if l1.val > l2.val:
        #         l1, l2 = l2, l1
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        # return l1 or l2
    
    
        ################
        # other sol 2: same as sol 1
        
#         if not l1:
#             return l2
#         if not l2:
#             return l1
        
#         head = None
#         if l1.val < l2.val:
#             head = l1
#             head.next = self.mergeTwoLists(l1.next, l2)
#         else:
#             head = l2
#             head.next = self.mergeTwoLists(l1, l2.next)
#         return head
    
        ################
        # other sol 3: iteratively
        
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
