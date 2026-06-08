class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        seen = set()

        for ele in nums:
            count = 0
            if ele in seen:
                continue

            while count + ele in nums_set:
                count += 1
                seen.add(count+ele)
            
            longest = max(longest, count)
        
        return longest 
                