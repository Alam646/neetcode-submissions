# Problem: Find the length of the longest substring without repeating characters in O(n) time.
# Core Pattern: Variable Sliding Window with Hash Map Index Tracking.
# Key Intuition: Use a right pointer to expand the substring window continuously. 
# Store each character's latest index in a hash map. When a duplicate is detected 
# inside the active window (hash[char] >= left), teleport the left pointer to the 
# spot right after the duplicate (hash[char] + 1) to restore substring validity instantly.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            # If character exists in map and is inside the active window, teleport left
            if s[right] in char_map and char_map[s[right]] >= left:
                left = char_map[s[right]] + 1
            
            # Store/update the character's most recent index
            char_map[s[right]] = right
            
            # Calculate current window size and track maximum
            max_len = max(max_len, right - left + 1)

        return max_len