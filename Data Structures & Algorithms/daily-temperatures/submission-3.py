class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0], 0)] # (temp, index)
        res = [0]*len(temperatures)

        for i in range(1, len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                _, j = stack.pop()
                res[j] = i - j
            stack.append((temperatures[i], i))
        
        while stack:
            _, i = stack.pop()
            res[i] = 0
        
        return res