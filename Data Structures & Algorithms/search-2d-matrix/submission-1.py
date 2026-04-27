import math

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            smallest = row[0]
            largest = row[-1]

            if smallest <= target <= largest:
                return self.bst(row, target)
        
        return False
        
    
    def bst(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = math.floor((left + right)/2)
            if nums[mid] == target:
                return True
            
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return False