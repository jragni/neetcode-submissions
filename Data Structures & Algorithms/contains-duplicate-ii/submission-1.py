class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not k:
            return False
            
        seen = set()
        for i in range(0,k):
            if nums[i] in seen:
                return True
            else:
                seen.add(nums[i])
        
        for j in range(k, len(nums)):
            if nums[j] in seen:
                return True
            else:
                seen.remove(nums[j - k])
                seen.add(nums[j])
        return False
