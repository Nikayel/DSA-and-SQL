# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            temp = curr.next #1
            curr.next = prev #0.prev = 1
            prev = curr #prev = 0
            curr = temp #curr = 1

        return prev
        #first loop
        # curr = 3
        # temp = 2
        # 3.prev = 2
        # curr = 2
        #3.prev = 2 temp = curr now 2.next -> 1 
        