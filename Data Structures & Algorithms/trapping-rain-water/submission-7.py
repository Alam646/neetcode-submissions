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