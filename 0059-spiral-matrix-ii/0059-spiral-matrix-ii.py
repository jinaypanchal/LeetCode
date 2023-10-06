class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[None]*n for _ in range(n)]
        num = 1
        i = 0
        j = 0
        d = (0, 1)
        dirs = {(0, 1) : (1, 0),
         (1, 0) : (0, -1),
          (0,-1) : (-1, 0),
          (-1, 0) : (0 , 1)}
        
        while num <= n*n:
            mat[i][j] = num
            num += 1
            next_i = i + d[0]
            next_j = j + d[1]
            if (next_i < 0 or next_i == n or next_j < 0 or next_j == n
             or mat[next_i][next_j] is not None):
                d = dirs[d]
            i += d[0]
            j += d[1]
        
        return mat
        