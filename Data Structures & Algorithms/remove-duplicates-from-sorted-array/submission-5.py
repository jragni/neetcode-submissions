class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 1
        k = 1
        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                nums[k] = nums[right]
                left = right
                right += 1
                k += 1
        return k 