class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) <= 1:
            return False
        
        if len(nums) == 2 and nums[0] != nums[1]:
            return False
        
        left, right = 0, 0
        window = []
        while right < len(nums):
            if left + right > k:
                window.remove(nums[left])
                left += 1
                
            if nums[right] in window:
                return True
                
            window.append(nums[right])
            right += 1
        
        return False