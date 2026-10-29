# Problem: Calculating trapped water requires finding the tallest walls to the left and right of every index i. Scanning dynamically takes O(N^2) time.
# Core Pattern: Prefix & Suffix Accumulation
# Key Intuition: Water at index i = min(max_left, max_right) - height[i].
#   - Strategy 1 (O(N) Space): Precompute `left_max` (left-to-right pass) and `right_max` (right-to-left pass) arrays to query running extremes in O(1).

class Solution:
    def trap(self, height: List[int]) -> int:
        
        # 1. Build Prefix Max Array (Left-to-Right)
        # Stores the tallest wall seen from index 0 up to 'l'
        left_arr = []
        left_max = 0
        for l in range(len(height)):
            if height[l] > left_max:
                left_max = height[l]
                left_arr.append(left_max)
            else:
                left_arr.append(left_max)
        
        # 2. Build Suffix Max Array (Right-to-Left)
        # Stores the tallest wall seen from the end of the array down to 'r'
        right_arr = []
        right_max = 0
        for r in range(len(height) - 1, -1, -1):
            if height[r] > right_max:
                right_max = height[r]
                right_arr.append(right_max)
            else:
                right_arr.append(right_max)
        
        # Since we appended while iterating backward, the array is built in reverse order.
        # We must flip it so right_arr[i] correctly aligns with height[i].
        right_arr.reverse()

        # 3. Calculate Trapped Water
        # Instantly look up the bottleneck walls in O(1) time and apply the formula
        res = 0
        for i in range(len(height)):
            res += min(left_arr[i], right_arr[i]) - height[i]
        
        return res