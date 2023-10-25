class Solution:
    def countAndSay(self, n: int) -> str:
    
        if n == 1:
            return "1"
        
        say = self.countAndSay(n-1)
        res = ""

        i = 0
        while i <len(say):
            ch = say[i]
            count = 1
            j = i + 1
            
            while j < len(say) and say[i] == say[j]:
                count += 1
                j += 1
            
            res += str(count) + str(ch)
            i = j
        
        return res



        