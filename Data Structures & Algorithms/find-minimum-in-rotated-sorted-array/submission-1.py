class Solution:
    def findMin(self, nums: List[int]) -> int:
        print(nums)
        if not nums:
            print('here')
            return math.inf
        if len(nums) == 1:
            return nums[0]
        return min(self.findMin(nums[0:len(nums)//2]), self.findMin(nums[len(nums)//2:]))