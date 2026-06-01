class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2  # Acts as floor
            if target == nums[mid]:
                return mid
            
            if target > nums[mid]:
                left = mid + 1
            
            else:
                right = mid - 1
            
        
        return -1