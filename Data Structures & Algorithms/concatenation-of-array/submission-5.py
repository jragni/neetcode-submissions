class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0]*2*len(nums)
        for i in range(len(ans)):
            idx = i % len(nums)
            print(f"{idx}, i: {i}")
            ans[i] = nums[idx]
        
        return ans
