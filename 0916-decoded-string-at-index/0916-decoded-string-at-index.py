class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        tot_len = 0
        for ch in s:
            if ch.isdigit():
                tot_len *= int(ch)
            else:
                tot_len += 1
        
        for ch in reversed(s):
            k %= tot_len
            if k == 0 and ch.isalpha():
                return ch
            
            if ch.isdigit():
                tot_len //= int(ch)
            else:
                tot_len -= 1
                

 
            # l = 0
            # r = len(st) - 1
            # while l < r:
            #     mid = (l + r) // 2
            #     if mid == k-1:
            #         return st[mid]
            #     elif mid < k-1:
            #         l = mid + 1
            #     else:
            #         r = mid - 1
            
            # return st[k-1] if k <= len(st) else None

        # myset = {"2", "3", "4", "5", "6", "7", "8", "9"}
        # cur_res = ""

        # for ch in s:
        #     if ch in myset:
        #         cur_res *= (int(ch) - 1)
        #     else:
        #         cur_res += ch
        
        # print(cur_res)
        
        # return f(cur_res)
        