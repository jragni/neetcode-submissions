class Solution {
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {boolean}
     */
    canFinish(numCourses, prerequisites) {
        const _createAdjList = (prerequisites) => {
            const adjList = new Map();
            for (const [course, pre] of prerequisites) {
                if (!adjList.has(course)) adjList.set(course, new Set());
                if (!adjList.has(pre)) adjList.set(pre, new Set());
                adjList.get(course).add(pre);
            }
            return adjList;
        }

        const adjList = _createAdjList(prerequisites);

        const _canComplete = (course, visited, checked) => {
            // check for cycle --> if cycle return false
            if (visited.has(course)) return false;
            if (checked.has(course)) return true;
            // add course to visited for cycle detection
            visited.add(course);
            
            // for each dependency
            for (const c of adjList.get(course) || []) {
                // check if we can complete course. if not -> return false
                if (!_canComplete(c, visited, checked)) return false;
            }
            
            // return true
            visited.delete(course)
            checked.add(course);
            return true;
        }

        const checked = new Set();
        for (let i = 0; i < numCourses; i++) {
            if (!checked.has(i) && !_canComplete(i, new Set(), checked)) return false;
        }
        return true;
    }
}
