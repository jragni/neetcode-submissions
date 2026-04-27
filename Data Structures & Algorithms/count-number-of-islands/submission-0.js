class Solution {
    /**
     * @param {character[][]} grid
     * @return {number}
     */
    numIslands(grid) {
        const ROW = grid.length
        const COL = grid[0].length
        const visited = new Set();
        let island = 0;

        function dfs(r, c) {
            if (
                visited.has(`${r}-${c}`)
                || r === ROW
                || c === COL
                || Math.min(r, c) < 0
                || grid[r][c] === '0'
            ) return;
            visited.add(`${r}-${c}`);
            // left
            dfs(r-1, c);
            // right
            dfs(r+1, c);
            // up
            dfs(r, c+1);
            // down
            dfs(r, c-1);
        }

        for (let row = 0; row < ROW; row++) {
            for (let col = 0; col < COL; col++) {
                if (
                    visited.has(`${row}-${col}`)
                    || grid[row][col] === "0"
                ) continue;

                dfs(row, col);
                island++;
            }
        }
        return island;
    }
}
