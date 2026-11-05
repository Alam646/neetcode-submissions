class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        half = (len(nums1) + len(nums2)) // 2  

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        left = 0
        right = len(nums1) - 1

        while True:
            mid1 = (left + right) // 2
            mid2 = half - mid1 - 2
            print(mid1)

            if mid1 >= 0:
                nums1_left = nums1[mid1]
            else:
                nums1_left = float('-inf')

            if mid2 >= 0:
                nums2_left = nums2[mid2]
            else:
                nums2_left = float('-inf')



            if (mid1 + 1) < len(nums1):
                nums1_right = nums1[mid1 + 1]
            else:
                nums1_right = float('inf')

            if (mid2 + 1) < len(nums2):
                nums2_right = nums2[mid2 + 1]
            else:
                nums2_right = float('inf')



            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if (len(nums1) + len(nums2)) % 2 == 1: #odd
                    return min(nums1_right,nums2_right)
                else:
                    return (max(nums1_left,nums2_left) + min(nums1_right,nums2_right)) / 2
            
            elif nums1_left > nums2_right:
                right = mid1 - 1
            
            else:
                left = mid1 + 1
        
