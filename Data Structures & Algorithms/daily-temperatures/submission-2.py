class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for left in range(len(temperatures)):
            right = left + 1
            while right < len(temperatures):
                if temperatures[right] > temperatures[left]:
                    res.append(right - left)
                    break
                right += 1 

            if right == len(temperatures):
                res.append(0)
            
        return res
