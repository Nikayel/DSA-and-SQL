# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #start from curr
        prev = None
        curr = head
        #loop :
        while curr:
            #keep track of curent
            temp = curr.next # 0
            #make currentPointerPoint to prev
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        #return prev
        