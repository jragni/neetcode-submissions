class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.array = [None]*self.capacity


    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        self.array[self.length] = n
        self.length += 1


    def popback(self) -> int:
        if self.length > 0:
            self.length -=1
        res = self.array[self.length]
        return res

    def resize(self) -> None:
        filler = [0] * self.capacity
        self.capacity = 2 * self.capacity
        self.array = [*self.array, *filler]

    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
