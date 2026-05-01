# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Start to point head to prev(None)
        # store head.next to a var temp
        # then move the pointer where prev becomes current
        # Current becomes temp
        current,prev = head,None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
        
