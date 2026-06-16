class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for (u, v, t) in times:
            if u in adj:
                adj[u].append((t, v))
            else:
                adj[u] = [(t, v)]
            
            if v not in adj:
                adj[v] = []
        
        visited = set()
        open_heap = []
        heapq.heapify(open_heap)
        heapq.heappush(open_heap, (0, k))
        

        total_time = 0

        while open_heap:
            (curr_cost, node) = heapq.heappop(open_heap)
            if node in visited:
                continue 
            visited.add(node)
            
            total_time = curr_cost

            for (neighbor_cost, neighbor) in adj[node]:
                if neighbor in visited:
                    continue 
                heapq.heappush(open_heap, (curr_cost+neighbor_cost, neighbor))
            
        return total_time if len(visited) == n else -1



