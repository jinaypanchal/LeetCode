class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def f(s1, s2, i, j):
            if (i,j) in memo:
                return memo[(i,j)]  

            if i >= len(s1) or j >= len(s2):
                return 0
            
            if s1[i] == s2[j]:
                memo[(i,j)] = 1 + f(s1, s2, i + 1, j + 1)
                return memo[(i,j)]
            
            else:
                memo[(i,j)] = max(f(s1,s2,i+1,j), f(s1,s2,i, j+1))
                return memo[(i,j)]

        return f(text1, text2, 0, 0)
        