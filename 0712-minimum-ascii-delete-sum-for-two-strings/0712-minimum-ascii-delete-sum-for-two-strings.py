class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        memo = {}
        def f(i, j):
            if (i,j) in memo:
                return memo[(i,j)]

            if i >= m and j >= n:
                return 0     

            if  i >= m:
                memo[(i,j)] = ord(s2[j]) +  f(i, j+1)
            elif j >= n:
                memo[(i,j)] = ord(s1[i]) + f(i+1, j)
            
            elif s1[i] == s2[j]:
                memo[(i,j)] = f(i + 1, j + 1)
            else:                    
                del_s1 = ord(s1[i]) + f(i + 1, j)
                del_s2 = ord(s2[j]) + f(i, j+1)
                memo[(i,j)] = min(del_s1, del_s2)

            return memo[(i,j)]


        return f(0,0)
        