class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest_heap = []
        heapq.heapify_max(closest_heap)
        for point in points:
            heapq.heappush_max(closest_heap, (math.hypot(point[0], point[1]), point))

        while len(closest_heap) > k:
            heapq.heappop_max(closest_heap)

        return [point for _, point in closest_heap]

            


