class Solution {
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {boolean}
     */
    canFinish(numCourses, prerequisites) {
        // Build our adjacency list
        const adjList = new Map();
        for (const [dst, src] of prerequisites) {
            if (!adjList.has(src)) adjList.set(src, new Set());
            if (!adjList.has(dst)) adjList.set(dst, new Set());
            adjList.get(src).add(dst);
        }
        const visited = new Set();

        function _dfs(course) {
            if (visited.has(course)) return false;
            visited.add(course);
            for (const pre of adjList.get(course) || []) {
                if (!_dfs(pre)) return false
            }
            visited.delete(course);
            return true;
        }

        for (let i = 0; i < numCourses; i++) {
            if (!_dfs(i)) return false
        }
        return true;
    }
}
