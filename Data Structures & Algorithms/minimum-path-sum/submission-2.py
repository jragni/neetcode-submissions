class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        q = []
        heapq.heapify(q)
        visited = set()
        # cost, (coords)
        heapq.heappush(q, (grid[0][0], (0, 0)))

        ROW = len(grid)
        COL = len(grid[0])

        while q:
            cost, coords = heapq.heappop(q)

            if coords == (ROW-1, COL-1):
                return cost
            
            if coords in visited: 
                continue

            visited.add(coords) 

            directions = [(0, 1), (1, 0)]

            for d in directions:
                rr = coords[0] + d[0]
                cc = coords[1] + d[1]

                if (
                    rr < 0 or rr >= ROW
                    or cc < 0 or cc >= COL
                    or (rr, cc) in visited
                ):
                    continue
                
                heapq.heappush(q, (cost + grid[rr][cc], (rr, cc)))
        
        return 0
            