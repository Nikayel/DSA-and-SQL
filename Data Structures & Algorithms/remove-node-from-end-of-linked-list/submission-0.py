# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #move both 1st and 2nd pointers, 1st pointers
        # Headstart 2nd Pointer by n
        #Node to remove would be 1st.next
        #1,2,3,4 n = 2 - slow.next 1 -> 2, fast.next -> 3-> 4
        #
        dummy = ListNode(0,head) 
        left,right = dummy, head
        for _ in range(n):
          right = right.next
        while right:
            left = left.next # 0-> 1
            right = right.next # 3 -> 4
        left.next = left.next.next
        return dummy.next

        