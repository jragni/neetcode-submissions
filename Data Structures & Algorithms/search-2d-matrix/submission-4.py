class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            row_mid = (top + bottom) // 2

            if target >= matrix[row_mid][0] and target <= matrix[row_mid][-1]:
                left, right = 0, len(matrix[row_mid]) - 1
                while left <= right: 
                    mid = (right + left) // 2
                    if target == matrix[row_mid][mid]:
                        return True
                    elif target > matrix[row_mid][mid]:
                        left = mid + 1
                    else:
                        right = mid - 1
                    
                return False

            elif target > matrix[row_mid][-1]:
                top = row_mid + 1

            else:
                bottom = row_mid -1 
                
        
        return False