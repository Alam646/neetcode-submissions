class Solution:
    """
    Problem:
        Find the Duplicate Number in an array of `n + 1` integers in range `[1, n]`
        without modifying the array and using O(1) extra space.

    Pattern:
        Floyd's Tortoise and Hare (Cycle Detection + Cycle Entrance) via Array-as-Linked-List.

    Intuition:
        - Array-as-Linked-List: Because every value in `nums` is in `[1, n]`, each index
          acts as a node and `nums[i]` acts as its `.next` pointer. Index `0` is guaranteed
          to sit outside any cycle because no value equals `0`.
        - Duplicate = Cycle Entrance: When two different indices hold the same value `d`,
          two paths point into index `d`, making `d` the exact entrance of a cycle.
        - Two-Phase Floyd's Algorithm:
          1. Phase 1: Advance `slow` by 1 jump and `fast` by 2 jumps until they collide
             inside the cycle.
          2. Phase 2: Reset a second slow pointer (`val`) to `0` and advance both `slow`
             and `val` by 1 jump per step—they are mathematically guaranteed to meet
             at the cycle entrance (`d`).

    Complexity:
        - Time Complexity: O(N) - Both pointers traverse at most O(N) steps across both phases.
        - Space Complexity: O(1) - Only integer index pointers (`slow`, `fast`, `val`) are used.
    """
    def findDuplicate(self, nums: List[int]) -> int:
        # =========================================================================
        # SETUP: Start both tortoise (`slow`) and hare (`fast`) at index 0
        # =========================================================================
        slow = 0                 # Tortoise pointer (moves 1 jump per turn)
        fast = 0                 # Hare pointer (moves 2 jumps per turn)

        # Take the first move before the loop so `slow != fast` on the first check
        slow = nums[slow]        # Move `slow` 1 step forward using value as next index

        fast = nums[fast]        # Move `fast` 1st step forward
        fast = nums[fast]        # Move `fast` 2nd step forward (total: 2 jumps)

        # =========================================================================
        # PHASE 1: Detect the cycle by finding where `slow` and `fast` collide
        # =========================================================================
        while slow != fast:      # Keep running until the hare laps the tortoise inside the cycle
            slow = nums[slow]    # Tortoise advances 1 jump

            fast = nums[fast]    # Hare advances 1st jump
            fast = nums[fast]    # Hare advances 2nd jump

        # =========================================================================
        # PHASE 2: Find the cycle entrance (the duplicate number)
        # =========================================================================
        val = 0                  # Place a second slow pointer back at the starting index 0

        while slow != val:       # Advance both pointers 1 jump at a time until they meet
            slow = nums[slow]    # Move `slow` forward 1 jump from the Phase 1 collision spot
            val = nums[val]      # Move `val` forward 1 jump from index 0

        # The index where both pointers meet is the cycle entrance (= duplicate value)
        return val