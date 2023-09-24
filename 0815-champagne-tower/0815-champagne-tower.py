class Solution:

    def __init__(self):
        self.memo = {}
        
    def f(self, q, i , j):        
        if i < 0 or j < 0 or i <j:
            return 0.0
        
        if i == 0 and j == 0:
            return q

        if (q, i, j) in self.memo:
            return self.memo[(q, i, j)]

        up_left = max((self.f(q, i-1, j-1) - 1)/ 2.0, 0.0)
        up_right = max((self.f(q, i-1, j) - 1)/ 2.0, 0.0)

        # if up_left < 0:
        #     up_left = 0.0
        
        # if up_right < 0:
        #     up_right = 0.0
        
        res = up_left + up_right
        self.memo[(q, i, j)] = res

        return res        

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        return min(1.0, self.f(poured, query_row, query_glass))

        