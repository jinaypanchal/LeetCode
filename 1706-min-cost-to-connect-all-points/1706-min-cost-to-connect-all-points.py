class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        if n ==1:
            return 0
        
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        mini_cost = 0
        pq = [(0,0)]
        seen = set()
        while pq:
            cost, u = heapq.heappop(pq)

            if u in seen:
                continue
            
            seen.add(u)
            mini_cost += cost
            for v in range(n):
                if v not in seen:
                    heapq.heappush(pq, (manhattan(points[u], points[v]), v))
        
        return mini_cost

        