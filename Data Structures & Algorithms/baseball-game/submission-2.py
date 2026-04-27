class Solution:
    def calPoints(self, operations: List[str]) -> int:
        self.stack = []

        actions_dict = {
            "C": self.stack.pop,
            "D": self.double,
            "+": self.sums,
        }

        for op in operations:
            if op in actions_dict:
                actions_dict[op]()
            else:
                self.stack.append(int(op))
        
        total = sum(self.stack)

        return total
    
    def double(self):
        self.stack.append(2*self.stack[-1])
    
    def sums(self):
        self.stack.append(self.stack[-2] + self.stack[-1])
            
            