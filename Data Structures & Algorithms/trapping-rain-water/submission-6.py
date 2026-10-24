class Solution:
    def trap(self, height: List[int]) -> int:
        # initialize the total water, left and right pointers, and the max of heights left and right sides
        total_water = 0

        left = 0
        right = len(height)-1
        
        max_left = 0
        max_right = 0

        # two pointer approach, left < right loop to ensure it iterates through the full array
        while left < right:
            # compare the 2 heights at both sides, we need to keep track of the shorter height  
            # since that limits amount of water it can trap, it's the weakest link
            if height[left] < height[right]:
                #so if height of left side is less than height of right pointer...
                
                if height[left] > max_left:
                    max_left = height[left]
                    left += 1
                else:
                    total_water += (max_left - height[left])
                    left += 1

            elif height[right] <= height[left]:
                if height[right] > max_right:
                    max_right = height[right]
                    right -= 1
                else:
                    total_water += (max_right - height[right])
                    right -= 1

        return total_water
                
            



