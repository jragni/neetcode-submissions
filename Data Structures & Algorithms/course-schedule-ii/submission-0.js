class Solution {
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {number[]}
     */
    findOrder(numCourses, prerequisites) {
        // create an adjList
        function _createAdjList(edges) {
            const adjList = new Map();
            for (const [course, pre] of edges) {
                if (!adjList.has(course)) adjList.set(course, new Set());
                if (!adjList.has(pre)) adjList.set(pre, new Set());
                adjList.get(course).add(pre);
            }
            return adjList;
        }

        const adjList = _createAdjList(prerequisites);


        // dfs
            // check if course is visited --> return true (since we know that the path has already been done)
            // check if course is visiting --> current dfs cycle --> return false since a cycle is found
            
            // add node to visiting

            // for each neighbor
                // dfs the nodes --> if false at any time, return false
            
            // remove note from visiting
            // add node to visited
            // add node to path

            // return true
        function _dfs(c, visiting=new Set(), visited=new Set(), path=[]) {
            if (visiting.has(c)) {
                return false;
            }
            if (visited.has(c)) return true;

            visiting.add(c);

            for (const pre of adjList.get(c) || []) {
               if (!_dfs(pre, visiting, visited, path)) return false;
            }

            visiting.delete(c);
            visited.add(c);
            path.push(c);
            return true;
        }

        // initialize path 
        const res = [];
        const visited = new Set();  // completed path
        const visiting = new Set();  // current path
        // for each value on the adjList
        for (let i = 0; i < numCourses; i++) {
            // fun dfs on the node
            if (!_dfs(i, visiting, visited, res)) return [];
        }
        
        // return path
        return res;

    }
}
