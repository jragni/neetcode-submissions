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
            if (!adjList.has(c)) adjList.set(c, new Set())
            if (!adjList.has(pre)) adjList.set(pre, new Set())
            adjList.get(c).add(pre);
        }

        const completed = new Set();
        const visiting = new Set();

        // canComplete _dfs
        const canComplete = (course) => {
            // cycle detection,
            if (visiting.has(course)) return false;
            if (completed.has(course)) return true;

            visiting.add(course)

            for (const pre of adjList.get(course)) {
                if (!canComplete(pre)) return false;
            }

            visiting.delete(course);
            completed.add(course)
            return true;
        }

        for (const course of adjList.keys()) {
            if(!canComplete(course)) return false;
        }
        return true;
    }
}
