class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        res = []

        left = 0

        for right in range(len(nums)):
            while window and nums[window[-1]] <= nums[right]:
                window.pop()
            
            window.append(right)

            if window[0] < right - k + 1:
                window.popleft()

            
            if right - k + 1 >= 0:
                res.append(nums[window[0]])

        return res