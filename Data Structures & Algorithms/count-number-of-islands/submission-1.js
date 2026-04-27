class Solution {
    /**
     * @param {character[][]} grid
     * @return {number}
     */
    numIslands(grid) {
        const COL = grid[0].length;
        const ROW = grid.length;
        const visited = new Set();
        let count = 0;

        function dfs(r, c) {
            if (
                Math.min(c, r) < 0
                || r === ROW
                || c === COL
                || visited.has(`${r}-${c}`)
                || grid[r][c] === '0'
            ) return

            visited.add(`${r}-${c}`);
            dfs(r-1, c);
            dfs(r+1, c);
            dfs(r, c+1);
            dfs(r, c-1);
        }

        for (let row = 0; row < ROW; row++) {
            for (let col = 0; col < COL; col++) {
                if (!visited.has(`${row}-${col}`) && grid[row][col] === '1') {
                    dfs(row,col);
                    count++;
                } else {
                    visited.add(`${row}-${col}`);
                }
            }
        }

        return count;
    }
}
