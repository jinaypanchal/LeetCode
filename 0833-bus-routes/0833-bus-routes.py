from collections import defaultdict as d
from collections import deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        maxi_v = max(max(i) for i in routes)
        if maxi_v < target:
            return -1
        
        adj = collections.defaultdict(list)

        for route, stops in enumerate(routes):
            for stop in stops:
                adj[stop].append(route)
        
        queue = deque()
        vis = set()
        for route in adj[source]:
            queue.append(route)
            vis.add(route)
        
        ct = 1

        while queue:
            for _ in range(len(queue)):
                route = queue.popleft()
                for stop in routes[route]:
                    if stop == target:
                        return ct

                    for next_rt in adj[stop]:
                        if next_rt not in vis:
                            vis.add(next_rt)
                            queue.append(next_rt)
            ct += 1
        
        return -1
        

        