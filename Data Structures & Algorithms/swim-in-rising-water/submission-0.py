class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [(-1,0), (1,0), (0, 1), (0, -1)]
        open_heap = []
        heapq.heapify(open_heap)
        ROW = COL = len(grid)


        heapq.heappush(open_heap, (grid[0][0], (0,0)))

        visited = set()

        while open_heap:
            curr_cost, point = heapq.heappop(open_heap)
            
            if point in visited:
                continue
            
            # at the end
            visited.add(point)
            if point[0] == ROW - 1 and point[1] == COL - 1:
                return curr_cost

            for d in directions:
                i = d[0] + point[0]
                j = d[1] + point[1]
                neighbor = (i, j)
                print(neighbor, i, j)
                # is valid
                if neighbor in visited:
                    continue
                if not (0 <= i < COL ) or not (0 <= j < ROW):
                    continue
                
                heapq.heappush(open_heap, (max(curr_cost, grid[i][j]), neighbor))

