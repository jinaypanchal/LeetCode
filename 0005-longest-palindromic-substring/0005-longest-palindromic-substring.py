class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s

        memo = {}
        def pali(st, i , j):
            if (i, j) in memo:
                return memo[i,j]

            if i >= j:
                return True
            
            if st[i] == st[j]:
                t = pali(st, i+1, j - 1)
                memo[(i, j)] = t 
                return t
            
            return False

       
        n = len(s)
        maxi = float('-inf')
        sp = 0
        for i in range(n):
            for j in range(i, n):
                if pali(s, i, j) == True:
                    if j-i+1 > maxi:
                        maxi = j - i + 1
                        sp = i
        
        return s[sp: sp+maxi]
            

        