class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0

        # define _traverse_land
        def _traverse_land(coord):
            if coord in visited:
                return

            [r_str, c_str] = coord.split(':')
            r, c = int(r_str), int(c_str)
            print(f'r: {r}, c: {c}') 
            if (
                r >= len(grid) or r < 0
                or c >= len(grid[0]) or c < 0 
                or grid[r][c] == '0'
            ):
                return
            
            visited.add(coord)
            # go north
            _traverse_land(f'{r+1}:{c}')
            # go south
            _traverse_land(f'{r-1}:{c}')
            # go east
            _traverse_land(f'{r}:{c+1}')
            # go west
            _traverse_land(f'{r}:{c-1}')

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                coord = f'{row}:{col}'
                if coord in visited or grid[row][col] == "0":
                    continue
                
                _traverse_land(coord)
                count += 1
                
        return count 
        

