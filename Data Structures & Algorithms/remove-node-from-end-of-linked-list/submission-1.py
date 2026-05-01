# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #left,right , n 
        #Move the pointers until we are at the n
        left,right = head,head
        # right = head + n
        for _ in range(n):
            right = right.next
        if not right:
            return head.next
        while right.next:    #L = 1, r = 3 -> L = 2, r = 4 -> l = 3, 
            left = left.next     
            right = right.next
        left.next = left.next.next
        return head
        
        
        
