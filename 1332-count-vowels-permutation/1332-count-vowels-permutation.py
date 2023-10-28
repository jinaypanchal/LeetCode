class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        a,e,i,o,u = 1,1,1,1,1
        for l in range(2,n+1):
            new_a = (e + u + i) % mod
            new_e = (a + i) % mod
            new_i = (e + o) % mod
            new_o = i % mod
            new_u = (o + i) % mod

            a,e,i,o,u = new_a, new_e, new_i, new_o, new_u
        
        ct = (a + e + i + o + u) % mod
        return ct

        
        