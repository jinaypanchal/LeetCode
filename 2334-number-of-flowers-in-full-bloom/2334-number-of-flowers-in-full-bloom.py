class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:

        s, e, res = [], [], []
        for i in flowers:
            s.append(i[0])
            e.append(i[1])
        s.sort()  
        e.sort()

        for p in people:
            num = bisect_right(s, p) - bisect_left(e, p)
            res.append(num)
        return res

        #Niche vala brute hai, 45/52
        # flowers = sorted(flowers, key = lambda x:x[0])
        # n = len(flowers)
        # # print(flowers)
        # # people.sort()
        # res = []
        # for p in people:
        #     ct = 0
        #     for j in range(len(flowers)):
        #         if flowers[j][0] <= p <= flowers[j][1]:
        #             ct += 1
            
        #     res.append(ct)
        
        # return res
                    