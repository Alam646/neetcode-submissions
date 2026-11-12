# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Problem:
        Add Two Numbers (Reverse-Ordered Linked Lists).

    Pattern:
        Simultaneous Two-Pointer Traversal + Dummy Sentinel + Carry Propagation.

    Intuition:
        - Reverse Alignment: Because digits are stored in reverse order, both `head`
          pointers already sit at the ones place—allowing single-pass column addition
          from left to right without reversing either list.
        - Dummy Sentinel Node: Anchoring `dummy` before the output list avoids special
          `if` logic when creating the very first digit node.
        - Unified Loop Condition (`p1 or p2 or carry != 0`): Treats exhausted lists as `0`
          and automatically runs one final turn if a leftover `carry` remains at the tail.

    Complexity:
        - Time Complexity: O(max(M, N)) - Walks the longer of the two lists once (plus at most 1 carry node).
        - Space Complexity: O(1) - Only fixed pointers and variables used (excluding the O(max(M, N)) output list).
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # =========================================================================
        # SETUP: Initialize list walkers, dummy head anchor, and carry tracker
        # =========================================================================
        p1 = l1               # Walker pointer for list 1 (keeps `l1` head intact)
        p2 = l2               # Walker pointer for list 2 (keeps `l2` head intact)
        dummy = ListNode(0)   # Sentinel placeholder node sitting right before our result list
        curr = dummy          # Builder pointer that attaches each newly created digit node

        carry = 0             # Stores tens-place overflow carried over from the previous column

        # =========================================================================
        # MAIN LOOP: Process column by column until both lists AND carry are done
        # =========================================================================
        while p1 or p2 or carry != 0:     # Keep looping if l1 has nodes, l2 has nodes, or a carry remains
            val1 = 0                      # Reset digit placeholder for l1's current column
            val2 = 0                      # Reset digit placeholder for l2's current column

            # --- Extract current digit from l1 (or 0 if l1 has already ended) ---
            if p1:                        # Check that p1 is still pointing to a valid node (not None)
                val1 = p1.val             # Read l1's digit for this place value
            else:                         # If l1 is shorter and already finished...
                val1 = 0                  # Pad missing place value with 0 so addition still works

            # --- Extract current digit from l2 (or 0 if l2 has already ended) ---
            if p2:                        # Check that p2 is still pointing to a valid node (not None)
                val2 = p2.val             # Read l2's digit for this place value
            else:                         # If l2 is shorter and already finished...
                val2 = 0                  # Pad missing place value with 0 so addition still works

            # --- Compute column total and split into node digit vs. carry ---
            sum = val1 + val2 + carry     # Add both digits plus any overflow from the previous turn
            ones = sum % 10               # Remainder gives the single digit (0-9) for this column's node
            carry = sum // 10             # Integer division gives tens overflow (0 or 1) for the next turn

            # --- Build and link the new result node ---
            curr.next = ListNode(ones)    # Create a new node with the ones digit and attach it to the chain
            curr = curr.next              # Move the builder pointer forward onto the newly attached node

            # --- Safely advance input list walkers ---
            if p1:                        # Only step p1 forward if it hasn't reached None yet
                p1 = p1.next              # Move p1 to the next digit in l1

            if p2:                        # Only step p2 forward if it hasn't reached None yet
                p2 = p2.next              # Move p2 to the next digit in l2

        # =========================================================================
        # RETURN: Skip the dummy placeholder and return the actual head node
        # =========================================================================
        return dummy.next                 # `dummy.next` points to the very first digit node we created