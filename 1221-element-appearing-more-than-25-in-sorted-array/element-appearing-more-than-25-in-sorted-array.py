class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)//4 
        # d = {}
        # t = None
        # for i in arr:
        #     if i not in d:
        #         d[i] = 1
        #     else:
        #         d[i] +=1
                
        # for i,v in d.items():
        #     if v > n:
        #         return i
        ct = 0
        cand = arr[0]
        for i in arr:
            if i == cand:
                ct += 1
                if ct > n:
                    return cand
            else:
                cand = i
                ct = 1
        


        