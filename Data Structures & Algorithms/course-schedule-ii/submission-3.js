class Solution {
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {number[]}
     */
    findOrder(numCourses, prerequisites) {
        // create an adjacency list
        const adjList = new Map();
        for (const [c, pre] of prerequisites) {
            if (!adjList.has(c)) adjList.set(c, new Set());
            if (!adjList.has(pre)) adjList.set(pre, new Set());
            adjList.get(c).add(pre);
        }

        const schedule = [];
        const completed = new Set();
        const visiting = new Set();

        const canComplete = (node) => {
            if (visiting.has(node)) return false;
            if (completed.has(node)) return true;

            visiting.add(node);

            for (const course of adjList.get(node) || []) {
                if (!canComplete(course)) return false;
            }

            visiting.delete(node);
            completed.add(node);
            schedule.push(node);
            return true;
        }

        for (let i = 0; i < numCourses; i++) {
            if (!canComplete(i)) return [];
        }

        return schedule;
    }
}
