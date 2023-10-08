class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key = lambda x:x[1])
        curr = float('-inf')
        ct = 0
        for i in range(len(pairs)):
                if pairs[i][0] > curr:
                    curr = pairs[i][1]
                    # res.append(pairs[i])
                    ct += 1
        return ct 

        