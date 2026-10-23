class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for x in range(len(nums)):
            curr = nums[x]
            needed = target - curr
            if needed in hash:
                return [hash[needed], x]
            else:
                hash[curr] = x