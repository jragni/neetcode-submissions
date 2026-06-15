class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # create an adjacency list
        adj_list = {}
        for u, v, w in times:
            if u in adj_list:
                adj_list[u].append((v, w))
            else:
                adj_list[u] = [(v, w)]
            
            if v not in adj_list:
                adj_list[v] = [] 

        # create a min heap for open
        open_list = []
        heapq.heapify(open_list)

        # add first value to heap
        heapq.heappush(open_list, (0, k))

        # create a closed set for visited
        visited = set()
        # get t
        t = 0
        # while open list
        while open_list:
            # pop from set
            w1, n1 = heapq.heappop(open_list)

            # check if in visited -> continue
            if n1 in visited:
                continue
            # add to visited
            visited.add(n1)
            t = w1
            # for each neighbor
            for n2, w2 in adj_list[n1]:
                # check if in visited -> contiue
                if n2 not in visited:
                    heapq.heappush(open_list, (w2 + w1, n2))
                
        return -1 if len(visited) != n else t