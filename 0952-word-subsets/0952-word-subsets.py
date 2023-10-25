class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def t(st):
            d = {}
            for ch in st:
                d[ch] = d.get(ch, 0) + 1
            return d

        maxi = {}
        for w in words2:
            wc = t(w)
            for ch, ct in wc.items():
                maxi[ch] = max(maxi.get(ch, 0), ct)
        
        res = []
        for w in words1:
            d_words1 = t(w)
            uni = True
            for ch, ct in maxi.items():
                if d_words1.get(ch, 0) < ct:
                    uni = False
                    break
            
            if uni:
                res.append(w)
        
        return res







            

        