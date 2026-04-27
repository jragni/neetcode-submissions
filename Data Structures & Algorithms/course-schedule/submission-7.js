class Solution {
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {boolean}
     */
    canFinish(numCourses, prerequisites) {
        // create an adjacencyList
        const adjList = new Map();
        for (const [c, pre] of prerequisites) {
            if (!adjList.has(c)) adjList.set(c, new Set());
            if (!adjList.has(pre)) adjList.set(pre, new Set());
            adjList.get(c).add(pre);
        }
        // create a helper util
        // to check if the course can be completed using dfs
        const _canComplete = (
            course,
            adjList,
            taking,
            completed,
        ) => {
            if (taking.has(course)) return false;
            if (completed.has(course)) return true;
            
            taking.add(course);

            for (const pre of adjList.get(course) || []) {
                if (!_canComplete(pre, adjList, taking, completed)) return false;
            }
            
            taking.delete(course);
            completed.add(course);

            return true;
        }

        // for each node, run dfs to see if the course can be completed
        const taking = new Set();
        const completed = new Set();

        return adjList.keys().every((c) => _canComplete(c, adjList, taking, completed));
    }
}
