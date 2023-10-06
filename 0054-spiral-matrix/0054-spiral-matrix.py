class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # u = (-1, 0), d = (1,0), r = (0, 1) , l = (0, -1)
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = 0
        initial = (0, 1)    
        dirs = {(0, 1) : (1, 0),
         (1, 0) : (0, -1),
          (0,-1) : (-1, 0),
          (-1, 0) : (0 , 1)} 
        
        spiral = [matrix[i][j]]
        matrix[i][j] = None

        while len(spiral) < m*n:
            next_i = i + initial[0]
            next_j = j + initial[1]
            if (next_i < 0 or next_i == m  or next_j < 0 or next_j == n
             or matrix[next_i][next_j] is None):
                initial = dirs[initial]
            else:
                i ,j = next_i, next_j
                spiral.append(matrix[i][j])
                matrix[i][j] = None
        
        return spiral
        