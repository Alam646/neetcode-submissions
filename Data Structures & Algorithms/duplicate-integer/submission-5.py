class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for x in range(len(nums)):
            char = nums[x]
            if char in hash:
                return True
            else:
                hash[char] = True

        return False
