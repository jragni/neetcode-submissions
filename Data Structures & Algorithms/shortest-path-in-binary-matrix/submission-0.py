class Solution:
    def _is_valid(self, point: List[int]):
        return (
          0 <= point[0] < self.ROW
          and 0 <= point[1] < self.COL
        )

    def _is_blocked(self, point: List[int]):
        return self.grid[point[0]][point[1]] == 1

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.ROW = len(grid)
        self.COL = len(grid[0])

        self.DIAGONALS = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
        self.DIRECTIONS = [(1,0), (0,1), (-1, 0), (0, -1), *self.DIAGONALS]
        
        # check if start or end is blocked
        if self._is_blocked([0,0]) or self._is_blocked([self.ROW -1, self.COL-1]):
            return -1
        
        # initialized a visited set
        visited = set()
        open_heap = []
        heapq.heapify(open_heap)

        heapq.heappush(open_heap, (1, [0, 0]))
            
        while open_heap:
            dist, point = heapq.heappop(open_heap)

            if tuple(point) in visited:
                continue
            
            if point == [self.ROW-1, self.COL-1]:
                return dist

            visited.add(tuple(point))
            for dir in self.DIRECTIONS:
                i = dir[0] + point[0]
                j = dir[1] + point[1]

                if self._is_valid([i,j]) and not self._is_blocked([i,j]):
                    heapq.heappush(open_heap, (dist+1, [i,j]))
                
        return -1
                