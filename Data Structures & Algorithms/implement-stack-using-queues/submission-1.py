class MyStack:

    def __init__(self):
        # holding 
        self.q1 = deque()

    def push(self, x: int) -> None:
       self.q1.append(x) 

    def pop(self) -> int:
        temp = deque()

        while len(self.q1) > 1:
            temp.append(self.q1.popleft())
        
        res = self.q1.pop()

        while len(temp):
            self.q1.append(temp.popleft())
        
        return res


    def top(self) -> int:
        return self.q1[-1]
        

    def empty(self) -> bool:
       return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()