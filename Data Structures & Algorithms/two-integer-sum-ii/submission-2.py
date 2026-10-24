class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        curr_sum = numbers[left] + numbers[right]

        while curr_sum != target:
            if curr_sum < target:
                left += 1
                curr_sum = numbers[left] + numbers[right]
            else:
                right -= 1
                curr_sum = numbers[left] + numbers[right]
        return [left + 1,right + 1]