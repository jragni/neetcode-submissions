class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # create an adj_list
        adj_list = {}
        for i, (u, v) in enumerate(edges):
            cost = succProb[i]
            if u in adj_list:
                adj_list[u].append((cost, v))
            else:
                adj_list[u] = [(cost, v)]
            
            if v not in adj_list:
                adj_list[v] = [(cost, u)]
            else:
                adj_list[v].append((cost, u))


        # create a visited set
        visited = set()
        
        # create an open heap
        open_heap = []
        heapq.heapify_max(open_heap)

        # add start edge to heap
        heapq.heappush_max(open_heap, (1.0, start_node))

        # while heap
        while open_heap:
            # pop from heap (current, edge)
            (current_cost, edge) = heapq.heappop_max(open_heap)
            
            # if edge is in visited, continue
            if edge in visited:
                continue
            
            if edge == end_node:
                return current_cost
            
            # add edge to visited
            visited.add(edge)

            # for (cost, edge2) in adj_list[edge1]:
            if edge in adj_list:
                for cost, edge2 in adj_list[edge]:
                    if edge2 in visited:
                        continue
                    
                    heapq.heappush_max(open_heap, (cost*current_cost, edge2))
            

        
        return 0.0