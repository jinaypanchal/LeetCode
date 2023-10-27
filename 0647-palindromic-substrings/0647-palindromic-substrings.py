class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = {}

        def pali(i , j):
            if (i,j) in memo:
                return memo[(i,j)]
            
            if i>=j:
                return 1
            
            if s[i] == s[j]:
                t = pali(i+1, j-1)
                memo[(i,j)] = t 
                return t

        n = len(s)
        sp = 0
        ct = 0
        for i in range(n):
            for j in range(i, n):
                if pali(i,j) == True:
                    ct += 1
        
        return ct

    
        