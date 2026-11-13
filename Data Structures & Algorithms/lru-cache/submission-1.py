class Node:
    """
    Doubly Linked List node storing both `key` and `val` plus bidirectional links.
    - `val` allows `get(key)` to return the cached value directly from the node.
    - `key` allows eviction from the `self.old` boundary to delete the matching
      entry from `self.hash` in O(1) time without reverse-searching the map.
    """
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    """
    Problem:
        Design a Least Recently Used (LRU) Cache supporting O(1) `get(key)` and
        O(1) `put(key, value)` operations within a fixed `capacity`.

    Pattern:
        Hash Map + Doubly Linked List with Dual Dummy Sentinels.

    Intuition:
        - Hash Map (`key -> Node`): Provides O(1) random access directly to any
          node's position in memory so we never traverse the list to find it.
        - Doubly Linked List (`self.old <---> ... <---> self.new`): Maintains exact
          usage order. Every touched node (`get` or `put`) is detached via `remove`
          and re-inserted right before `self.new` (Most Recently Used end).
        - Eviction: When `len(self.hash) > self.cap`, the oldest node is always
          sitting immediately after `self.old` (`self.old.next`), allowing O(1)
          unlinking and hash map deletion.

    Complexity:
        - Time Complexity: O(1) average for both `get` and `put` (all pointer
          rewiring and dictionary operations take constant steps).
        - Space Complexity: O(capacity) to store at most `capacity` nodes in the
          doubly linked list and hash map.
    """
    def __init__(self, capacity: int):
        self.cap = capacity
        self.hash = {}               # Maps key -> Node reference for O(1) lookup

        # Dummy boundary sentinels eliminate None checks at both ends
        self.old = Node(0, 0)        # Left boundary (Least Recently Used side)
        self.new = Node(0, 0)        # Right boundary (Most Recently Used side)

        # Wire sentinels together: [self.old] <---> [self.new]
        self.old.next = self.new
        self.new.prev = self.old

    def remove(self, node: Node) -> None:
        # Bridge `node`'s left and right neighbors directly around `node`
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node: Node) -> None:
        # Splice `node` into the newest slot right before `self.new`
        new_node = self.new.prev     # Grab current most-recently-used real node
        self.new.prev = node         # Point `self.new` back to `node`
        node.next = self.new         # Point `node` forward to `self.new`
        node.prev = new_node         # Point `node` back to previous newest node
        new_node.next = node         # Point previous newest node forward to `node`

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1

        # Refresh usage: detach from current spot and move to newest end
        curr = self.hash[key]
        self.remove(curr)
        self.insert(curr)

        return curr.val

    def put(self, key: int, value: int) -> None:
        # If key already exists, remove its stale node before inserting updated one
        if key in self.hash:
            self.remove(self.hash[key])

        # Create new node, register in hash map, and place at newest end
        self.hash[key] = Node(key, value)
        self.insert(self.hash[key])

        # Evict the least recently used node (`self.old.next`) if over capacity
        if len(self.hash) > self.cap:
            old = self.old.next
            self.remove(old)
            del self.hash[old.key]