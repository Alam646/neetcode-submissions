# Problem: Find the median of two sorted arrays in O(log(min(m, n))) time.
# Core Pattern: Binary Search on Partitions (Array Cuts).
# Key Intuition: Don't merge the arrays. You are looking for a dividing line that puts exactly half 
# the total elements on the left, and half on the right. 
# Use Binary Search to guess where to draw the line in the smaller array. Math automatically dictates 
# where the line must fall in the larger array to keep the halves even. 
# Then, ask: "Are the biggest numbers on the left of my line smaller than the smallest numbers on the right?"
# If yes, you found the median. If no, adjust the line based on which side is too heavy.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # Ensure nums1 is always the smaller array so our binary search runs as fast as possible.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        # The exact number of elements our Left Basket needs to hold
        half = (len(nums1) + len(nums2)) // 2  

        left = 0
        right = len(nums1) - 1

        # Use while True because every pair of arrays mathematically guarantees a median exists
        while True:
            
            # STEP 1: Guess the partition index for nums1. 
            # Then use math to force nums2 to fill the exact remainder of the basket.
            mid1 = (left + right) // 2
            mid2 = half - mid1 - 2

            # STEP 2: Pull the 4 boundary numbers touching our cut.
            # If a cut goes out of bounds (taking 0 elements, or taking all elements), 
            # we use the Infinity Trick to safely bypass the cross-check without crashing.

            # Map left boundary for nums1 (handle out-of-bounds with -infinity)
            if mid1 >= 0:
                nums1_left = nums1[mid1]
            else:
                nums1_left = float('-inf')  # Took 0 elements from nums1

            # Map left boundary for nums2 (handle out-of-bounds with -infinity)
            if mid2 >= 0:
                nums2_left = nums2[mid2]
            else:
                nums2_left = float('-inf')  # Took 0 elements from nums2

            # Map right boundary for nums1 (handle out-of-bounds with +infinity)
            if (mid1 + 1) < len(nums1):
                nums1_right = nums1[mid1 + 1]
            else:
                nums1_right = float('inf')  # Took ALL elements from nums1

            # Map right boundary for nums2 (handle out-of-bounds with +infinity)
            if (mid2 + 1) < len(nums2):
                nums2_right = nums2[mid2 + 1]
            else:
                nums2_right = float('inf')  # Took ALL elements from nums2


            # STEP 3: The Cross-Check. Are the biggest numbers we took smaller than 
            # the smallest numbers we left behind?
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                
                # Instant win: We found the perfect split line!
                # If total length is odd, the median is just the smallest number on the right side.
                if (len(nums1) + len(nums2)) % 2 == 1: 
                    return float(min(nums1_right, nums2_right))
                
                # If total length is even, the median averages the biggest left number and smallest right number.
                else:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2.0
            
            # STEP 4: Adjust the guess. 
            # If nums1_left is bigger than nums2_right, we took too much heavy stuff from nums1.
            elif nums1_left > nums2_right:
                right = mid1 - 1   # Throw away the right side, take fewer elements.
            
            # If nums2_left is too heavy, it means we didn't take ENOUGH from nums1. 
            else:
                left = mid1 + 1    # Throw away the left side, take more elements.