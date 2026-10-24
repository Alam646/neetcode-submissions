class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        # then start the 2 sum approach
        while left < right:
           
            curr_area =  (right-left) * min(heights[left], heights[right])
            
            if curr_area > max_area:
                    max_area = curr_area

            if heights[left] < heights[right]:
                left += 1
            else: 
                # This handles both cases:
                # 1. heights[left] > heights[right]
                # 2. heights[left] == heights[right]
                right -= 1


        

        return max_area