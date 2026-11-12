"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    """
    Problem:
        Copy Linked List with Random Pointer (Deep Copy).

    Pattern:
        Two-Pass Hash Map (Object-to-Object Mapping).

    Intuition:
        - Pass 1 (Clone & Register): Walk the original list to instantiate isolated twin nodes
          and store `{original_node: cloned_node}` pairs in a hash map. Using the node object
          itself as the key avoids collisions when multiple nodes share the same integer value.
        - Pass 2 (Wire Pointers): Walk the original list a second time, using the hash map
          as a translator to connect each clone's `.next` and `.random` pointers to the
          corresponding cloned targets.

    Complexity:
        - Time Complexity: O(N) - Two linear passes over a list of N nodes with O(1) map lookups.
        - Space Complexity: O(N) - Hash map stores N original-to-clone node references.
    """
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Dictionary mapping {original Node object -> cloned Node object}
        hash = {}

        # Pre-map None -> None so original pointers ending in None translate cleanly
        # during Pass 2 without triggering a KeyError
        hash[None] = None

        # =========================================================================
        # PASS 1: Create all isolated clone nodes and register them in the hash map
        # =========================================================================
        p1 = head  # Walker pointer for Pass 1 (keeps `head` anchored at the start)

        while p1:
            hash[p1] = Node(p1.val)  # Allocate brand-new node with matching value
            p1 = p1.next             # Advance walker to the next original node

        # =========================================================================
        # PASS 2: Wire up `.next` and `.random` pointers on all cloned nodes
        # =========================================================================
        p2 = head  # Reset a second walker pointer to the start of the original list

        while p2:
            clone = hash[p2]                # Grab the cloned twin of the current node
            clone.next = hash[p2.next]      # Link clone's .next to the twin of p2.next
            clone.random = hash[p2.random]  # Link clone's .random to the twin of p2.random
            p2 = p2.next                    # Advance walker to the next original node

        # Look up original `head` in the map to return the head of the cloned list
        # (also handles an empty input list by returning None)
        return hash[head]