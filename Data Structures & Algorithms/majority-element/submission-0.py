class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_count = 0
        max_num = None
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] >= len(nums) / 2:
                return num
            
            if freq[num] > max_count:
                max_num = num
                max_count = freq[num]
            
        return max_num
