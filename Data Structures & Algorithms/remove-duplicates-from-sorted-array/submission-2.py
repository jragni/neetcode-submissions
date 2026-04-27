class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 1

        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
        return left + 1