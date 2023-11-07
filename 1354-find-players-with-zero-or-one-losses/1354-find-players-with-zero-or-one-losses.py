class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losser = {}
        winner = {}
        for i in range(len(matches)):
            if matches[i][0] not in winner:
                winner[matches[i][0]] = 1
            else:
                winner[matches[i][0]] += 1

            if matches[i][1] not in losser:
                losser [matches[i][1]] = 1
            else:
                losser[matches[i][1]] += 1
        
        print(winner)
        print(losser)
        w = []
        for key, val in winner.items():
            if key not in losser:
                w.append(key)
        
        
        l = []
        for key, val in losser.items():
            if val == 1:
                l.append(key)
                
        w = sorted(w)
        l = sorted(l)
        return [w, l] 

        


        