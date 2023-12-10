class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        ans = [[None for _ in range(m)] for _ in range(n)]
          
        for i in range(0,m):
            for j in range(0,n):              
                ans[j][i] = matrix[i][j]
        
        return ans
        
