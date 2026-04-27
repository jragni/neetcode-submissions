class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the frequencies
        counts = self.get_counts(nums)
        stack = []
        for key, val in counts.items():
            temp_stack = []
            # if the top of the stack is smaller, pop -> put popped in temp
            while stack and val > counts[stack[-1]]:
                temp_stack.append(stack.pop())
            stack.append(key)
            while temp_stack:
                stack.append(temp_stack.pop())
        
        return stack[0:k]

    def get_counts(self, nums):
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] = counts[n] + 1
            else:
                counts[n] = 1
        return counts