class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        largest_area = 0 
        visited = set()

        def _travel_island(coord: str) -> int:
            r_str, c_str = coord.split(':')
            r, c = int(r_str), int(c_str)

            if (
                coord in visited
                or r > len(grid) - 1 or r < 0
                or c > len(grid[0]) - 1 or c < 0
                or grid[r][c] == 0
            ):
                return 0

            visited.add(coord)
            
            return  (
                1 + _travel_island(f'{r+1}:{c}')
                + _travel_island(f'{r-1}:{c}')
                + _travel_island(f'{r}:{c+1}')
                + _travel_island(f'{r}:{c-1}')
            )


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                coord = f'{row}:{col}'

                if coord in visited or grid[row][col] == 0:
                    continue
                
                largest_area = max(_travel_island(coord), largest_area)

        return largest_area 
                


