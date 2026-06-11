class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return 0

        nums.sort()

        left, right = 0, k-1

        min_diff = math.inf

        while right < len(nums):
            diff = nums[right] - nums[left]
            print(f'{diff}')
            min_diff = min(diff, min_diff)
            right += 1 
            left += 1
        
        return min_diff