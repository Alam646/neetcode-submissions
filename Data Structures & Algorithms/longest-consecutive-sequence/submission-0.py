class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = {}
        count = 0
        maxcount = 0


        for x in range(len(nums)):
            hash[nums[x]] = nums[x]

        
        for x in range(len(nums)):
            if nums[x] - 1 not in hash:
                count = 1
                start = nums[x]
                while start + 1 in hash:
                    start += 1 
                    count += 1
                if count > maxcount:
                    maxcount = count
            else:
                continue
    
        return maxcount