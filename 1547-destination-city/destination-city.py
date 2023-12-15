class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = set()
        city = ""
        for i in paths:
            s.add(i[0])
        
        for i in paths:
            if i[1] not in s:
                city = i[1]
                break
        return i[1]
        