class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # create an adjacency list
        adj_list = {}
        for u, v, w in times:
            if u in adj_list:
                adj_list[u].append((v, w))
            else:
                adj_list[u] = [(v,w)]
            if v not in adj_list:
                adj_list[v] = []

        # create closed set
        closed = set()

        # create an open set (heap)
        open_set = []
        heapq.heapify(open_set)
        # create a g mapping
        # init open set
        heapq.heappush(open_set, (0, k))
        # while open set
        t = 0
        while open_set:
            # pop current node
            w1, n1 = heapq.heappop(open_set)

            # check if in closed, -> continue
            if n1 in closed:
                continue

            # add to closed
            closed.add(n1)

            
            t = w1
            for (n2, w2) in adj_list[n1]:
                if n2 not in closed:
                    heapq.heappush(open_set, (w1+w2, n2))
        
        return -1 if len(closed) != n else t
            


