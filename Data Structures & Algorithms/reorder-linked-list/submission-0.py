# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        mid1 = head
        mid2 = head

        while mid1 and mid1.next:
            mid1 = mid1.next.next
            mid2 = mid2.next
        
        #now mid2 will start from the middle
        #now start to reverse mid2

        prev = None

        while mid2:
            temp = mid2.next
            mid2.next = prev
            prev = mid2
            mid2 = temp
        
        first = head
        second = prev

        while second.next:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

        return