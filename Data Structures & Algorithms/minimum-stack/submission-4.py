class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        return 

    def top(self) -> int:
        return self.stack[-1] 

    def getMin(self) -> int:
        temp = []
        min_num = self.stack[-1]
        while self.stack:
            top = self.stack.pop()
            min_num = min_num if min_num <= top else top
            temp.append(top)
        
        while temp:
            self.stack.append(temp.pop())
        
        return min_num