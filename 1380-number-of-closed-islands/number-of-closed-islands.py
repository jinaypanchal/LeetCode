class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ct = 0
        def  dfs(r ,c):
            if r >= m or r< 0 or c >= n or c < 0:
                return False
            if grid[r][c] == 1:
                return True

            grid[r][c] = 1 #marking vis
            left = dfs(r, c-1)
            right = dfs(r, c+1)
            up = dfs(r-1, c)
            down = dfs(r+1, c)

            return left and right and up and down


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if dfs(i, j):
                        ct += 1

        return ct

        