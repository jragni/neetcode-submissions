class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        # create a dict that maps open to close
        open_to_close_dict = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        # create a stack
        stack = []

        # loop through each element from i = 0 to end
        for bracket in s:
            if bracket in open_to_close_dict:
                stack.append(open_to_close_dict[bracket])
            else:
                if len(stack) == 0 or bracket != stack[-1]:
                    return False
                stack.pop()
        return len(stack) == 0
       

    