class Solution {
    /**
     * @param {number[][]} grid
     * @returns {number}
     */
    countPaths(grid) {
        const ROW = grid.length;
        const COL = grid[0].length;

        const dfs = (r, c, visit = new Set()) => {
            // check if within bounds
            if (
                r < 0
                || c < 0
                || r === ROW
                || c === COL
                || visit.has(`${r}-${c}`)
                || grid[r][c] === 1
            ) return 0;
            // check if at goal
            if (r === ROW - 1 && c === COL - 1) return 1;

            // add to visit
            visit.add(`${r}-${c}`);

            let count = 0
            // move recursively in each direction

            // left
            count += dfs(r, c - 1, visit);
            // right
            count += dfs(r, c + 1, visit);
            // up
            count += dfs(r + 1, c, visit);
            // down
            count += dfs(r - 1, c, visit);

            visit.delete(`${r}-${c}`);

            return count;
        };

        return dfs(0, 0, new Set());
    }
}
