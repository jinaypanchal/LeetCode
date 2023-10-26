from collections import defaultdict
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # sumi = len(arr)
        mod = 10**9 + 7
        n = len(arr)
        arr.sort()
        d = defaultdict()
        for num in arr:
            d[num] = d.get(num, 0) + 1

        for i in range(1,n):
            for j in range(i+1):
                if arr[i] % arr[j] == 0 and (arr[i] / arr[j]) in d:
                    d[arr[i]] += d[arr[j]] * d[arr[i]/arr[j]]
        
        return sum(d.values()) % mod
        





        