class Graph {
    constructor() {
        this.adjList = {}
    }

    /**
     * @param {number} src
     * @param {number} dst
     * @return {void}
     */
    addEdge(src, dst) {
        if (!(src in this.adjList)) {
            this.adjList[src] = new Set();
        }

        if (!(dst in this.adjList)) {
            this.adjList[dst] = new Set();
        }
        this.adjList[src].add(dst);
    }

    /**
     * @param {number} src
     * @param {number} dst
     * @return {boolean}
     */
    removeEdge(src, dst) {
        if (
            src in this.adjList
            && this.adjList[src].has(dst)
        ) {

            this.adjList[src].delete(dst);
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
        return this._dfs(src, dst, new Set());
    }

    _dfs(src, dst, visited) {
        if (src === dst) return true;
        for (const v of this.adjList[src]) {
            if (!visited.has(v)) {
                if (this._dfs(v, dst, visited)) {
                    return true;
                }
            }
        }
        return false;
    }
}
