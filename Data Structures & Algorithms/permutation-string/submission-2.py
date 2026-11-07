# Problem: Determine if s2 contains a permutation of s1 as a substring.
# Core Pattern: Fixed-Size Sliding Window with Dual Frequency Hash Maps.
# Key Intuition: Any permutation of s1 must have the exact same length as s1 and identical character frequencies.
# Maintain a rigid window of size len(s1) across s2. As the right pointer expands the window, 
# evict the character at the left pointer whenever window size exceeds len(s1).
# If the active window's frequency map matches s1's target frequency map, a permutation exists.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Time Complexity: O(N) — where N is len(s2). We traverse s2 once, and dictionary equality checks take O(26) = O(1) time.
        Space Complexity: O(1) — hash maps store at most 26 lowercase English letters.
        """
        target = {}

        # STEP 1: Build the character frequency map for s1
        for x in range(len(s1)):
            if s1[x] in target:
                target[s1[x]] += 1
            else:
                target[s1[x]] = 1

        window = {}
        left = 0
        win_len = len(s1)

        # STEP 2: Slide the fixed window across s2
        for right in range(len(s2)):
            # Add or increment incoming right character
            if s2[right] in window:
                window[s2[right]] += 1
            else:
                window[s2[right]] = 1

            # STEP 3: Maintain fixed window size (must not exceed len(s1))
            if (right - left + 1) > win_len:
                # Decrement count of leftmost element
                window[s2[left]] -= 1 
                
                # Delete key if count reaches 0 so window == target comparison works cleanly
                if window[s2[left]] == 0:
                    del window[s2[left]]
                
                # Advance left pointer to shift the rigid frame forward
                left += 1

            # STEP 4: Check if active window matches target character frequencies
            if window == target:
                return True

        return False