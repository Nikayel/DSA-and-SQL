# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle node
         # -> slow, fast
        # Break the connection in between
            # Reverse the second half - start of sec = slow.next
        #Join them  
            #picking one node from 1st and next node from 2nd list
        slow,fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next #4,5,6 slow.next -> 4
        slow.next = None # 0,1,2,3 
        prev = None
        while second:
            tmp = second.next # temp = 5
            second.next = prev # 4 -> None
            prev = second # prev = 4 , 4-> None
            second = tmp # second = 5
        #0,1,2,3 || 6,5,4
        first = head
        second = prev
        while second:
            temp1,temp2 = first.next, second.next # temp1 = 1, temp2 = 5
            first.next = second #0 -> 6
            second.next = temp1 #0->6->1
            first = temp1
            second = temp2
            
            


