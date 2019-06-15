# Sol 1 Brute Force 2019-06-14  Runtime: 60 ms 
# Time complexity : O(NlogN). Space complexity : O(N)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next
    
# Sol 2 2019-06-14  Runtime: 48 ms DP


# Sol 3 2019-06-14  Runtime: 48 ms DP


# Sol 4 2019-06-14  Runtime: 48 ms DP


# Sol 5 2019-06-14  Runtime: 48 ms DP
