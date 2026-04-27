class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        maximum = 0
        for n in nums:
            if n != 1:
                curr = 0
            else:
                curr += 1
                maximum = max(curr, maximum)
                
        return maximum
        