class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts[num] + 1 if num in counts else 1
        
        min_heap = []
        for num, count in counts.items():
            heapq.heappush(min_heap, (count, num)) 
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [num for count, num in min_heap]