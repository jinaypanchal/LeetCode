from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}

        if len(s) != len(t):
            return False
        
        for ch in s:
            if ch not in d1.keys():
                d1[ch] = 1
            else:
                d1[ch]+=1
        
        for ch in t:
            if ch not in d2.keys():
                d2[ch] = 1
            else:
                d2[ch]+=1
        
        return d1 == d2