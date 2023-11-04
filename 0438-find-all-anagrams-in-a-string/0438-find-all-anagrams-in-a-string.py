class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        arr = [0] * 26
        m = len(s)
        n = len(p)
        
        for ch in p:
            arr[ord(ch) - ord('a')] += 1
        
        i = 0
        j = 0
        result = []
        
        while j < m:
            arr[ord(s[j]) - ord('a')] -= 1
            
            if j - i + 1 == n:
                if arr == [0] * 26:
                    result.append(i)
                
                arr[ord(s[i]) - ord('a')] += 1
                i += 1
            j += 1
        
        return result
        # def dic_val(d):
        #     for v in d.values():
        #         if v != 0:
        #             return False

        #     return True

        # i = 0
        # j = 0
        # res = []
        # dic = {}
        # for  ch in p:
        #     dic[ch] = dic.get(ch, 0) + 1
        
        # while j < len(s):
        #     idx = s[j]
        #     if idx in dic:
        #         dic[idx] -= 1

        #         if j - i + 1 == len(p):
        #             if dic_val(dic):
        #                 res.append(i)
                    
        #             dic[s[i]] += 1
        #             i+=1
        #     j+=1

       
        # return res
