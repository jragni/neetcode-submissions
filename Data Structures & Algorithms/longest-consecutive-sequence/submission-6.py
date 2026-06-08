class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        longest = 0

        for ele in seen:

            curr = 0
            curr_ele = ele

            while curr_ele in seen:

                curr += 1
                curr_ele += 1
            
            longest = max(longest, curr)
            curr = 0
        
        return longest