class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    maxAreaOfIsland(grid) {
        const ROW = grid.length;
        const COL = grid[0].length;
        const visited = new Set();
        
        let maxArea = 0;

        function dfs(r, c) {
            if (
               visited.has(`${r}-${c}`)
               || Math.min(r, c) < 0
               || r === ROW
               || c === COL
               || grid[r][c] === 0
            ) return 0;
            visited.add(`${r}-${c}`);

            return 1 + dfs(r-1, c) + dfs(r+1,c) + dfs(r, c+1) + dfs(r, c-1);
        }

        for (let row = 0; row < ROW; row++) {
            for (let col = 0; col < COL; col++) {
                if (visited.has(grid[row][col])) continue;
                if (grid[row][col] === 1) {
                    maxArea = Math.max(dfs(row, col), maxArea);
                } else {
                    visited.add(`${row}-${col}`);
                }
            }
        }
        return maxArea;
    }
}
