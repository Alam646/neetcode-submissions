class Solution:
    def trap(self, height: List[int]) -> int:
        
        total_water = 0

        left = 0
        right = len(height)-1
        
        max_left = 0
        max_right = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                    left += 1
                else:
                    total_water += (max_left - height[left])
                    left += 1

            elif height[right] <= height[left]:
                if height[right] >= max_right:
                    max_right = height[right]
                    right -= 1
                else:
                    total_water += (max_right - height[right])
                    right -= 1
            




        return total_water
                
            



