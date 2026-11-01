class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            mid = right + left // 2
            mid_row = mid // len(matrix[0])
            mid_ind = mid % len(matrix[0])

            if target == matrix[mid_row][mid_ind]:
                return True
            elif target > matrix[mid_row][mid_ind]:
                left = mid + 1
            elif target < matrix[mid_row][mid_ind]:
                right = mid - 1
            
        return False