# Problem: Sliding Window Maximum
# Pattern: Monotonic Decreasing Deque (Double-Ended Queue)
# Key Intuition: Maintain indices in deque such that their corresponding values 
# are strictly decreasing. The front of the deque (window[0]) always holds the maximum.

from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Time Complexity: O(N) — Each index is pushed and popped at most once.
        Space Complexity: O(K) — The deque stores at most K indices at any time.
        """
        window = deque()
        res = []

        for right in range(len(nums)):
            # 1. Back cleaning: Remove indices of smaller/equal elements (they can never be max)
            while window and nums[window[-1]] <= nums[right]:
                window.pop()
            
            # 2. Push current index
            window.append(right)

            # 3. Front cleaning: Remove index if it has fallen out of window bounds
            if window[0] < right - k + 1:
                window.popleft()

            # 4. Record maximum once window reaches size k
            if right - k + 1 >= 0:
                res.append(nums[window[0]])

        return res