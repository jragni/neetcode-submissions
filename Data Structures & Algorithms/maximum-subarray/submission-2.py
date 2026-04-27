class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left, right = 0, 0
        max_sum = nums[0]
        curr_sum = 0
        while right < len(nums):
            curr_sum = max(0, curr_sum)
            curr_sum += nums[right]
            max_sum = max(curr_sum, max_sum)

            if curr_sum < 0:
                left = right + 1
            right += 1
        return max_sum

            
