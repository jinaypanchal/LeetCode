class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rowSum = {}
        for i, row in enumerate(mat):
            row_sum = sum(row)
            rowSum[i] = row_sum
        
        rowSum = sorted(rowSum.items(), key = lambda x:x[1])
        print(rowSum)

        res = []
        ct = 0
        for tup in rowSum:
            ct += 1
            # print(tup)
            res.append(tup[0])
            if ct == k:
                break

        return res

   
        