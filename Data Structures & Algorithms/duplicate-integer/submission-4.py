class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         for n in range(len(nums)):
            for m in range(n+1, len(nums)):
                if nums[n] == nums[m]:
                    return True
         else:
            return False
