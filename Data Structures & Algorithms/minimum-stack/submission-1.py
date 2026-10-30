# Problem: Design a stack that can return the minimum value in O(1) time without searching.
# Core Pattern: Two Stacks (Parallel State Tracking)
# Key Intuition: A single variable forgets the previous minimum when the current minimum is popped. To fix this, maintain a second stack (`minstack`) that is perfectly synced in size with the main stack. For every `val` pushed, push the minimum of `(val, current_min)` to the `minstack`. When popping, pop from both. This creates a perfect history so the top of `minstack` is always the correct minimum for the current state.

class MinStack:

    def __init__(self):
        # Main stack stores the actual values
        self.stack = []
        # Min stack acts as a perfectly synced shadow, storing the minimum value at each state
        self.minstack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        
        # Sync the minstack:
        if not self.minstack:
            # If it's the first item, it's automatically the minimum
            self.minstack.append(val)
        elif val < self.minstack[-1]:
            # If the new value is smaller than the current minimum, it becomes the new minimum
            self.minstack.append(val)
        else:
            # If it's not smaller, duplicate the current minimum to keep the stacks exactly the same size
            self.minstack.append(self.minstack[-1])

    def pop(self) -> None:
        # Blindly pop both stacks. This instantly "rewinds" the minstack to the previous minimum.
        self.stack.pop()
        self.minstack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # Look up the current state's minimum in O(1) time without searching
        return self.minstack[-1]