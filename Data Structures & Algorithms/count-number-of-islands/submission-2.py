class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        # loop through each row
        for row in range(len(grid)):
            # loop through each column
            for col in range(len(grid[0])):
                # if visited, continue
                coord = f'{row}:{col}'
                if coord in visited:
                    continue
                
                # if isLand
                if grid[row][col] == "1":
                    # explore
                    self._explore(coord, visited, grid)
                    # add to count
                    count += 1

        #return the count
        return count
    
    def _explore(self, coord: str, visited: Set[str], grid) -> None:
        if coord in visited:
            return
        
        [r, c]= [int(val) for val in coord.split(':')]

        if (
            r < 0
            or r >= len(grid)
            or c >= len(grid[0])
            or c < 0
            or grid[r][c] == "0"
        ):
            return
        
        visited.add(coord)
        
        # go left
        self._explore(f'{r-1}:{c}', visited, grid)
        # go right
        self._explore(f'{r+1}:{c}', visited, grid)
        # go down
        self._explore(f'{r}:{c+1}', visited, grid)
        # go up
        self._explore(f'{r}:{c-1}', visited, grid)