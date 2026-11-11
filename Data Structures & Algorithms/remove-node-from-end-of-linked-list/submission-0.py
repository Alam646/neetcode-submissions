# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        front = head
        dummy = ListNode(0)
        dummy.next = head
        back = dummy
    
        count = 0

        while count < n:
            front = front.next
            count += 1
        
        while front:
            back = back.next
            front = front.next
        
        back.next = back.next.next

        return dummy.next