class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        #looks like combination of isSubsquence and LIS
        def isPredecessor(s1, s2):
            if len(s1) >= len(s2) or abs(len(s1)  - len(s2)) != 1:
                return False
            i = 0
            j = 0
            while i < len(s1) and j < len(s2):
                if s1[i] ==  s2[j]:
                    i+=1
                j+=1
            
            return i == len(s1)

        words = sorted(words, key = lambda x:len(x))

        n = len(words)

        if not words:
            return 0
        
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if isPredecessor(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
        
        print(dp)
        return max(dp)

        