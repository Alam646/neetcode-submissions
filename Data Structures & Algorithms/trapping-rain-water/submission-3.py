class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0

        for i in range(1, len(height)-1):
            #tallest left wall
            max_left = 0
            # range here has to be i as it needs to be from the very left wall
            for j in range(i):
                curr_left = height[j]
                if curr_left > max_left:
                    max_left = curr_left
            
            #tallest right wall
            max_right = 0
            # range here has to be it+1 to len(height) as it needs to the very right wall
            for k in range(i+1, len(height)):
                curr_right = height[k]
                if curr_right > max_right:
                    max_right = curr_right

            water_at_i = min(max_left, max_right) - height[i]
            if water_at_i > 0:
                total_water += water_at_i

        return total_water

