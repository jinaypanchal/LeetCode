from collections import defaultdict as d, deque
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = d(list)
        indegree = [0] * n

        for u, v in relations:
            u -= 1
            v -= 1
            adj[u].append(v)
            indegree[v] += 1
        
        queue = deque()
        maxTime = [0] * n

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                maxTime[i] = time[i]
        
        while queue:
            u = queue.popleft()

            for v in adj[u]:
                maxTime[v] = max(maxTime[v], maxTime[u] + time[v])
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        
        return max(maxTime)


        