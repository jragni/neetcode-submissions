class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            self.min_stack = (
                [val, *self.min_stack]
                if val > self.min_stack[-1]
                else [*self.min_stack, val]
            )
        else:
            self.min_stack = [val]


    def pop(self) -> None:
       val = self.stack.pop()
       idx = self.min_stack.index(val)
       self.min_stack = [
            self.min_stack[i] 
            for i in range(len(self.min_stack))
            if i != idx
        ]

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]