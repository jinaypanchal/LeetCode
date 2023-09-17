class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        #looks like Dijkstra - PQ (for diff and (row and col)), and MinHeap(for getting min val)

        rows = len(heights)
        cols = len(heights[0])

        dirs = [(0,1), (1,0), (0,-1), (-1,0)]

        # def dijkstra():
        min_heap_pq = [(0,0,0)]
        efforts = [[float('inf')]*cols for _ in range(rows)]
        efforts[0][0] = 0

        while min_heap_pq:
            effort, x, y = heapq.heappop(min_heap_pq)

            if x == rows - 1 and y == cols - 1:
                return effort
            
            for dx, dy in dirs:
                new_x, new_y = x+dx, y+dy

                if 0 <= new_x < rows and 0 <= new_y < cols:
                    new_effort = max(effort, abs(heights[new_x][new_y] - heights[x][y]))

                    if new_effort < efforts[new_x][new_y]:
                        efforts[new_x][new_y] = new_effort
                        heapq.heappush(min_heap_pq, (new_effort, new_x, new_y))

        return efforts[rows - 1][cols - 1]


        # return dijkstra()