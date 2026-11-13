class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        slow = nums[slow]

        fast = nums[fast]
        fast = nums[fast]

        while slow != fast:
            slow = nums[slow]


            fast = nums[fast]
            fast = nums[fast]
        
        val = 0

        while slow != val:
            slow = nums[slow]
            val = nums[val]

        return val