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
        if (!this.adjList.has(src)) this.adjList.set(src, new Set());
        if (!this.adjList.has(dst)) this.adjList.set(dst, new Set());
        this.adjList.get(src).add(dst)
    }

    /**
     * @param {number} src
     * @param {number} dst
     * @return {boolean}
     */
    removeEdge(src, dst) {
        if (!this.adjList.has(src) || !this.adjList.has(dst)) return false;
        if (this.adjList.get(src).has(dst)) {
            this.adjList.get(src).delete(dst);
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
        if (!this.adjList.has(src) || !this.adjList.has(dst)) return false;

        const _dfs = (node, visited=new Set()) => {
            if (node === dst) return true;
            visited.add(node);

            for (const n of this.adjList.get(node) || []) {
                if (!visited.has(n) && _dfs(n, visited)) {
                    return true
                }
            }
            return false;
        };

        return _dfs(src, new Set());
    }
}
