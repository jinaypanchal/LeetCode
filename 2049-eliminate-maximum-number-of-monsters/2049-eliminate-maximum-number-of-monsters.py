class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = []
        for i in range(len(dist)):
            time.append(dist[i]/speed[i])
        
        time.sort()
        curr = 0
        prev = 0
        for i in range(len(time)):
            if time[i] <= curr:
                return prev
            else:
                prev += 1
                curr += 1
        
        return len(dist)
                
