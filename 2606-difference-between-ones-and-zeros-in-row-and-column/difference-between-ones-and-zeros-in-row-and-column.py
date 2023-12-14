class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        r = [[0, 0] for _ in range(m)]
        c = [[0, 0] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    r[i][0] += 1
                    c[j][0] += 1
                elif grid[i][j] == 1:
                    r[i][1] += 1 
                    c[j][1] += 1
        print(r)
        print(c)
        
        for i in range(m):
            for j in range(n):
                grid[i][j] = r[i][1] + c[j][1] - r[i][0] - c[j][0]
        
        return grid
        

        