# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       # 1 - > 2 ->  - > 3
        prev, curr = None, head
        #while head not None:
        while curr:
       #keep the head value safe in temp
            temp = curr.next
       #change the head to point to prev
            curr.next = prev
            prev = curr
       #chagne the prev to be the current*head)
            curr = temp
        return prev
       #change the 

