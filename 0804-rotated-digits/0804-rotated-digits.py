class Solution:
    def rotatedDigits(self, n: int) -> int:
        mp = {'0' :'0', '1': '1', '8': '8', '2': '5', '5': '2', '6': '9', '9': '6'}

        ct = 0
        for i in range(1, n + 1):
            stri = str(i)
            rot = ""
            for ch in stri:
                if ch in mp:
                    rot += mp[ch]
                else:
                    rot = ""
                    break

            if rot and rot != stri:
                ct += 1            

      
        return ct
                
                




        