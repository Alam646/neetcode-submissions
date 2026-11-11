# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Problem: Linked List Cycle Detection
Pattern: Fast & Slow Pointers (Floyd's Cycle-Finding Algorithm)

Intuition:
- Linear List: `fast` reaches `None` in O(N) time and exits.
- Circular List: Both pointers get trapped in the cycle. Because `fast` moves 
    2 steps and `slow` moves 1 step per iteration, the gap between them shrinks 
    by exactly 1 node per turn, guaranteeing a collision.

Complexity:
- Time Complexity: O(N)
- Space Complexity: O(1)
"""


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize fast and slow pointers at the head
        fast = head
        slow = head

        # Safely traverse while fast and fast.next exist to avoid NoneType errors
        while fast and fast.next:
            fast = fast.next.next  # Advance fast pointer 2 steps
            slow = slow.next       # Advance slow pointer 1 step

            # If the pointers meet on the same node, a cycle is detected
            if fast == slow:
                return True

        # Fast reached the end (None), meaning the list has no cycle
        return False
