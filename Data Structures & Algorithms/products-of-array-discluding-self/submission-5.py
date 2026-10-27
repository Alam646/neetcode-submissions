class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        hash = []
        left = 1
        for x in range(len(nums)):
            hash.append(left)
            left *= nums[x]

        right = 1
        for y in range(len(nums)-1, -1, -1):
            hash[y] *= right
            right *= nums[y]
        
        return hash