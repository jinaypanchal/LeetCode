class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # def f(num):
        #     if num == 0:
        #         return 0            
        #     bn = ""
        #     while num > 0:
        #         rem = num % 2
        #         bn = str(rem) + bn
        #         num = num // 2
            
        #     return bn.count("1")

        # arr.sort(key=lambda x: (f(x), x))
        # return arr
        ones_count = {num: bin(num).count("1") for num in arr}
        arr.sort(key=lambda x: (ones_count[x], x))
        return arr


        # d = {}
        # for n in arr:
        #     d.setdefault(f(n), []).append(n)
        
        # # print(d)

        # t = []
        # for k in sorted(d.keys()):
        #     t.extend(d[k])
       

        # return t
        