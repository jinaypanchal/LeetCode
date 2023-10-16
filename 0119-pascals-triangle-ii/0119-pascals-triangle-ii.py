class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for i in range(rowIndex+1):
            row = [1] * (i+1)
            for j in range(1,i):
                row[j] = res[i-1][j] + res[i-1][j-1]
            res.append(row)
        print(res)
        return res[-1]
        
        