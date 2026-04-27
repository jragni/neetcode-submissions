class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} 
        for i in range(len(nums)):
            complimentary = target - nums[i]
            if complimentary in seen:
                return [seen[complimentary], i]
            else:
                seen[nums[i]] = i
        return []