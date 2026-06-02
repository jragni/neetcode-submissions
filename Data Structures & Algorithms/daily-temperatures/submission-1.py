class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        left = 0
        right = len(temperatures) - 1

        while left < len(temperatures) - 1:
            right = left + 1
            while right < len(temperatures) and temperatures[left] >= temperatures[right]:
                right += 1
            
            res[left] = 0 if right == len(temperatures) else right - left

            left += 1
        
        return res
