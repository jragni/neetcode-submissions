class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        self.nums = nums
        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        stack = []
        while len(self.nums) > self.k:
            stack.append(heapq.heappop(self.nums))
        
        kth_largest = heapq.heappop(self.nums)

        heapq.heappush(self.nums, kth_largest)
        while stack:
            heapq.heappush(self.nums, stack.pop())
        
        return kth_largest
