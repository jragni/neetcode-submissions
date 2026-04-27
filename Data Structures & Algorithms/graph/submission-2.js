class Graph {
    constructor() {
        this.adjList = new Map();
    }

    /**
     * @param {number} src
     * @param {number} dst
     * @return {void}
     */
    addEdge(src, dst) {
        if (!this.adjList.has(src)) {
            this.adjList.set(src, new Set())
        }
        if (!this.adjList.has(dst)) {
            this.adjList.set(dst, new Set())
        }
        this.adjList.get(src).add(dst);
    }

    /**
     * @param {number} src
     * @param {number} dst
     * @return {boolean}
     */
    removeEdge(src, dst) {
        if (
            this.adjList.has(src)
            && this.adjList.has(dst)
        ) {
            this.adjList.get(src).delete(dst)
            return true;
        }
        return false;
    }

    /**
     * @param {number} src
     * @param {number} dst
     * @return {boolean}
     */
    hasPath(src, dst) {
        if (!this.adjList.has(src) && !this.adjList.has(dst)) return false;
        const visited = new Set();

        function _dfs(adjList, start) {
            
            if (start === dst) return true;
            visited.add(start);
            for (let n of adjList.get(start)) {
                if (_dfs(adjList, n)) {
                    return true;
                }
            }
            return false;
        }

        return _dfs(this.adjList, src);
    }
}
