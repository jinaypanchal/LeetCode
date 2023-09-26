class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurence = [-1] * 26
        visited = set()
        res = []
        n = len(s)

        for i in range(n):
            last_occurence[ord(s[i]) - ord('a')] = i
        
        for i in range(n):
            index = ord(s[i]) - ord('a')

            if index in visited:
                continue
            
            while res and s[i] < res[-1] and last_occurence[ord(res[-1]) - ord('a')] > i:
                visited.remove(ord(res.pop()) - ord('a'))
            
            res.append(s[i])
            visited.add(index)
        
        return "".join(res)


 
        