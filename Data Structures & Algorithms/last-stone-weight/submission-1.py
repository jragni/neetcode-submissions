class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # check for length, if 1, return 1
        if len(stones) == 1:
            return stones[0]
        # if 2, return delta 
        if len(stones) == 2:
            return abs(stones[0] - stones[1])

        # turn stones into a heap_max
        heapq.heapify_max(stones)
        delta = 0
        # delta = 0
        # while there is still a heap
        while stones:
            # pop stone 1
            stone1 = heapq.heappop_max(stones)

            if stones:
                stone2 = heapq.heappop_max(stones)
                delta = abs(stone1 - stone2)

                if delta:
                    heapq.heappush_max(stones, delta)
            else:
                return stone1

        return delta 

            # if there is only one on the heap
                # return delta
            # if there is still a heap
                # pop stone two
                # get abs difference
                # get the delta, 
                # if there is a delta
                    # add it back to the heap
            
        
    