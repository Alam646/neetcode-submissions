class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1 for i in range(len(nums))]
        suffix = [1 for i in range(len(nums))]

        #creating the prefix array
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]

        #for creating the suffix array
        for i in range(len(nums)-2,-1,-1):
            suffix[i] = suffix[i+1]*nums[i+1]

        res = []
        for i in range(len(nums)):
            res.append(prefix[i]*suffix[i])

        return res