class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = [[] for _ in range(n)]

        def prims(adj_li, v):
            pq = [(0,0)]
            heapq.heapify(pq)

            seen = set()
            min_cost = 0

            while pq:
                cost, u = heapq.heappop(pq)
                if u in seen:
                    continue
                seen.add(u)
                min_cost += cost
                
                for neigh, neigh_cost in adj_li[u]:
                    if neigh not in seen:
                        heapq.heappush(pq, (neigh_cost, neigh))
            
            return min_cost

        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                d = abs(x1- x2) + abs(y1-y2)

                adj[i].append((j,d))
                adj[j].append((i,d))
        
        return prims(adj, n)



        