class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [None for i in range(2*len(nums))]
        i = 0;
        while i < len(nums):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
            i+=1
        return ans