class Solution:
    def trap(self, height: List[int]) -> int:
        

        left_arr = []
        left_max = 0
        for l in range(len(height)):
            if height[l] > left_max:
                left_max = height[l]
                left_arr.append(left_max)
            else:
                left_arr.append(left_max)
        
        right_arr = []
        right_max = 0
        for r in range(len(height) - 1, -1, -1):
            if height[r] > right_max:
                right_max = height[r]
                right_arr.append(right_max)
            else:
                right_arr.append(right_max)
        
        right_arr.reverse()

        res = 0
        for i in range(len(height)):
            res += min(left_arr[i],right_arr[i]) - height[i]
        
        return res

# Problem: Calculating trapped water requires finding the tallest walls to the left and right of every index i. Scanning dynamically takes O(N^2) time.
# Core Pattern: Prefix & Suffix Accumulation (or Two-Pointer Boundary Convergence)
# Key Intuition: Water at index i = min(max_left, max_right) - height[i].
#   - Strategy 1 (O(N) Space): Precompute `left_max` (left-to-right pass) and `right_max` (right-to-left pass) arrays to query running extremes in O(1).
#   - Strategy 2 (O(1) Space): Use L and R pointers with running `left_max` and `right_max`. Process whichever side has the smaller height, because the taller wall on the opposite side guarantees the smaller wall is the only bottleneck.