# Problem: Search for a target in a strictly sorted 2D matrix in O(log(m * n)) time.
# Core Pattern: 1D Binary Search with 2D Coordinate Translation.
# Key Intuition: Because the end of one row is strictly smaller than the start of the next, the matrix is functionally just a single sorted 1D array folded up. 
# You don't need to waste time flattening it. Just set your pointers to the start (0) and end (total_items - 1) of the imaginary 1D array. 
# Calculate your 1D 'mid', then translate it into 2D coordinates on the fly using the row width (COLS):
# - mid_row = mid // COLS (How many full rows fit into the index?)
# - mid_col = mid % COLS (What is the remainder/spillover?)
# Then just do standard binary search pointer shifts.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Treat the 2D grid as one long 1D array. 
        # left is the first index, right is the absolute last index.
        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            # (left + right) // 2 ensures division happens AFTER addition.
            # This guarantees we actually find the middle and cut the space in half.
            mid = (left + right) // 2
            
            # Floor division (//) tells us how many full rows fit into our index.
            mid_row = mid // len(matrix[0])
            # Modulo (%) tells us the remainder, mapping to the exact column.
            mid_ind = mid % len(matrix[0])

            # Check the matrix using our translated coordinates
            if target == matrix[mid_row][mid_ind]:
                return True
            elif target > matrix[mid_row][mid_ind]:
                left = mid + 1
            elif target < matrix[mid_row][mid_ind]:
                right = mid - 1
            
        return False