class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        city = ""
        d = {}
        for i in paths:
            d[i[0]] = d.get(0, i[1])
        
        for i in paths:
            if i[1] not in d:
                city = i[1]
                break
        return city

        # s = set()
        # city = ""
        # for i in paths:
        #     s.add(i[0])
        
        # for i in paths:
        #     if i[1] not in s:
        #         city = i[1]
        #         break
        # return city
        