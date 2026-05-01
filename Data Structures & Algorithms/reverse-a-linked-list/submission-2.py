# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #prev,curr = 0,head
        # 0 -> None
        # 1 -> 0
        # 2 -> 1 
        prev,curr = None, head
        while curr:
            next_node = curr.next #tem[ -> 1]
            curr.next = prev #0 -> None, 1->2->3
            prev = curr #0
            curr = next_node #1
        return prev
        
