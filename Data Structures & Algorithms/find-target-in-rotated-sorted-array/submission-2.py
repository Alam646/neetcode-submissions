# Problem: Find the exact index of a target value in a rotated sorted array in O(log n) time, or return -1.
# Core Pattern: Binary Search with Segment Sorting Validation.
# Key Intuition: No matter where you slice a rotated array with your `mid` pointer, 
# one half is always perfectly sorted. You don't need to unravel the rotation. 
# First, identify the perfectly sorted side by comparing `mid` to the boundaries. 
# Then, ask: "Does my target mathematically fit inside the minimum and maximum values of this perfect side?" 
# If it does, narrow your search to that side. If it doesn't, it must be hiding in the other, messy side.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # Use <= because the window can shrink down to a single element
        while left <= right:
            mid = (left + right) // 2

            # Instant win if we land exactly on it
            if nums[mid] == target:
                return mid

            # STEP 1: Identify if the LEFT side is the perfectly sorted half
            # (>= ensures this works even if left and mid are on the same index)
            elif nums[mid] >= nums[left]:
                
                # STEP 2: Does the target fit smoothly inside this perfect left half?
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1   # Yes: it must be here. Throw away the right side.
                else:
                    left = mid + 1    # No: it must be in the messy right side. Throw away left.
            
            # STEP 1: If left isn't perfectly sorted, the RIGHT side MUST be perfectly sorted.
            elif nums[mid] < nums[right]:
                
                # STEP 2: Does the target fit smoothly inside this perfect right half?
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1    #


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # Use <= because the window can shrink down to a single element
        while left <= right:
            mid = (left + right) // 2

            # Instant win if we land exactly on it
            if nums[mid] == target:
                return mid

            # STEP 1: Identify if the LEFT side is the perfectly sorted half
            # (>= ensures this works even if left and mid are on the same index)
            elif nums[mid] >= nums[left]:
                
                # STEP 2: Does the target fit smoothly inside this perfect left half?
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1   # Yes: it must be here. Throw away the right side.
                else:
                    left = mid + 1    # No: it must be in the messy right side. Throw away left.
            
            # STEP 1: If left isn't perfectly sorted, the RIGHT side MUST be perfectly sorted.
            elif nums[mid] < nums[right]:
                
                # STEP 2: Does the target fit smoothly inside this perfect right half?
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1    # Yes: it must be here. Throw away the left side.
                else:
                    right = mid - 1   # No: it must be in the messy left side. Throw away right.

        # The while loop ended, meaning the target isn't in the array
        return -1