class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # -4 -1 -1 0 1 2

        sorted_nums=sorted(nums)
        sol = []
        # if l + m + r != 0 //
        # re-arrange this into a 2-sum equation, a + b + c == 0 or a + b = 0 - c or 
        # a + b = -c
        #-c is a fixed interval , we'll loop though sorted nums and sorted_nums[i] will be c
        for i in range(len(sorted_nums)):
            #in otder to handle the duplicates
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            c = sorted_nums[i]
            left = i + 1
            right = len(sorted_nums) - 1
            
            while left < right:
                curr_sum = sorted_nums[left] + sorted_nums[right] + c
                if curr_sum < 0:
                    left += 1
                    curr_sum = sorted_nums[left] + sorted_nums[right] + c
                elif curr_sum > 0:
                    right -= 1
                    curr_sum = sorted_nums[left] + sorted_nums[right] + c
                elif curr_sum == 0:
                    sol.append([sorted_nums[left], sorted_nums[right], c])
                    left += 1
                    right -= 1
                    while left < right and sorted_nums[left] == sorted_nums[left-1]:
                        left += 1
        
        return sol
                

            
            

