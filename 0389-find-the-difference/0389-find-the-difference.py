class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for ch in s:
            res ^= ord(ch)
        
        for ch in t:
            res ^= ord(ch)

        return chr(res)
        # if len(s)==0:
        #     return t

        # d2 = {}
        # for i in t:
        #     if i not in d2:
        #         d2[i] = 1
        #     else:
        #         d2[i]+=1
        
        # d1 = {}
        # for i in s:
        #     if i not in d1:
        #         d1[i] = 1
        #     else:
        #         d1[i] +=1
        
        # for ch in t:
        #     if ch not in d1 or d1[ch] != d2[ch]:
        #         return ch



   


        
    

       
        
 
        
        