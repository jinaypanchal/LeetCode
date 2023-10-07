class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod = 10**9 + 7
        memo = {}
        def f(idx, sc, maxi):
            res = 0
            if sc > k:
                return 0
                
            if idx == n:
                if sc == k:
                    return 1
                else:
                    return 0

            if (idx, sc, maxi) in memo:
                return memo[(idx, sc, maxi)]
            
            for i in range(1, m+1):
                if i > maxi:
                    res += f(idx+1, sc+1, i)
                else:
                    res += f(idx+1, sc, maxi)

            memo[(idx, sc, maxi)] = res%mod         
            return memo[(idx, sc, maxi)]
        
        return f(0, 0, -1)


        