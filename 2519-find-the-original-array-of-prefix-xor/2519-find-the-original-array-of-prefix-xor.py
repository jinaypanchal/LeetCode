class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        t = [pref[0]]
        for i in range(1, len(pref)):
            t.append(pref[i]^pref[i-1])
        
        return t
        