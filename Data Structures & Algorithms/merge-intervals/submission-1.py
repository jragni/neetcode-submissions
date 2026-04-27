class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])

        stack = [intervals[0]]

        for i in range(1, len(intervals)):
            if stack[-1][0] <= intervals[i][0] <= stack[-1][1]:
                stack[-1][1] = max(stack[-1][1], intervals[i][1])
            else:
                stack.append(intervals[i])
        return stack